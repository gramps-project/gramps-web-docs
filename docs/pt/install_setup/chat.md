# Configurando o chat de IA

!!! info
    O chat de IA requer a versão 2.5.0 ou superior da Gramps Web API. A versão 3.6.0 introduziu capacidades de chamada de ferramentas para interações mais inteligentes.

A Gramps Web API suporta a formulação de perguntas sobre o banco de dados genealógico usando modelos de linguagem grandes (LLM) com chamada de ferramentas.

## Como funciona

O assistente de IA usa ferramentas especializadas para consultar seus dados de genealogia diretamente. Essas ferramentas permitem que o assistente pesquise o banco de dados com busca de texto completo, filtre pessoas/eventos/famílias/lugares por critérios específicos, calcule relacionamentos entre indivíduos e recupere registros completos, incluindo notas. O assistente então responde com base nos registros que consultou e fornece links para eles em sua resposta.

Desde a Gramps Web API 3.24, o chat de IA não requer mais um modelo de incorporação vetorial. Versões anteriores também usavam *busca semântica* (geração aumentada por recuperação, RAG), que compara o significado de uma pergunta a um índice de vetores numéricos calculados para todos os objetos no banco de dados. A busca semântica está obsoleta e será removida na Gramps Web API 3.25, veja [Busca semântica (obsoleta)](#semantic-search-deprecated) abaixo.

Para habilitar o endpoint de chat na Gramps Web API, são necessárias duas etapas:

1. Instalar as dependências necessárias,
2. Configurar um provedor de LLM.

As duas etapas são descritas abaixo, uma a uma. Finalmente, um proprietário ou administrador deve [configurar quais usuários podem acessar o recurso de chat](users.md#configuring-who-can-use-ai-chat) nas configurações de Gerenciar Usuários.

## Instalando as dependências necessárias

As imagens padrão do Docker para Gramps Web já têm todas as dependências necessárias para o chat de IA pré-instaladas.

Ao instalar a Gramps Web API via `pip` (isso não é necessário ao usar as imagens do Docker), as dependências necessárias são instaladas com

```bash
pip install gramps_webapi[ai]
```

## Busca semântica (obsoleta)

!!! warning "Busca semântica está obsoleta"
    A busca semântica está obsoleta desde a Gramps Web API 3.24 e será removida na versão 3.25. O chat de IA e a [busca de texto completo](../user-guide/search.md) não precisam dela. Após a remoção, a configuração `VECTOR_EMBEDDING_MODEL` ainda será aceita, mas ignorada. Se você a definir apenas para habilitar o chat de IA, pode removê-la agora, juntamente com as outras configurações `VECTOR_EMBEDDING_*`, o que também economiza a memória necessária para o modelo de incorporação.

O restante desta seção descreve a busca semântica para servidores que ainda a utilizam com a Gramps Web API 3.24.

Se as dependências necessárias estiverem instaladas, habilitar a busca semântica pode ser tão simples quanto definir a opção de configuração `VECTOR_EMBEDDING_MODEL` (por exemplo, definindo a variável de ambiente `GRAMPSWEB_VECTOR_EMBEDDING_MODEL`), veja [Configuração do Servidor](configuration.md). Isso pode ser qualquer string de um modelo suportado pela biblioteca [Sentence Transformers](https://sbert.net/). Consulte a documentação deste projeto para detalhes e os modelos disponíveis.

!!! warning
    Observe que as imagens padrão do Docker não incluem uma versão do PyTorch com suporte a GPU. Se você tiver acesso a uma GPU (o que acelerará significativamente a indexação semântica), instale uma versão do PyTorch habilitada para GPU.

Há várias considerações a serem feitas ao escolher um modelo.

- Quando você muda o modelo, precisa recriar manualmente o índice de busca semântica para sua árvore (ou todas as árvores em uma configuração de múltiplas árvores), caso contrário, você encontrará erros ou resultados sem sentido. A Gramps Web detecta quando o modelo de incorporação configurado não corresponde mais ao índice existente e mostra um aviso persistente para os administradores, solicitando que eles acionem uma reindexação completa nas [Configurações de Administração](../administration/settings.md#semantic-search-index).
- Os modelos são um compromisso entre precisão/generalidade de um lado e tempo de computação/espaco de armazenamento do outro. Se você não estiver executando a Gramps Web API em um sistema que tenha acesso a uma GPU poderosa, modelos maiores geralmente são muito lentos na prática.
- A menos que todo o seu banco de dados esteja em inglês e todos os seus usuários sejam esperados para fazer perguntas no chat apenas em inglês, você precisará de um modelo de incorporação multilíngue, que é mais raro do que modelos puramente em inglês.

Se o modelo não estiver presente no cache local, ele será baixado quando a Gramps Web API for iniciada pela primeira vez com a nova configuração. O modelo `sentence-transformers/distiluse-base-multilingual-cased-v2` já está disponível localmente ao usar as imagens padrão do Docker. Este modelo é um bom ponto de partida e suporta entrada multilíngue.

Por favor, compartilhe aprendizados sobre diferentes modelos com a comunidade!

!!! info
    A biblioteca sentence transformers consome uma quantidade significativa de memória, o que pode causar o encerramento de processos de trabalho. Como regra geral, com a busca semântica habilitada, cada trabalhador do Gunicorn consome cerca de 200 MB de memória e cada trabalhador do celery cerca de 500 MB de memória mesmo quando ocioso, e até 1 GB ao computar incorporações. Veja [Limitar uso de CPU e memória](cpu-limited.md) para configurações que limitam o uso de memória. Além disso, é aconselhável provisionar uma partição de swap suficientemente grande para evitar erros OOM devido a picos transitórios de uso de memória.

### Usando uma API de incorporação remota

Como alternativa a executar um modelo Sentence Transformers localmente, você pode usar uma API de incorporação compatível com OpenAI para busca semântica. Isso é útil se você quiser descarregar a computação de incorporação para um serviço separado (por exemplo, [Ollama](https://ollama.com/)), usar um provedor de incorporação em nuvem (por exemplo, OpenAI) ou evitar carregar as bibliotecas Sentence Transformers e PyTorch na memória.

A API remota deve ser compatível com o [endpoint de incorporações da OpenAI](https://platform.openai.com/docs/api-reference/embeddings) (`/v1/embeddings`).

Para usar uma API de incorporação remota, defina as seguintes opções de configuração (veja [Configuração do Servidor](configuration.md)):

Chave | Descrição
----|-------------
`VECTOR_EMBEDDING_MODEL` | O nome do modelo a ser passado para o provedor remoto
`VECTOR_EMBEDDING_BASE_URL` | URL base da API remota
`VECTOR_EMBEDDING_API_KEY` | Chave da API (somente necessária se o provedor exigir autenticação)

#### Usando Ollama para incorporações

Ao implantar a Gramps Web com Docker Compose, você pode adicionar um serviço Ollama e usá-lo tanto para incorporações quanto (opcionalmente) para o LLM:

```yaml
services:
  grampsweb: &grampsweb
    # ... configuração existente ...
    environment:
      GRAMPSWEB_VECTOR_EMBEDDING_MODEL: nomic-embed-text
      GRAMPSWEB_VECTOR_EMBEDDING_BASE_URL: http://ollama:11434

  grampsweb_celery: &grampsweb_celery
    # ... configuração existente ...
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

Após iniciar os serviços, puxe o modelo de incorporação para o Ollama:

```bash
docker compose exec ollama ollama pull nomic-embed-text
```

!!! info
    Ao usar o Ollama para incorporações, as bibliotecas Sentence Transformers e PyTorch não são necessárias, o que reduz significativamente o uso de memória dos trabalhadores da Gramps Web API.

#### Usando OpenAI para incorporações

Para usar a API de incorporações da OpenAI, defina a URL base para a API da OpenAI e forneça sua chave da API:

```yaml
environment:
  GRAMPSWEB_VECTOR_EMBEDDING_MODEL: text-embedding-3-small
  GRAMPSWEB_VECTOR_EMBEDDING_BASE_URL: https://api.openai.com
  GRAMPSWEB_VECTOR_EMBEDDING_API_KEY: sk-...
```

!!! warning
    Mudar o modelo de incorporação requer reindexar todos os registros da sua árvore (ou todas as árvores em uma configuração de múltiplas árvores), uma vez que diferentes modelos produzem vetores com dimensões diferentes.

## Configurando um provedor de LLM

A comunicação com o LLM utiliza o framework Pydantic AI, que suporta APIs compatíveis com OpenAI. Isso permite usar um LLM implantado localmente via Ollama (veja [Compatibilidade OpenAI do Ollama](https://ollama.com/blog/openai-compatibility)) ou APIs hospedadas como OpenAI, Anthropic ou Hugging Face TGI (Text Generation Inference). O LLM é configurado através dos parâmetros de configuração `LLM_MODEL` e `LLM_BASE_URL`.

### Usando um LLM hospedado via API da OpenAI

Ao usar a API da OpenAI, `LLM_BASE_URL` pode ser deixado não definido, enquanto `LLM_MODEL` deve ser definido como um dos modelos da OpenAI, por exemplo, `gpt-4o-mini`. O LLM usa chamada de ferramentas para responder perguntas: ele consulta o banco de dados diretamente usando ferramentas especializadas e responde com base nos registros que encontra. Não requer conhecimento genealógico ou histórico profundo. Portanto, você pode tentar se um modelo pequeno/barato é suficiente.

Você também precisará se inscrever para uma conta, obter uma chave de API e armazená-la na variável de ambiente `OPENAI_API_KEY`.

!!! info
    `LLM_MODEL` é um parâmetro de configuração; se você quiser defini-lo através de uma variável de ambiente, use `GRAMPSWEB_LLM_MODEL` (veja [Configuração](configuration.md)). `OPENAI_API_KEY` não é um parâmetro de configuração, mas uma variável de ambiente usada diretamente pela biblioteca Pydantic AI, portanto, não deve ser prefixada.

### Usando Mistral AI

Para usar os modelos hospedados da Mistral AI, prefixe o nome do modelo com `mistral:` ao definir `LLM_MODEL`.

Você precisará se inscrever para uma conta Mistral AI, obter uma chave de API e armazená-la na variável de ambiente `MISTRAL_API_KEY`. Não é necessário definir `LLM_BASE_URL`, pois o Pydantic AI usará automaticamente o endpoint correto da API da Mistral.

Exemplo de configuração ao usar docker compose com variáveis de ambiente:
```yaml
environment:
  GRAMPSWEB_LLM_MODEL: mistral:mistral-large-latest
  MISTRAL_API_KEY: sua-chave-api-mistral-aqui
```

### Usando um LLM local via Ollama

[Ollama](https://ollama.com/) é uma maneira conveniente de executar LLMs localmente. Consulte a documentação do Ollama para detalhes. Observe que os LLMs requerem recursos computacionais significativos e todos, exceto os menores modelos, provavelmente serão muito lentos sem suporte a GPU. Como o assistente depende de chamada de ferramentas, escolha um modelo que suporte ferramentas, como [`qwen2.5`](https://ollama.com/library/qwen2.5). Comece com uma variante pequena como `qwen2.5:7b` e experimente uma maior se as respostas não forem boas o suficiente. Por favor, compartilhe qualquer experiência com a comunidade!

Ao implantar a Gramps Web com Docker Compose, você pode adicionar um serviço Ollama e apontar a Gramps Web para ele:

```yaml
services:
  grampsweb: &grampsweb
    # ... configuração existente ...
    environment:
      GRAMPSWEB_LLM_MODEL: ollama:qwen2.5:7b
      GRAMPSWEB_LLM_BASE_URL: http://ollama:11434/v1/

  grampsweb_celery: &grampsweb_celery
    # ... configuração existente ...
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

Após iniciar os serviços, puxe o modelo para o Ollama:

```bash
docker compose exec ollama ollama pull qwen2.5:7b
```

Algumas coisas a serem observadas:

- Defina `LLM_MODEL` como o nome do modelo do Ollama, incluindo sua tag (a parte após os dois pontos, por exemplo, `7b`), prefixada com `ollama:`. O prefixo faz com que o Pydantic AI use suas configurações específicas do Ollama para o modelo, que é a configuração recomendada.
- `LLM_BASE_URL` deve terminar em `/v1/`, por exemplo, `http://ollama:11434/v1/`.
- Com o prefixo `ollama:`, nem `OPENAI_API_KEY` nem a variável de ambiente `OLLAMA_BASE_URL` são necessárias. Se `LLM_BASE_URL` não estiver definido, a Gramps Web recuará para `OLLAMA_BASE_URL`.
- Alternativamente, você pode deixar de fora o prefixo (por exemplo, `LLM_MODEL: qwen2.5:7b`) e usar o Ollama através de sua API genérica compatível com OpenAI. Nesse caso, você também deve definir a variável de ambiente `OPENAI_API_KEY` como `ollama` (qualquer valor não vazio funciona).

Para solucionar problemas com o Ollama, você pode habilitar o registro de depuração definindo a variável de ambiente `OLLAMA_DEBUG=1` no ambiente do serviço Ollama.

!!! info
    Se você estiver usando o Ollama para o chat de IA da Gramps Web, por favor, apoie a comunidade completando esta documentação com quaisquer detalhes que estiverem faltando.

### Usando outros provedores

Sinta-se à vontade para enviar documentação para outros provedores e compartilhar sua experiência com a comunidade!
