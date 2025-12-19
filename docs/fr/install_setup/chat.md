# Configuration du chat IA

!!! info
    Le chat IA nécessite l'API Web Gramps version 2.5.0 ou supérieure. La version 3.6.0 a introduit des capacités d'appel d'outils pour des interactions plus intelligentes.


L'API Web Gramps prend en charge la possibilité de poser des questions sur la base de données généalogique en utilisant des modèles de langage de grande taille (LLM) via une technique appelée génération augmentée par récupération (RAG) combinée à l'appel d'outils.

## Comment ça fonctionne

L'assistant IA utilise deux approches complémentaires :

**Génération Augmentée par Récupération (RAG)** : Un *modèle d'embedding vectoriel* crée un index de tous les objets dans la base de données Gramps sous la forme de vecteurs numériques qui codent le sens des objets. Lorsqu'un utilisateur pose une question, cette question est également convertie en vecteur et comparée aux objets de la base de données. Cette *recherche sémantique* retourne les objets les plus sémantiquement similaires à la question.

**Appel d'Outils (v3.6.0+)** : L'assistant IA peut désormais utiliser des outils spécialisés pour interroger directement vos données généalogiques. Ces outils permettent à l'assistant de rechercher dans la base de données, de filtrer les personnes/événements/familles/lieux selon des critères spécifiques, de calculer les relations entre les individus et de récupérer des informations détaillées sur les objets. Cela rend l'assistant beaucoup plus capable de répondre avec précision à des questions généalogiques complexes.

Pour activer le point de terminaison de chat dans l'API Web Gramps, trois étapes sont nécessaires :

1. Installer les dépendances requises,
2. Activer la recherche sémantique,
3. Configurer un fournisseur LLM.

Les trois étapes sont décrites ci-dessous à tour de rôle. Enfin, un propriétaire ou un administrateur doit [configurer quels utilisateurs peuvent accéder à la fonction de chat](users.md#configuring-who-can-use-ai-chat) dans les paramètres de gestion des utilisateurs.

## Installation des dépendances requises

Le chat IA nécessite l'installation des bibliothèques Sentence Transformers et PyTorch.

Les images Docker standard pour Gramps Web les ont déjà préinstallées pour les architectures `amd64` (par exemple, PC de bureau 64 bits) et `arm64` (par exemple, Raspberry Pi 64 bits). Malheureusement, le chat IA n'est pas pris en charge sur l'architecture `armv7` (par exemple, Raspberry Pi 32 bits) en raison du manque de support de PyTorch.

Lors de l'installation de l'API Web Gramps via `pip` (ceci n'est pas nécessaire lors de l'utilisation des images Docker), les dépendances nécessaires sont installées avec

```bash
pip install gramps_webapi[ai]
```


## Activation de la recherche sémantique

Si les dépendances nécessaires sont installées, l'activation de la recherche sémantique peut être aussi simple que de définir l'option de configuration `VECTOR_EMBEDDING_MODEL` (par exemple, en définissant la variable d'environnement `GRAMPSWEB_VECTOR_EMBEDDING_MODEL`), voir [Configuration du Serveur](configuration.md). Cela peut être n'importe quelle chaîne d'un modèle pris en charge par la bibliothèque [Sentence Transformers](https://sbert.net/). Consultez la documentation de ce projet pour plus de détails et les modèles disponibles.


!!! warning
    Notez que les images Docker par défaut n'incluent pas de version de PyTorch avec support GPU. Si vous avez accès à un GPU (ce qui accélérera considérablement l'indexation sémantique), veuillez installer une version de PyTorch activée pour GPU.

Il y a plusieurs considérations à prendre en compte lors du choix d'un modèle.

- Lorsque vous changez de modèle, vous devez recréer manuellement l'index de recherche sémantique pour votre arbre (ou tous les arbres dans une configuration multi-arbres), sinon vous rencontrerez des erreurs ou des résultats sans signification.
- Les modèles représentent un compromis entre précision/généralité d'une part et temps de calcul/espace de stockage d'autre part. Si vous n'exécutez pas l'API Web Gramps sur un système ayant accès à un GPU puissant, les modèles plus grands sont généralement trop lents en pratique.
- À moins que votre base de données entière ne soit en anglais et que tous vos utilisateurs ne soient censés poser des questions de chat qu'en anglais, vous aurez besoin d'un modèle d'embedding multilingue, qui est plus rare que les modèles purement anglais.


Si le modèle n'est pas présent dans le cache local, il sera téléchargé lorsque l'API Web Gramps sera démarrée pour la première fois avec la nouvelle configuration. Le modèle `sentence-transformers/distiluse-base-multilingual-cased-v2` est déjà disponible localement lors de l'utilisation des images Docker standard. Ce modèle est un bon point de départ et prend en charge l'entrée multilingue.

Veuillez partager vos apprentissages sur les différents modèles avec la communauté !

!!! info
    La bibliothèque sentence transformers consomme une quantité significative de mémoire, ce qui peut entraîner la fermeture de processus de travail. En règle générale, avec la recherche sémantique activée, chaque worker Gunicorn consomme environ 200 Mo de mémoire et chaque worker celery environ 500 Mo de mémoire même lorsqu'il est inactif, et jusqu'à 1 Go lors du calcul des embeddings. Voir [Limiter l'utilisation du CPU et de la mémoire](cpu-limited.md) pour les paramètres qui limitent l'utilisation de la mémoire. De plus, il est conseillé de prévoir une partition d'échange suffisamment grande pour éviter les erreurs OOM dues à des pics d'utilisation de mémoire transitoires.

## Configuration d'un fournisseur LLM

La communication avec le LLM utilise le cadre Pydantic AI, qui prend en charge les API compatibles OpenAI. Cela permet d'utiliser un LLM déployé localement via Ollama (voir [Compatibilité OpenAI d'Ollama](https://ollama.com/blog/openai-compatibility)) ou des API hébergées comme OpenAI, Anthropic ou Hugging Face TGI (Text Generation Inference). Le LLM est configuré via les paramètres de configuration `LLM_MODEL` et `LLM_BASE_URL`.


### Utilisation d'un LLM hébergé via l'API OpenAI

Lors de l'utilisation de l'API OpenAI, `LLM_BASE_URL` peut rester non défini, tandis que `LLM_MODEL` doit être défini sur l'un des modèles OpenAI, par exemple `gpt-4o-mini`. Le LLM utilise à la fois RAG et l'appel d'outils pour répondre aux questions : il sélectionne des informations pertinentes à partir des résultats de recherche sémantique et peut interroger directement la base de données en utilisant des outils spécialisés. Il ne nécessite pas de connaissances généalogiques ou historiques approfondies. Par conséquent, vous pouvez essayer si un modèle petit/économique est suffisant.

Vous devrez également vous inscrire pour obtenir un compte, obtenir une clé API et la stocker dans la variable d'environnement `OPENAI_API_KEY`.

!!! info
    `LLM_MODEL` est un paramètre de configuration ; si vous souhaitez le définir via une variable d'environnement, utilisez `GRAMPSWEB_LLM_MODEL` (voir [Configuration](configuration.md)). `OPENAI_API_KEY` n'est pas un paramètre de configuration mais une variable d'environnement utilisée directement par la bibliothèque Pydantic AI, donc elle ne doit pas être préfixée.


### Utilisation de Mistral AI

Pour utiliser les modèles hébergés de Mistral AI, préfixez le nom du modèle avec `mistral:` lors de la définition de `LLM_MODEL`.

Vous devrez vous inscrire pour obtenir un compte Mistral AI, obtenir une clé API et la stocker dans la variable d'environnement `MISTRAL_API_KEY`. Pas besoin de définir `LLM_BASE_URL` car Pydantic AI utilisera automatiquement le bon point de terminaison API de Mistral.

Exemple de configuration lors de l'utilisation de docker compose avec des variables d'environnement :
```yaml
environment:
  GRAMPSWEB_LLM_MODEL: mistral:mistral-large-latest
  MISTRAL_API_KEY: votre-clé-api-mistral-ici
  GRAMPSWEB_VECTOR_EMBEDDING_MODEL: sentence-transformers/distiluse-base-multilingual-cased-v2
```


### Utilisation d'un LLM local via Ollama

[Ollama](https://ollama.com/) est un moyen pratique d'exécuter des LLM localement. Veuillez consulter la documentation d'Ollama pour plus de détails. Veuillez noter que les LLM nécessitent des ressources informatiques significatives et que tous les modèles sauf les plus petits seront probablement trop lents sans support GPU. Vous pouvez essayer si [`tinyllama`](https://ollama.com/library/tinyllama) répond à vos besoins. Sinon, essayez l'un des modèles plus grands. Veuillez partager toute expérience avec la communauté !

Lors du déploiement de Gramps Web avec Docker Compose, vous pouvez ajouter un service Ollama

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

et ensuite définir le paramètre de configuration `LLM_BASE_URL` sur `http://ollama:11434/v1`. Définissez `LLM_MODEL` sur un modèle pris en charge par Ollama, et téléchargez-le dans votre conteneur avec `ollama pull <model>`. Enfin, définissez `OPENAI_API_KEY` sur `ollama`.

Pour résoudre les problèmes avec Ollama, vous pouvez activer la journalisation de débogage en définissant la variable d'environnement `OLLAMA_DEBUG=1` dans l'environnement du service Ollama.

!!! info
    Si vous utilisez Ollama pour le chat IA de Gramps Web, veuillez soutenir la communauté en complétant cette documentation avec les détails manquants.

### Utilisation d'autres fournisseurs

N'hésitez pas à soumettre de la documentation pour d'autres fournisseurs et à partager votre expérience avec la communauté !
