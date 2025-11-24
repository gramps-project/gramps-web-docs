# 遥测

从 Gramps Web API 版本 3.2.0 开始，Gramps Web 默认每 24 小时向 Gramps Web 团队控制的分析端点发送完全匿名的遥测数据。此页面包含有关收集的遥测数据、其使用方式以及如何在需要时禁用它的信息。

## 收集了什么数据？

遥测数据是一个小的 JSON 负载，格式如下：

```json
{
  "server_uuid": "c04325bfa7ae4578bcf134ec8fc046a7",
  "tree_uuid": "abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890",
  "timestamp": 1701234567,
}
```

正如您可以在 [源代码](https://github.com/gramps-project/gramps-web-api/blob/master/gramps_webapi/api/telemetry.py#L83-L87) 中检查到的，服务器和树的标识符对于服务器和树是唯一的，但它们不包含任何个人可识别的信息。`timestamp` 是当前时间的 Unix 时间戳。

## 为什么收集这些数据？

每天发送一次唯一标识符使 Gramps Web 团队能够跟踪有多少个唯一的服务器在运行 Gramps Web，以及有多少个唯一的树在使用。

这对于理解 Gramps Web 使用的外部服务（例如地图瓦片）的影响非常重要。

## 数据是如何收集的？

当向您的 Gramps Web API 服务器发出请求时，它会检查在过去 24 小时内是否发送过遥测数据（通过检查本地缓存中的一个键）。如果没有，则将上述负载发送到一个记录数据的端点。

该记录端点托管在 Google Cloud Run 上，并直接从一个 [开源代码库](https://github.com/DavidMStraub/cloud-run-telemetry) 部署，因此您可以检查数据是如何处理的。

## 数据将如何使用？

首先，Gramps Web 团队不会使用任何超出匿名负载的数据（例如服务器的 IP 地址）。

收集的匿名 ID 和时间戳将被汇总以生成如下图表：

- 活跃的 Gramps Web 安装数量随时间变化
- 活跃的 Gramps Web 树数量随时间变化

这些图表将发布在 Gramps Web 文档网站上。

## 如何禁用遥测？

由于统计数据对 Gramps Web 团队非常有用，并且我们已确保不会发送任何个人可识别的数据，**我们将非常感激您不要禁用遥测！**

然而，Gramps Web 让用户完全控制，因此您当然可以选择禁用此功能。

为此，只需将 `DISABLE_TELEMETRY` 配置选项设置为 `True`（例如，通过将 `GRAMPSWEB_DISABLE_TELEMETRY` 环境变量设置为 `true` &ndash; 有关详细信息，请参见 [配置文档](configuration.md)）。
