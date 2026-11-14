# Søgeindeks

Afsnittet **Søgeindeks** i [Administrationsindstillinger](settings.md) viser tilstanden af fuldtekst søgeindekset og giver dig mulighed for at genopbygge det.

## Administrer søgeindeks

Gramps Web opretholder et fuldtekst søgeindeks, der normalt opdateres automatisk, når data ændres. Statusindikatoren viser, hvor mange objekter der i øjeblikket er indekseret i forhold til det samlede antal objekter.

Klik på **Opdater søgeindeks** for at udløse en fuld genopbygning. En statusindikator vises, mens opgaven kører i baggrunden. Dette er sjældent nødvendigt.

Hvis et træ endnu ikke har noget søgeindeks, for eksempel efter en serveropgradering, der ændrede indeksformatet, bygger Gramps Web det i baggrunden, første gang træet åbnes. Mens det bliver bygget, viser sektionen "Søgeindekset bliver bygget." i stedet for tællerne, **Opdater søgeindeks** er deaktiveret, og søgeresultaterne kan være ufuldstændige. Bygningen vises i [Notifikationer](../user-guide/notifications.md) som opgaven "Opdater søgeindeks".
