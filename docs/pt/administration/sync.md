# Sincronizar Gramps Web e Gramps Desktop

*Gramps Web Sync* é um complemento para Gramps que permite sincronizar seu banco de dados Gramps em seu computador desktop com o Gramps Web, incluindo arquivos de mídia.

!!! warning
    Assim como qualquer ferramenta de sincronização, não considere isso como uma ferramenta de backup. Uma exclusão acidental de um lado será propagada para o outro lado. Certifique-se de criar backups regulares (no formato XML do Gramps) de sua árvore genealógica.

!!! info
    A documentação refere-se à versão mais recente do complemento Gramps Web Sync. Utilize o gerenciador de complementos do Gramps para atualizar o complemento para a versão mais recente, se necessário.

!!! note "O que mudou na versão 1.5"
    A interface do complemento foi reescrita na versão 1.5. O assistente passo a passo foi removido, substituído por uma única janela, e os arquivos de mídia agora são confirmados juntamente com as alterações dos objetos, em vez de em uma página separada depois. Se você está procurando o seletor de modo de sincronização, ele agora está **acima** da lista de alterações, em vez de abaixo. O modo de sincronização **mesclar** foi removido; veja [Modo de sincronização](#sync-mode) abaixo.

## Instalação

O complemento requer Gramps 6.0 rodando em Python 3.10 ou mais recente.  
Está disponível no Gramps Desktop e pode ser instalado [da maneira usual](https://www.gramps-project.org/wiki/index.php/5.2_Addons#Installing_Addons_in_Gramps).

!!! warning
    Certifique-se de usar a mesma versão do Gramps em seu desktop que a que está rodando em seu servidor. Veja a seção [Obter Ajuda](../help/help.md) para saber como descobrir qual versão do Gramps seu servidor está rodando. A versão do Gramps tem a forma `MAJOR.MINOR.PATCH`, e `MAJOR` e `MINOR` devem ser os mesmos na web e no desktop.

### Requisitos do servidor

O complemento verifica duas coisas sobre seu servidor assim que se conecta e se recusa a continuar se alguma delas não for atendida. Ambas as verificações ocorrem antes de qualquer coisa ser baixada.

- **Versão da API Gramps Web 3.x.** Esta versão do complemento, para Gramps 6.0, funciona com a API Gramps Web 3. Um servidor mais antigo precisa ser atualizado; um servidor rodando uma versão principal da API *mais nova* precisa de uma versão mais nova do Gramps, não de um complemento mais novo, pois cada linha de lançamento do Gramps emparelha com uma versão da API. Você pode encontrar a versão do seu servidor em *Configurações ▸ Informações da versão* no Gramps Web.
- **Uma fila de tarefas em segundo plano.** A sincronização envia suas alterações como uma tarefa em segundo plano. Em um servidor sem uma fila de tarefas configurada, aplicar alterações ocorreria de forma síncrona e expiraria em qualquer árvore genealógica real, então o complemento se recusa a iniciar em vez de falhar parcialmente.

Você também precisa de uma conta com pelo menos privilégios de editor para aplicar alterações ao banco de dados remoto.

Passo opcional:

??? note inline end "Erro no keyring do Gnome"
    Atualmente, há um [erro no keyring do python](https://github.com/jaraco/keyring/issues/496) que afeta muitas configurações de desktop do Gnome. Você pode precisar criar o arquivo de configuração `~/.config/python_keyring/keyringrc.cfg` e editá-lo para que fique assim:

        [backend]
        default-keyring=keyring.backends.SecretService.Keyring

- Instale `keyring` (por exemplo, `sudo apt install python3-keyring` ou `sudo dnf install python3-keyring`) para permitir o armazenamento da senha da API de forma segura no gerenciador de senhas do seu sistema.

Se o keyring não puder ser usado, o complemento informa isso e continua sem ele — você simplesmente será solicitado a inserir sua senha a cada vez. No pacote **Snap** do Gramps, o keyring do sistema é bloqueado por confinamento até que você conecte a interface uma vez:

```bash
snap connect gramps:password-manager-service
```

O complemento mostra este comando exato quando detecta a situação.

## Uso

Uma vez instalado, o complemento está disponível no Gramps em *Ferramentas ▸ Processamento de Árvore Genealógica ▸ Gramps&nbsp;Web&nbsp;Sync*. Após confirmar o aviso do diálogo de que o histórico de desfazer será descartado, a janela de sincronização se abre.

**Nenhuma alteração é aplicada à sua árvore local ou ao servidor até que você as confirme explicitamente.**

A janela tem uma faixa na parte superior nomeando a árvore genealógica com a qual você está sincronizando, a conta e o endereço a que pertence, e quando foi sincronizada pela última vez. Na parte inferior, a versão do complemento e da API Web do servidor são mostradas — útil ao relatar um problema.

### Conectando

Se você já sincronizou esta árvore genealógica antes e sua senha está armazenada, o complemento se conecta assim que é aberto e vai direto para a comparação. Caso contrário, ele pede a URL base de sua instância do Gramps Web (exemplo: `https://mygrampsweb.com/`), seu nome de usuário e sua senha.

A URL e o nome de usuário são armazenados em texto simples no diretório do usuário do Gramps. A senha é armazenada no gerenciador de senhas do seu sistema apenas se você deixar **Lembrar senha** marcado; desmarcá-lo remove qualquer senha já armazenada para aquele servidor.

!!! tip "Várias árvores genealógicas, vários servidores"
    Cada servidor com o qual você sincroniza é armazenado separadamente, juntamente com seu próprio registro de quando foi sincronizado pela última vez. Alternar entre dois servidores não perturba mais nenhum deles.

    Cada entrada também registra **qual árvore genealógica local** foi sincronizada pela última vez. O complemento só se conecta por conta própria quando isso corresponde à árvore que você tem aberta; caso contrário, ele mostra os detalhes da conexão e espera que você pressione *Conectar*, com um aviso se as credenciais armazenadas pertencem a uma árvore diferente. Isso é importante porque sincronizar uma árvore contra um servidor que possui uma árvore *diferente* proporia excluir o conteúdo de ambas.

Duas ações estão disponíveis enquanto nada está sendo escrito:

- **Mudar servidor…**, na faixa superior, retorna aos detalhes da conexão para que você possa apontar esta árvore para um servidor diferente. Isso interrompe uma comparação em andamento em vez de fazê-lo esperar que termine.
- **Esquecer este servidor**, no painel de conexão, remove o endereço, nome de usuário e senha armazenados, juntamente com o registro de quando esta árvore foi sincronizada pela última vez. A próxima sincronização então compara as duas árvores do zero.

Se você inserir um endereço começando com `http://` em vez de `https://`, um aviso aparecerá enquanto você digita. Sua senha seria enviada em texto claro, então use-a apenas para testes locais.

### Revisando as mudanças

O complemento compara os bancos de dados local e remoto e mostra o que propõe fazer. Ao contrário das versões anteriores, que listavam as diferenças brutas entre as duas árvores, a lista agora mostra as **ações** que serão realizadas, agrupadas por qual banco de dados elas alteram:

```
▾ Mudará neste computador (7 objetos)
    ▾ Adicionar 3 objetos
        Pessoa   John Smith        I0123
    ▾ Atualizar 4 objetos
        …
▾ Mudará no servidor (5 objetos)
    …
```

Cada linha nomeia o objeto, para que você possa saber quem ou o que está afetado, em vez de apenas ver um ID do Gramps.

Se algo for excluído, um aviso acima da lista diz quantos objetos e de qual lado. Isso aparece sempre que exclusões estão envolvidas, incluindo durante uma sincronização bidirecional comum que está propagando uma exclusão que você fez.

Pressione **Aplicar** para realizar o que a lista descreve.

!!! warning "Não edite enquanto revisa"
    A janela de sincronização não bloqueia o restante do Gramps, então você pode continuar trabalhando enquanto a lista está aberta. Se você editar um objeto afetado, o complemento detecta isso quando você pressiona Aplicar, para sem alterar nada, e pede que você compare novamente. Nada é perdido, mas a comparação precisa ser repetida.

#### Modo de sincronização

O modo de sincronização é selecionado **acima** da lista de alterações. Alterá-lo reconstrói a lista, pois o modo decide o que cada diferença realmente se torna.

- **Sincronização bidirecional** (o padrão) — alterações de ambos os lados são combinadas. Objetos editados em ambos os lugares são mesclados.
- **Redefinir o servidor para corresponder a este computador** — o servidor é feito para corresponder a este computador. Qualquer coisa alterada apenas no servidor é descartada.
- **Redefinir este computador para corresponder ao servidor** — este computador é feito para corresponder ao servidor. Qualquer coisa alterada apenas aqui é descartada.

!!! note
    O modo **mesclar** disponível em versões anteriores foi removido. Ele diferia da sincronização bidirecional apenas em restaurar objetos excluídos de um lado em vez de propagar a exclusão, o que não era uma distinção que a interface pudesse explicar de forma útil. Se você dependia disso, use a sincronização bidirecional e restaure qualquer coisa que você queira manter de um backup.

### Arquivos de mídia

Os arquivos de mídia são tratados como parte da mesma confirmação, não como um passo separado. Se algum arquivo precisar ser transferido, uma caixa de seleção abaixo da lista oferece movê-los:

```
[x] Também transferir 12 arquivos de mídia (4 para baixar, 8 para enviar)
```

Desmarque-a para sincronizar as alterações dos objetos sem tocar nos arquivos.

Arquivos que estão faltando em *ambos* os lados são listados separadamente, porque nada pode ser feito sobre eles:

```
2 arquivos de mídia estão faltando em ambos os lados e não podem ser transferidos.
```

Observe as seguintes limitações da sincronização de arquivos de mídia:

- Se um arquivo local tiver um checksum diferente do que está armazenado no banco de dados do Gramps (isso pode acontecer, por exemplo, com arquivos do Word quando editados após serem adicionados ao Gramps), o upload falhará com uma mensagem de erro.
- A ferramenta não verifica a integridade de todos os arquivos locais, então, se um arquivo local existir sob o caminho armazenado para o objeto de mídia, mas o arquivo for diferente do arquivo no servidor, a ferramenta não o detectará. Use o complemento Media Verify para detectar arquivos com checksums incorretos.

### Quando algo dá errado

Se uma sincronização falhar parcialmente — uma conexão perdida, por exemplo — o complemento relata o que já havia aplicado e oferece **Tentar novamente**, que retoma na etapa que falhou em vez de começar de novo. A cópia baixada da árvore remota é mantida, então tentar novamente não baixa e compara-a uma segunda vez.

Detalhes técnicos da falha estão disponíveis atrás de um expansor *Detalhes*, com um botão para copiá-los para um relatório de bug.

## Solução de Problemas

### Registro de depuração

Se você estiver enfrentando problemas com o complemento de Sincronização, inicie o Gramps com o registro de depuração ativado, [iniciando o Gramps a partir da linha de comando](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Command_Line) com a seguinte opção:

```bash
gramps --debug grampswebsync
```

Isso imprimirá muitas declarações de registro úteis na linha de comando que ajudarão você a identificar a causa do problema.

### Credenciais do servidor

Se a conexão falhar, verifique novamente a URL do servidor, seu nome de usuário e senha.

### O complemento se recusa a conectar

Se o complemento relata que a versão da API Gramps Web do servidor é muito antiga ou muito nova, ou que nenhuma fila de tarefas em segundo plano está configurada, veja [Requisitos do servidor](#server-requirements) acima. Essas verificações são feitas antes de qualquer outra coisa, então a mensagem nomeia o problema diretamente.

### Problemas de permissões

Se você encontrar um erro envolvendo permissões, verifique o papel do usuário da sua conta de usuário do Gramps Web. Você só pode aplicar alterações ao banco de dados remoto se for um usuário com o papel de editor, proprietário ou administrador.

### Mudanças inesperadas no banco de dados

Se a ferramenta de sincronização detectar mudanças que você acha que não aconteceram, pode ser que haja inconsistências em um dos bancos de dados que confundem o Gramps ao detectar uma diferença, ou que o horário esteja fora de sincronia entre seu computador local e seu servidor.

Verifique se os relógios em ambas as máquinas estão corretamente ajustados (observe que o fuso horário não importa, pois a ferramenta usa timestamps Unix, que são agnósticos em relação ao fuso horário).

Você também pode executar a ferramenta de verificação e reparo em seu banco de dados local e ver se isso ajuda.

Um método bruto, mas eficaz, para garantir que inconsistências em seu banco de dados local não estejam causando falsos positivos é exportar seu banco de dados para XML do Gramps e reimportá-lo em um novo banco de dados vazio. Esta é uma operação sem perdas, mas garante que todos os dados sejam importados de forma consistente.

!!! tip
    Se o complemento propuser um número alarmante de exclusões, verifique a faixa superior primeiro: ela nomeia a árvore genealógica no servidor para a qual você está prestes a escrever. Sincronizar contra um servidor que possui uma árvore *diferente* produz exatamente esse sintoma.

### Erros de timeout

A sincronização com o servidor é processada por um trabalhador em segundo plano, então sincronizações longas não devem expirar. Um servidor sem uma fila de tarefas configurada é recusado no momento da conexão por esse motivo — veja [Requisitos do servidor](#server-requirements).

Solicitações do complemento ao servidor expiram após 60 segundos sem uma resposta, então um servidor inacessível relata um erro de conexão em vez de travar indefinidamente.

### Erros inesperados de arquivos de mídia

Se o upload de um arquivo de mídia falhar, isso geralmente é causado por uma incompatibilidade no checksum do arquivo real no disco e o checksum no banco de dados local do Gramps. Isso acontece frequentemente com arquivos editáveis, como documentos de escritório, editados fora do Gramps. Por favor, use o complemento Gramps Media Verify para corrigir os checksums de todos os arquivos de mídia.

### Peça ajuda

Se tudo o que foi mencionado acima não ajudar, você pode pedir ajuda à comunidade postando na [categoria Gramps Web do fórum Gramps](https://gramps.discourse.group/c/gramps-web/28). Certifique-se de fornecer:

- a versão do complemento Gramps Web Sync (e use a versão mais recente lançada, por favor) — ela é mostrada na parte inferior da janela de sincronização, ao lado da versão da API Web do servidor
- a versão do Gramps desktop que você está usando
- a saída do registro de depuração do Gramps, ativada conforme descrito acima
- as informações da versão do Gramps Web (você pode encontrá-las em Configurações/Informações da versão)
- quaisquer detalhes que você puder fornecer sobre sua instalação do Gramps Web (auto-hospedado, Grampshub, ...)
- a saída dos logs do servidor Gramps Web, se você tiver acesso a eles (ao usar docker: `docker compose logs --tail 100 grampsweb` e `docker compose logs --tail 100 grampsweb-celery`)

## Contexto: como o complemento funciona

Se você está curioso sobre como o complemento realmente funciona, pode encontrar mais detalhes nesta seção.

O complemento é destinado a manter um banco de dados Gramps local em sincronia com um banco de dados Gramps Web remoto, permitindo alterações locais e remotas (edição colaborativa).

Ele **não é adequado**

- Para sincronizar com um banco de dados que não é um derivado direto (começando a partir de uma cópia do banco de dados ou exportação/importação XML do Gramps) do banco de dados local
- Para mesclar dois bancos de dados com um grande número de alterações em ambos os lados que precisam de atenção manual para mesclagem. Use a excelente [Ferramenta de Mesclagem de Importação](https://www.gramps-project.org/wiki/index.php/Import_Merge_Tool) para esse propósito.

Os princípios de operação da ferramenta são muito simples:

- Ele compara os bancos de dados local e remoto
- Se houver diferenças, verifica o timestamp do último objeto idêntico, vamos chamar de **t**
- Se um objeto mudou mais recentemente do que **t** existe em um banco de dados, mas não no outro, ele é sincronizado para ambos (assuma objeto novo)
- Se um objeto mudou pela última vez antes de **t** estiver ausente em um banco de dados, ele é excluído em ambos (assuma objeto excluído)
- Se um objeto é diferente, mas mudou após **t** apenas em um banco de dados, sincronize com o outro (assuma objeto modificado)
- Se um objeto é diferente, mas mudou após **t** em ambos os bancos de dados, mescle-os (assuma modificação conflitante)

O tempo da última sincronização bem-sucedida também é registrado, separadamente para cada servidor, e usado como **t** quando é mais recente do que o objeto idêntico mais novo.

Este algoritmo é simples e robusto, pois não requer o rastreamento do histórico de sincronização. No entanto, funciona melhor quando você *sincroniza frequentemente*.
