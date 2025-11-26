---
hide:
  - navigation
---

If you run into issues or need help with Gramps Web, please pick one of the following options.

[Forum :material-forum:](https://gramps.discourse.group/c/gramps-web/){ .md-button }
[Backend issues :material-github:](https://github.com/gramps-project/gramps-web-api/issues){ .md-button }
[Frontend issues :material-github:](https://github.com/gramps-project/gramps-web/issues){ .md-button }

See below for some guidance on where to head first.

## Asking questions

The official Gramps Discourse forum has a [separate category for Gramps Web](https://gramps.discourse.group/c/gramps-web/). Please use it to ask any questions you may have about Gramps Web, for instance

- Questions on the usage of Gramps Web
- Questions on the configuration of Gramps Web
- Troubleshooting a deployment of Gramps Web
- Ideas about improvements to Gramps Web
- ...

## Reporting issues

If you encounter a problem that you believe is a bug in Gramps Web, please report it via GitHub.

There are two separate GitHub repositories for the code used in Gramps Web, one for the user interface (&ldquo;frontend&rdquo;) and one for the server code (&ldquo;backend&rdquo;):

- [Frontend issues](https://github.com/gramps-project/gramps-web/issues)
- [Backend issues](https://github.com/gramps-project/gramps-web-api/issues)


If you are unsure where to file an issue, don't worry and just choose either of the two &ndash; the maintainers will be able to transfer the issue if necessary.

In either case, please always include the following information in your report:

- Details about your setup (e.g. a docker-compose file with sensitive values redacted, or whether your are using a hosted version, such as Grampshub, or a pre-configured image, such as DigitalOcean)
- Version information. To obtain it, go to the "System information" tab on the Settings page in Gramps Web and copy/paste the values in the box, which should look something like this:

```
Gramps 5.1.6
Gramps Web API 1.5.1
Gramps.js 24.1.0
locale: en
multi-tree: false
task queue: true
```

## Suggesting enhancements

For general ideas and discussion about future improvements, feel free to open a discussion in the [forum](https://gramps.discourse.group/c/gramps-web/). You may also want to check the issue pages (see links above) whether a particular feature is already planned or being worked on.

For specific enhancements with a limited scope, feel free to directly open an issue with a feature request in the appropriate frontend or backend Github repository.