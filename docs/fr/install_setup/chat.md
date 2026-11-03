# Configuration du chat AI

!!! info
    Le chat AI nécessite la version 2.5.0 ou supérieure de l'API Web Gramps. La version 3.6.0 a introduit des capacités d'appel d'outils pour des interactions plus intelligentes.

L'API Web Gramps prend en charge la possibilité de poser des questions sur la base de données généalogique en utilisant des modèles de langage large (LLM) avec appel d'outils.

## Comment ça fonctionne

L'assistant AI utilise des outils spécialisés pour interroger directement vos données généalogiques. Ces outils permettent à l'assistant de rechercher dans la base de données avec une recherche en texte intégral, de filtrer les personnes/événements/familles/lieux selon des critères spécifiques, de calculer les relations entre les individus et de récupérer des dossiers complets, y compris des notes. L'assistant répond ensuite en fonction des dossiers qu'il a consultés et en fournissant des liens vers ceux-ci dans sa réponse. Il répond uniquement à partir de l'arbre, pas à partir de connaissances générales : si l'arbre ne consigne pas quelque chose, l'assistant le dit. Les liens vers des objets qui n'existent pas ou qui sont privés pour l'utilisateur sont remplacés par leur texte.

Le chat AI n'a pas besoin d'un modèle d'incorporation vectorielle. Les versions de l'API Web Gramps avant 3.24 utilisaient également la *recherche sémantique* (génération augmentée par récupération, RAG), qui comparait le sens d'une question à un index de vecteurs numériques calculés pour tous les objets de la base de données. La recherche sémantique a été supprimée dans l'API Web Gramps 3.25 ; les paramètres `VECTOR_EMBEDDING_MODEL`, `VECTOR_EMBEDDING_BASE_URL` et `VECTOR_EMBEDDING_API_KEY` sont ignorés et peuvent être supprimés de votre configuration.

Pour activer le point de terminaison de chat dans l'API Web Gramps, deux étapes sont nécessaires :

1. Installer les dépendances requises,
2. Configurer un fournisseur LLM.

Les deux étapes sont décrites ci-dessous à tour de rôle. Enfin, un propriétaire ou un administrateur doit [configurer quels utilisateurs peuvent accéder à la fonctionnalité de chat](users.md#configuring-who-can-use-ai-chat) dans les paramètres de gestion des utilisateurs.

## Installation des dépendances requises

Les images Docker standard pour Gramps Web ont déjà toutes les dépendances nécessaires pour le chat AI pré-installées.

Lors de l'installation de l'API Web Gramps via `pip` (ceci n'est pas nécessaire lors de l'utilisation des images Docker), les dépendances nécessaires sont installées avec

```bash
pip install gramps_webapi[ai]
```

## Configuration d'un fournisseur LLM

La communication avec le LLM utilise le cadre Pydantic AI, qui prend en charge les API compatibles avec OpenAI. Cela permet d'utiliser un LLM déployé localement via Ollama (voir [Compatibilité OpenAI d'Ollama](https://ollama.com/blog/openai-compatibility)) ou des API hébergées comme OpenAI, Anthropic ou Hugging Face TGI (Text Generation Inference). Le LLM est configuré via les paramètres de configuration `LLM_MODEL` et `LLM_BASE_URL`.

En plus des API compatibles avec OpenAI, les préfixes de modèle spécifiques au fournisseur de Pydantic AI peuvent être utilisés pour OpenAI, Anthropic, Google, Mistral, Groq, AWS Bedrock et Ollama. D'autres fournisseurs, tels que Cohere, Hugging Face et xAI, ne sont pas installés ; les fournisseurs d'inférence Hugging Face peuvent toujours être utilisés via leur point de terminaison compatible avec OpenAI (`LLM_BASE_URL` défini sur `https://router.huggingface.co/v1`).

Si votre serveur de modèle ne limite pas la longueur d'une réponse, définissez `LLM_MAX_OUTPUT_TOKENS` sur le nombre maximum de tokens que le modèle peut générer par réponse (voir [Configuration](configuration.md)).

### Utilisation d'un LLM hébergé via l'API OpenAI

Lors de l'utilisation de l'API OpenAI, `LLM_BASE_URL` peut être laissé non défini, tandis que `LLM_MODEL` doit être défini sur l'un des modèles OpenAI, par exemple `gpt-4o-mini`. Le LLM utilise l'appel d'outils pour répondre aux questions : il interroge directement la base de données en utilisant des outils spécialisés et répond en fonction des dossiers qu'il trouve. Il ne nécessite pas de connaissances généalogiques ou historiques approfondies. Par conséquent, vous pouvez essayer si un modèle petit/économique est suffisant.

Vous devrez également vous inscrire pour obtenir un compte, obtenir une clé API et la stocker dans la variable d'environnement `OPENAI_API_KEY`.

!!! info
    `LLM_MODEL` est un paramètre de configuration ; si vous souhaitez le définir via une variable d'environnement, utilisez `GRAMPSWEB_LLM_MODEL` (voir [Configuration](configuration.md)). `OPENAI_API_KEY` n'est pas un paramètre de configuration mais une variable d'environnement utilisée directement par la bibliothèque Pydantic AI, donc elle ne doit pas être préfixée.

### Utilisation de Mistral AI

Pour utiliser les modèles hébergés de Mistral AI, préfixez le nom du modèle avec `mistral:` lors de la définition de `LLM_MODEL`.

Vous devrez vous inscrire pour un compte Mistral AI, obtenir une clé API et la stocker dans la variable d'environnement `MISTRAL_API_KEY`. Pas besoin de définir `LLM_BASE_URL` car Pydantic AI utilisera automatiquement le bon point de terminaison API de Mistral.

Exemple de configuration lors de l'utilisation de docker compose avec des variables d'environnement :
```yaml
environment:
  GRAMPSWEB_LLM_MODEL: mistral:mistral-large-latest
  MISTRAL_API_KEY: your-mistral-api-key-here
```

### Utilisation d'un LLM local via Ollama

[Ollama](https://ollama.com/) est un moyen pratique de faire fonctionner des LLM localement. Veuillez consulter la documentation d'Ollama pour plus de détails. Veuillez noter que les LLM nécessitent des ressources informatiques significatives et que tous les modèles sauf les plus petits seront probablement trop lents sans support GPU. Puisque l'assistant s'appuie sur l'appel d'outils, choisissez un modèle qui prend en charge les outils, tel que [`qwen2.5`](https://ollama.com/library/qwen2.5). Commencez avec une variante petite comme `qwen2.5:7b` et essayez un modèle plus grand si les réponses ne sont pas assez bonnes. Merci de partager toute expérience avec la communauté !

Lors du déploiement de Gramps Web avec Docker Compose, vous pouvez ajouter un service Ollama et pointer Gramps Web vers celui-ci :

```yaml
services:
  grampsweb: &grampsweb
    # ... config existante ...
    environment:
      GRAMPSWEB_LLM_MODEL: ollama:qwen2.5:7b
      GRAMPSWEB_LLM_BASE_URL: http://ollama:11434/v1/

  grampsweb_celery: &grampsweb_celery
    # ... config existante ...
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

- Définissez `LLM_MODEL` sur le nom du modèle Ollama, y compris son tag (la partie après le deux-points, par exemple `7b`), préfixé par `ollama:`. Le préfixe permet à Pydantic AI d'utiliser ses paramètres spécifiques à Ollama pour le modèle, ce qui est la configuration recommandée.
- `LLM_BASE_URL` doit se terminer par `/v1/`, par exemple `http://ollama:11434/v1/`.
- Avec le préfixe `ollama:`, ni `OPENAI_API_KEY` ni la variable d'environnement `OLLAMA_BASE_URL` ne sont nécessaires. Si `LLM_BASE_URL` n'est pas défini, Gramps Web revient à `OLLAMA_BASE_URL`.
- Alternativement, vous pouvez omettre le préfixe (par exemple `LLM_MODEL: qwen2.5:7b`) et utiliser Ollama via son API générique compatible avec OpenAI. Dans ce cas, vous devez également définir la variable d'environnement `OPENAI_API_KEY` sur `ollama` (n'importe quelle valeur non vide fonctionne).

Pour résoudre les problèmes avec Ollama, vous pouvez activer la journalisation de débogage en définissant la variable d'environnement `OLLAMA_DEBUG=1` dans l'environnement du service Ollama.

!!! info
    Si vous utilisez Ollama pour le chat AI de Gramps Web, veuillez soutenir la communauté en complétant cette documentation avec tous les détails manquants.

### Utilisation d'autres fournisseurs

N'hésitez pas à soumettre de la documentation pour d'autres fournisseurs et à partager votre expérience avec la communauté !
