# Check and verify data

The **Family Tree Processing** section of the [Administration settings](settings.md) contains two tools that check the family tree: one for technical problems in the database and one for implausible data.

## Check and Repair Database

This tool checks the Gramps database for internal inconsistencies and fixes the ones it can – analogous to the [Check and Repair Database tool](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) in Gramps Desktop.

Click **Check and Repair** and wait for the progress indicator to complete. The result is shown below the button:

- If no errors were found, a confirmation message is displayed.
- If errors were found, a summary of the fixes applied is shown.

Run this tool if you encounter unexpected errors or behavior that may be caused by database inconsistencies, such as missing relationships between objects.

## Verify the Data

While [Check and Repair Database](#check-and-repair-database) looks for *technical* inconsistencies, this tool looks for *implausible* data – analogous to the [Verify the Data tool](https://gramps-project.org/wiki/index.php/Gramps_5.0_Wiki_Manual_-_Tools#Verify_the_Data) in Gramps Desktop. It reports things that are not impossible but are unlikely enough to be worth a second look, such as a mother aged 12 or a person who lived to 130.

Under **Options** you can adjust the thresholds the tests use – maximum age, minimum and maximum age to marry or to have children, maximum number of children, and so on – as well as whether to estimate missing or inexact dates and whether to report invalid dates such as 31 February. The options you change are remembered in your browser for the next run; **Reset** restores the defaults.

Click **Verify the Data** to start. The check runs as a background task, and the findings are then listed under **Data Verification Results**. Nothing is changed by this tool: it only reports what it finds.

!!! note
    A finding is not proof of an error. Long lives and large age gaps do occur, so treat the results as a list of things to check rather than a list of things to fix.
