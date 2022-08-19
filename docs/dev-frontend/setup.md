This page describes the steps needed to start with frontend development. It is assumed that you are using Ubuntu Linux.

!!! info
    Note since the `*.json` translation files are imported with the new syntax suggested in [T39](https://github.com/tc39/proposal-import-assertions), you must use the Chrome browser for the development server to work without errors. This issue is about to change in the feature.


## Install Node.js

To get started, install Node.js with [`nvm`](https://github.com/nvm-sh/nvm):

```
nvm install node
```

## Clone the repository

Clone the Gramps.js repository
```
git clone git@github.com:gramps-project/Gramps.js.git
cd Gramps.js
```

## Install development dependencies

To install all dependencies, run
```
npm install
```
at the repository's root.

## Start the backend

To see Gramps Web live in action, you need a running Gramps Web API backend where the frontend can fetch its data from.

If you have followed the setup steps for [backend development](../dev-backend/setup.md), this can be achieved with a command like
```
python3 -m gramps_webapi --config path/to/config run --port 5555
```

A backend at a different location can be used during development by changing the `__APIHOST__` variable in `api.js`.

## Run the frontend in development mode

You can now run the frontend with 
```
npm run start
```