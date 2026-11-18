# Tjek og verificer data

Afdelingen **Familietræbehandling** i [Administrationsindstillinger](settings.md) indeholder to værktøjer, der tjekker familietræet: et til tekniske problemer i databasen og et til usandsynlige data.

## Tjek og reparer database

Dette værktøj tjekker Gramps-databasen for interne uoverensstemmelser og reparerer dem, det kan – analogt med [Tjek og reparer databaseværktøjet](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) i Gramps Desktop.

Klik på **Tjek og reparer** og vent på, at fremdriftsindikatoren er færdig. Resultatet vises under knappen:

- Hvis der ikke blev fundet fejl, vises en bekræftelsesmeddelelse.
- Hvis der blev fundet fejl, vises et resumé af de anvendte reparationer.

Kør dette værktøj, hvis du støder på uventede fejl eller adfærd, der kan skyldes database-uoverensstemmelser, såsom manglende relationer mellem objekter.

## Verificer dataene

Mens [Tjek og reparer database](#check-and-repair-database) ser efter *tekniske* uoverensstemmelser, ser dette værktøj efter *usandsynlige* data – analogt med [Verificer dataværktøjet](https://gramps-project.org/wiki/index.php/Gramps_5.0_Wiki_Manual_-_Tools#Verify_the_Data) i Gramps Desktop. Det rapporterer ting, der ikke er umulige, men som er usandsynlige nok til at være værd at se nærmere på, såsom en mor på 12 år eller en person, der levede til 130.

Under **Indstillinger** kan du justere tærsklerne, som testene bruger – maksimal alder, minimums- og maksimumsalder for at gifte sig eller få børn, maksimalt antal børn osv. – samt om der skal estimeres manglende eller unøjagtige datoer, og om der skal rapporteres ugyldige datoer som 31. februar. De indstillinger, du ændrer, huskes i din browser til næste kørsel; **Nulstil** gendanner standardindstillingerne.

Klik på **Verificer dataene** for at starte. Tjekket kører som en baggrundsopgave, og resultaterne listes derefter under **Dataverifikationsresultater**. Intet ændres af dette værktøj: det rapporterer kun, hvad det finder.

!!! note
    Et fund er ikke bevis på en fejl. Lange liv og store aldersforskelle forekommer, så behandl resultaterne som en liste over ting, der skal tjekkes, snarere end en liste over ting, der skal rettes.
