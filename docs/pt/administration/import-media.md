# Importar arquivos de mídia

Se você importou uma [árvore genealógica](import.md) e precisa fazer o upload dos arquivos de mídia correspondentes, use **Importar Arquivos de Mídia** na seção Dados das [configurações de Administração](settings.md). Ele espera um arquivo ZIP contendo os arquivos de mídia ausentes. Os arquivos são correspondidos a objetos de mídia na sua árvore de uma das duas maneiras:

- **Por checksum.** Para objetos de mídia que têm um checksum – como é o caso de árvores importadas do Gramps Desktop – o arquivo com o checksum correspondente é usado, independentemente do seu nome ou da estrutura de pastas no arquivo ZIP. Isso só funciona se os checksums no banco de dados do Gramps estiverem corretos, o que é garantido ao executar a ferramenta de verificação e reparo.
- **Por caminho.** Objetos de mídia sem um checksum – como é típico após uma importação GEDCOM – são correspondidos pelo seu caminho: o arquivo ZIP deve conter o arquivo exatamente sob o caminho relativo armazenado no objeto de mídia.

Se os caminhos armazenados no seu arquivo GEDCOM forem absolutos (por exemplo, `C:\Users\...\photo.jpg`), a correspondência por caminho não funcionará. Nesse caso, é recomendado primeiro importar tudo para o Gramps Desktop, que tem mais opções para associar arquivos de mídia existentes a uma árvore importada, e depois mover para o Gramps Web, conforme descrito em [Vindo do Gramps Desktop](import.md#coming-from-gramps-desktop).

## Status do arquivo de mídia

A seção **Dados** das [configurações de Administração](settings.md) mostra:

- O número total de objetos de mídia na árvore e se algum está sem um checksum
- O número de objetos de mídia cujo arquivo associado está ausente do servidor

Uma marca de verificação verde indica que está tudo em ordem. Se problemas forem detectados, links para os objetos afetados são exibidos. Checksums ausentes geralmente ocorrem quando os dados foram importados de um formato como GEDCOM que inclui referências de mídia, mas não os arquivos reais. Os arquivos ausentes podem ser enviados conforme descrito acima.
