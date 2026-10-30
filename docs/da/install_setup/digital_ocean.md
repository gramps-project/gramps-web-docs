# Gramps Web DigitalOcean 1-Click App

I stedet for [at opsætte Gramps Web selv](deployment.md), kan du også bruge [Gramps Web DigitalOcean 1-Click App](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy). Digital Ocean hoster demo-versionen af Gramps Web.

<a href="https://www.digitalocean.com/?refcode=b1d13ebe86ac&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="DigitalOcean Referral Badge" /></a>

Som en del af opsætningsproceduren skal du tilmelde dig en konto hos DigitalOcean og vælge en betalt plan for "droplet" (virtuel maskine) at bruge.

Det kan argumenteres for, at dette i øjeblikket er den nemmeste måde at implementere din egen, selvhostede Gramps Web-instans, sikret med SSL, uden at bruge dit eget hardware.

!!! info
    Bemærk, at du vil betale DigitalOcean for hostingtjenesterne. Gramps open source-projektet tilbyder ikke betalt support.

## Trin 1: Opret en DigitalOcean-konto

Opret en konto på [DigitalOcean](https://www.digitalocean.com/), hvis du ikke allerede har en.

## Trin 2: Opret droplet

- Gå til [Gramps Web 1-Click App](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy) og klik på "Opret Gramps Web Droplet".
- Vælg en plan med mindst 2 GB RAM.
- Opsæt autentificering til din droplet.
- Klik på "Opret Droplet".

## Trin 3: Opsæt et domænenavn

Du skal bruge et domænenavn (eller subdomæne). Hvis du ejer et domæne, skal du pege det mod IP-adressen på din droplet. Ellers kan du bruge en gratis tjeneste som [DuckDNS](https://www.duckdns.org/).

## Trin 4: Log ind på din droplet

SSH ind i din droplet. Du bør blive præsenteret for beskeden "Velkommen til opsætningen af Gramps Web DigitalOcean 1-click app!". Hvis dette ikke er tilfældet, skal du vente et par minutter og prøve igen (installationen er ikke færdig endnu).

Opsætningsscriptet vil bede dig om domænenavnet (f.eks. `mygrampswebinstance.duckdns.org`) og en e-mailadresse (nødvendig til Let's Encrypt-certifikatet). Valgfrit vil det også spørge om SMTP-indstillingerne, som Gramps Web bruger til at sende e-mails, f.eks. til nulstilling af adgangskoder; lad SMTP-værten være tom for at springe dette over.

Når dette er gjort, skal du vente på, at opsætningen er færdig i baggrunden.

## Trin 5: Start Gramps Web

Din Gramps Web-instans bør nu være tilgængelig på roden af dit domæne, med et gyldigt SSL-certifikat, og den bør vise første gang-assistenten.

## Ændring af konfigurationen senere

Opsætningsscriptet gemmer basis-URL'en og e-mailindstillingerne i filen `/root/letsencrypt.env` som [konfigurationsmuligheder](configuration.md) præfiks med `GRAMPSWEB_`, f.eks.

```
GRAMPSWEB_EMAIL_HOST=smtp.example.com
GRAMPSWEB_EMAIL_PORT=587
GRAMPSWEB_EMAIL_USE_STARTTLS=true
```

For at tilføje eller ændre indstillinger, rediger denne fil på droplet og anvend ændringen med

```bash
cd /opt/grampsweb && docker compose up -d
