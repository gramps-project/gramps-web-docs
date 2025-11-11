# Backend development setup

This page lists the steps required to start developing [Gramps Web API](https://github.com/gramps-project/gramps-web-api/), the backend (server component) of Gramps Web.


## Prerequisites

The recommended development setup uses Visual Studio Code with devcontainers. This approach will create a preconfigured development environment with all the tools you need. To get started, you'll need the following ingredients:

- [Docker](https://docs.docker.com/get-docker/)
- [Visual Studio Code](https://code.visualstudio.com/) with the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) installed
- [Git](https://git-scm.com)

You can use Linux, macOS, or Windows as your operating system.


## Getting started

1. Open the [Gramps Web API repository](https://github.com/gramps-project/gramps-web-api) and click "fork"
2. Clone your forked repository to your local machine using Git
3. Open the cloned repository in Visual Studio Code. When prompted, select "Reopen in Container" or manually open the command palette (Ctrl+Shift+P or Cmd+Shift+P) and select "Dev Containers: Rebuild and Reopen in Container".
4. Wait for the dev container to build and start. This may take a few minutes, especially the first time.


## Tasks

If you are only modifying the backend code, you do not necessarily need to spin up a web server - unit tests use a Flask test client that allow simulating requests to the API without needing a running server.

However, running a server is useful if you

- want to try out your changes with real HTTP requests (see [manual queries](queries.md)), 
- want to preview the impact of changes on the full Gramps Web application, or
- also want to make simultaneous changes to the frontend (see [frontend development setup](../frontend/setup.md)).

Running the server is simplified in the dev container by predefined tasks. You can run these tasks from the command palette (Ctrl+Shift+P or Cmd+Shift+P) by selecting "Tasks: Run Task" and then choosing one of the following:
- "Serve Web API" - starts the Flask development server on port 5555 with debug logging enabled
- "Start Celery worker" - starts a Celery worker to process background tasks.


## Debugging

Debugging can sometimes be challenging, especially when trying to trace complex behavior or identify subtle issues. To make this easier, you can debug both a running API instance and individual test cases directly within Visual Studio Code.

### Debugging the Gramps Web API

To debug the running API:

1. Open Visual Studio Code and go to the **Run and Debug** view.  
2. Select the **"Web API"** configuration from the dropdown menu.  
3. Start debugging.  
4. When you send requests to the backend (either manually or through the Gramps Web GUI), the execution will pause at any breakpoints you have set in the code.  
   This allows you to inspect variables, control flow, and other runtime details.

### Debugging Test Cases

To debug a specific test case:

1. Open the test file you want to debug (for example, `test_people.py`).  
2. In Visual Studio Code, open the **Run and Debug** view.  
3. Choose the **"Current Test File"** configuration.  
4. Start debugging — execution will stop at any breakpoints set within that test file.  

This setup allows you to step through test logic, examine variable values, and better understand test failures or unexpected results.
