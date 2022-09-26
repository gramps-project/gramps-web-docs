This page lists the steps required to start developing [Gramps Web API](https://github.com/gramps-project/gramps-webapi/). It will be assumed that you are using Ubuntu Linux.

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

Clone the Web API to your PC with

```
git clone git@github.com:gramps-project/gramps-webapi.git
cd gramps-webapi
```

### Install prerequisites

To start development, please install the dependencies by running
```
pip3 install -r requirements-dev.txt
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

### Install the library in editable mode

Run
```
pip3 install -e . --user
```

### Generate a configuration file

Example content:

```python
TREE="My Family Tree"
DISABLE_AUTH=True
```

!!! warning
    Do not use this configuration in production.

See [Configuration](../Configuration.md) for a full list of config options.

!!! warning
    Do not use your production database for development, but use a copy of it or the Gramps example database.

### Run the app in development mode


Run
```
python3 -m gramps_webapi --config path/to/config run
```
The API will be accesible at `http://127.0.0.1:5000` by default, which displays an empty page.  Access your Gramps data using the API described by [gramps-project.github.io/gramps-webapi](https://gramps-project.github.io/gramps-webapi/). For example, to show people go to `http://127.0.0.1:5000/api/people`

To choose a different port, add the `--port` option.

!!! warning
    Do not expose this as-is to a public network or the internet, as anyone will be able to view and modify your family tree!

