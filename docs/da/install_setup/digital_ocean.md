# Gramps Web DigitalOcean-appen med installation med ét klik

I stedet for [selv at konfigurere Gramps Web](deployment.md) kan du også bruge [Gramps Web DigitalOcean-appen med installation med ét klik](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy). Digital Ocean hoster demoversionen af Gramps Web.

<a href="https://www.digitalocean.com/?refcode=b1d13ebe86ac&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="DigitalOcean-henvisningsbadge" /></a>

Som en del af konfigurationsproceduren skal du oprette en konto hos DigitalOcean og vælge en betalingsplan for den "droplet" (virtuelle maskine), der skal bruges.

Dette er muligvis i øjeblikket den enkleste måde at implementere din egen, selvhostede Gramps Web-instans på, sikret med SSL, uden at bruge din egen hardware.

!!! info
    Bemærk, at du skal betale DigitalOcean for hostingtjenesterne. Gramps' open source-projekt tilbyder ikke betalt support.

## Trin 1: Opret en DigitalOcean-konto

Opret en konto hos [DigitalOcean](https://www.digitalocean.com/), hvis du ikke allerede har en.

## Trin 2: Opret dropleten

- Gå til [Gramps Web-appen med installation med ét klik](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy), og klik på "Create Gramps Web Droplet".
- Vælg en plan med mindst 2 GB RAM.
- Konfigurer godkendelse til din droplet
- Klik på "Create Droplet"

## Trin 3: Konfigurer et domænenavn

Du skal bruge et domænenavn (eller underdomæne). Hvis du ejer et domæne, skal du pege det på din droplets IP-adresse. Ellers kan du bruge en gratis tjeneste som f.eks. [DuckDNS](https://www.duckdns.org/).

## Trin 4: Log ind på din droplet

Opret forbindelse til din droplet via SSH. Du bør få vist meddelelsen "Welcome to the Gramps Web DigitalOcean 1-click app setup!". Hvis det ikke er tilfældet, skal du vente et par minutter og prøve igen (installationen er endnu ikke færdig).

Konfigurationsscriptet beder dig om domænenavnet (f.eks. `mygrampswebinstance.duckdns.org`) og en e-mailadresse (nødvendig til Let's Encrypt-certifikatet). Det vil også eventuelt bede om de SMTP-indstillinger, som Gramps Web bruger til at sende e-mails, f.eks. ved nulstilling af adgangskoder; lad SMTP-værten være tom for at springe dette over.

Når dette er gjort, skal du vente på, at konfigurationen færdiggøres i baggrunden

## Trin 5: Start Gramps Web

Din Gramps Web-instans bør nu være tilgængelig på roden af dit domæne med et gyldigt SSL-certifikat, og den bør vise førstegangsassistenten.

## Ændring af konfigurationen senere

Konfigurationsscriptet gemmer basis-URL'en og e-mailindstillingerne i filen `/root/letsencrypt.env` som [konfigurationsindstillinger](configuration.md) med præfikset `GRAMPSWEB_`, f.eks.

```
GRAMPSWEB_EMAIL_HOST=smtp.example.com
GRAMPSWEB_EMAIL_PORT=587
GRAMPSWEB_EMAIL_USE_STARTTLS=true
```

Hvis du vil tilføje eller ændre indstillinger, skal du redigere denne fil på dropleten og anvende ændringen med

```bash
cd /opt/grampsweb && docker compose up -d
```
