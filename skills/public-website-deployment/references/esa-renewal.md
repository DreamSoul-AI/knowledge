# ESA 订阅与续订检查

用于检查 ESA 网站依赖的订阅是否到期，以及在用户已授权时设置自动续订。普通内容发布只核对所需服务状态，不默认改变续订设置。复用官方 CLI 的指定 OAuth profile，核对操作者与资源主账号；身份检查沿用 [ESA CLI](esa-cli.md#oauth-认证)，账务查询与续订权限另行核对。

## 分别定位订阅

| 对象 | 检查内容 |
| --- | --- |
| 计算订阅 | 目标 Pages 项目实际使用的计算套餐、实例、规格、额度、到期及续订状态 |
| 站点套餐 | 自定义域名所属 ESA 站点、其套餐实例、规格、到期及续订状态 |

两个对象分别确认，不把站点套餐有效当作计算订阅有效。它们可能被多个项目或子域名共用，应记录影响范围。短时测试链接的有效期和证书期限也分别处理，不作为套餐到期时间。

私人配置的站点字段可以未填写。此时先按本次目标项目查询 `ListRoutineRelatedRecords`，从目标域名的实际绑定取得 `SiteId`，再用 `GetSite` 核对站点与套餐实例；不要把空配置传给 API，也不自动改写私人默认值。查询方式见 [ESA CLI 域名回读](esa-cli.md#首次绑定子域名)。

计算订阅可由 `GetSubscriptionPlan` 回读。阿里云 CLI 3.5.3 的本地 API 元数据未登记该接口时，会在请求前报告无效 API。2026-11-20 已在中国站使用以下参数查询成功；其他入口先核对其 API 版本和官方端点。`--force` 仅跳过 CLI 本地 API 元数据校验，身份与云端权限检查仍然适用，不作为其他错误的通用重试方式。

```powershell
aliyun esa GetSubscriptionPlan --profile '<OAuth配置名>' --force --version '2024-09-10' --endpoint 'esa.cn-hangzhou.aliyuncs.com'
```

从实际资源与账务信息核对实例 ID、`OwnerId`、`ProductCode`、`ProductType`、`SubscriptionType`、状态及 `EndTime`。产品类型和实例 ID 取本次回读值，不从历史案例或名称猜测。将原始时间与用户时区一并记录；无记录或权限不足时先解决查询问题，不自动购买替代套餐。

可用已认证的阿里云 CLI 查询指定实例，参数替换为本次核验值；实例较多时检查分页及缺项。[QueryAvailableInstances](https://help.aliyun.com/en/user-center/developer-reference/api-bssopenapi-2017-12-14-queryavailableinstances)

```powershell
aliyun bssopenapi QueryAvailableInstances --profile '<OAuth配置名>' --InstanceIDs '<计算实例ID>,<站点实例ID>'
```

## 核对费用条件

截至 2026-11-20，官方说明站点免费套餐支持零元购买与续费；计算免费版为零元月费、100 Credits，用尽后停止相关服务，不自动转按量。具体实例是否仍采用这些规格，需要本次回读确认。[站点免费套餐](https://help.aliyun.com/zh/edge-security-acceleration/esa/product-overview/free-plan)、[计算订阅计费](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/functions-and-pages-billing)

用户要求“免费才设置”时，核对当前实例规格、续费规则及可取得的报价或订单证据。询价接口报错不等于报价为零；保留错误，说明实际采用的费用依据。无法确认免费条件时停止设置，不能通过升级、立即续费下单或新增服务来绕过。

到期停服、额度耗尽和额外收费是不同问题；自动续订不会取消现有额度限制。站点套餐与计算订阅的到期及释放策略分别核对，不互相套用宽限期。续订时的价格和规则仍需以当时实际情况为准。

## 设置与回读

用户只要求查询时，到此交付两份订阅的状态。已授权设置且费用条件满足时，保存原续订状态与周期；目标状态和周期已经一致则直接验收。周期按本次需求和当前套餐支持范围选定，不把案例中的一个月当作所有套餐的固定默认值。

使用 `SetRenewal` 时，按各自实例的产品信息分别设置，传入自动续订状态、周期与单位。下面是参数模板，仅在上述核验完成后使用。[SetRenewal](https://help.aliyun.com/en/user-center/developer-reference/api-bssopenapi-2017-12-14-setrenewal)

```powershell
aliyun bssopenapi SetRenewal --profile '<OAuth配置名>' --ProductCode '<回读的产品代码>' --ProductType '<回读的产品类型>' --SubscriptionType 'Subscription' --InstanceIDs '<本次实例ID>' --RenewalStatus 'AutoRenewal' --RenewalPeriod '<已确定的周期整数>' --RenewalPeriodUnit '<M或Y>'
```

命令退出码和响应的 `Success`、`Code` 均需检查；随后独立查询每个实例，核对 `RenewStatus`、`RenewalDuration`、`RenewalDurationUnit`、规格、状态及到期时间。一个实例成功、另一个失败时分别记录；状态未知时先查询，不盲目重发。上述回读字段见 [QueryAvailableInstances](https://help.aliyun.com/en/user-center/developer-reference/api-bssopenapi-2017-12-14-queryavailableinstances)。

也可在官方资源续订入口修改设置；平台续费购买页面可能同时提交续费订单，不能将点击购买视为仅修改自动续订。账户权限或接口能力不足时说明缺项，使用其他入口须符合本次授权及既有操作偏好。[套餐续费与自动续费](https://help.aliyun.com/zh/edge-security-acceleration/esa/product-overview/renewal-package)

## 交付与证据

分别列出计算订阅与站点套餐的当前规格、到期时间、续订状态与周期、费用依据、操作及回读结果，保留失败与未确认项。账号与原始回执继续留在任务的私人记录中。

`AutoRenewal` 表示已配置自动续订，不表示未来续订已成功。实际执行后，取得续订订单或账务结果及新的到期时间，才能记录该次续订成功；当前周期未改变不等于设置失败。是否安排后续检查按用户请求处理，不自动创建定时任务。

2026-11-19 来源项目已分别设置计算免费订阅与站点免费套餐的自动续订，并回读状态及周期成功；当时询价接口未返回有效报价，采用官方免费规则、实例规格与历史零元订单作为依据。2026-11-20 安装后只读复核，两份实例仍为原免费规格、正常状态及每次一个月自动续订，未修改设置。未来自动续订执行、价格变化和长期可用性尚未验证。本参考的官方说明于 2026-11-20 核对。
