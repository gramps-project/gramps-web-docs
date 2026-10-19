# AI-keskustelun asetukset

!!! info
    AI-keskustelu vaatii Gramps Web API -version 2.5.0 tai uudemman. Versiossa 3.6.0 otettiin käyttöön työkalujen kutsumismahdollisuudet älykkäämpiin vuorovaikutuksiin.


Gramps Web API tukee kysymysten esittämistä sukututkimustietokannasta käyttämällä suuria kielimalleja (LLM) työkalujen kutsumisen avulla.

## Kuinka se toimii

AI-avustaja käyttää erikoistyökaluja sukututkimustietojesi kyselyyn suoraan. Nämä työkalut mahdollistavat avustajan etsiä tietokannasta täysimääräisellä tekstihaku, suodattaa henkilöitä/tapahtumia/perheitä/paikkoja tiettyjen kriteerien mukaan, laskea suhteita yksilöiden välillä ja noutaa täydellisiä tietueita, mukaan lukien muistiinpanot. Avustaja vastaa sitten perustuen niihin tietueisiin, joita se on tarkastellut, ja linkittää niihin vastauksessaan.

Gramps Web API 3.24:stä alkaen AI-keskustelu ei enää vaadi vektorin upotusmallia. Aikaisemmat versiot käyttivät myös *semanttista hakua* (retrieval-augmented generation, RAG), joka vertaa kysymyksen merkitystä tietokannan kaikkien objektien laskettujen numeeristen vektoreiden indeksiin. Semanttinen haku on poistettu käytöstä ja se poistetaan Gramps Web API 3.25:ssä, katso [Semanttinen haku (poistettu käytöstä)](#semantic-search-deprecated) alla.

Ottaaksesi käyttöön keskustelupisteen Gramps Web API:ssa, tarvitaan kaksi vaihetta:

1. Tarvittavien riippuvuuksien asentaminen,
2. LLM-toimittajan määrittäminen.

Kaksi vaihetta kuvataan alla vuorotellen. Lopuksi omistajan tai ylläpitäjän on [määritettävä, mitkä käyttäjät voivat käyttää keskustelutoimintoa](users.md#configuring-who-can-use-ai-chat) Käyttäjien hallinta -asetuksissa.

## Tarvittavien riippuvuuksien asentaminen

Gramps Webin standardidocker-kuvat sisältävät jo kaikki AI-keskusteluun tarvittavat riippuvuudet esiasennettuna.

Kun asennat Gramps Web API:n `pip`-komennolla (tätä ei tarvita käytettäessä Docker-kuvia), tarvittavat riippuvuudet asennetaan komennolla

```bash
pip install gramps_webapi[ai]
```

## Semanttinen haku (poistettu käytöstä)

!!! warning "Semanttinen haku on poistettu käytöstä"
    Semanttinen haku on poistettu käytöstä Gramps Web API 3.24:stä alkaen ja se poistetaan versiosta 3.25. AI-keskustelu ja [täysimääräinen tekstihaku](../user-guide/search.md) eivät tarvitse sitä. Poiston jälkeen `VECTOR_EMBEDDING_MODEL` -asetusta hyväksytään edelleen, mutta se ohitetaan. Jos asetat sen vain AI-keskustelun mahdollistamiseksi, voit poistaa sen nyt yhdessä muiden `VECTOR_EMBEDDING_*` -asetusten kanssa, mikä myös säästää muistin, jota upotusmalli tarvitsee.

Tämän osion muu sisältö kuvaa semanttista hakua palvelimille, jotka käyttävät sitä edelleen Gramps Web API 3.24:ssä.

Jos tarvittavat riippuvuudet on asennettu, semanttisen haun mahdollistaminen voi olla niin yksinkertaista kuin `VECTOR_EMBEDDING_MODEL` -konfiguraatioasetuksen asettaminen (esim. asettamalla `GRAMPSWEB_VECTOR_EMBEDDING_MODEL` ympäristömuuttuja), katso [Palvelimen konfigurointi](configuration.md). Tämä voi olla mikä tahansa merkkijono mallista, jota [Sentence Transformers](https://sbert.net/) -kirjasto tukee. Katso tämän projektin dokumentaatio yksityiskohtia ja saatavilla olevia malleja varten.

!!! warning
    Huomaa, että oletusdocker-kuvat eivät sisällä PyTorch-versiota, jossa on GPU-tuki. Jos sinulla on pääsy GPU:hun (mikä nopeuttaa semanttista indeksointia merkittävästi), asenna GPU-yhteensopiva versio PyTorchista.

Valittaessa mallia on useita seikkoja, jotka on otettava huomioon.

- Kun vaihdat mallia, sinun on manuaalisesti luotava semanttinen hakuintressi uudelleen puullesi (tai kaikille puille monipuisessa asetuksessa), muuten kohtaat virheitä tai merkityksettömiä tuloksia. Gramps Web havaitsee, kun määritetty upotusmalli ei enää vastaa olemassa olevaa indeksiä ja näyttää pysyvän ilmoituksen ylläpitäjille, joka kehottaa heitä käynnistämään täydellisen uudelleenindeksoinnin [Hallinta-asetuksista](../administration/settings.md#semantic-search-index).
- Mallit ovat kompromissi tarkkuuden/yhteensopivuuden ja laskenta-ajan/tallennustilan välillä. Jos et käytä Gramps Web API:ta järjestelmässä, jossa on pääsy tehokkaaseen GPU:hun, suuremmat mallit ovat yleensä käytännössä liian hitaita.
- Ellei koko tietokantasi ole englanniksi ja kaikkien käyttäjiesi odotetaan kysyvän keskustelukysymyksiä vain englanniksi, tarvitset monikielisen upotusmallin, joita on harvinaisempia kuin puhtaasti englanninkieliset mallit.

Jos mallia ei ole paikallisessa välimuistissa, se ladataan, kun Gramps Web API käynnistetään ensimmäistä kertaa uuden konfiguraation kanssa. Malli `sentence-transformers/distiluse-base-multilingual-cased-v2` on jo saatavilla paikallisesti käytettäessä standardidocker-kuvia. Tämä malli on hyvä lähtökohta ja tukee monikielistä syötettä.

Jaa oppimiasi asioita eri malleista yhteisön kanssa!

!!! info
    Sentence Transformers -kirjasto kuluttaa merkittävän määrän muistia, mikä voi aiheuttaa työntekijäprosessien tappamisen. Nyrkkisääntönä, kun semanttinen haku on käytössä, jokainen Gunicorn-työntekijä kuluttaa noin 200 MB muistia ja jokainen celery-työntekijä noin 500 MB muistia, vaikka ne olisivat käyttämättömiä, ja jopa 1 GB, kun lasketaan upotuksia. Katso [Rajoita CPU- ja muistinkäyttöä](cpu-limited.md) asetuksista, jotka rajoittavat muistinkäyttöä. Lisäksi on suositeltavaa varata riittävän suuri swap-osio estämään OOM-virheitä tilapäisten muistinkäyttöpiikkien vuoksi.

### Etäupotus-API:n käyttäminen

Paikallisen Sentence Transformers -mallin ajamisen vaihtoehtona voit käyttää etäistä OpenAI-yhteensopivaa upotus-API:a semanttiseen hakuun. Tämä on hyödyllistä, jos haluat siirtää upotusten laskennan erilliseen palveluun (esim. [Ollama](https://ollama.com/)), käyttää pilvipohjaista upotuspalvelua (esim. OpenAI) tai välttää Sentence Transformers- ja PyTorch-kirjastojen lataamista muistiin.

Etä-API:n on oltava yhteensopiva [OpenAI upotusten päätepisteen](https://platform.openai.com/docs/api-reference/embeddings) (`/v1/embeddings`) kanssa.

Käyttääksesi etäistä upotus-API:a, aseta seuraavat konfiguraatioasetukset (katso [Palvelimen konfigurointi](configuration.md)):

Avain | Kuvaus
----|-------------
`VECTOR_EMBEDDING_MODEL` | Mallin nimi, joka annetaan etäiselle toimittajalle
`VECTOR_EMBEDDING_BASE_URL` | Etä-API:n perus-URL
`VECTOR_EMBEDDING_API_KEY` | API-avain (tarvitaan vain, jos toimittaja vaatii todennusta)

#### Ollaman käyttäminen upotuksiin

Kun otat Gramps Webin käyttöön Docker Composen avulla, voit lisätä Ollama-palvelun ja käyttää sitä sekä upotuksiin että (valinnaisesti) LLM:ään:

```yaml
services:
  grampsweb: &grampsweb
    # ... olemassa oleva konfiguraatio ...
    environment:
      GRAMPSWEB_VECTOR_EMBEDDING_MODEL: nomic-embed-text
      GRAMPSWEB_VECTOR_EMBEDDING_BASE_URL: http://ollama:11434

  grampsweb_celery: &grampsweb_celery
    # ... olemassa oleva konfiguraatio ...
    environment:
      GRAMPSWEB_VECTOR_EMBEDDING_MODEL: nomic-embed-text
      GRAMPSWEB_VECTOR_EMBEDDING_BASE_URL: http://ollama:11434

  ollama:
    image: ollama/ollama
    container_name: ollama
    ports:
      - "11434:11434"
    volumes:
      - ollama_data:/root/.ollama

volumes:
  ollama_data:
```

Kun palvelut on käynnistetty, lataa upotusmalli Ollamaan:

```bash
docker compose exec ollama ollama pull nomic-embed-text
```

!!! info
    Kun käytät Ollamaa upotuksiin, Sentence Transformers- ja PyTorch-kirjastoja ei tarvita, mikä vähentää merkittävästi Gramps Web API -työntekijöiden muistinkäyttöä.

#### OpenAI:n käyttäminen upotuksiin

Käyttääksesi OpenAI:n upotus-API:a, aseta perus-URL OpenAI API:ksi ja anna API-avaimesi:

```yaml
environment:
  GRAMPSWEB_VECTOR_EMBEDDING_MODEL: text-embedding-3-small
  GRAMPSWEB_VECTOR_EMBEDDING_BASE_URL: https://api.openai.com
  GRAMPSWEB_VECTOR_EMBEDDING_API_KEY: sk-...
```

!!! warning
    Upotusmallin muuttaminen vaatii kaikkien tietueiden uudelleenindeksoinnin puullesi (tai kaikille puille monipuisessa asetuksessa), koska eri mallit tuottavat vektoreita eri ulottuvuuksilla.

## LLM-toimittajan määrittäminen

Viestintä LLM:n kanssa käyttää Pydantic AI -kehystä, joka tukee OpenAI-yhteensopivia API:ita. Tämä mahdollistaa paikallisesti otetun LLM:n käytön Ollaman kautta (katso [Ollama OpenAI -yhteensopivuus](https://ollama.com/blog/openai-compatibility)) tai isännöityjä API:ita, kuten OpenAI, Anthropic tai Hugging Face TGI (Text Generation Inference). LLM määritetään konfiguraatioasetusten `LLM_MODEL` ja `LLM_BASE_URL` kautta.

### Isännöidyn LLM:n käyttäminen OpenAI API:n kautta

Käyttäessäsi OpenAI API:a, `LLM_BASE_URL` voidaan jättää asettamatta, kun taas `LLM_MODEL` on asetettava yhdeksi OpenAI-malleista, esim. `gpt-4o-mini`. LLM käyttää työkalujen kutsumista vastatakseen kysymyksiin: se kysyy tietokannasta suoraan erikoistyökaluilla ja vastaa löytämistään tietueista. Se ei vaadi syvällistä sukututkimus- tai historiallista tietämystä. Siksi voit kokeilla, riittääkö pieni/halpa malli.

Sinun on myös rekisteröidyttävä tilille, saatava API-avain ja tallennettava se ympäristömuuttujaan `OPENAI_API_KEY`.

!!! info
    `LLM_MODEL` on konfiguraatioasetus; jos haluat asettaa sen ympäristömuuttujan kautta, käytä `GRAMPSWEB_LLM_MODEL` (katso [Konfigurointi](configuration.md)). `OPENAI_API_KEY` ei ole konfiguraatioasetus, vaan ympäristömuuttuja, jota Pydantic AI -kirjasto käyttää suoraan, joten sitä ei pitäisi etuliittää.

### Mistral AI:n käyttäminen

Käyttääksesi Mistral AI:n isännöityjä malleja, etuliitä mallin nimi `mistral:` kun asetat `LLM_MODEL`.

Sinun on rekisteröidyttävä Mistral AI -tilille, saatava API-avain ja tallennettava se ympäristömuuttujaan `MISTRAL_API_KEY`. `LLM_BASE_URL` -asetusta ei tarvitse määrittää, koska Pydantic AI käyttää automaattisesti oikeaa Mistral API -päätepistettä.

Esimerkkikonfiguraatio käytettäessä docker composea ympäristömuuttujilla:
```yaml
environment:
  GRAMPSWEB_LLM_MODEL: mistral:mistral-large-latest
  MISTRAL_API_KEY: your-mistral-api-key-here
```

### Paikallisen LLM:n käyttäminen Ollaman kautta

[Ollama](https://ollama.com/) on kätevä tapa ajaa LLM:ää paikallisesti. Tarkista Ollaman dokumentaatio yksityiskohtia varten. Huomaa, että LLM:t vaativat merkittäviä laskentatehoja, ja kaikki muut kuin pienimmät mallit ovat todennäköisesti liian hitaita ilman GPU-tukea. Koska avustaja luottaa työkalujen kutsumiseen, valitse malli, joka tukee työkaluja, kuten [`qwen2.5`](https://ollama.com/library/qwen2.5). Aloita pienellä variantilla, kuten `qwen2.5:7b`, ja kokeile suurempaa, jos vastaukset eivät ole riittävän hyviä. Jaa kokemuksesi yhteisön kanssa!

Kun otat Gramps Webin käyttöön Docker Composen avulla, voit lisätä Ollama-palvelun ja ohjata Gramps Webin siihen:

```yaml
services:
  grampsweb: &grampsweb
    # ... olemassa oleva konfiguraatio ...
    environment:
      GRAMPSWEB_LLM_MODEL: ollama:qwen2.5:7b
      GRAMPSWEB_LLM_BASE_URL: http://ollama:11434/v1/

  grampsweb_celery: &grampsweb_celery
    # ... olemassa oleva konfiguraatio ...
    environment:
      GRAMPSWEB_LLM_MODEL: ollama:qwen2.5:7b
      GRAMPSWEB_LLM_BASE_URL: http://ollama:11434/v1/

  ollama:
    image: ollama/ollama
    container_name: ollama
    ports:
      - "11434:11434"
    volumes:
      - ollama_data:/root/.ollama

volumes:
  ollama_data:
```

Kun palvelut on käynnistetty, lataa malli Ollamaan:

```bash
docker compose exec ollama ollama pull qwen2.5:7b
```

Muutama asia, jotka on syytä huomioida:

- Aseta `LLM_MODEL` Ollama-mallin nimeksi, mukaan lukien sen tagi (osa kaksoispisteen jälkeen, esim. `7b`), etuliitteellä `ollama:`. Etuliite saa Pydantic AI:n käyttämään mallille sen Ollama-spesifisiä asetuksia, mikä on suositeltava asetus.
- `LLM_BASE_URL` on päättäväisesti päätyttävä `/v1/`, esim. `http://ollama:11434/v1/`.
- `ollama:`-etuliitteellä ei tarvita `OPENAI_API_KEY`- eikä `OLLAMA_BASE_URL`-ympäristömuuttujaa. Jos `LLM_BASE_URL` ei ole asetettu, Gramps Web siirtyy `OLLAMA_BASE_URL`:iin.
- Vaihtoehtoisesti voit jättää etuliitteen pois (esim. `LLM_MODEL: qwen2.5:7b`) ja käyttää Ollamaa sen yleisen OpenAI-yhteensopivan API:n kautta. Tässä tapauksessa sinun on myös asetettava `OPENAI_API_KEY` ympäristömuuttujaan `ollama` (mikä tahansa ei-tyhjää arvoa toimii).

Jos kohtaat ongelmia Ollaman kanssa, voit ottaa käyttöön virheenkorjauslokituksen asettamalla ympäristömuuttujan `OLLAMA_DEBUG=1` Ollama-palvelun ympäristöön.

!!! info
    Jos käytät Ollamaa Gramps Web AI -keskustelussa, tue yhteisöä täydentämällä tätä dokumentaatiota kaikilla puuttuvilla tiedoilla.

### Muiden toimittajien käyttäminen

Älä epäröi lähettää dokumentaatiota muista toimittajista ja jakaa kokemuksiasi yhteisön kanssa!
