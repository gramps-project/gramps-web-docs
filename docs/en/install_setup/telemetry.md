# Telemetry

Starting from Gramps Web API version 3.2.0, Gramps Web by default sends fully anonymized telemetry data every 24 hours to an analytics endpoint controlled by the Gramps Web team. This page contains information about the telemetry data collected, how it is used, and how to disable it if desired.

## What data is collected?

The telemetry data is a small JSON payload of the following form:

```json
{
  "server_uuid": "c04325bfa7ae4578bcf134ec8fc046a7",
  "tree_uuid": "abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890",
  "timestamp": 1701234567,
}
```

As you can check yourself [in the source code](https://github.com/gramps-project/gramps-web-api/blob/master/gramps_webapi/api/telemetry.py#L83-L87), the server and tree identifiers are unique for the server and tree, but they do not contain any personally identifiable information. The `timestamp` is the current time as a Unix timestamp

## Why is the data collected?

Sending a unique identifier once a day allows the Gramps Web team to track how many unique servers are running Gramps Web, and how many unique trees are being used.

This is important to understand the impact on external services that are used by Gramps Web, such as map tiles.

## How is the data collected?

When a request is made to your Gramps Web API server, it checks whether telemetry has been sent in the last 24 hours (by checking a key in the local cache). If not, the above payload is sent to an endpoint that logs the data.

The logging endpoint is hosted on Google Cloud Run and is directly deployed from an [open source repository](https://github.com/DavidMStraub/cloud-run-telemetry), so you can inspect how the data is processed.

## What will be done with the data?

First and foremost, no data beyond the anonymized payload, that could hypothetically be collected (such as the server's IP address), will be used by the Gramps Web team.

The collected anonymized IDs and timestamp will be aggregated to produce graphs such as:

- Number of active Gramps Web installations as function of time
- Number of active Gramps Web trees as function of time

These graphs will be published on the Gramps Web documentation site.

## How to disable telemetry?

Since the statistics data is useful for the Gramps Web team and we have ensured that no personally identifiable data is sent, **we would be grateful if you don't disable telemetry!**

Nevertheless, Gramps Web puts users in full control, so of course you can choose to disable the feature if you want.

To do so, simply set the `DISABLE_TELEMETRY` configuration option to `True` (e.g. by setting the `GRAMPSWEB_DISABLE_TELEMETRY` environment varaible to `true` &ndash; see the [configuration docs](configuration.md) for details).