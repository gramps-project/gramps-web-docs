# Sincronizar Gramps Web e Gramps Desktop

*Gramps Web Sync* é um complemento para Gramps que permite sincronizar seu banco de dados Gramps em seu computador desktop com o Gramps Web, incluindo arquivos de mídia.

!!! warning
    Assim como qualquer ferramenta de sincronização, não considere isso como uma ferramenta de backup. Uma exclusão acidental de um lado será propagada para o outro lado. Certifique-se de criar backups regulares (no formato XML do Gramps) da sua árvore genealógica.

!!! info
    A documentação refere-se à versão mais recente do complemento Gramps Web Sync. Por favor, use o gerenciador de complementos do Gramps para atualizar o complemento para a versão mais recente, se necessário.

## Instalação

O complemento requer Gramps 6.0 rodando em Python 3.10 ou mais recente.  
Está disponível no Gramps Desktop e pode ser instalado [da maneira usual](https://www.gramps-project.org/wiki/index.php/5.2_Addons#Installing_Addons_in_Gramps).

!!! warn
    Certifique-se de usar a mesma versão do Gramps em seu desktop que a que está rodando em seu servidor. Veja a seção [Obter Ajuda](../help/help.md) para saber como descobrir qual versão do Gramps seu servidor está rodando. A versão do Gramps tem a forma `MAJOR.MINOR.PATCH`, e `MAJOR` e `MINOR` devem ser os mesmos na web e no desktop.

Passo opcional:

??? note inline end "Erro no chaveiro do Gnome"
    Atualmente, há um [erro no python keyring](https://github.com/jaraco/keyring/issues/496) que afeta muitas configurações de desktop do Gnome. Você pode precisar criar o arquivo de configuração `~/.config/python_keyring/keyringrc.cfg` e editá-lo para ficar assim:

        [backend]
        default-keyring=keyring.backends.SecretService.Keyring

- Instale `keyring` (por exemplo, `sudo apt install python3-keyring` ou `sudo dnf install python3-keyring`) para permitir armazenar a senha da API com segurança no gerenciador de senhas do seu sistema.

## Uso

Uma vez instalado, o complemento está disponível no Gramps em *Ferramentas > Processamento de Árvore Genealógica > Gramps&nbsp;Web&nbsp;Sync*. Uma vez iniciado, e após confirmar o diálogo de que o histórico de desfazer será descartado, um assistente o guiará pelos passos de sincronização. Observe que nenhuma alteração será aplicada à sua árvore local ou ao servidor até que você as confirme explicitamente.

### Passo 1: inserir credenciais do servidor

A ferramenta pedirá a URL base (exemplo: `https://mygrampsweb.com/`) da sua instância do Gramps Web, seu nome de usuário e senha. Você precisa de uma conta com pelo menos privilégios de editor para sincronizar alterações de volta ao seu banco de dados remoto. O nome de usuário e a URL serão armazenados em texto simples no diretório do usuário do Gramps, a senha será armazenada apenas se `keyring` estiver instalado (veja acima).

### Passo 2: revisar alterações

Após confirmar suas credenciais, a ferramenta compara os bancos de dados local e remoto e avalia se há diferenças. Se houver, ela exibe uma lista de alterações de objetos (onde um objeto pode ser uma pessoa, família, evento, lugar, etc.) pertencentes a uma das seguintes categorias:

- adicionado localmente
- excluído localmente
- modificado localmente
- adicionado remotamente 
- excluído remotamente
- modificado remotamente
- modificado simultaneamente (ou seja, em ambos os lados)

A ferramenta usa carimbos de data/hora para avaliar qual lado é mais recente para cada objeto (veja "Contexto" abaixo se você estiver interessado nos detalhes).

Se as alterações parecerem conforme o esperado, você pode clicar em "Aplicar" para aplicar as alterações necessárias aos bancos de dados local e remoto.

!!! tip "Avançado: Modo de sincronização"
    Abaixo da lista de alterações, você pode selecionar um modo de sincronização.
    
    O padrão, **sincronização bidirecional**, significa que aplicará alterações a ambos os lados (local e remoto) replicando as alterações detectadas (objetos adicionados localmente serão adicionados no lado remoto, etc.). Objetos modificados em ambos os lados serão mesclados e atualizados em ambos os lados também.

    A opção **reiniciar remoto para local** garantirá que o banco de dados remoto do Gramps fique exatamente como o local. Quaisquer objetos detectados como "adicionados remotamente" serão excluídos novamente, objetos detectados como "excluídos remotamente" serão adicionados novamente, etc. *Nenhuma alteração será aplicada ao banco de dados local do Gramps.*

    A opção **reiniciar local para remoto** funciona de forma oposta e define o estado local para o do banco de dados remoto. *Nenhuma alteração será aplicada ao banco de dados remoto.*

    Finalmente, a opção **mesclar** é semelhante à sincronização bidirecional, pois modifica ambos os bancos de dados, mas *não exclui nenhum objeto*, mas sim restaura todos os objetos excluídos de apenas um lado.

### Passo 3: sincronizar arquivos de mídia

*Após* os bancos de dados terem sido sincronizados, a ferramenta verifica se há novos arquivos de mídia ou arquivos atualizados. Se encontrar algum, exibirá uma lista e pedirá confirmação para fazer o upload/download dos arquivos necessários.

Observe as seguintes limitações da sincronização de arquivos de mídia:

- Se um arquivo local tiver um checksum diferente do armazenado no banco de dados do Gramps (isso pode acontecer, por exemplo, com arquivos do Word quando editados após serem adicionados ao Gramps), o upload falhará com uma mensagem de erro.
- A ferramenta não verifica a integridade de todos os arquivos locais, portanto, se um arquivo local existir no caminho armazenado para o objeto de mídia, mas o arquivo for diferente do arquivo no servidor, a ferramenta não o detectará. Use o complemento Media Verify para detectar arquivos com checksums incorretos.

## Solução de Problemas

### Registro de depuração

Se você estiver enfrentando problemas com o complemento Sync, inicie o Gramps com o registro de depuração habilitado [iniciando o Gramps a partir da linha de comando](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Command_Line) com a seguinte opção:

```bash
gramps --debug grampswebsync
```

Isso imprimirá muitas declarações de registro úteis na linha de comando que ajudarão você a identificar a causa do problema.

### Credenciais do servidor

Se o primeiro passo já falhar, verifique novamente a URL do servidor, seu nome de usuário e senha.

### Problemas de permissões

Se você encontrar um erro envolvendo permissões, verifique o papel do usuário da sua conta de usuário do Gramps Web. Você só pode aplicar alterações ao banco de dados remoto se for um usuário com o papel de editor, proprietário ou administrador.

### Alterações inesperadas no banco de dados

Se a ferramenta de sincronização detectar alterações que você acha que não ocorreram, pode ser que haja inconsistências em um dos bancos de dados que enganem o Gramps ao detectar uma diferença, ou que o tempo esteja fora de sincronia entre seu computador local e seu servidor.

Verifique se os relógios em ambas as máquinas estão configurados corretamente (observe que o fuso horário não importa, pois a ferramenta usa timestamps Unix, que são agnósticos em relação ao fuso horário).

Você também pode executar a ferramenta de verificação e reparo em seu banco de dados local e ver se isso ajuda.

Um método de força bruta, mas eficaz, para garantir que inconsistências em seu banco de dados local não estejam causando falsos positivos é exportar seu banco de dados para Gramps XML e reimportá-lo em um novo banco de dados vazio. Esta é uma operação sem perdas, mas garante que todos os dados sejam importados de forma consistente.

### Erros de tempo limite

Se você estiver enfrentando erros de tempo limite (por exemplo, indicados por um erro de status HTTP 408 ou outra mensagem de erro incluindo a palavra "timeout"), é provável que seja devido a um grande número de alterações que precisam ser sincronizadas para o lado remoto em combinação com a configuração do seu servidor.

Para versões do complemento de sincronização anteriores a v1.2.0 e versões da API do Gramps Web anteriores a v2.7.0 (veja a guia de informações da versão no Gramps Web), a sincronização para o lado do servidor era processada em uma única solicitação que poderia expirar, dependendo da configuração do servidor, após um a, no máximo, alguns minutos. Para sincronizações grandes (como após importar milhares de objetos no banco de dados local ou tentar sincronizar um banco de dados local completo com um banco de dados do lado do servidor vazio), isso pode ser muito curto.

Se você estiver usando o complemento de sincronização v1.2.0 ou posterior e a API do Gramps Web v2.7.0 ou posterior, a sincronização do lado do servidor é processada por um trabalhador em segundo plano e pode durar muito tempo (uma barra de progresso será exibida) e erros de tempo limite não devem ocorrer.

### Erros inesperados de arquivos de mídia

Se o upload de um arquivo de mídia falhar, isso geralmente é causado por uma incompatibilidade entre o checksum do arquivo real no disco e o checksum no banco de dados local do Gramps. Isso acontece frequentemente com arquivos editáveis, como documentos de escritório, editados fora do Gramps. Por favor, use o complemento Gramps Media Verify para corrigir os checksums de todos os arquivos de mídia.

### Peça ajuda

Se tudo o que foi mencionado acima não ajudar, você pode pedir ajuda à comunidade postando na [categoria Gramps Web do fórum Gramps](https://gramps.discourse.group/c/gramps-web/28). Certifique-se de fornecer:

- a versão do complemento Gramps Web Sync (e use a versão mais recente lançada, por favor)
- a versão do Gramps desktop que você está usando
- a saída do registro de depuração do Gramps, habilitado conforme descrito acima
- as informações da versão do Gramps Web (você pode encontrá-las em Configurações/Informações da versão)
- quaisquer detalhes que você puder fornecer sobre sua instalação do Gramps Web (auto-hospedado, Grampshub, ...)
- a saída dos logs do servidor do Gramps Web, se você tiver acesso a eles (ao usar docker: `docker compose logs --tail 100 grampsweb` e `docker compose logs --tail 100 grampsweb-celery`)

## Contexto: como o complemento funciona

Se você estiver curioso sobre como o complemento realmente funciona, pode encontrar mais detalhes nesta seção.

O complemento é destinado a manter um banco de dados local do Gramps em sincronia com um banco de dados remoto do Gramps Web, para permitir tanto alterações locais quanto remotas (edição colaborativa).

Ele **não é adequado**

- Para sincronizar com um banco de dados que não seja um derivado direto (começando de uma cópia do banco de dados ou exportação/importação do Gramps XML) do banco de dados local
- Para mesclar dois bancos de dados com um grande número de alterações em ambos os lados que precisam de atenção manual para mesclagem. Use a excelente [Import Merge Tool](https://www.gramps-project.org/wiki/index.php/Import_Merge_Tool) para esse propósito.

Os princípios de operação da ferramenta são muito simples:

- Ela compara os bancos de dados local e remoto
- Se houver diferenças, verifica o carimbo de data/hora do último objeto idêntico, vamos chamá-lo de **t**
- Se um objeto mudou mais recentemente do que **t** existe em um banco de dados, mas não no outro, ele é sincronizado para ambos (assuma que é um novo objeto)
- Se um objeto mudou pela última vez antes de **t** estiver ausente em um banco de dados, ele é excluído em ambos (assuma que é um objeto excluído)
- Se um objeto é diferente, mas mudou após **t** apenas em um banco de dados, sincronize para o outro (assuma que é um objeto modificado)
- Se um objeto é diferente, mas mudou após **t** em ambos os bancos de dados, mescle-os (assuma que é uma modificação conflitante)

Esse algoritmo é simples e robusto, pois não requer rastreamento do histórico de sincronização. No entanto, funciona melhor quando você *sincroniza com frequência*.
