# 后端开发设置

本页面列出了开始开发 [Gramps Web API](https://github.com/gramps-project/gramps-web-api/) 的步骤，这是 Gramps Web 的后端（服务器组件）。

## 先决条件

推荐的开发设置使用带有开发容器的 Visual Studio Code。此方法将创建一个预配置的开发环境，包含您所需的所有工具。要开始，您需要以下组件：

- [Docker](https://docs.docker.com/get-docker/)
- [Visual Studio Code](https://code.visualstudio.com/) 和安装了 [Dev Containers 扩展](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
- [Git](https://git-scm.com)

您可以使用 Linux、macOS 或 Windows 作为操作系统。

## 开始

1. 打开 [Gramps Web API 仓库](https://github.com/gramps-project/gramps-web-api) 并点击“fork”
2. 使用 Git 将您 fork 的仓库克隆到本地计算机
3. 在 Visual Studio Code 中打开克隆的仓库。当提示时，选择“在容器中重新打开”或手动打开命令面板（Ctrl+Shift+P 或 Cmd+Shift+P），并选择“Dev Containers: Rebuild and Reopen in Container”。
4. 等待开发容器构建并启动。这可能需要几分钟，特别是第一次。

    **在 Dev Container 构建成功后，命令将返回：**

    `Successfully installed gramps-webapi-x.x.x.`

    !!! info
        在 Visual Studio Code 中重建容器：

        - 如果在容器中，请使用“在容器中重建”调色板命令。

        - 如果在文件夹视图中（即不在容器中），请使用“重建并在容器中重新打开”调色板命令。

## 任务

如果您只是在修改后端代码，您不一定需要启动一个 web 服务器 - 单元测试使用 Flask 测试客户端，可以模拟对 API 的请求，而无需运行服务器。

然而，如果您想：

- 使用真实的 HTTP 请求尝试您的更改（请参见 [手动查询](queries.md)），
- 预览更改对整个 Gramps Web 应用程序的影响，或
- 同时对前端进行更改（请参见 [前端开发设置](../frontend/setup.md)），

运行服务器是有用的。

在开发容器中，通过预定义任务简化了运行服务器的过程。您可以从命令面板（Ctrl+Shift+P 或 Cmd+Shift+P）运行这些任务，选择“Tasks: Run Task”，然后选择以下之一：
- “Serve Web API” - 在端口 5555 启动 Flask 开发服务器，并启用调试日志
- “Start Celery worker” - 启动一个 Celery 工作进程以处理后台任务。

## 调试

调试有时可能具有挑战性，尤其是在尝试追踪复杂行为或识别微妙问题时。为了简化这一过程，您可以直接在 Visual Studio Code 中调试运行的 API 实例和单个测试用例。

### 调试 Gramps Web API

要调试运行中的 API：

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
4. 开始调试 - 执行将在该测试文件中设置的任何断点处停止。  

此设置允许您逐步执行测试逻辑，检查变量值，更好地理解测试失败或意外结果。
