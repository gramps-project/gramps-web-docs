# Configurando o chat de IA

!!! info
    O chat de IA requer a versão 2.5.0 ou superior da Gramps Web API. A versão 3.6.0 introduziu capacidades de chamada de ferramentas para interações mais inteligentes.

A Gramps Web API suporta fazer perguntas sobre o banco de dados genealógico usando modelos de linguagem grandes (LLM) por meio de uma técnica chamada geração aumentada por recuperação (RAG) combinada com chamadas de ferramentas.

## Como funciona

O assistente de IA utiliza duas abordagens complementares:

**Geração Aumentada por Recuperação (RAG)**: Um *modelo de incorporação vetorial* cria um índice de todos os objetos no banco de dados Gramps na forma de vetores numéricos que codificam o significado dos objetos. Quando um usuário faz uma pergunta, essa pergunta também é convertida em um vetor e comparada aos objetos no banco de dados. Essa *busca semântica* retorna objetos que são semanticamente mais semelhantes à pergunta.

**Chamada de Ferramentas (v3.6.0+)**: O assistente de IA agora pode usar ferramentas especializadas para consultar seus dados genealógicos diretamente. Essas ferramentas permitem que o assistente busque no banco de dados, filtre pessoas/eventos/famílias/lugares por critérios específicos, calcule relacionamentos entre indivíduos e recupere informações detalhadas sobre objetos. Isso torna o assistente muito mais capaz de responder a perguntas genealógicas complexas com precisão.

Para habilitar o endpoint de chat na Gramps Web API, três etapas são necessárias:

1. Instalar as dependências necessárias,
2. Habilitar a busca semântica,
3. Configurar um provedor de LLM.

As três etapas são descritas abaixo, uma a uma. Finalmente, um proprietário ou administrador deve [configurar quais usuários podem acessar o recurso de chat](users.md#configuring-who-can-use-ai-chat) nas configurações de Gerenciar Usuários.

## Instalando as dependências necessárias

O chat de IA requer que as bibliotecas Sentence Transformers e PyTorch sejam instaladas.

As imagens padrão do Docker para Gramps Web já as têm pré-instaladas para as arquiteturas `amd64` (por exemplo, PC desktop de 64 bits) e `arm64` (por exemplo, Raspberry Pi de 64 bits). Infelizmente, o chat de IA não é suportado na arquitetura `armv7` (por exemplo, Raspberry Pi de 32 bits) devido à falta de suporte do PyTorch.

Ao instalar a Gramps Web API via `pip` (isso não é necessário ao usar as imagens do Docker), as dependências necessárias são instaladas com

```bash
pip install gramps_webapi[ai]
```

## Habilitando a busca semântica

Se as dependências necessárias estiverem instaladas, habilitar a busca semântica pode ser tão simples quanto definir a opção de configuração `VECTOR_EMBEDDING_MODEL` (por exemplo, definindo a variável de ambiente `GRAMPSWEB_VECTOR_EMBEDDING_MODEL`), veja [Configuração do Servidor](configuration.md). Isso pode ser qualquer string de um modelo suportado pela biblioteca [Sentence Transformers](https://sbert.net/). Consulte a documentação deste projeto para detalhes e os modelos disponíveis.

!!! warning
    Observe que as imagens padrão do Docker não incluem uma versão do PyTorch com suporte a GPU. Se você tiver acesso a uma GPU (o que acelerará significativamente a indexação semântica), instale uma versão do PyTorch habilitada para GPU.

Há várias considerações a serem feitas ao escolher um modelo.

- Quando você muda o modelo, precisa recriar manualmente o índice de busca semântica para sua árvore (ou todas as árvores em uma configuração de múltiplas árvores), caso contrário, você encontrará erros ou resultados sem sentido.
- Os modelos são um compromisso entre precisão/generalidade, por um lado, e tempo de computação/espaço de armazenamento, por outro. Se você não estiver executando a Gramps Web API em um sistema que tenha acesso a uma GPU poderosa, modelos maiores geralmente são muito lentos na prática.
- A menos que todo o seu banco de dados esteja em inglês e todos os seus usuários sejam esperados para fazer perguntas de chat apenas em inglês, você precisará de um modelo de incorporação multilíngue, que é mais raro do que modelos puramente em inglês.

Se o modelo não estiver presente no cache local, ele será baixado quando a Gramps Web API for iniciada pela primeira vez com a nova configuração. O modelo `sentence-transformers/distiluse-base-multilingual-cased-v2` já está disponível localmente ao usar as imagens padrão do Docker. Este modelo é um bom ponto de partida e suporta entrada multilíngue.

Por favor, compartilhe aprendizados sobre diferentes modelos com a comunidade!

!!! info
    A biblioteca sentence transformers consome uma quantidade significativa de memória, o que pode causar a morte de processos de trabalho. Como regra geral, com a busca semântica habilitada, cada trabalhador do Gunicorn consome cerca de 200 MB de memória e cada trabalhador do celery cerca de 500 MB de memória, mesmo quando ocioso, e até 1 GB ao calcular incorporações. Veja [Limitar uso de CPU e memória](cpu-limited.md) para configurações que limitam o uso de memória. Além disso, é aconselhável provisionar uma partição de swap suficientemente grande para evitar erros OOM devido a picos transitórios de uso de memória.

## Configurando um provedor de LLM

A comunicação com o LLM usa o framework Pydantic AI, que suporta APIs compatíveis com OpenAI. Isso permite usar um LLM implantado localmente via Ollama (veja [Compatibilidade do Ollama com OpenAI](https://ollama.com/blog/openai-compatibility)) ou APIs hospedadas como OpenAI, Anthropic ou Hugging Face TGI (Text Generation Inference). O LLM é configurado por meio dos parâmetros de configuração `LLM_MODEL` e `LLM_BASE_URL`.

### Usando um LLM hospedado via a API OpenAI

Ao usar a API OpenAI, `LLM_BASE_URL` pode ser deixado não definido, enquanto `LLM_MODEL` deve ser definido como um dos modelos OpenAI, por exemplo, `gpt-4o-mini`. O LLM usa tanto RAG quanto chamadas de ferramentas para responder perguntas: ele seleciona informações relevantes dos resultados da busca semântica e pode consultar diretamente o banco de dados usando ferramentas especializadas. Não requer conhecimento genealógico ou histórico profundo. Portanto, você pode tentar se um modelo pequeno/barato é suficiente.

Você também precisará se inscrever para uma conta, obter uma chave de API e armazená-la na variável de ambiente `OPENAI_API_KEY`.

!!! info
    `LLM_MODEL` é um parâmetro de configuração; se você quiser defini-lo via uma variável de ambiente, use `GRAMPSWEB_LLM_MODEL` (veja [Configuração](configuration.md)). `OPENAI_API_KEY` não é um parâmetro de configuração, mas uma variável de ambiente usada diretamente pela biblioteca Pydantic AI, portanto, não deve ser prefixada.

### Usando Mistral AI

Para usar os modelos hospedados da Mistral AI, prefixe o nome do modelo com `mistral:` ao definir `LLM_MODEL`.

Você precisará se inscrever para uma conta Mistral AI, obter uma chave de API e armazená-la na variável de ambiente `MISTRAL_API_KEY`. Não é necessário definir `LLM_BASE_URL`, pois o Pydantic AI usará automaticamente o endpoint correto da API Mistral.

Exemplo de configuração ao usar docker compose com variáveis de ambiente:
```yaml
environment:
  GRAMPSWEB_LLM_MODEL: mistral:mistral-large-latest
  MISTRAL_API_KEY: sua-chave-api-mistral-aqui
  GRAMPSWEB_VECTOR_EMBEDDING_MODEL: sentence-transformers/distiluse-base-multilingual-cased-v2
```

### Usando um LLM local via Ollama

[Ollama](https://ollama.com/) é uma maneira conveniente de executar LLMs localmente. Consulte a documentação do Ollama para detalhes. Observe que os LLMs requerem recursos computacionais significativos e todos, exceto os menores modelos, provavelmente serão muito lentos sem suporte a GPU. Você pode tentar se [`tinyllama`](https://ollama.com/library/tinyllama) atende às suas necessidades. Se não, experimente um dos modelos maiores. Por favor, compartilhe qualquer experiência com a comunidade!

Ao implantar a Gramps Web com Docker Compose, você pode adicionar um serviço Ollama

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

e então definir o parâmetro de configuração `LLM_BASE_URL` para `http://ollama:11434/v1`. Defina `LLM_MODEL` para um modelo suportado pelo Ollama e faça o download no seu contêiner com `ollama pull <model>`. Finalmente, defina `OPENAI_API_KEY` como `ollama`.

Para solucionar problemas com o Ollama, você pode habilitar o registro de depuração definindo a variável de ambiente `OLLAMA_DEBUG=1` no ambiente do serviço Ollama.

!!! info
    Se você estiver usando Ollama para o chat de IA da Gramps Web, por favor, apoie a comunidade completando esta documentação com quaisquer detalhes ausentes.

### Usando outros provedores

Sinta-se à vontade para enviar documentação para outros provedores e compartilhar sua experiência com a comunidade!
