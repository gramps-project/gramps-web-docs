# Frontend development setup

This page describes the steps needed to start with frontend development. 

## Prerequisites

The recommended development setup uses Visual Studio Code with devcontainers. This approach will create a preconfigured development environment with all the tools you need.

See [Backend development setup](../backend/setup.md#prerequisites) for the prerequisites needed.

## Getting started

1. Open the [Gramps Web frontend repository](https://github.com/gramps-project/gramps-web) and click "fork"
2. Clone your forked repository to your local machine using Git
3. Open the cloned repository in Visual Studio Code. When prompted, select "Reopen in Container" or manually open the command palette (Ctrl+Shift+P or Cmd+Shift+P) and select "Dev Containers: Rebuild and Reopen in Container".
4. Wait for the dev container to build and start. This may take a few minutes, especially the first time.


## Running the frontend development server

To run the frontend development server and preview the impact of your changes in the browser, you can use the predefined tasks in the dev container.

For that to work, you first need to spin up an instance of the [Gramps Web API backend](../backend/setup.md#tasks). The easiest way to do this is to use the backend dev container and [run the "Serve Web API" task](../backend/setup.md#tasks) in a separate VS Code window.

Once the backend is running, you can run the frontend development server by selecting "Tasks: Run Task" from the command palette (Ctrl+Shift+P or Cmd+Shift+P) and then choosing "Serve Gramps Web frontend".

This will start the frontend development server on port 8001, which you can access in your browser at `http://localhost:8001`. The browser will automatically reload when you make changes to the frontend code, allowing you to see the impact of your changes immediately.

