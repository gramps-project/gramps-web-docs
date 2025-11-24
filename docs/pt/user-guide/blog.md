# Use o blog embutido

O blog é destinado a apresentar histórias sobre sua pesquisa de história familiar.

No banco de dados Gramps, as postagens do blog são representadas como fontes com uma nota anexada, contendo o texto do blog e, opcionalmente, arquivos de mídia para as imagens da postagem do blog. O Gramps Web trata cada fonte com a tag `Blog` como um artigo de blog.

## Adicionar uma postagem no blog

Para adicionar uma postagem no blog, você pode usar o Gramps Web ou o Gramps Desktop ([sincronizado](../administration/sync.md) com o Gramps Web), os passos são os mesmos em ambos os casos:

- Adicione uma nova fonte. O título da fonte será o título da sua postagem no blog, o autor da fonte será o autor da postagem.
- Opcionalmente, associe a fonte a um repositório correspondente ao seu blog no Gramps Web.
- Adicione uma nova nota à fonte. Escreva sua postagem no blog e copie o texto para a nota.
- Opcionalmente, adicione um ou mais arquivos de mídia à sua fonte. O primeiro arquivo de mídia será considerado como a imagem de pré-visualização da postagem exibida acima do texto. Todos os arquivos de mídia serão exibidos abaixo do texto como uma galeria.
- Adicione o rótulo `Blog` à fonte (crie-o se não existir).

## Relação entre blog e fontes

Como as postagens do blog são apenas fontes, todos os artigos do blog também aparecem na lista de fontes e aparecem como fontes nas pesquisas. Na visualização da fonte, há um botão "mostrar no blog" que o levará à visualização do blog para aquela postagem. A URL da postagem do blog também contém o ID Gramps da fonte correspondente, então um artigo em `seudominio.com/blog/S0123` corresponde à fonte em `seudominio.com/source/S0123`.

Na parte inferior de cada postagem do blog, há um botão "detalhes" que o levará à visualização da fonte.
