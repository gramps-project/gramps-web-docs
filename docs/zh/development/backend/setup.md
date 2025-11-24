# 后端开发设置

本页面列出了开始开发 [Gramps Web API](https://github.com/gramps-project/gramps-web-api/) 的步骤，这是 Gramps Web 的后端（服务器组件）。

## 先决条件

推荐的开发设置使用带有开发容器的 Visual Studio Code。这种方法将创建一个预配置的开发环境，包含您所需的所有工具。要开始，您需要以下组件：

- [Docker](https://docs.docker.com/get-docker/)
- [Visual Studio Code](https://code.visualstudio.com/) 和安装了 [Dev Containers 扩展](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
- [Git](https://git-scm.com)

您可以使用 Linux、macOS 或 Windows 作为操作系统。

## 开始

1. 打开 [Gramps Web API 仓库](https://github.com/gramps-project/gramps-web-api) 并点击“fork”
2. 使用 Git 将您的 forked 仓库克隆到本地计算机
3. 在 Visual Studio Code 中打开克隆的仓库。当提示时，选择“在容器中重新打开”或手动打开命令面板（Ctrl+Shift+P 或 Cmd+Shift+P），选择“Dev Containers: Rebuild and Reopen in Container”。
4. 等待开发容器构建并启动。这可能需要几分钟，特别是第一次。

## 任务

如果您只是修改后端代码，您不一定需要启动一个 web 服务器——单元测试使用 Flask 测试客户端，可以在不需要运行服务器的情况下模拟对 API 的请求。

然而，运行服务器是有用的，如果您

- 想通过真实的 HTTP 请求尝试您的更改（请参见 [手动查询](queries.md)），
- 想预览更改对整个 Gramps Web 应用程序的影响，或者
- 还想对前端进行同时更改（请参见 [前端开发设置](../frontend/setup.md)）。

在开发容器中，通过预定义的任务简化了服务器的运行。您可以通过从命令面板（Ctrl+Shift+P 或 Cmd+Shift+P）选择“Tasks: Run Task”并选择以下之一来运行这些任务：
- “Serve Web API” - 在端口 5555 启动 Flask 开发服务器，并启用调试日志
- “Start Celery worker” - 启动一个 Celery 工作进程以处理后台任务。

## 调试

调试有时可能会很具挑战性，尤其是在尝试追踪复杂行为或识别微妙问题时。为了简化这一过程，您可以直接在 Visual Studio Code 中调试正在运行的 API 实例和单个测试用例。

### 调试 Gramps Web API

要调试正在运行的 API：

1. 打开 Visual Studio Code 并转到 **运行和调试** 视图。  
2. 从下拉菜单中选择 **“Web API”** 配置。  
3. 开始调试。  
4. 当您向后端发送请求（无论是手动还是通过 Gramps Web GUI）时，执行将在您在代码中设置的任何断点处暂停。  
   这允许您检查变量、控制流和其他运行时细节。

### 调试测试用例

要调试特定的测试用例：

1. 打开您想要调试的测试文件（例如，`test_people.py`）。  
2. 在 Visual Studio Code 中，打开 **运行和调试** 视图。  
3. 选择 **“当前测试文件”** 配置。  
4. 开始调试——执行将在该测试文件中设置的任何断点处停止。  

此设置允许您逐步检查测试逻辑，检查变量值，更好地理解测试失败或意外结果。
