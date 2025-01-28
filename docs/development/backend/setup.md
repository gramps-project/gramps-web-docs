This page lists the steps required to start developing [Gramps Web API](https://github.com/gramps-project/gramps-web-api/). It will be assumed that you are using Ubuntu Linux.

### Python version

The Web API requires Python 3.7 or newer.

### Install Gramps

The Web API requires the Gramps Python library to be importable. Starting from Gramps 5.2.0, it will be installable via `pip`. Right now, development is still based on Gramps 5.1.x, so the most convenient option is to install the Gramps `apt` package on Ubuntu

```
sudo apt install gramps
```

!!! info
    Note that using the `gramps` Python package from Gramps installed with `apt` requires using the system Python interpreter, so you cannot work in a virtual environment.

### Clone the Web API repository

Clone the Web API to your PC (assuming you have set up an SSH key with Github) using

```
git clone git@github.com:gramps-project/gramps-web-api.git
cd gramps-web-api
```


### Install prerequisites

To start development, please install the dependencies by running
```
pip3 install -r requirements-dev.txt
```

### Install the library in editable mode

Run
```
pip3 install -e . --user
```

### Set up pre-commit hooks

To set up the pre-commit hooks for the repository, run
```
pre-commit install
```
in the repository root. This will e.g. make sure that all source files are nicely formatted with `black`.

### Run tests

To run the unit tests, run
```
pytest
```
in the repository root.

### Generate a configuration file

Example content:

```python
TREE="My Family Tree"
SECRET_KEY="not_secure_enough"
USER_DB_URI="sqlite:///users.sqlite"
```

!!! warning
    Do not use this configuration in production.

See [Configuration](../../install_setup/configuration.md) for a full list of config options.

!!! warning
    Do not use your production database for development, but use a copy of it or the Gramps example database.


### Add users


You can add a user with owner permissions by running
```
python3 -m gramps_webapi --config path/to/config user add owner owner --role 4
```
This uses username and password `owner`.


### Run the app in development mode


Run
```
python3 -m gramps_webapi --config path/to/config run
```
The API will be accessible at `http://127.0.0.1:5000` by default, which displays an empty page.  Access your Gramps data using the API described by [gramps-project.github.io/gramps-web-api](https://gramps-project.github.io/gramps-web-api/). For example, to show people go to `http://127.0.0.1:5000/api/people`

#### Options

To choose a different port, add the `--port PORT` option, where `PORT` is a number. The default port is `5000`.

To send the log data to a file, use `--log-file FILENAME`. The default is not to log to a file.

To set the log level (for console or file) use `--debug-level LEVEL` where LEVEL is `info`, `debug`, `warning`, or `critical`. The default is `info`.

If running the gramps-web-api server locally, the following additional flags may be useful:

* `--use-wsgi` - adds a WSGI wrapper to the application.
* `--host IP` - the IP address to use for the WSGI listener. The default IP is `127.0.0.1`.
* `--max-workers NUMBER` - for the WSGI server. Default is set dynamically based on the number of CPUs.
* `--open-browser WHERE` - to open the browser on the default gramps-web-api page in a `tab` or a `window`. The default of `WHERE` is `no`, meaning to not open a browser tab or window.

To find out more about the options, use `--help`.
