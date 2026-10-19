# Configuration du chat IA

!!! info
    Le chat IA nécessite l'API Web Gramps version 2.5.0 ou supérieure. La version 3.6.0 a introduit des capacités d'appel d'outils pour des interactions plus intelligentes.

L'API Web Gramps prend en charge la possibilité de poser des questions sur la base de données généalogique en utilisant des modèles de langage de grande taille (LLM) avec appel d'outils.

## Comment ça fonctionne

L'assistant IA utilise des outils spécialisés pour interroger directement vos données généalogiques. Ces outils permettent à l'assistant de rechercher dans la base de données avec une recherche en texte intégral, de filtrer les personnes/événements/familles/lieux selon des critères spécifiques, de calculer des relations entre individus et de récupérer des dossiers complets, y compris des notes. L'assistant répond ensuite en fonction des dossiers qu'il a consultés et fournit des liens vers ceux-ci dans sa réponse.

Depuis l'API Web Gramps 3.24, le chat IA ne nécessite plus de modèle d'incorporation vectorielle. Les versions antérieures utilisaient également la *recherche sémantique* (génération augmentée par récupération, RAG), qui compare le sens d'une question à un index de vecteurs numériques calculés pour tous les objets de la base de données. La recherche sémantique est obsolète et sera supprimée dans l'API Web Gramps 3.25, voir [Recherche sémantique (obsolète)](#semantic-search-deprecated) ci-dessous.

Pour activer le point de terminaison de chat dans l'API Web Gramps, deux étapes sont nécessaires :

1. Installer les dépendances requises,
2. Configurer un fournisseur de LLM.

Les deux étapes sont décrites ci-dessous à tour de rôle. Enfin, un propriétaire ou un administrateur doit [configurer quels utilisateurs peuvent accéder à la fonction de chat](users.md#configuring-who-can-use-ai-chat) dans les paramètres de gestion des utilisateurs.

## Installation des dépendances requises

Les images Docker standard pour Gramps Web ont déjà toutes les dépendances nécessaires pour le chat IA préinstallées.

Lors de l'installation de l'API Web Gramps via `pip` (ceci n'est pas nécessaire lors de l'utilisation des images Docker), les dépendances nécessaires sont installées avec

```bash
pip install gramps_webapi[ai]
```

## Recherche sémantique (obsolète)

!!! warning "La recherche sémantique est obsolète"
    La recherche sémantique est obsolète depuis l'API Web Gramps 3.24 et sera supprimée dans la version 3.25. Le chat IA et la [recherche en texte intégral](../user-guide/search.md) n'en ont pas besoin. Après la suppression, le paramètre `VECTOR_EMBEDDING_MODEL` est toujours accepté mais ignoré. Si vous le définissez uniquement pour activer le chat IA, vous pouvez le supprimer maintenant, ainsi que les autres paramètres `VECTOR_EMBEDDING_*`, ce qui permet également d'économiser la mémoire nécessaire au modèle d'incorporation.

Le reste de cette section décrit la recherche sémantique pour les serveurs qui l'utilisent encore avec l'API Web Gramps 3.24.

Si les dépendances nécessaires sont installées, activer la recherche sémantique peut être aussi simple que de définir l'option de configuration `VECTOR_EMBEDDING_MODEL` (par exemple, en définissant la variable d'environnement `GRAMPSWEB_VECTOR_EMBEDDING_MODEL`), voir [Configuration du serveur](configuration.md). Cela peut être n'importe quelle chaîne d'un modèle pris en charge par la bibliothèque [Sentence Transformers](https://sbert.net/). Consultez la documentation de ce projet pour des détails et les modèles disponibles.

!!! warning
    Notez que les images Docker par défaut n'incluent pas de version de PyTorch avec prise en charge GPU. Si vous avez accès à un GPU (ce qui accélérera considérablement l'indexation sémantique), veuillez installer une version de PyTorch compatible avec le GPU.

Il y a plusieurs considérations à prendre en compte lors du choix d'un modèle.

- Lorsque vous changez de modèle, vous devez recréer manuellement l'index de recherche sémantique pour votre arbre (ou tous les arbres dans une configuration multi-arbres), sinon vous rencontrerez des erreurs ou des résultats sans signification. Gramps Web détecte lorsque le modèle d'incorporation configuré ne correspond plus à l'index existant et affiche une notification persistante aux administrateurs leur demandant de déclencher un réindex complet depuis [Paramètres d'administration](../administration/settings.md#semantic-search-index).
- Les modèles sont un compromis entre précision/généralité d'une part et temps de calcul/espace de stockage d'autre part. Si vous n'exécutez pas l'API Web Gramps sur un système ayant accès à un GPU puissant, les modèles plus grands sont généralement trop lents en pratique.
- À moins que votre base de données entière ne soit en anglais et que tous vos utilisateurs ne soient censés poser des questions de chat uniquement en anglais, vous aurez besoin d'un modèle d'incorporation multilingue, qui est plus rare que les modèles purement anglais.

Si le modèle n'est pas présent dans le cache local, il sera téléchargé lorsque l'API Web Gramps sera démarrée pour la première fois avec la nouvelle configuration. Le modèle `sentence-transformers/distiluse-base-multilingual-cased-v2` est déjà disponible localement lors de l'utilisation des images Docker standard. Ce modèle est un bon point de départ et prend en charge les entrées multilingues.

Veuillez partager vos expériences concernant les différents modèles avec la communauté !

!!! info
    La bibliothèque sentence transformers consomme une quantité significative de mémoire, ce qui peut entraîner la fermeture des processus de travail. En règle générale, avec la recherche sémantique activée, chaque processus de travail Gunicorn consomme environ 200 Mo de mémoire et chaque processus de travail Celery environ 500 Mo de mémoire même lorsqu'il est inactif, et jusqu'à 1 Go lors du calcul des incorporations. Consultez [Limiter l'utilisation du CPU et de la mémoire](cpu-limited.md) pour des paramètres qui limitent l'utilisation de la mémoire. De plus, il est conseillé de prévoir une partition d'échange suffisamment grande pour éviter les erreurs OOM dues à des pics d'utilisation de mémoire transitoires.

### Utilisation d'une API d'incorporation distante

En alternative à l'exécution d'un modèle Sentence Transformers local, vous pouvez utiliser une API d'incorporation distante compatible OpenAI pour la recherche sémantique. Cela est utile si vous souhaitez décharger le calcul d'incorporation vers un service séparé (par exemple, [Ollama](https://ollama.com/)), utiliser un fournisseur d'incorporation dans le cloud (par exemple, OpenAI) ou éviter de charger les bibliothèques Sentence Transformers et PyTorch en mémoire.

L'API distante doit être compatible avec le [point de terminaison d'incorporation OpenAI](https://platform.openai.com/docs/api-reference/embeddings) (`/v1/embeddings`).

Pour utiliser une API d'incorporation distante, définissez les options de configuration suivantes (voir [Configuration du serveur](configuration.md)) :

Clé | Description
----|-------------
`VECTOR_EMBEDDING_MODEL` | Le nom du modèle à passer au fournisseur distant
`VECTOR_EMBEDDING_BASE_URL` | URL de base de l'API distante
`VECTOR_EMBEDDING_API_KEY` | Clé API (uniquement nécessaire si le fournisseur nécessite une authentification)

#### Utilisation d'Ollama pour les incorporations

Lors du déploiement de Gramps Web avec Docker Compose, vous pouvez ajouter un service Ollama et l'utiliser à la fois pour les incorporations et (optionnellement) le LLM :

```yaml
services:
  grampsweb: &grampsweb
    # ... configuration existante ...
    environment:
      GRAMPSWEB_VECTOR_EMBEDDING_MODEL: nomic-embed-text
      GRAMPSWEB_VECTOR_EMBEDDING_BASE_URL: http://ollama:11434

  grampsweb_celery: &grampsweb_celery
    # ... configuration existante ...
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

Après avoir démarré les services, tirez le modèle d'incorporation dans Ollama :

```bash
docker compose exec ollama ollama pull nomic-embed-text
```

!!! info
    Lors de l'utilisation d'Ollama pour les incorporations, les bibliothèques Sentence Transformers et PyTorch ne sont pas nécessaires, ce qui réduit considérablement l'utilisation de la mémoire des travailleurs de l'API Web Gramps.

#### Utilisation d'OpenAI pour les incorporations

Pour utiliser l'API d'incorporation OpenAI, définissez l'URL de base sur l'API OpenAI et fournissez votre clé API :

```yaml
environment:
  GRAMPSWEB_VECTOR_EMBEDDING_MODEL: text-embedding-3-small
  GRAMPSWEB_VECTOR_EMBEDDING_BASE_URL: https://api.openai.com
  GRAMPSWEB_VECTOR_EMBEDDING_API_KEY: sk-...
```

!!! warning
    Changer le modèle d'incorporation nécessite de réindexer tous les enregistrements de votre arbre (ou tous les arbres dans une configuration multi-arbres), car différents modèles produisent des vecteurs avec des dimensions différentes.

## Configuration d'un fournisseur de LLM

La communication avec le LLM utilise le cadre AI Pydantic, qui prend en charge les API compatibles avec OpenAI. Cela permet d'utiliser un LLM déployé localement via Ollama (voir [Compatibilité OpenAI d'Ollama](https://ollama.com/blog/openai-compatibility)) ou des API hébergées comme OpenAI, Anthropic ou Hugging Face TGI (Text Generation Inference). Le LLM est configuré via les paramètres de configuration `LLM_MODEL` et `LLM_BASE_URL`.

### Utilisation d'un LLM hébergé via l'API OpenAI

Lors de l'utilisation de l'API OpenAI, `LLM_BASE_URL` peut être laissé non défini, tandis que `LLM_MODEL` doit être défini sur l'un des modèles OpenAI, par exemple `gpt-4o-mini`. Le LLM utilise l'appel d'outils pour répondre aux questions : il interroge directement la base de données en utilisant des outils spécialisés et répond en fonction des dossiers qu'il trouve. Il ne nécessite pas de connaissances généalogiques ou historiques approfondies. Par conséquent, vous pouvez essayer si un modèle petit/économique est suffisant.

Vous devrez également vous inscrire pour un compte, obtenir une clé API et la stocker dans la variable d'environnement `OPENAI_API_KEY`.

!!! info
    `LLM_MODEL` est un paramètre de configuration ; si vous souhaitez le définir via une variable d'environnement, utilisez `GRAMPSWEB_LLM_MODEL` (voir [Configuration](configuration.md)). `OPENAI_API_KEY` n'est pas un paramètre de configuration mais une variable d'environnement utilisée directement par la bibliothèque Pydantic AI, donc elle ne doit pas être préfixée.

### Utilisation de Mistral AI

Pour utiliser les modèles hébergés de Mistral AI, préfixez le nom du modèle avec `mistral:` lors de la définition de `LLM_MODEL`.

Vous devrez vous inscrire pour un compte Mistral AI, obtenir une clé API et la stocker dans la variable d'environnement `MISTRAL_API_KEY`. Pas besoin de définir `LLM_BASE_URL` car Pydantic AI utilisera automatiquement le bon point de terminaison de l'API Mistral.

Exemple de configuration lors de l'utilisation de Docker Compose avec des variables d'environnement :
```yaml
environment:
  GRAMPSWEB_LLM_MODEL: mistral:mistral-large-latest
  MISTRAL_API_KEY: votre-clé-api-mistral-ici
```

### Utilisation d'un LLM local via Ollama

[Ollama](https://ollama.com/) est un moyen pratique d'exécuter des LLM localement. Veuillez consulter la documentation d'Ollama pour plus de détails. Veuillez noter que les LLM nécessitent des ressources informatiques significatives et que tous les modèles sauf les plus petits seront probablement trop lents sans prise en charge GPU. Comme l'assistant s'appuie sur l'appel d'outils, choisissez un modèle qui prend en charge les outils, tel que [`qwen2.5`](https://ollama.com/library/qwen2.5). Commencez avec une variante petite comme `qwen2.5:7b` et essayez un modèle plus grand si les réponses ne sont pas suffisamment bonnes. Veuillez partager toute expérience avec la communauté !

Lors du déploiement de Gramps Web avec Docker Compose, vous pouvez ajouter un service Ollama et pointer Gramps Web vers celui-ci :

```yaml
services:
  grampsweb: &grampsweb
    # ... configuration existante ...
    environment:
      GRAMPSWEB_LLM_MODEL: ollama:qwen2.5:7b
      GRAMPSWEB_LLM_BASE_URL: http://ollama:11434/v1/

  grampsweb_celery: &grampsweb_celery
    # ... configuration existante ...
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

Après avoir démarré les services, tirez le modèle dans Ollama :

```bash
docker compose exec ollama ollama pull qwen2.5:7b
```

Quelques points à noter :

- Définissez `LLM_MODEL` sur le nom du modèle Ollama, y compris son tag (la partie après les deux-points, par exemple `7b`), préfixé par `ollama:`. Le préfixe permet à Pydantic AI d'utiliser ses paramètres spécifiques à Ollama pour le modèle, ce qui est la configuration recommandée.
- `LLM_BASE_URL` doit se terminer par `/v1/`, par exemple `http://ollama:11434/v1/`.
- Avec le préfixe `ollama:`, ni `OPENAI_API_KEY` ni la variable d'environnement `OLLAMA_BASE_URL` ne sont nécessaires. Si `LLM_BASE_URL` n'est pas défini, Gramps Web revient à `OLLAMA_BASE_URL`.
- Alternativement, vous pouvez omettre le préfixe (par exemple `LLM_MODEL: qwen2.5:7b`) et utiliser Ollama via son API générique compatible OpenAI. Dans ce cas, vous devez également définir la variable d'environnement `OPENAI_API_KEY` sur `ollama` (n'importe quelle valeur non vide fonctionne).

Pour résoudre les problèmes avec Ollama, vous pouvez activer la journalisation de débogage en définissant la variable d'environnement `OLLAMA_DEBUG=1` dans l'environnement du service Ollama.

!!! info
    Si vous utilisez Ollama pour le chat IA de Gramps Web, veuillez soutenir la communauté en complétant cette documentation avec tous les détails manquants.

### Utilisation d'autres fournisseurs

N'hésitez pas à soumettre de la documentation pour d'autres fournisseurs et à partager votre expérience avec la communauté !
