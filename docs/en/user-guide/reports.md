# Reports

A report is a formatted, downloadable document generated from your family tree data. Reports are the same plugins available in Gramps Desktop – see the [Gramps Wiki page on Reports](https://gramps-project.org/wiki/index.php/Gramps_5.1_Wiki_Manual_-_Reports) for a full overview. The web interface runs the same report engine on the server and delivers the resulting file to your browser.

Reports are accessible from the sidebar.

## Report categories

The Reports page lists all available reports grouped by category:

- **Text Reports** – narrative or tabular documents such as ancestor lists, descendant reports, and birthday calendars. Output formats include PDF, ODT/OpenDocument, RTF, HTML, and others.
- **Graphical Reports** – charts and diagrams such as ancestor trees and fan charts. Output formats include PDF, SVG, PNG, and others.
- **Trees** – family tree diagrams.
- **Books** – multi-chapter report books that combine several text and graphical reports into a single document.
- **Web Pages** – static website generators that produce a complete set of HTML pages from your tree.

The reports shown depend on which Gramps report plugins are installed on the server.

## Running a report

Click a report to open its options page, which shows:

- **Description** – what the report contains
- **Author** and **Version** of the plugin
- **Options** – report-specific settings such as the starting person, number of generations, output format, page size, and other parameters

Adjust the options as needed, then click **Generate**. The report is generated on the server and the resulting file is downloaded to your browser automatically.

!!! tip
    Most reports default to the **database home person** – the home person set in the Gramps database, which may differ from your personal home person setting in the browser. If the report covers the wrong person, change the person option in the report's settings.
