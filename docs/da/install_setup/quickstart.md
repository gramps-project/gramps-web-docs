For at prøve Gramps Web på din lokale computer (Linux, Mac eller Windows) uden at forstyrre din Gramps Desktop-installation, kan du bruge Docker med følgende kommando:

```bash
docker run -p "5055:5000" -e TREE=new ghcr.io/gramps-project/grampsweb:latest
```

Dette vil gøre en ny, tom Gramps Web-instans tilgængelig på [http://localhost:5055](http://localhost:5055), hvor du kan oprette en admin-bruger og importere en Gramps XML-fil.

!!! info
    Da denne enkle opsætning ikke tillader at køre lange opgaver i en separat proces, kan importen af en stor Gramps XML-fil fejle på grund af en timeout i første gangs assistenten.


For at bruge mediefiler fra din computer kan du montere Gramps mediemappen ind i containeren med

```bash
docker run -p "5055:5000" -e TREE=new \
  -v /path/to/my/gramps_media_folder:/app/media \
  ghcr.io/gramps-project/grampsweb:latest
```

Bemærk, at dette ikke vil bevare de ændringer, du laver i databasen, når du genstarter containeren. For at opsætte Gramps Web korrekt, fortsæt med at læse om [Deployment](deployment.md).
