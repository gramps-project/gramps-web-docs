# Gramps Web Docs Contributing Guide

Thanks for helping to improve the Gramps Web documentation! This guide will help you get started with contributing.

## Finding your way around

The documentation pages are written in Markdown and stored in the `docs` directory. Each page on [grampsweb.org](https://www.grampsweb.org/) corresponds to a `.md` file in this directory.

The navigation structure is defined in the `mkdocs.yml` file at the root of the repository. This file controls how the pages are organized and displayed in the sidebar.

## Making changes

To make changes to the documentation, simply change the relevant Markdown files in the `docs` directory and submit a pull request.

If you are proficient with git, you can clone the repository, make your changes locally, and push them to your fork. If you're not familiar with git, you can also edit files directly on Github using the web interface.

## Adding new pages

To add a new page to the documentation, create a new Markdown file in the `docs` directory and add it to the `mkdocs.yml` file under the appropriate section. Make sure to follow the existing structure and formatting.

## Previewing changes

If you are just editing or adding Markdown to a page, there may not be a need to preview your changes. However, if you are making significant changes or adding new pages, you can preview your changes locally by following these steps:

1. Install the necessary dependencies:

```bash
python -m pip install -r requirements.txt
```

2. Run the MkDocs development server:

```bash
python -m mkdocs serve -a localhost:8211
```

3. Open your web browser and go to [http://localhost:8211](http://localhost:8211) to see your changes live. The web server will automatically reload when you make changes to the Markdown files.
