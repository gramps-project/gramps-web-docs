# AI-keskustelun asetukset

!!! info
    AI-keskustelu vaatii Gramps Web API -version 2.5.0 tai uudemman. Versio 3.6.0 esitteli työkalukutsumismahdollisuuksia älykkäämpiin vuorovaikutuksiin.


Gramps Web API tukee kysymysten esittämistä sukututkimustietokannasta suurten kielimallien (LLM) avulla tekniikalla, jota kutsutaan hakua parantavaksi generoinniksi (RAG) yhdistettynä työkalukutsumiseen.

## Kuinka se toimii

AI-avustaja käyttää kahta täydentävää lähestymistapaa:

**Hakua Parantava Generointi (RAG)**: *vektorin upotuksen malli* luo indeksin kaikista objekteista Gramps-tietokannassa numeeristen vektorien muodossa, jotka koodavat objektien merkityksiä. Kun käyttäjä esittää kysymyksen, kysymys muunnetaan myös vektoriksi ja verrataan tietokannan objekteihin. Tämä *semanttinen haku* palauttaa objektit, jotka ovat semanttiselta kannalta kaikkein samankaltaisimpia kysymyksen kanssa.

**Työkalukutsuminen (v3.6.0+)**: AI-avustaja voi nyt käyttää erikoistyökaluja sukututkimustietojesi kyselyyn suoraan. Nämä työkalut mahdollistavat avustajan etsiä tietokannasta, suodattaa ihmisiä/tapahtumia/perheitä/paikkoja tiettyjen kriteerien mukaan, laskea suhteita yksilöiden välillä ja noutaa yksityiskohtaista objektitietoa. Tämä tekee avustajasta paljon kykenevämmän vastaamaan monimutkaisiin sukututkimuskysymyksiin tarkasti.

AI-keskustelupisteen mahdollistamiseksi Gramps Web API:ssa tarvitaan kolme vaihetta:

1. Vaadittavien riippuvuuksien asentaminen,
2. Semanttisen haun mahdollistaminen,
3. LLM-toimittajan määrittäminen.

Nämä kolme vaihetta kuvataan alla vuorotellen. Lopuksi omistajan tai ylläpitäjän on [määritettävä, mitkä käyttäjät voivat käyttää keskustelutoimintoa](users.md#configuring-who-can-use-ai-chat) Käyttäjien hallinta -asetuksissa.

## Vaadittavien riippuvuuksien asentaminen

AI-keskustelu vaatii Sentence Transformers- ja PyTorch-kirjastojen asentamista.

Gramps Webin standardi Docker-kuvat sisältävät jo valmiiksi nämä kirjastot `amd64` (esim. 64-bittinen työpöytä-PC) ja `arm64` (esim. 64-bittinen Raspberry Pi) arkkitehtuureille. Valitettavasti AI-keskustelua ei tueta `armv7` (esim. 32-bittinen Raspberry Pi) arkkitehtuurilla PyTorch-tuen puutteen vuoksi.

Kun asennat Gramps Web API:n `pip`-komennolla (tätä ei tarvita, kun käytetään Docker-kuvia), tarvittavat riippuvuudet asennetaan komennolla

```bash
pip install gramps_webapi[ai]
```

## Semanttisen haun mahdollistaminen

Jos tarvittavat riippuvuudet on asennettu, semanttisen haun mahdollistaminen voi olla niin yksinkertaista kuin `VECTOR_EMBEDDING_MODEL` -konfiguraatio-option asettaminen (esim. asettamalla `GRAMPSWEB_VECTOR_EMBEDDING_MODEL` ympäristömuuttuja), katso [Palvelimen konfigurointi](configuration.md). Tämä voi olla mikä tahansa merkkijono, joka on tuettu [Sentence Transformers](https://sbert.net/) -kirjastossa. Katso tämän projektin dokumentaatio yksityiskohtia ja saatavilla olevia malleja varten.

!!! warning
    Huomaa, että oletusarvoiset Docker-kuvat eivät sisällä PyTorch-versiota, jossa on GPU-tuki. Jos sinulla on pääsy GPU:hun (mikä nopeuttaa semanttista indeksointia merkittävästi), asenna GPU-ominaisuuksilla varustettu versio PyTorchista.

Malleja valitessa on useita huomioitavia seikkoja.

- Kun vaihdat mallia, sinun on manuaalisesti luotava semanttinen hakuinto uudelleen puullesi (tai kaikille puille monipuisessa kokoonpanossa), muuten kohtaat virheitä tai merkityksettömiä tuloksia. Gramps Web havaitsee, kun määritetty upotusmalli ei enää vastaa olemassa olevaa indeksiä ja näyttää jatkuvan ilmoituksen ylläpitäjille, joka kehottaa heitä käynnistämään täydellisen uudelleenindeksoinnin [Hallinta-asetuksista](../administration/settings.md#semantic-search-index).
- Mallit ovat kompromissi tarkkuuden/yhteensopivuuden ja laskenta-ajan/tallennustilan välillä. Jos et käytä Gramps Web API:ta järjestelmässä, jossa on pääsy tehokkaaseen GPU:hun, suuremmat mallit ovat käytännössä yleensä liian hitaita.
- Ellet koko tietokantaasi ole englanniksi ja kaikkien käyttäjiesi odotetaan kysyvän keskustelukysymyksiä vain englanniksi, tarvitset monikielisen upotusmallin, joita on harvinaisempia kuin puhtaat englanninkieliset mallit.

Jos mallia ei ole paikallisessa välimuistissa, se ladataan, kun Gramps Web API käynnistetään ensimmäistä kertaa uuden konfiguraation kanssa. Malli `sentence-transformers/distiluse-base-multilingual-cased-v2` on jo saatavilla paikallisesti käytettäessä standardi Docker-kuvia. Tämä malli on hyvä lähtökohta ja tukee monikielistä syöttöä.

Jaa oppimiasi asioita eri malleista yhteisön kanssa!

!!! info
    Sentence Transformers -kirjasto kuluttaa merkittävän määrän muistia, mikä voi aiheuttaa työntekijäprosessien kaatumisen. Nyrkkisääntönä, kun semanttinen haku on käytössä, jokainen Gunicorn-työntekijä kuluttaa noin 200 MB muistia ja jokainen celery-työntekijä noin 500 MB muistia jopa ollessaan käyttämättömänä, ja jopa 1 GB laskettaessa upotuksia. Katso [Rajoita CPU- ja muistinkäyttöä](cpu-limited.md) asetuksista, jotka rajoittavat muistinkäyttöä. Lisäksi on suositeltavaa varata riittävän suuri swap-osio estämään OOM-virheitä tilapäisten muistinkäyttöpiikkien vuoksi.

## Etäupotus-API:n käyttäminen

Paikallisen Sentence Transformers -mallin käyttämisen vaihtoehtona voit käyttää etäistä OpenAI-yhteensopivaa upotus-API:a semanttiseen hakuun. Tämä on hyödyllistä, jos haluat siirtää upotusten laskennan erilliseen palveluun (esim. [Ollama](https://ollama.com/)), käyttää pilvipalveluntarjoajaa (esim. OpenAI) tai välttää Sentence Transformers- ja PyTorch-riippuvuuksien asentamista.

Etä-API:n on oltava yhteensopiva [OpenAI upotusten päätepisteen](https://platform.openai.com/docs/api-reference/embeddings) (`/v1/embeddings`) kanssa.

Käyttääksesi etäupotus-API:a, aseta seuraavat konfiguraatio-option (katso [Palvelimen konfigurointi](configuration.md)):

Avain | Kuvaus
----|-------------
`VECTOR_EMBEDDING_MODEL` | Mallin nimi, joka annetaan etätoimittajalle
`VECTOR_EMBEDDING_BASE_URL` | Etä-API:n perus-URL
`VECTOR_EMBEDDING_API_KEY` | API-avain (tarvitaan vain, jos toimittaja vaatii todennusta)

### Ollaman käyttäminen upotuksiin

Kun otat Gramps Webin käyttöön Docker Compose -työkalulla, voit lisätä Ollama-palvelun ja käyttää sitä sekä upotuksiin että (valinnaisesti) LLM:ään:

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

Kun olet käynnistänyt palvelut, lataa upotusmalli Ollamaan:

```bash
docker compose exec ollama ollama pull nomic-embed-text
```

!!! info
    Kun käytät Ollamaa upotuksiin, Sentence Transformers- ja PyTorch-kirjastoja ei tarvita, mikä vähentää merkittävästi Gramps Web API:n työntekijöiden muistinkäyttöä.

### OpenAI:n käyttäminen upotuksiin

Käyttääksesi OpenAI upotusten API:a, aseta perus-URL OpenAI API:iin ja anna API-avain:

```yaml
environment:
  GRAMPSWEB_VECTOR_EMBEDDING_MODEL: text-embedding-3-small
  GRAMPSWEB_VECTOR_EMBEDDING_BASE_URL: https://api.openai.com
  GRAMPSWEB_VECTOR_EMBEDDING_API_KEY: sk-...
```

!!! warning
    Upotusmallin muuttaminen vaatii kaikkien tietueiden uudelleenindeksoimista puullesi (tai kaikille puille monipuisessa kokoonpanossa), koska eri mallit tuottavat vektoreita eri ulottuvuuksilla.

## LLM-toimittajan määrittäminen

Viestintä LLM:n kanssa käyttää Pydantic AI -kehystä, joka tukee OpenAI-yhteensopivia API:ita. Tämä mahdollistaa paikallisesti otetun LLM:n käytön Ollaman kautta (katso [Ollama OpenAI yhteensopivuus](https://ollama.com/blog/openai-compatibility)) tai isännöityjä API:ita kuten OpenAI, Anthropic tai Hugging Face TGI (Tekstigeneroinnin Inference). LLM määritetään konfiguraatioparametreilla `LLM_MODEL` ja `LLM_BASE_URL`.

### Isännöidyn LLM:n käyttäminen OpenAI API:n kautta

Kun käytät OpenAI API:a, `LLM_BASE_URL` voidaan jättää asettamatta, kun taas `LLM_MODEL` on asetettava yhdeksi OpenAI-malleista, esim. `gpt-4o-mini`. LLM käyttää sekä RAG:ta että työkalukutsumista kysymyksiin vastaamiseen: se valitsee olennaista tietoa semanttisen haun tuloksista ja voi suoraan kysyä tietokannasta erikoistyökalujen avulla. Se ei vaadi syvällistä sukututkimus- tai historiallista tietämystä. Siksi voit kokeilla, riittääkö pieni/halpa malli.

Sinun on myös rekisteröidyttävä tilille, saatava API-avain ja tallennettava se `OPENAI_API_KEY` ympäristömuuttujaan.

!!! info
    `LLM_MODEL` on konfiguraatioparametri; jos haluat asettaa sen ympäristömuuttujan kautta, käytä `GRAMPSWEB_LLM_MODEL` (katso [Konfigurointi](configuration.md)). `OPENAI_API_KEY` ei ole konfiguraatioparametri, vaan ympäristömuuttuja, jota Pydantic AI -kirjasto käyttää suoraan, joten sitä ei tule etuliittää.

### Mistral AI:n käyttäminen

Käyttääksesi Mistral AI:n isännöityjä malleja, etuliitä mallin nimi `mistral:` kun asetat `LLM_MODEL`.

Sinun on rekisteröidyttävä Mistral AI -tilille, saatava API-avain ja tallennettava se `MISTRAL_API_KEY` ympäristömuuttujaan. `LLM_BASE_URL` -asetusta ei tarvitse määrittää, koska Pydantic AI käyttää automaattisesti oikeaa Mistral API -päätepistettä.

Esimerkkikonfiguraatio käytettäessä Docker Composea ympäristömuuttujilla:
```yaml
environment:
  GRAMPSWEB_LLM_MODEL: mistral:mistral-large-latest
  MISTRAL_API_KEY: your-mistral-api-key-here
  GRAMPSWEB_VECTOR_EMBEDDING_MODEL: sentence-transformers/distiluse-base-multilingual-cased-v2
```

### Paikallisen LLM:n käyttäminen Ollaman kautta

[Ollama](https://ollama.com/) on kätevä tapa ajaa LLM:ää paikallisesti. Katso Ollama-dokumentaatio yksityiskohtia varten. Huomaa, että LLM:t vaativat merkittäviä laskentatehoja, ja kaikki paitsi pienimmät mallit ovat todennäköisesti liian hitaita ilman GPU-tukea. Voit kokeilla, täyttääkö [`tinyllama`](https://ollama.com/library/tinyllama) tarpeesi. Jos ei, kokeile yhtä suuremmista malleista. Jaa kokemuksesi yhteisön kanssa!

Kun otat Gramps Webin käyttöön Docker Compose -työkalulla, voit lisätä Ollama-palvelun

```yaml
services:
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

ja sitten asettaa `LLM_BASE_URL` -konfiguraatioparametrin arvoon `http://ollama:11434/v1`. Aseta `LLM_MODEL` malliksi, jota Ollama tukee, ja lataa se säiliöösi komennolla `ollama pull <malli>`. Lopuksi aseta `OPENAI_API_KEY` arvoksi `ollama`.

Ongelmatilanteiden ratkaisemiseksi Ollaman kanssa voit ottaa käyttöön virheenkorjauslokituksen asettamalla ympäristömuuttuja `OLLAMA_DEBUG=1` Ollama-palvelun ympäristöön.

!!! info
    Jos käytät Ollamaa Gramps Web AI -keskustelussa, tue yhteisöä täydentämällä tätä dokumentaatiota kaikilla puuttuvilla tiedoilla.

### Muiden toimittajien käyttäminen

Älä epäröi lähettää dokumentaatiota muista toimittajista ja jakaa kokemuksiasi yhteisön kanssa!
