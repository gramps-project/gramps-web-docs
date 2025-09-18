# Gramps Web: Documentation

This is the source repository for the [Gramps Web documentation website](https://www.grampsweb.org/).

For the source code of Gramps Web, please see

- [Gramps Web API](https://github.com/gramps-project/gramps-web-api/) for the (Python) backend
- [Gramps Web Frontend](https://github.com/gramps-project/gramps-web) for the (Javascript) frontend

Please use those repositories for reporting issues or feature requests.


## Serving the documentation locally

You can run the website locally and preview it in your browser while editing.

To do that, first install the required Python dependencies (you may want to do this in a virtual environment):

```bash
python -m pip install -r requirements.txt
```

Then, you can serve the documentation and open it in the browser with:

```bash
mkdocs serve -a localhost:8211 -o
```

## Contributing

Contributions to the documentation are welcome! Please see the [Contributing Guide](CONTRIBUTING.md) for details.
