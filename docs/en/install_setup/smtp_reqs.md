# Simple Mail Transfer Protocol (SMTP) Prerequisites
Gramps Web supports Simple Mail Transfer Protocaol (SMTP) for features such as:

1. New user account registration
2. Account password reset
## Prior to configuring SMTP support in Gramps Web

Obtain your SMTP server parameters:

    a) server name of your SMTP host
    b) port number supported by your Gramps Web server
    c) cryptographic protocol of your SMTP host (ie. SSL/TLS)
    d) username and password of your SMTP host.

##Test your SMTP parameters

Use a `command-line` utility or `script` to test your SMTP settings on your Gramps Web server.

Ensure your SMTP host can send an e-mail using your SMTP parameters.

!!! info    
    If your SMTP host returns an error, refer to your SMTP host documentation.


## Configure Gramps Web using your SMTP settings

After a successfuly testing your SMTP parameters, follow the steps in [configuration.md] to add the parameters to your configuration file.

