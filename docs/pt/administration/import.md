# Importar dados

Você pode trazer uma árvore genealógica existente para o Gramps Web fazendo o upload de um arquivo exportado de outro programa de genealogia, de um serviço online ou do Gramps Desktop.

A importação pode ser encontrada na seção **Dados** das [configurações de Administração](settings.md) (ícone do usuário na barra superior do aplicativo ▸ Administração), que está disponível para proprietários de árvores e administradores. Enquanto a árvore ainda estiver vazia, o botão **Importar Árvore Genealógica** no cartão "Começar" da página inicial também leva a essa seção.

## Qual arquivo usar

| Vindo de | Exporte sua árvore como | Extensão do arquivo |
|---|---|---|
| Outro programa de genealogia ou serviço online | GEDCOM | `.ged` |
| Gramps Desktop | Gramps XML | `.gramps` |
| GeneWeb | GeneWeb | `.gw` |
| Pro-Gen | Pro-Gen | `.def` |
| Uma planilha | Gramps CSV | `.csv` |
| Um catálogo de endereços | vCard | `.vcf` |

GEDCOM é o formato de troca comum que quase todos os programas de genealogia e serviços online podem exportar. Procure uma opção de "Exportar" ou "Baixar" em seu programa ou no site, e escolha GEDCOM se você tiver várias opções de formato. A página do Gramps Wiki [Importar de outro programa de genealogia](https://www.gramps-project.org/wiki/index.php/Import_from_another_genealogy_program) tem notas sobre programas específicos.

Se você usar o Gramps Desktop, escolha Gramps XML (`.gramps`) em vez de GEDCOM. Ele carrega todos os dados do Gramps sem perda, e suas árvores online e offline mantêm os mesmos identificadores, para que possam ser [sincronizadas](sync.md). Veja [Vindo do Gramps Desktop](#coming-from-gramps-desktop) abaixo.

## Importar um arquivo de árvore genealógica

1. Abra a seção **Dados** das configurações de Administração.
2. Em "Importar Árvore Genealógica", escolha seu arquivo e clique em **Importar**.
3. O arquivo é analisado primeiro, e uma caixa de diálogo "Confirmar Importação" mostra quantos objetos ele contém (pessoas, famílias, eventos, lugares, e assim por diante). Nada foi adicionado à sua árvore ainda. Verifique se as contagens parecem plausíveis, depois clique em **Importar** para prosseguir ou **Cancelar** para abortar sem alterar nada.
4. A importação é executada em segundo plano e um indicador de progresso é exibido. Assim que os dados forem importados, o índice de pesquisa é atualizado, o que pode levar algum tempo para uma árvore grande.

Quando a importação terminar, verifique o resultado: compare o número de pessoas no painel **Estatísticas** na página inicial com o número em seu programa antigo e abra uma família que você conhece bem para ver se pais, filhos, datas e lugares foram transferidos conforme o esperado.

!!! warning
    Uma importação regular é puramente aditiva: ela sempre cria novos objetos e nunca atualiza ou exclui os existentes, mesmo para objetos que já existem em sua árvore sob o mesmo ID ou identificador do Gramps. Importar o mesmo arquivo duas vezes – ou importar um arquivo que se sobreponha a dados já na árvore – duplicará cada objeto correspondente em vez de mesclá-lo ou ignorá-lo.

    Se você precisar trazer alterações feitas em outro lugar para uma árvore que já foi importada, use [Restaurar do Backup](settings.md#restore-from-backup) em vez disso, que substitui a árvore para corresponder ao arquivo carregado em vez de adicionar a ele. Isso requer um arquivo Gramps XML.

Se um limite no número de pessoas foi definido para sua árvore (veja [Cotas de uso](settings.md#usage-quotas)), uma importação que excederia esse limite é recusada como um todo.

## Arquivos GEDCOM

Tanto arquivos GEDCOM 5.5.1 quanto GEDCOM 7 podem ser importados. Há algumas coisas a serem observadas.

### Codificação de caracteres

Um arquivo GEDCOM 5.5.1 declara sua codificação de caracteres em seu cabeçalho. As codificações UTF-8, UTF-16, ANSEL e Windows (ANSI) são suportadas. Se nomes com acentos ou outros caracteres especiais parecerem embaralhados após a importação (por exemplo, `MÃ¼ller` em vez de `Müller`), o arquivo provavelmente foi exportado com uma codificação diferente da que declara. Exporte o arquivo novamente de seu programa antigo, escolhendo UTF-8 se houver essa opção, e [comece de novo](#starting-over).

Arquivos GEDCOM 7 devem sempre ser codificados como UTF-8; outros arquivos são rejeitados com um erro "Arquivo GEDCOM inválido".

### Dados específicos do programa

Muitos programas adicionam suas próprias extensões ao GEDCOM que outros programas não entendem. O Gramps não descarta silenciosamente esses dados: linhas que não pode interpretar são coletadas em uma nota do tipo "importação GEDCOM", anexada à pessoa, família ou outro objeto ao qual pertencem. Revise essas notas para ver se algo importante não foi transferido.

### Arquivos de mídia

Um arquivo GEDCOM contém referências a arquivos de mídia (como fotos ou documentos digitalizados), mas não os arquivos em si. Após a importação, os objetos de mídia existem em sua árvore, mas seus arquivos estão ausentes, o que é mostrado sob [Status do arquivo de mídia](settings.md#media-file-status). Para adicionar os arquivos, veja [Importar arquivos de mídia](#import-media-files) abaixo.

## Vindo do Gramps Desktop

Se você estiver usando o Gramps Desktop, há duas etapas para preparar seu banco de dados para garantir que tudo funcione sem problemas a seguir.

1. Verifique e repare o banco de dados
    - Opcional: crie um backup do banco de dados exportando para Gramps XML
    - Execute a [ferramenta de Verificar e Reparar Banco de Dados](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database). Isso corrige algumas inconsistências internas que podem levar a problemas no Gramps Web.
2. Converter caminhos de mídia para relativos
    - Use o Gerenciador de Mídia do Gramps para [converter todos os caminhos de mídia de absolutos para relativos](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Convert_paths_from_relative_to_absolute). Observe que mesmo com caminhos relativos, quaisquer arquivos de mídia fora do diretório de mídia do Gramps não funcionarão corretamente quando sincronizados com o Gramps Web.

Em seguida, exporte sua árvore para Gramps XML (`.gramps`), importe-a conforme descrito acima e faça o upload de seus arquivos de mídia conforme descrito na próxima seção. Para continuar trabalhando na mesma árvore em seu computador e na web, use o [complemento Gramps Web Sync](sync.md).

### Por que não há suporte para pacote Gramps XML?

Embora Gramps XML (`.gramps`) seja o formato preferido para importação de dados, o pacote Gramps XML (`.gpkg`) não é suportado pelo Gramps Web. Isso ocorre porque as rotinas de importação e exportação para arquivos de mídia não são adequadas para uso em um servidor web.

## Importar arquivos de mídia

Se você importou uma árvore genealógica e precisa fazer o upload dos arquivos de mídia correspondentes, use **Importar Arquivos de Mídia** na seção Dados das configurações de Administração. Ele espera um arquivo ZIP contendo os arquivos de mídia ausentes. Os arquivos são correspondidos a objetos de mídia em sua árvore de uma das duas maneiras:

- **Por checksum.** Para objetos de mídia que têm um checksum – como é o caso de árvores importadas do Gramps Desktop – o arquivo com o checksum correspondente é usado, independentemente de seu nome ou da estrutura de pastas no arquivo ZIP. Isso só funciona se os checksums no banco de dados do Gramps estiverem corretos, o que a execução da ferramenta de verificação e reparo garante.
- **Por caminho.** Objetos de mídia sem um checksum – como é típico após uma importação GEDCOM – são correspondidos pelo seu caminho: o arquivo ZIP deve conter o arquivo exatamente sob o caminho relativo armazenado no objeto de mídia.

Se os caminhos armazenados em seu arquivo GEDCOM forem absolutos (por exemplo, `C:\Users\...\photo.jpg`), a correspondência por caminho não funcionará. Nesse caso, recomenda-se primeiro importar tudo para o Gramps Desktop, que tem mais opções para associar arquivos de mídia existentes a uma árvore importada, e depois mudar para o Gramps Web conforme descrito em [Vindo do Gramps Desktop](#coming-from-gramps-desktop).

## Problemas comuns

**"Formato não suportado".** Somente as extensões de arquivo listadas [acima](#qual-arquivo-usar) podem ser importadas. Se seu programa ou serviço online lhe deu um arquivo ZIP, descompacte-o e faça o upload do arquivo `.ged` dentro.

**Tudo aparece duas vezes.** O mesmo arquivo foi importado duas vezes. Como as importações nunca se mesclam, [comece de novo](#starting-over).

**Caracteres especiais embaralhados.** Veja [Codificação de caracteres](#character-encoding).

**Fotos estão faltando.** Veja [Importar arquivos de mídia](#import-media-files).

### Começando de novo

Se uma importação deu errado, ou você deseja corrigir algo em seu programa antigo e importar novamente, primeiro esvazie a árvore usando [Excluir todos os objetos](settings.md#delete-all-objects) na Zona de Perigo das configurações de Administração, depois importe o arquivo corrigido. Observe que isso também exclui quaisquer alterações que você tenha feito no Gramps Web desde a importação.
