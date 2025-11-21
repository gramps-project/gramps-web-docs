# 前端开发设置

本页描述了开始前端开发所需的步骤。

## 先决条件

推荐的开发设置使用带有开发容器的 Visual Studio Code。此方法将创建一个预配置的开发环境，包含您所需的所有工具。

有关所需先决条件，请参见 [后端开发设置](../backend/setup.md#prerequisites)。

## 开始使用

1. 打开 [Gramps Web 前端代码库](https://github.com/gramps-project/gramps-web) 并点击“fork”
2. 使用 Git 将您的 forked 代码库克隆到本地计算机
3. 在 Visual Studio Code 中打开克隆的代码库。当提示时，选择“在容器中重新打开”或手动打开命令面板 (Ctrl+Shift+P 或 Cmd+Shift+P)，然后选择“开发容器：重建并在容器中重新打开”。
4. 等待开发容器构建并启动。这可能需要几分钟，尤其是第一次。

## 运行前端开发服务器

要运行前端开发服务器并在浏览器中预览更改的影响，您可以使用开发容器中的预定义任务。

为此，您首先需要启动一个 [Gramps Web API 后端](../backend/setup.md#tasks) 的实例。最简单的方法是使用后端开发容器并在单独的 VS Code 窗口中 [运行“服务 Web API”任务](../backend/setup.md#tasks)。

一旦后端正在运行，您可以通过从命令面板 (Ctrl+Shift+P 或 Cmd+Shift+P) 中选择“任务：运行任务”，然后选择“服务 Gramps Web 前端”来运行前端开发服务器。

这将启动前端开发服务器，端口为 8001，您可以在浏览器中访问 `http://localhost:8001`。当您对前端代码进行更改时，浏览器将自动重新加载，允许您立即看到更改的影响。
