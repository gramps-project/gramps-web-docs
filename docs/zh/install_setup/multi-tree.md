# 设置多个树的托管

默认情况下，Gramps Web 仅允许访问单个家谱数据库（“树”），该树在配置文件中指定。

然而，从 Gramps Web API 后端的 0.7.0 版本开始，也可以从单个安装中提供多个树。然而，目前每个用户都绑定到单个树，因此此设置不适合在用户之间共享树，而是用于托管多个独立的 Gramps Web 实例。

## 启用多树支持

要启用多树支持，必须将 `TREE` 配置选项设置为单个星号 `*`，例如在配置文件中：

```python
TREE = "*"
```

这将使服务器的 Gramps 数据库目录中的所有树可访问（前提是用户权限足够）。树的 ID 是子目录的名称。您可以使用以下命令列出现有树（名称和 ID）：

```bash
python -m gramps_webapi --config /app/config/config.cfg tree list
```

此外，您应该将 `MEDIA_PREFIX_TREE` 配置选项设置为 `True`，以确保媒体文件存储在单独的子文件夹中。否则，用户将能够访问他们没有权限的树所属于的媒体文件！

## 将用户帐户添加到特定树

要将用户添加到特定树，只需将 `--tree TREEID` 命令行选项添加到添加用户命令中。您也可以通过将 `tree` 属性设置在 JSON 有效负载中，POST 到 `/users/` 端点。

用户名和电子邮件地址在 *所有* 树中必须是唯一的。

## 创建新树

要创建新树，建议 POST 到 `/trees/` 端点，而不是使用 Gramps CLI。这将使用 UUIDv4 作为树 ID，从而提高安全性，因为名称无法被猜测。目前，仅支持新创建树的 SQLite。

## 授权

要授权（获取令牌），只需用户名和密码，如同单树模式，因为每个用户的树 ID 是已知的，因此无需提供它。

## 迁移现有媒体文件

如果您想将现有的 Gramps Web 实例迁移到多树支持并使用本地媒体文件，您可以简单地将它们移动到原始位置的子文件夹中，子文件夹的名称为树 ID。

如果您使用的是托管在 S3 上的媒体文件，您可以使用 `gramps-web-api` 仓库的 `scripts` 目录中提供的脚本：

```bash
python scripts/s3_rename.py BUCKET_NAME TREE_ID
```

这假设相关的访问密钥已经设置为环境变量。

## 迁移现有用户数据库

如果您想启用多树支持并重用现有用户，您需要将他们分配到特定树。您可以使用以下命令来实现这一目的：

```bash
python -m gramps_webapi --config /app/config/config.cfg user fill-tree TREE_ID
```

## 自定义前端

从登录页面访问的注册页面在多树设置中无法使用，因为需要为注册指定一棵树。因此，建议在 [前端配置](frontend-config.md) 中将 `hideRegisterLink` 设置为 `true`。
