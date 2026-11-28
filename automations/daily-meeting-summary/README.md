# Legacy entry compatibility

The formal definition is now [scheduled-meeting-summary](../scheduled-meeting-summary/README.md). The [old prompt](prompt.md) forwards to the current procedure; it is not a second task definition.

Retain the deployed configuration, path resolution, successful checkpoints and receipts. Use the new [configuration example](../scheduled-meeting-summary/config.example.yaml) only to add relevant fields, without creating fresh production state. Frequency, time and timezone remain deployment choices; renaming repository entries does not change the actual schedule.
