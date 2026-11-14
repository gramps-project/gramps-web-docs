# Tjek og verificer data

Afsnittet **Familietræbehandling** i [Administrationsindstillinger](settings.md) indeholder to værktøjer, der tjekker familietræet: et til tekniske problemer i databasen og et til usandsynlige data.

## Tjek og reparation af database

Dette værktøj tjekker Gramps-databasen for interne inkonsistenser og retter dem, det kan – analogt med [Tjek og reparation af databaseværktøjet](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) i Gramps Desktop.

Klik på **Tjek og reparation** og vent på, at fremdriftsindikatoren er færdig. Resultatet vises under knappen:

- Hvis der ikke blev fundet fejl, vises en bekræftelsesmeddelelse.
- Hvis der blev fundet fejl, vises et resumé af de anvendte reparationer.

Kør dette værktøj, hvis du støder på uventede fejl eller adfærd, der kan skyldes databaseinkonsistenser, såsom manglende relationer mellem objekter.

## Verificer dataene

Mens [Tjek og reparation af database](#check-and-repair-database) leder efter *tekniske* inkonsistenser, leder dette værktøj efter *usandsynlige* data – analogt med [Verificer dataværktøjet](https://gramps-project.org/wiki/index.php/Gramps_5.0_Wiki_Manual_-_Tools#Verify_the_Data) i Gramps Desktop. Det rapporterer ting, der ikke er umulige, men som er usandsynlige nok til at være værd at se nærmere på, såsom en mor på 12 år eller en person, der levede til 130.

Under **Indstillinger** kan du justere tærsklerne, som testene bruger – maksimal alder, minimums- og maksimumsalder for at gifte sig eller få børn, maksimalt antal børn, og så videre – samt om der skal estimeres manglende eller unøjagtige datoer, og om der skal rapporteres ugyldige datoer såsom 31. februar.

Klik på **Verificer dataene** for at starte. Tjekket kører som en baggrundsopgave, og resultaterne listes derefter under **Resultater af dataverificering**. Intet ændres af dette værktøj: det rapporterer kun, hvad det finder.

!!! note
    Et fund er ikke bevis på en fejl. Lange liv og store aldersforskelle forekommer, så behandl resultaterne som en liste over ting, der skal tjekkes, snarere end en liste over ting, der skal rettes.
