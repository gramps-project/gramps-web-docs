# Sincronizar Gramps Web e Gramps Desktop

*Gramps Web Sync* é um complemento para Gramps que sincroniza o banco de dados do Gramps em seu computador desktop com o Gramps Web, incluindo arquivos de mídia. As alterações feitas em qualquer um dos lados são transferidas para o outro, para que você possa trabalhar localmente e na web na mesma árvore genealógica.

Como qualquer ferramenta de sincronização, não é um backup: se você excluir algo de um lado, será excluído do outro lado também. Mantenha backups regulares de sua árvore genealógica no formato Gramps XML.

## Instalação

O complemento requer Gramps 6.0 rodando em Python 3.10 ou mais recente. Ele está disponível no Gramps Desktop e pode ser instalado [da maneira usual](https://www.gramps-project.org/wiki/index.php/5.2_Addons#Installing_Addons_in_Gramps). Esta documentação descreve a versão mais recente do complemento; use o gerenciador de complementos do Gramps para atualizá-lo se necessário.

Seu desktop e seu servidor devem executar a mesma versão do Gramps. A versão tem a forma `MAJOR.MINOR.PATCH`, e `MAJOR` e `MINOR` devem coincidir. Veja [Obter Ajuda](../help/help.md) para saber como descobrir qual versão do Gramps seu servidor está executando.

### Requisitos do servidor

O complemento verifica duas coisas sobre o seu servidor assim que se conecta, antes de qualquer coisa ser baixada, e para com uma mensagem se alguma delas não for atendida:

- **Versão da API do Gramps Web 3.x.** Esta versão do complemento, para Gramps 6.0, funciona com a API do Gramps Web 3. Um servidor mais antigo precisa ser atualizado; um servidor rodando uma versão principal da API *mais nova* precisa de uma versão mais nova do Gramps, não de um complemento mais novo, porque cada linha de lançamento do Gramps emparelha com uma versão da API. Você pode encontrar a versão do seu servidor em *Configurações ▸ Informações da versão* no Gramps Web.
- **Uma fila de tarefas em segundo plano.** As alterações são aplicadas no servidor como uma tarefa em segundo plano. Sem uma fila de tarefas, isso ocorreria de forma síncrona e expiraria em qualquer árvore genealógica real.

Para aplicar alterações ao banco de dados remoto, você precisa de uma conta com o papel de editor, proprietário ou administrador.

### Armazenando sua senha (opcional)

Instale `keyring` (por exemplo, `sudo apt install python3-keyring` ou `sudo dnf install python3-keyring`) para armazenar a senha da API no gerenciador de senhas do seu sistema. Se o keyring não puder ser usado, o complemento informa e continua sem ele – você será simplesmente solicitado a inserir sua senha a cada vez.

No pacote **Snap** do Gramps, o keyring do sistema é bloqueado por confinamento até que você conecte a interface uma vez. O complemento mostra este comando quando detecta a situação:

```bash
snap connect gramps:password-manager-service
```

Em muitas configurações de desktop Gnome, um [bug no python keyring](https://github.com/jaraco/keyring/issues/496) significa que você precisa criar o arquivo de configuração `~/.config/python_keyring/keyringrc.cfg` com o seguinte conteúdo:

```ini
[backend]
default-keyring=keyring.backends.SecretService.Keyring
```

## Uso

O complemento está disponível no Gramps em *Ferramentas ▸ Processamento de Árvore Genealógica ▸ Gramps&nbsp;Web&nbsp;Sync*. Após confirmar o aviso do diálogo de que o histórico de desfazer será descartado, a janela de sincronização se abre. Nenhuma alteração é aplicada à sua árvore local ou ao servidor até que você as confirme explicitamente.

Uma faixa na parte superior da janela nomeia a árvore genealógica com a qual você está sincronizando, a conta e o endereço a que pertence, e quando foi sincronizada pela última vez. Na parte inferior, a versão do complemento e da API Web do servidor são mostradas, o que é útil ao relatar um problema.

### Conectando

Se você já sincronizou esta árvore genealógica antes e sua senha está armazenada, o complemento se conecta assim que é aberto e vai direto para a comparação. Caso contrário, ele solicita a URL base da sua instância do Gramps Web (exemplo: `https://mygrampsweb.com/`), seu nome de usuário e sua senha.

A URL e o nome de usuário são armazenados em texto simples no diretório do usuário do Gramps. A senha é armazenada no gerenciador de senhas do seu sistema apenas se você deixar **Lembrar senha** marcado; desmarcá-la remove qualquer senha já armazenada para aquele servidor. Se você inserir um endereço começando com `http://` em vez de `https://`, o complemento avisa você enquanto digita, porque sua senha seria enviada em texto claro.

Cada servidor com o qual você sincroniza é armazenado separadamente, juntamente com seu próprio registro de quando foi sincronizado pela última vez, para que você possa alternar entre dois servidores sem perturbar nenhum deles. Cada entrada também registra qual árvore genealógica local foi sincronizada pela última vez. O complemento só se conecta por conta própria quando isso coincide com a árvore que você tem aberta; caso contrário, ele mostra os detalhes da conexão e aguarda que você pressione *Conectar*.

Duas ações estão disponíveis enquanto nada está sendo escrito:

- **Mudar servidor…**, na faixa superior, retorna aos detalhes da conexão para que você possa apontar esta árvore para um servidor diferente. Isso interrompe uma comparação em andamento, em vez de fazê-lo esperar que termine.
- **Esquecer este servidor**, no painel de conexão, remove o endereço armazenado, nome de usuário e senha, juntamente com o registro de quando esta árvore foi sincronizada pela última vez. A próxima sincronização então compara as duas árvores do zero.

### Revisando as alterações

O complemento compara os bancos de dados local e remoto e mostra as ações que propõe realizar, agrupadas por qual banco de dados elas alteram:

```
▾ Mudará neste computador (7 objetos)
    ▾ Adicionar 3 objetos
        Pessoa   John Smith        I0123
    ▾ Atualizar 4 objetos
        …
▾ Mudará no servidor (5 objetos)
    …
```

Cada linha nomeia o objeto, para que você possa saber quem ou o que está afetado, em vez de apenas ver um ID do Gramps. Se algo vai ser excluído, uma nota acima da lista diz quantos objetos e de qual lado.

Pressione **Aplicar** para realizar o que a lista descreve.

A janela de sincronização não bloqueia o restante do Gramps, então você pode continuar trabalhando enquanto a lista está aberta. Se você editar um objeto afetado nesse meio tempo, o complemento percebe quando você pressiona Aplicar, para sem alterar nada, e pede que você compare novamente.

#### Modo de sincronização

O modo de sincronização é selecionado acima da lista de alterações. Alterá-lo reconstrói a lista, porque o modo decide o que cada diferença se torna.

- **Sincronização bidirecional** (o padrão) – as alterações de ambos os lados são combinadas. Objetos editados em ambos os lugares são mesclados.
- **Redefinir o servidor para corresponder a este computador** – o servidor é ajustado para corresponder a este computador. Qualquer coisa alterada apenas no servidor é descartada.
- **Redefinir este computador para corresponder ao servidor** – este computador é ajustado para corresponder ao servidor. Qualquer coisa alterada apenas aqui é descartada.

O modo **mesclar** disponível em versões anteriores à 1.5 foi removido. Ele diferia da sincronização bidirecional apenas em restaurar objetos excluídos de um lado em vez de propagar a exclusão. Se você dependia dele, use a sincronização bidirecional e restaure qualquer coisa que você deseja manter de um backup.

### Arquivos de mídia

Os arquivos de mídia são tratados como parte da mesma confirmação, não como um passo separado. Se algum arquivo precisar ser transferido, uma caixa de seleção abaixo da lista oferece movê-los:

```
[x] Também transferir 12 arquivos de mídia (4 para baixar, 8 para enviar)
```

Desmarque-a para sincronizar as alterações de objeto sem tocar nos arquivos.

Arquivos que estão faltando em *ambos* os lados são listados separadamente, porque nada pode ser feito sobre eles:

```
2 arquivos de mídia estão faltando em ambos os lados e não podem ser transferidos.
```

A sincronização de arquivos de mídia tem duas limitações:

- Se um arquivo local tiver um checksum diferente do que está armazenado no banco de dados do Gramps (isso pode acontecer, por exemplo, com arquivos do Word editados após serem adicionados ao Gramps), o upload falhará com uma mensagem de erro.
- A ferramenta não verifica a integridade de todos os arquivos locais. Se um arquivo existir sob o caminho armazenado para o objeto de mídia, mas diferir do arquivo no servidor, a ferramenta não o detectará. Use o complemento Media Verify para encontrar arquivos com checksums incorretos.

### Se uma sincronização falhar

Se uma sincronização falhar parcialmente – uma conexão perdida, por exemplo – o complemento relata o que já havia aplicado e oferece **Tentar novamente**, que retoma na etapa que falhou em vez de começar de novo. A cópia baixada da árvore remota é mantida, então tentar novamente não baixa e compara-a uma segunda vez.

Detalhes técnicos da falha estão disponíveis atrás de um expansor *Detalhes*, com um botão para copiá-los para um relatório de bug.

## Solução de problemas

**Mudanças inesperadas.** Se o complemento propuser um número alarmante de exclusões, verifique primeiro a faixa superior: ela nomeia a árvore genealógica no servidor para a qual você está prestes a escrever. Sincronizar uma árvore contra um servidor que possui uma árvore *diferente* produz exatamente esse sintoma.

Caso contrário, diferenças que você não esperava podem vir de inconsistências em um dos bancos de dados ou de relógios que estão fora de sincronia entre seu computador e seu servidor. Verifique se ambos os relógios estão corretamente ajustados (o fuso horário não importa, pois a ferramenta usa timestamps Unix) e execute a ferramenta de verificação e reparo em seu banco de dados local. Como último recurso, exporte seu banco de dados local para Gramps XML e reimporte-o em um novo banco de dados vazio. Esta é uma operação sem perda, mas garante que todos os dados sejam armazenados de forma consistente.

**Erros de arquivo de mídia.** Um upload falhado é frequentemente causado por uma incompatibilidade entre o checksum do arquivo no disco e o checksum no banco de dados local do Gramps, o que acontece com arquivos editáveis, como documentos de escritório editados fora do Gramps. Use o complemento Gramps Media Verify para corrigir os checksums.

**Erros de permissão.** Verifique o papel da sua conta de usuário do Gramps Web: apenas editores, proprietários e administradores podem aplicar alterações ao banco de dados remoto.

### Peça ajuda

Se nada do acima ajudar, pergunte à comunidade postando na [categoria Gramps Web do fórum Gramps](https://gramps.discourse.group/c/gramps-web/28). Por favor, forneça:

- a versão do complemento Gramps Web Sync, mostrada na parte inferior da janela de sincronização ao lado da versão da API Web do servidor (e por favor, use a versão mais recente lançada)
- a versão do Gramps desktop que você está usando
- as informações da versão do Gramps Web, encontradas em *Configurações ▸ Informações da versão*
- quaisquer detalhes sobre sua instalação do Gramps Web (auto-hospedado, Grampshub, ...)
- a saída dos logs do servidor do Gramps Web, se você tiver acesso a eles (ao usar Docker: `docker compose logs --tail 100 grampsweb` e `docker compose logs --tail 100 grampsweb-celery`)

Se você for solicitado a fornecer um log de depuração, inicie o Gramps [a partir da linha de comando](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Command_Line) com o registro de depuração ativado e reproduza o problema:

```bash
gramps --debug grampswebsync
```

## Contexto: como o complemento funciona

O complemento é destinado a manter um banco de dados local do Gramps em sincronia com um banco de dados remoto do Gramps Web, permitindo alterações locais e remotas (edição colaborativa).

Ele **não é adequado**

- para sincronizar com um banco de dados que não é um derivado direto (começando a partir de uma cópia do banco de dados ou exportação/importação do Gramps XML) do banco de dados local,
- para mesclar dois bancos de dados com um grande número de alterações em ambos os lados que precisam de atenção manual para mesclagem. Use a excelente [Ferramenta de Mesclagem de Importação](https://www.gramps-project.org/wiki/index.php/Import_Merge_Tool) para esse propósito.

Os princípios de operação são simples:

- Ele compara os bancos de dados local e remoto.
- Se houver diferenças, ele verifica o timestamp do último objeto idêntico, vamos chamá-lo de **t**.
- Se um objeto mudou mais recentemente do que **t** existe em um banco de dados, mas não no outro, ele é sincronizado para ambos (assuma como novo objeto).
- Se um objeto mudou pela última vez antes de **t** estiver ausente em um banco de dados, ele é excluído em ambos (assuma como objeto excluído).
- Se um objeto é diferente, mas mudou após **t** apenas em um banco de dados, sincronize-o para o outro (assuma como objeto modificado).
- Se um objeto é diferente, mas mudou após **t** em ambos os bancos de dados, mescle-os (assuma como modificação conflitante).

O tempo da última sincronização bem-sucedida também é registrado, separadamente para cada servidor, e usado como **t** quando é mais recente do que o mais novo objeto idêntico.

Este algoritmo é simples e robusto, pois não requer rastreamento do histórico de sincronização. No entanto, funciona melhor quando você *sincroniza frequentemente*.
