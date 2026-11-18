# Importar arquivos de mídia

Se você importou uma [árvore genealógica](import.md) e precisa fazer o upload dos arquivos de mídia correspondentes, use **Importar Arquivos de Mídia** na [página de Importação](import.md), abaixo da importação da árvore genealógica. Ele espera um arquivo ZIP contendo os arquivos de mídia ausentes. O upload só é possível uma vez que a árvore contenha objetos de mídia, uma vez que os arquivos são correspondidos a objetos de mídia existentes – um arquivo de árvore genealógica apenas se refere aos seus arquivos de mídia, então importe-o primeiro.

Os arquivos são correspondidos a objetos de mídia na sua árvore de uma das duas maneiras:

- **Por checksum.** Para objetos de mídia que têm um checksum – como é o caso de árvores importadas do Gramps Desktop – o arquivo com o checksum correspondente é utilizado, independentemente do seu nome ou da estrutura de pastas no arquivo ZIP. Isso só funciona se os checksums no banco de dados do Gramps estiverem corretos, o que é garantido ao executar a ferramenta de verificação e reparo.
- **Por caminho ou nome de arquivo.** Objetos de mídia sem um checksum – como é típico após uma importação GEDCOM – são correspondidos pelo caminho relativo armazenado no objeto de mídia. Se nenhum arquivo no ZIP tiver esse caminho, eles são correspondidos apenas pelo nome do arquivo, ignorando maiúsculas e minúsculas (desde a API Gramps Web 3.26). Isso também funciona para caminhos absolutos de outros programas, como `C:\Users\...\Family\grandpa.jpg`, então você pode simplesmente colocar todos os arquivos no arquivo ZIP. Um nome de arquivo é usado apenas se for único, tanto no arquivo ZIP quanto entre os objetos de mídia que ainda não têm um arquivo.

Após o upload, o resultado indica para quantos objetos de mídia um arquivo foi encontrado e lista aqueles para os quais o arquivo ZIP não tinha arquivo, com seu ID do Gramps e caminho armazenado. Use esta lista para encontrar os arquivos ausentes e, em seguida, faça o upload de outro arquivo ZIP apenas com estes – arquivos que já estão no servidor não são afetados.

Se vários objetos de mídia tiverem o mesmo nome de arquivo em pastas diferentes, a correspondência pelo nome do arquivo não funciona para eles. Ou recrie a estrutura de pastas a partir dos caminhos armazenados no arquivo ZIP, ou importe tudo para o Gramps Desktop primeiro, que tem mais opções para associar arquivos de mídia existentes a uma árvore importada, e depois mova para o Gramps Web como descrito em [Vindo do Gramps Desktop](import.md#coming-from-gramps-desktop).

## Status do arquivo de mídia

A seção **Dados** das [Configurações de Administração](settings.md) mostra:

- O número total de objetos de mídia na árvore e se algum está sem um checksum
- O número de objetos de mídia cujo arquivo associado está ausente do servidor

Uma marca de verificação verde indica que está tudo em ordem. Se problemas forem detectados, links para os objetos afetados são exibidos. Checksums ausentes geralmente ocorrem quando os dados foram importados de um formato como GEDCOM que inclui referências de mídia, mas não os arquivos reais. Os arquivos ausentes podem ser carregados conforme descrito acima.
