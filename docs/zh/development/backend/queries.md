对于后端和前端开发，手动查询 Gramps Web API 可能会很有用。使用 HTTPie 和 jq，可以方便地进行此操作，包括 JWT 认证。

## 安装

HTTPie 可以通过 `pip` 安装：

```bash
python3 -m pip install httpie
```

您需要 HTTPie 版本 3.0.0 或更高版本。

可以通过以下命令在 Ubuntu 中安装 jq：

```bash
sudo apt install jq
```

## 获取访问令牌

要获取访问令牌，请查询令牌端点。假设您的开发实例运行在 `localhost:5555`，您可以使用以下命令：

```bash
http POST http://localhost:5555/api/token/ username=owner password=owner
```

您将看到 JSON 令牌作为输出。

使用 jq，您还可以将访问令牌存储在环境变量中：

```bash
export ACCESS_TOKEN=$(http POST http://localhost:5555/api/token/ \
  username=owner password=owner | jq -r '.access_token')
```

您现在可以在所有需要认证的 API 调用中使用此令牌，例如：

```bash
http -A bearer -a $ACCESS_TOKEN GET http://localhost:5555/api/metadata/
```

请注意，默认情况下，访问令牌将在 15 分钟后过期。
