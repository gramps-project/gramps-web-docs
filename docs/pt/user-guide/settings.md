# Configurações do Usuário

As Configurações do Usuário são acessíveis através do ícone do usuário na barra superior do aplicativo, em seguida, **Configurações do Usuário**. A página está organizada em seções colapsáveis. As alterações têm efeito imediato, a menos que indicado de outra forma.

!!! note
    As alterações nas Configurações do Usuário afetam apenas sua própria conta. As configurações que afetam todos os usuários da árvore são gerenciadas nas [Configurações de Administração](../administration/settings.md).

## Conta

Abrange suas informações de perfil, credenciais e segurança da conta.

### Informações do usuário

Mostra seu **nome de usuário** e **papel do usuário** atual (por exemplo, Convidado, Membro, Editor). Estes são somente leitura.

### Alterar e-mail

Digite um novo endereço de e-mail e clique em **Enviar** para atualizar o endereço associado à sua conta. O endereço de e-mail é usado para redefinições de senha e (se configurado) notificações.

### Alterar senha

Digite sua senha atual e uma nova senha, em seguida clique em **Enviar**. Se você esqueceu sua senha atual, use o link **Esqueceu a senha** na página de login.

### Métodos de login vinculados

Se o seu servidor oferece login único (veja [autenticação OIDC](../install_setup/oidc.md)), você pode vincular uma conta de um provedor, como Google ou o login da sua organização, à sua conta do Gramps Web. Você pode então fazer login com esse provedor e acessar sua conta existente, com seu papel e suas edições. Esta seção só aparece quando o login único está habilitado e o servidor suporta vinculação (API Gramps Web 3.24 e posteriores).

Para vincular uma conta, clique em **Vincular com** e o nome do provedor, faça login no provedor, e você será levado de volta às suas configurações. Se você não fez login recentemente, será solicitado que faça login novamente primeiro.

Uma conta de provedor só pode ser vinculada a uma conta do Gramps Web. Se você ver "Este login já está vinculado a outra conta", significa que está vinculado em outro lugar, por exemplo, a uma conta que foi criada quando você fez login pela primeira vez com esse provedor. Um administrador pode excluir essa outra conta, após a qual você poderá vinculá-la à sua.

Para desvincular uma conta, clique em **Desvincular**. Se for seu último método de login vinculado, você também precisará digitar sua senha, para que ainda possa fazer login depois. Se sua conta foi criada através de login único e você nunca definiu uma senha, use **Esqueceu a senha** na página de login para definir uma primeiro (isso requer que o servidor envie e-mails). Se o servidor permitir apenas login através de um provedor, a última conta vinculada não pode ser desvinculada.

## Aparência

Controla as preferências de exibição salvas em seu dispositivo.

### Idioma

Selecione o idioma para a interface do Gramps Web. A configuração de idioma é armazenada no armazenamento local do navegador e se aplica apenas ao dispositivo atual.

### Tema

Escolha entre:

- **Sistema** – segue a preferência de claro/escuro do sistema operacional (padrão)
- **Claro** – sempre usa o tema claro
- **Escuro** – sempre usa o tema escuro

A configuração do tema é armazenada no armazenamento local do navegador.

### Preferências da árvore genealógica

#### Visualização padrão da árvore genealógica

Define qual tipo de gráfico é aberto por padrão quando você navega para a página [Árvore Genealógica](tree.md). As opções são Árvore de Antepassados, Árvore de Descendentes, Gráfico de Ampulheta, Gráfico de Relacionamento e Gráfico em Leque.

Essa preferência é armazenada no armazenamento local do navegador.

## Ferramentas de desenvolvedor

### Token da API

Copia seu token de sessão atual para a área de transferência. O token pode ser usado para autenticar diretamente contra a API REST, por exemplo, na interface interativa Swagger UI servida pela sua instância do Gramps Web em `/api/swagger-ui`.

Clique em **Iniciar Swagger** para abrir a interface Swagger UI em uma nova aba com sua sessão já disponível.

!!! note
    O token de sessão tem um tempo de vida curto. Copie-o imediatamente antes de usá-lo no Swagger, pois pode expirar.
