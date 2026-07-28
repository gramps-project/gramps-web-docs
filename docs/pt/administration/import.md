## Prepare seu banco de dados Gramps

Se você está usando o Gramps Desktop, há duas etapas para preparar seu banco de dados e garantir que tudo funcione corretamente a seguir. Se você está migrando de um programa de genealogia diferente, pode pular esta etapa.

1. Verifique e repare o banco de dados
    - Opcional: crie um backup do banco de dados exportando para Gramps XML
    - Execute a ferramenta de [Verificar e reparar banco de dados](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database). Isso corrige algumas inconsistências internas que podem levar a problemas no Gramps Web.
2. Converta os caminhos de mídia para relativos
    - Use o Gerenciador de Mídia do Gramps para [converter todos os caminhos de mídia de absoluto para relativo](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Convert_paths_from_relative_to_absolute). Observe que mesmo com caminhos relativos, quaisquer arquivos de mídia fora do seu diretório de mídia do Gramps não funcionarão corretamente quando sincronizados com o Gramps Web.

## Importar dados genealógicos

Para importar uma árvore genealógica existente, use a página "Importar" e faça o upload de um arquivo em qualquer um dos formatos de arquivo suportados pelo Gramps &ndash; veja [Importar de outro programa de genealogia](https://www.gramps-project.org/wiki/index.php/Import_from_another_genealogy_program) na Wiki do Gramps.

Se você já usa o Gramps Desktop, é altamente recomendável usar o formato Gramps XML (`.gramps`) para garantir que suas árvores online e offline usem os mesmos identificadores e possam ser [sincronizadas](sync.md).

Após clicar em "Importar", o arquivo é primeiro analisado e um diálogo "Confirmar Importação" mostra uma prévia dos objetos que o arquivo contém (pessoas, famílias, eventos, lugares, e assim por diante) antes que qualquer coisa seja adicionada à sua árvore. Revise as contagens e, em seguida, clique em "Importar" no diálogo para prosseguir, ou "Cancelar" para abortar sem alterar nada.

!!! warning
    Uma importação regular é puramente aditiva: ela sempre cria novos objetos e nunca atualiza ou exclui os existentes, mesmo para objetos que já existem em sua árvore sob o mesmo ID ou identificador do Gramps. Importar o mesmo arquivo duas vezes &ndash; ou importar um arquivo que se sobrepõe a dados já existentes na árvore &ndash; duplicará cada objeto correspondente em vez de mesclar ou ignorá-lo.

    Se você precisar trazer alterações feitas em outro lugar para uma árvore que já foi importada, use [Restaurar de Backup](settings.md#restore-from-backup) em vez disso, que substitui a árvore para corresponder ao arquivo enviado em vez de adicionar a ele.

## Por que não há suporte para pacote Gramps XML?

Embora o Gramps XML (`.gramps`) seja o formato preferido para importar dados, o pacote Gramps XML (`.gpkg`) não é suportado pelo Gramps Web. Isso ocorre porque as rotinas de importação e exportação para arquivos de mídia não são adequadas para uso em um servidor web.

Para importar os arquivos de mídia pertencentes a um arquivo `.gramps` importado, veja a próxima seção.

## Importar arquivos de mídia

Se você fez o upload de uma árvore genealógica e precisa fazer o upload dos arquivos de mídia correspondentes, pode usar o botão "importar arquivo de mídia" na página "Importar".

Ele espera um arquivo ZIP com os arquivos de mídia ausentes dentro. A estrutura de pastas no arquivo ZIP não precisa ser a mesma que a estrutura de pastas dentro da pasta de mídia do Gramps, pois os arquivos são correspondidos a objetos de mídia por seu checksum.

Observe que este recurso só funciona para arquivos que têm o checksum correto no banco de dados do Gramps (o que deve ser garantido executando a ferramenta de verificação e reparo na primeira etapa).

Ao migrar para o Gramps Web a partir de um programa de genealogia diferente que inclui arquivos de mídia, é recomendável primeiro importar tudo para o Gramps Desktop, que tem mais opções para associar arquivos de mídia existentes a uma árvore importada.
