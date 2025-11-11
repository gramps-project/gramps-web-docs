# Configuration du chat AI

!!! info
    Le chat AI nécessite la version 2.5.0 ou supérieure de l'API Web Gramps.


L'API Web Gramps prend en charge la possibilité de poser des questions sur la base de données généalogique en utilisant des modèles de langage de grande taille (LLM) via une technique appelée génération augmentée par récupération (RAG).

RAG fonctionne comme suit. Tout d'abord, un *modèle d'embedding vectoriel* est utilisé pour créer un index de tous les objets dans la base de données Gramps sous la forme de vecteurs numériques qui codent le sens des objets. Ce processus est similaire à la création de l'index de recherche en texte intégral, mais est plus coûteux en calcul.

Ensuite, lorsqu'un utilisateur pose une question via le point de terminaison de chat, cette question est également convertie en vecteur, par le même modèle d'embedding, et comparée aux objets dans la base de données Gramps. Cette *recherche sémantique* renverra les objets dans la base de données qui sont les plus sémantiquement similaires à la question.

Dans l'étape finale, la question et les objets récupérés sont envoyés à un LLM pour formuler une réponse basée sur les informations fournies. De cette manière, le chatbot a accès à des informations détaillées sur le contenu de la base de données généalogique au lieu de se fier uniquement à des connaissances préexistantes.

Pour activer le point de terminaison de chat dans l'API Web Gramps, trois étapes sont nécessaires :

1. Installer les dépendances requises,
2. Activer la recherche sémantique,
3. Configurer un fournisseur LLM.

Les trois étapes sont décrites ci-dessous à tour de rôle. Enfin, un propriétaire ou un administrateur doit [configurer quels utilisateurs peuvent accéder à la fonctionnalité de chat](users.md#configuring-who-can-use-ai-chat) dans les paramètres de gestion des utilisateurs.

## Installation des dépendances requises

Le chat AI nécessite que les bibliothèques Sentence Transformers et PyTorch soient installées.

Les images Docker standard pour Gramps Web les ont déjà préinstallées pour les architectures `amd64` (par exemple, PC de bureau 64 bits) et `arm64` (par exemple, Raspberry Pi 64 bits). Malheureusement, le chat AI n'est pas pris en charge sur l'architecture `armv7` (par exemple, Raspberry Pi 32 bits) en raison du manque de support de PyTorch.

Lors de l'installation de l'API Web Gramps via `pip` (ceci n'est pas nécessaire lors de l'utilisation des images Docker), les dépendances nécessaires sont installées avec

```bash
pip install gramps_webapi[ai]
```


## Activation de la recherche sémantique

Si les dépendances nécessaires sont installées, l'activation de la recherche sémantique peut être aussi simple que de définir l'option de configuration `VECTOR_EMBEDDING_MODEL` (par exemple, en définissant la variable d'environnement `GRAMPSWEB_VECTOR_EMBEDDING_MODEL`), voir [Configuration du serveur](configuration.md). Cela peut être n'importe quelle chaîne d'un modèle pris en charge par la bibliothèque [Sentence Transformers](https://sbert.net/). Consultez la documentation de ce projet pour plus de détails et les modèles disponibles.


!!! warning
    Notez que les images Docker par défaut n'incluent pas de version de PyTorch avec support GPU. Si vous avez accès à un GPU (ce qui accélérera considérablement l'indexation sémantique), veuillez installer une version de PyTorch activée pour GPU.

Il y a plusieurs considérations à prendre en compte lors du choix d'un modèle.

- Lorsque vous changez de modèle, vous devez recréer manuellement l'index de recherche sémantique pour votre arbre (ou tous les arbres dans une configuration multi-arbres), sinon vous rencontrerez des erreurs ou des résultats sans signification.
- Les modèles représentent un compromis entre précision/généralité d'une part et temps de calcul/espace de stockage d'autre part. Si vous n'exécutez pas l'API Web Gramps sur un système ayant accès à un GPU puissant, les modèles plus grands sont généralement trop lents en pratique.
- À moins que votre base de données entière ne soit en anglais et que tous vos utilisateurs ne soient censés poser des questions de chat uniquement en anglais, vous aurez besoin d'un modèle d'embedding multilingue, qui est plus rare que les modèles purement anglais.


Si le modèle n'est pas présent dans le cache local, il sera téléchargé lorsque l'API Web Gramps sera démarrée pour la première fois avec la nouvelle configuration. Le modèle `sentence-transformers/distiluse-base-multilingual-cased-v2` est déjà disponible localement lors de l'utilisation des images Docker standard. Ce modèle est un bon point de départ et prend en charge les entrées multilingues.

Veuillez partager vos apprentissages sur les différents modèles avec la communauté !

!!! info
    La bibliothèque sentence transformers consomme une quantité significative de mémoire, ce qui pourrait entraîner l'arrêt des processus de travail. En règle générale, avec la recherche sémantique activée, chaque travailleur Gunicorn consomme environ 200 Mo de mémoire et chaque travailleur celery environ 500 Mo de mémoire même lorsqu'il est inactif, et jusqu'à 1 Go lors du calcul des embeddings. Voir [Limiter l'utilisation du CPU et de la mémoire](cpu-limited.md) pour les paramètres qui limitent l'utilisation de la mémoire. De plus, il est conseillé de prévoir une partition d'échange suffisamment grande pour éviter les erreurs OOM dues à des pics d'utilisation de mémoire transitoires.

## Configuration d'un fournisseur LLM

La communication avec le LLM utilise une API compatible OpenAI via la bibliothèque `openai-python`. Cela permet d'utiliser un LLM déployé localement via Ollama (voir [Compatibilité OpenAI d'Ollama](https://ollama.com/blog/openai-compatibility)) ou une API comme OpenAI ou Hugging Face TGI (Text Generation Inference). Le LLM est configuré via les paramètres de configuration `LLM_MODEL` et `LLM_BASE_URL`.


### Utilisation d'un LLM hébergé via l'API OpenAI

Lors de l'utilisation de l'API OpenAI, `LLM_BASE_URL` peut être laissé non défini, tandis que `LLM_MODEL` doit être défini sur l'un des modèles OpenAI, par exemple `gpt-4o-mini`. Notez qu'en raison de l'approche RAG, le LLM est "seulement" utilisé pour sélectionner les bonnes informations parmi les résultats de recherche sémantique et formuler une réponse, il ne nécessite pas de connaissances généalogiques ou historiques approfondies. Par conséquent, vous pouvez essayer si un modèle petit/économique est suffisant.

Vous devrez également créer un compte, obtenir une clé API et la stocker dans la variable d'environnement `OPENAI_API_KEY`.

!!! info
    `LLM_MODEL` est un paramètre de configuration ; si vous souhaitez le définir via une variable d'environnement, utilisez `GRAMPSWEB_LLM_MODEL` (voir [Configuration](configuration.md)). `OPENAI_API_KEY` n'est pas un paramètre de configuration mais une variable d'environnement directement utilisée par la bibliothèque `openai-python`, donc elle ne doit pas être préfixée.


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
    Si vous utilisez Ollama pour le chat AI de Gramps Web, veuillez soutenir la communauté en complétant cette documentation avec les détails manquants.

### Utilisation d'autres fournisseurs

N'hésitez pas à soumettre de la documentation pour d'autres fournisseurs et à partager votre expérience avec la communauté !
