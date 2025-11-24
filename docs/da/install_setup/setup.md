# Gramps Web Installation / Opsætning

Dette afsnit omhandler installation og opsætning af Gramps Web samt andre muligheder for at komme i gang.

## Kom i gang med Gramps Web

Gramps Web er en webapp, der kører på en server og tilgås via webbrowseren. Den er beregnet til at være tilgængelig for autentificerede brugere via internettet.

Hvis du vil bruge Gramps Web til dine genealogiske forskningsdata, skal du vælge en af følgende muligheder:

1. Selvhost på dit eget hardware
2. Selvhost i skyen
3. Tilmeld dig en hosted instans

Mens den første mulighed giver dig maksimal fleksibilitet og kontrol, kan det også være teknisk udfordrende.

!!! tip
    Et af de vigtigste principper for Gramps Web er at sætte brugerne i kontrol over deres egne data når som helst, så migrering af data fra en instans til en anden er enkel. Bekymr dig ikke om at blive låst fast efter at have valgt en af mulighederne!

## Selvhost på dit eget hardware

Den mest bekvemme måde at selvhoste Gramps Web på er via Docker Compose. Vi leverer også Docker-billeder til ARM-arkitekturen, så du kan køre Gramps Web på en Raspberry Pi i din kælder.

Se [Deploy med Docker](deployment.md) for installationsinstruktioner.

## Selvhost i skyen

Installation af Gramps Web kan være mere udfordrende end andre, simple webapplikationer og er ikke kompatibel med almindelige "shared hosting" udbydere. Du kan tilmelde dig en virtuel server og installere Gramps Web [manuelt](deployment.md).

En enklere mulighed er at bruge et forudinstalleret cloud-billede. Et eksempel er vores [DigitalOcean 1-click app](digital_ocean.md).

## Tilmeld dig en hosted instans

En hosted Gramps Web er den nemmeste måde at komme i gang med Gramps Web, da der ikke kræves installation eller konfiguration.

Her er en liste over dedikerede hostingudbydere for Gramps Web (Gramps open source samfundet påtager sig ikke ansvar for deres tjenester):

- Grampshub ([www.grampshub.com](https://www.grampshub.com)), tilbudt af en af de vigtigste bidragsydere til Gramps Web

Hvis du bruger en hosted mulighed for Gramps Web, kan du springe resten af dette afsnit over og gå direkte til [Administration](../administration/admin.md) afsnittet.
