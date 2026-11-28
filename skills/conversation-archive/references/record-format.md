# 记录适配与验证边界

公开原始记录的来源适配、筛选、ID与截止、转达和时间读取现由 [conversation-review](../../conversation-review/references/record-format.md) 维护。archive先调用review取得完整公开events和timing，不用回顾摘要作为原始记录。

archive继续负责原话渲染、逐字符与顺序核对、历史前缀比较、不可变版本和current.json原子提交。原CLI和档案格式保留，依赖缺失时提示安装完整review或通过--review-skill指定位置。

缺失历史、截断输出和外部附件不能恢复。未知来源、同ID内容改变或历史消失仍停止，不覆盖人工修改过的档案。输出结构见 [归档规范](archive-standard.md)。
