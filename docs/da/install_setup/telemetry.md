# Telemetri

Fra og med Gramps Web API version 3.2.0 sender Gramps Web som standard fuldt anonymiserede telemetridata hver 24. time til et analyse-endpoint, der styres af Gramps Web-teamet. Denne side indeholder oplysninger om de indsamlede telemetridata, hvordan de bruges, og hvordan man deaktiverer det, hvis ønskes.

## Hvilke data indsamles?

Telemetridataene er en lille JSON-payload af følgende form:

```json
{
  "server_uuid": "c04325bfa7ae4578bcf134ec8fc046a7",
  "tree_uuid": "abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890",
  "timestamp": 1701234567,
}
```

Som du selv kan tjekke [i kildekoden](https://github.com/gramps-project/gramps-web-api/blob/master/gramps_webapi/api/telemetry.py#L83-L87), er server- og træidentifikatorerne unikke for serveren og træet, men de indeholder ikke nogen personligt identificerbare oplysninger. `timestamp` er den aktuelle tid som et Unix-timestamp.

## Hvorfor indsamles dataene?

At sende en unik identifikator én gang om dagen giver Gramps Web-teamet mulighed for at spore, hvor mange unikke servere der kører Gramps Web, og hvor mange unikke træer der anvendes.

Dette er vigtigt for at forstå indvirkningen på eksterne tjenester, der bruges af Gramps Web, såsom kortfliser.

## Hvordan indsamles dataene?

Når der sendes en anmodning til din Gramps Web API-server, tjekker den, om telemetri er blevet sendt inden for de sidste 24 timer (ved at tjekke en nøgle i den lokale cache). Hvis ikke, sendes ovenstående payload til et endpoint, der logger dataene.

Logging-endpointet er hostet på Google Cloud Run og er direkte implementeret fra et [open source-repository](https://github.com/DavidMStraub/cloud-run-telemetry), så du kan inspicere, hvordan dataene behandles.

## Hvad vil der blive gjort med dataene?

Først og fremmest vil ingen data ud over den anonymiserede payload, der hypotetisk kunne indsamles (såsom serverens IP-adresse), blive brugt af Gramps Web-teamet.

De indsamlede anonymiserede ID'er og tidsstempel vil blive aggregeret for at producere grafer såsom:

- Antal aktive Gramps Web-installationer som funktion af tid
- Antal aktive Gramps Web-træer som funktion af tid

Disse grafer vil blive offentliggjort på Gramps Web-dokumentationssiden.

## Hvordan deaktiveres telemetri?

Da statistikdataene er nyttige for Gramps Web-teamet, og vi har sikret os, at der ikke sendes nogen personligt identificerbare data, **ville vi være taknemmelige, hvis du ikke deaktiverer telemetri!**

Ikke desto mindre giver Gramps Web brugerne fuld kontrol, så selvfølgelig kan du vælge at deaktivere funktionen, hvis du ønsker det.

For at gøre dette skal du blot indstille konfigurationsmuligheden `DISABLE_TELEMETRY` til `True` (f.eks. ved at indstille miljøvariablen `GRAMPSWEB_DISABLE_TELEMETRY` til `true` &ndash; se [konfigurationsdokumentationen](configuration.md) for detaljer).
