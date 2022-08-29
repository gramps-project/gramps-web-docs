This page describes the steps needed to start with frontend development. It is assumed that you are using Ubuntu Linux and you will need Docker, docker-compose, and git.

## Step 1: Clone the repository

Clone the Gramps.js repository
```
git clone git@github.com:gramps-project/Gramps.js.git
cd Gramps.js
```

## Step 2: Build and start the development containers

To build and start the containers running the Gramps Web backend with the Gramps example database, as well as the frontend in development mode, simply run

```bash
docker-compose up -d
```

Gramps Web will be accessible at [http://localhost:5555](http://localhost:5555).

Once you make changes to the frontend code, you browser will be reloaded automatically.

!!! warning
    Do not use the development server in production.

!!! info
    Note since the `*.json` translation files are imported with the new syntax suggested in [T39](https://github.com/tc39/proposal-import-assertions), you must use the Chrome or Chromium browser for the development server to work without errors. This issue is about to change in the future.