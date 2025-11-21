# Configuração de desenvolvimento frontend

Esta página descreve os passos necessários para começar com o desenvolvimento frontend.

## Pré-requisitos

A configuração de desenvolvimento recomendada utiliza o Visual Studio Code com devcontainers. Essa abordagem criará um ambiente de desenvolvimento pré-configurado com todas as ferramentas que você precisa.

Veja [Configuração de desenvolvimento backend](../backend/setup.md#prerequisites) para os pré-requisitos necessários.

## Começando

1. Abra o [repositório frontend do Gramps Web](https://github.com/gramps-project/gramps-web) e clique em "fork"
2. Clone seu repositório forked para sua máquina local usando Git
3. Abra o repositório clonado no Visual Studio Code. Quando solicitado, selecione "Reabrir no Container" ou abra manualmente a paleta de comandos (Ctrl+Shift+P ou Cmd+Shift+P) e selecione "Dev Containers: Rebuild and Reopen in Container".
4. Aguarde a construção e o início do dev container. Isso pode levar alguns minutos, especialmente na primeira vez.

## Executando o servidor de desenvolvimento frontend

Para executar o servidor de desenvolvimento frontend e visualizar o impacto de suas alterações no navegador, você pode usar as tarefas predefinidas no dev container.

Para que isso funcione, você primeiro precisa iniciar uma instância do [backend da API Gramps Web](../backend/setup.md#tasks). A maneira mais fácil de fazer isso é usar o dev container do backend e [executar a tarefa "Serve Web API"](../backend/setup.md#tasks) em uma janela separada do VS Code.

Uma vez que o backend esteja em execução, você pode executar o servidor de desenvolvimento frontend selecionando "Tasks: Run Task" na paleta de comandos (Ctrl+Shift+P ou Cmd+Shift+P) e, em seguida, escolhendo "Serve Gramps Web frontend".

Isso iniciará o servidor de desenvolvimento frontend na porta 8001, que você pode acessar em seu navegador em `http://localhost:8001`. O navegador será recarregado automaticamente quando você fizer alterações no código frontend, permitindo que você veja o impacto de suas alterações imediatamente.
