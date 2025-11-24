# Configuração de desenvolvimento do backend

Esta página lista os passos necessários para começar a desenvolver a [Gramps Web API](https://github.com/gramps-project/gramps-web-api/), o backend (componente do servidor) do Gramps Web.


## Pré-requisitos

A configuração de desenvolvimento recomendada utiliza o Visual Studio Code com devcontainers. Esta abordagem criará um ambiente de desenvolvimento pré-configurado com todas as ferramentas que você precisa. Para começar, você precisará dos seguintes ingredientes:

- [Docker](https://docs.docker.com/get-docker/)
- [Visual Studio Code](https://code.visualstudio.com/) com a [extensão Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) instalada
- [Git](https://git-scm.com)

Você pode usar Linux, macOS ou Windows como seu sistema operacional.


## Começando

1. Abra o [repositório Gramps Web API](https://github.com/gramps-project/gramps-web-api) e clique em "fork"
2. Clone seu repositório forked para sua máquina local usando o Git
3. Abra o repositório clonado no Visual Studio Code. Quando solicitado, selecione "Reabrir no Container" ou abra manualmente a paleta de comandos (Ctrl+Shift+P ou Cmd+Shift+P) e selecione "Dev Containers: Rebuild and Reopen in Container".
4. Aguarde o dev container ser construído e iniciado. Isso pode levar alguns minutos, especialmente na primeira vez.


## Tarefas

Se você estiver apenas modificando o código do backend, não é necessariamente necessário iniciar um servidor web - os testes unitários usam um cliente de teste Flask que permite simular solicitações à API sem precisar de um servidor em execução.

No entanto, executar um servidor é útil se você

- quiser experimentar suas alterações com solicitações HTTP reais (veja [consultas manuais](queries.md)), 
- quiser visualizar o impacto das alterações na aplicação completa do Gramps Web, ou
- também quiser fazer alterações simultâneas no frontend (veja [configuração de desenvolvimento do frontend](../frontend/setup.md)).

Executar o servidor é simplificado no dev container por tarefas predefinidas. Você pode executar essas tarefas a partir da paleta de comandos (Ctrl+Shift+P ou Cmd+Shift+P) selecionando "Tasks: Run Task" e, em seguida, escolhendo uma das seguintes:
- "Serve Web API" - inicia o servidor de desenvolvimento Flask na porta 5555 com registro de depuração ativado
- "Start Celery worker" - inicia um trabalhador Celery para processar tarefas em segundo plano.


## Depuração

A depuração pode ser desafiadora às vezes, especialmente ao tentar rastrear comportamentos complexos ou identificar problemas sutis. Para facilitar isso, você pode depurar tanto uma instância da API em execução quanto casos de teste individuais diretamente no Visual Studio Code.

### Depurando a Gramps Web API

Para depurar a API em execução:

1. Abra o Visual Studio Code e vá para a visualização **Executar e Depurar**.  
2. Selecione a configuração **"Web API"** no menu suspenso.  
3. Comece a depuração.  
4. Quando você enviar solicitações para o backend (seja manualmente ou através da GUI do Gramps Web), a execução será pausada em qualquer ponto de interrupção que você tenha definido no código.  
   Isso permite que você inspecione variáveis, controle o fluxo e outros detalhes em tempo de execução.

### Depurando Casos de Teste

Para depurar um caso de teste específico:

1. Abra o arquivo de teste que você deseja depurar (por exemplo, `test_people.py`).  
2. No Visual Studio Code, abra a visualização **Executar e Depurar**.  
3. Escolha a configuração **"Arquivo de Teste Atual"**.  
4. Comece a depuração — a execução será interrompida em qualquer ponto de interrupção definido dentro desse arquivo de teste.  

Essa configuração permite que você percorra a lógica do teste, examine os valores das variáveis e compreenda melhor as falhas dos testes ou resultados inesperados.
