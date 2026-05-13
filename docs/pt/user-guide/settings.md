# Configurações do Usuário

As Configurações do Usuário são acessíveis através do ícone do usuário na barra superior do aplicativo, em seguida, **Configurações do Usuário**. As alterações entram em vigor imediatamente, a menos que indicado de outra forma.

## Informações do usuário

Mostra seu **nome de usuário** e **papel do usuário** atual (por exemplo, Convidado, Membro, Editor). Estes são somente leitura.

## Idioma

Selecione o idioma para a interface do Gramps Web. A configuração de idioma é armazenada no armazenamento local do navegador e se aplica apenas ao dispositivo atual.

## Tema

Escolha entre:

- **Sistema** – segue a preferência de luz/escuro do sistema operacional (padrão)
- **Claro** – sempre use o tema claro
- **Escuro** – sempre use o tema escuro

A configuração do tema é armazenada no armazenamento local do navegador.

## Alterar e-mail

Digite um novo endereço de e-mail e clique em **Enviar** para atualizar o endereço associado à sua conta. O endereço de e-mail é usado para redefinições de senha e (se configurado) notificações.

## Alterar senha

Digite sua senha atual e uma nova senha, em seguida, clique em **Enviar**. Se você esqueceu sua senha atual, use o link **Esqueceu a senha** na página de login.

## Preferências da árvore genealógica

### Visualização padrão da árvore genealógica

Define qual tipo de gráfico é aberto por padrão quando você navega para a página [Árvore Genealógica](tree.md). As opções são Árvore de Antecessores, Árvore de Descendentes, Gráfico de Ampulheta, Gráfico de Relacionamento e Gráfico em Leque.

Essa preferência é armazenada no armazenamento local do navegador.

## Ferramentas de desenvolvedor

### Token da API

Copia seu token de sessão atual para a área de transferência. O token pode ser usado para autenticar diretamente contra a API REST, por exemplo, na interface Swagger interativa servida pela sua instância do Gramps Web em `/api/swagger-ui`.

Clique em **Iniciar Swagger** para abrir a interface Swagger em uma nova aba com sua sessão já disponível.

!!! note
    O token de sessão tem um tempo de vida curto. Copie-o imediatamente antes de usá-lo no Swagger, pois pode expirar.
