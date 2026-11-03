# Configurando o chat de IA

!!! info
    O chat de IA requer a versão 2.5.0 ou superior da Gramps Web API. A versão 3.6.0 introduziu capacidades de chamada de ferramentas para interações mais inteligentes.

A Gramps Web API suporta fazer perguntas sobre o banco de dados genealógico usando modelos de linguagem de grande porte (LLM) com chamada de ferramentas.

## Como funciona

O assistente de IA usa ferramentas especializadas para consultar seus dados genealógicos diretamente. Essas ferramentas permitem que o assistente pesquise o banco de dados com busca de texto completo, filtre pessoas/eventos/famílias/lugares por critérios específicos, calcule relacionamentos entre indivíduos e recupere registros completos, incluindo notas. O assistente então responde com base nos registros que consultou e fornece links para eles em sua resposta. Ele responde apenas a partir da árvore, não a partir do conhecimento geral: se a árvore não registrar algo, o assistente diz isso. Links para objetos que não existem ou que são privados para o usuário são substituídos pelo seu texto.

O chat de IA não precisa de um modelo de incorporação vetorial. Versões da Gramps Web API anteriores à 3.24 também usavam *busca semântica* (geração aumentada por recuperação, RAG), que comparava o significado de uma pergunta a um índice de vetores numéricos calculados para todos os objetos no banco de dados. A busca semântica foi removida na Gramps Web API 3.25; as configurações `VECTOR_EMBEDDING_MODEL`, `VECTOR_EMBEDDING_BASE_URL` e `VECTOR_EMBEDDING_API_KEY` são ignoradas e podem ser removidas de sua configuração.

Para habilitar o endpoint de chat na Gramps Web API, são necessários dois passos:

1. Instalar as dependências necessárias,
2. Configurar um provedor de LLM.

Os dois passos são descritos abaixo, um a um. Finalmente, um proprietário ou administrador deve [configurar quais usuários podem acessar o recurso de chat](users.md#configuring-who-can-use-ai-chat) nas configurações de Gerenciar Usuários.

## Instalando as dependências necessárias

As imagens padrão do docker para Gramps Web já têm todas as dependências necessárias para o chat de IA pré-instaladas.

Ao instalar a Gramps Web API via `pip` (isso não é necessário ao usar as imagens Docker), as dependências necessárias são instaladas com

```bash
pip install gramps_webapi[ai]
```

## Configurando um provedor de LLM

A comunicação com o LLM usa o framework Pydantic AI, que suporta APIs compatíveis com OpenAI. Isso permite usar um LLM implantado localmente via Ollama (veja [Compatibilidade do Ollama com OpenAI](https://ollama.com/blog/openai-compatibility)) ou APIs hospedadas como OpenAI, Anthropic ou Hugging Face TGI (Geração de Texto por Inferência). O LLM é configurado através dos parâmetros de configuração `LLM_MODEL` e `LLM_BASE_URL`.

Além das APIs compatíveis com OpenAI, os prefixos de modelo específicos do provedor do Pydantic AI podem ser usados para OpenAI, Anthropic, Google, Mistral, Groq, AWS Bedrock e Ollama. Outros provedores, como Cohere, Hugging Face e xAI, não estão instalados; os Provedores de Inferência do Hugging Face ainda podem ser usados através de seu endpoint compatível com OpenAI (`LLM_BASE_URL` definido como `https://router.huggingface.co/v1`).

Se o seu servidor de modelo não limitar o comprimento de uma resposta, defina `LLM_MAX_OUTPUT_TOKENS` para o número máximo de tokens que o modelo pode gerar por resposta (veja [Configuração](configuration.md)).

### Usando um LLM hospedado via a API OpenAI

Ao usar a API OpenAI, `LLM_BASE_URL` pode ser deixado não definido, enquanto `LLM_MODEL` deve ser definido como um dos modelos OpenAI, por exemplo, `gpt-4o-mini`. O LLM usa chamada de ferramentas para responder perguntas: ele consulta o banco de dados diretamente usando ferramentas especializadas e responde com base nos registros que encontra. Não requer conhecimento genealógico ou histórico profundo. Portanto, você pode tentar se um modelo pequeno/barato é suficiente.

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
```

### Usando um LLM local via Ollama

[Ollama](https://ollama.com/) é uma maneira conveniente de executar LLMs localmente. Consulte a documentação do Ollama para detalhes. Observe que LLMs requerem recursos computacionais significativos e todos, exceto os menores modelos, provavelmente serão muito lentos sem suporte a GPU. Como o assistente depende da chamada de ferramentas, escolha um modelo que suporte ferramentas, como [`qwen2.5`](https://ollama.com/library/qwen2.5). Comece com uma variante pequena como `qwen2.5:7b` e experimente uma maior se as respostas não forem boas o suficiente. Por favor, compartilhe qualquer experiência com a comunidade!

Ao implantar o Gramps Web com Docker Compose, você pode adicionar um serviço Ollama e apontar o Gramps Web para ele:

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

- Defina `LLM_MODEL` para o nome do modelo Ollama, incluindo sua tag (a parte após os dois pontos, por exemplo, `7b`), prefixada com `ollama:`. O prefixo faz com que o Pydantic AI use suas configurações específicas do Ollama para o modelo, que é a configuração recomendada.
- `LLM_BASE_URL` deve terminar em `/v1/`, por exemplo, `http://ollama:11434/v1/`.
- Com o prefixo `ollama:`, nem `OPENAI_API_KEY` nem a variável de ambiente `OLLAMA_BASE_URL` são necessárias. Se `LLM_BASE_URL` não estiver definido, o Gramps Web recuará para `OLLAMA_BASE_URL`.
- Alternativamente, você pode deixar de fora o prefixo (por exemplo, `LLM_MODEL: qwen2.5:7b`) e usar o Ollama através de sua API genérica compatível com OpenAI. Nesse caso, você também deve definir a variável de ambiente `OPENAI_API_KEY` como `ollama` (qualquer valor não vazio funciona).

Para solucionar problemas com o Ollama, você pode habilitar o registro de depuração definindo a variável de ambiente `OLLAMA_DEBUG=1` no ambiente do serviço Ollama.

!!! info
    Se você estiver usando o Ollama para o chat de IA do Gramps Web, por favor, apoie a comunidade completando esta documentação com quaisquer detalhes que estiverem faltando.

### Usando outros provedores

Sinta-se à vontade para enviar documentação para outros provedores e compartilhar sua experiência com a comunidade!
