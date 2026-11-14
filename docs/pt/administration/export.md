# Exportar dados

A página de Exportação permite que você baixe os dados da árvore genealógica em vários formatos, bem como um arquivo de todos os arquivos de mídia.

## Exportar a árvore genealógica como Gramps XML

Para obter uma cópia dos dados da árvore genealógica, abra a página de Exportação no Gramps Web e selecione o formato Gramps XML. Clicar em "exportar" gerará o arquivo e iniciará o download assim que estiver pronto.

Observe que, se o seu usuário do Gramps Web não tiver permissão para visualizar registros privados, a exportação não conterá nenhum registro privado.

## Fazer backup da sua árvore genealógica

Para backups completos da árvore – incluindo suas configurações e usuários – consulte [Fazer backup e restaurar](backups.md). Uma exportação em Gramps XML pode servir como um backup dos dados da árvore genealógica apenas e pode ser restaurada através de [Restaurar a partir do Backup](backups.md#restore-from-backup).

## Compartilhar sua árvore genealógica com usuários de outros programas de genealogia

Quando compartilhar dados genealógicos como Gramps XML não é uma opção, você também pode exportar um arquivo GEDCOM. Observe que isso não é adequado como um backup da sua árvore no Gramps Web.

## Fazer backup dos seus arquivos de mídia

Para fazer backup dos seus arquivos de mídia, você pode criar e baixar um arquivo ZIP de todos os arquivos de mídia na página de Exportação.

Observe que, especialmente para árvores grandes, isso pode ser uma operação cara para o servidor e deve ser feito apenas se absolutamente necessário. Por essa razão, o número de arquivos de mídia que podem ser criados é limitado (por padrão, a um por hora). Se você atingir o limite, a mensagem de erro mostrará isso.

Uma opção melhor para fazer backup dos seus arquivos de mídia regularmente é usar o [complemento Gramps Web Sync](sync.md) (que em si não é uma solução de backup) e criar backups incrementais no seu computador local.

Em ambas as bases, se o seu usuário do Gramps Web não tiver permissão para visualizar registros privados, a exportação não conterá arquivos de objetos de mídia privados.

## Mover para uma instância diferente do Gramps Web

O Gramps Web não o prende a um provedor específico e você pode sempre se mover para uma instância diferente do Gramps Web sem perder nenhum dado e sem ter acesso direto a nenhum dos servidores.

Para realizar uma migração completa, siga estas etapas (supondo que você tenha permissões de proprietário da árvore):

1. Vá para a página de Exportação e exporte sua árvore como um arquivo Gramps XML (`.gramps`). Se você usar o [complemento Sync](sync.md), você também pode gerar a exportação no Gramps desktop.
2. Na página de Exportação, gere e baixe um arquivo de mídia. Se você usar o [complemento Sync](sync.md), você também pode simplesmente ZIPar sua pasta de mídia local do Gramps.
3. Vá para Configurações > Administração > Gerenciar usuários e clique no botão "Exportar detalhes do usuário". Isso fará o download de um arquivo JSON.
4. Na nova instância do Gramps Web, abra a página de Importação. Importe o arquivo `.gramps` exportado na etapa 1.
5. Na página de Importação da nova instância do Gramps Web, faça o upload do arquivo de mídia (ZIP).
6. Vá para Configurações > Administração > Gerenciar usuários da nova instância do Gramps Web. Clique no botão "Importar contas de usuário" e faça o upload do arquivo JSON baixado na etapa 3.

Observe que, embora suas contas de usuário sejam migradas, todos os seus usuários precisarão definir novas senhas usando o link "esqueci a senha", uma vez que as senhas são armazenadas em forma criptografada e não podem ser exportadas.
