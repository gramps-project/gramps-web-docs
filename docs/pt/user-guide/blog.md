# Use o blog embutido

O blog é destinado a apresentar histórias sobre sua pesquisa de história familiar.

No banco de dados do Gramps, as postagens do blog são representadas como fontes com uma nota anexada, contendo o texto do blog e, opcionalmente, arquivos de mídia para as imagens da postagem do blog. O Gramps Web trata cada fonte com a tag `Blog` como um artigo de blog.

## Adicionar uma postagem no blog

A maneira mais rápida de escrever uma postagem é o formulário dedicado **Nova Postagem no Blog** no Gramps Web. Abra-o a partir do botão azul **+** na página do Blog ou do menu **Adicionar** (ícone de mais) na barra superior do aplicativo, escolhendo **Postagem no Blog**.

O formulário possui campos para:

- **Título** – o título da postagem (obrigatório)
- **Autor** – quem a escreveu
- **Conteúdo** – um editor de texto rico para a própria postagem
- **Mídia** – um ou mais objetos de mídia. O primeiro se torna a imagem de pré-visualização exibida acima do texto; todos eles aparecem como uma galeria abaixo.
- **Tags** e um interruptor **privado**, como para qualquer outro objeto

Salvar o formulário cria a fonte subjacente, a nota e a tag `Blog` para você, conforme descrito [abaixo](#relação-entre-blog-e-fontes).

### Adicionando uma postagem manualmente

Você também pode criar uma postagem construindo os objetos subjacentes você mesmo. Esta é a única maneira de fazê-lo no Gramps Desktop ([sincronizado](../administration/sync.md) com o Gramps Web), e os passos são os mesmos em ambos os aplicativos:

- Adicione uma nova fonte. O título da fonte será o título da sua postagem no blog, o autor da fonte será o autor da postagem.
- Opcionalmente, associe a fonte a um repositório correspondente ao seu blog no Gramps Web.
- Adicione uma nova nota à fonte. Escreva sua postagem no blog e copie o texto para a nota.
- Opcionalmente, adicione um ou mais arquivos de mídia à sua fonte. O primeiro arquivo de mídia será considerado a imagem de pré-visualização da postagem exibida acima do texto. Todos os arquivos de mídia serão mostrados abaixo do texto como uma galeria.
- Adicione o rótulo `Blog` à fonte (crie-o se não existir).

## Relação entre blog e fontes

Uma vez que as postagens do blog são apenas fontes, todos os artigos do blog também aparecem na lista de fontes e aparecem como fontes nas pesquisas. Na visualização da fonte, há um botão "mostrar no blog" que o levará à visualização do blog para essa postagem. A URL da postagem do blog também contém o ID do Gramps da fonte correspondente, então um artigo em `seudominio.com/blog/S0123` corresponde à fonte em `seudominio.com/source/S0123`.

Na parte inferior de cada postagem do blog, há um botão "detalhes" que o levará à visualização da fonte.
