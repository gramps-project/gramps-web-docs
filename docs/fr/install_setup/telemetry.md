# Télémétrie

À partir de la version 3.2.0 de l'API Web Gramps, Gramps Web envoie par défaut des données de télémétrie entièrement anonymisées toutes les 24 heures à un point de terminaison d'analyse contrôlé par l'équipe de Gramps Web. Cette page contient des informations sur les données de télémétrie collectées, comment elles sont utilisées et comment les désactiver si vous le souhaitez.

## Quelles données sont collectées ?

Les données de télémétrie sont une petite charge utile JSON de la forme suivante :

```json
{
  "server_uuid": "c04325bfa7ae4578bcf134ec8fc046a7",
  "tree_uuid": "abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890",
  "timestamp": 1701234567,
}
```

Comme vous pouvez le vérifier vous-même [dans le code source](https://github.com/gramps-project/gramps-web-api/blob/master/gramps_webapi/api/telemetry.py#L83-L87), les identifiants de serveur et d'arbre sont uniques pour le serveur et l'arbre, mais ils ne contiennent aucune information personnellement identifiable. Le `timestamp` est l'heure actuelle sous forme de timestamp Unix.

## Pourquoi les données sont-elles collectées ?

L'envoi d'un identifiant unique une fois par jour permet à l'équipe de Gramps Web de suivre combien de serveurs uniques exécutent Gramps Web et combien d'arbres uniques sont utilisés.

C'est important pour comprendre l'impact sur les services externes utilisés par Gramps Web, tels que les tuiles de carte.

## Comment les données sont-elles collectées ?

Lorsqu'une requête est faite à votre serveur API Gramps Web, il vérifie si la télémétrie a été envoyée au cours des 24 dernières heures (en vérifiant une clé dans le cache local). Si ce n'est pas le cas, la charge utile ci-dessus est envoyée à un point de terminaison qui enregistre les données.

Le point de terminaison d'enregistrement est hébergé sur Google Cloud Run et est directement déployé à partir d'un [dépôt open source](https://github.com/DavidMStraub/cloud-run-telemetry), vous pouvez donc inspecter comment les données sont traitées.

## Que sera-t-il fait des données ?

Tout d'abord, aucune donnée au-delà de la charge utile anonymisée, qui pourrait théoriquement être collectée (comme l'adresse IP du serveur), ne sera utilisée par l'équipe de Gramps Web.

Les identifiants anonymisés collectés et le timestamp seront agrégés pour produire des graphiques tels que :

- Nombre d'installations actives de Gramps Web en fonction du temps
- Nombre d'arbres Gramps Web actifs en fonction du temps

Ces graphiques seront publiés sur le site de documentation de Gramps Web.

## Comment désactiver la télémétrie ?

Étant donné que les données statistiques sont utiles pour l'équipe de Gramps Web et que nous avons veillé à ce qu'aucune donnée personnellement identifiable ne soit envoyée, **nous vous serions reconnaissants de ne pas désactiver la télémétrie !**

Néanmoins, Gramps Web donne aux utilisateurs un contrôle total, donc bien sûr vous pouvez choisir de désactiver la fonctionnalité si vous le souhaitez.

Pour ce faire, il vous suffit de définir l'option de configuration `DISABLE_TELEMETRY` sur `True` (par exemple, en définissant la variable d'environnement `GRAMPSWEB_DISABLE_TELEMETRY` sur `true` &ndash; consultez la [documentation de configuration](configuration.md) pour plus de détails).
