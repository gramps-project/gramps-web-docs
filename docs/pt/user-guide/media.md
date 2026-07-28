Existem duas maneiras de adicionar um novo arquivo de mídia (uma imagem, arquivo de áudio, arquivo de vídeo ou qualquer outro arquivo):

## Adicionar um novo arquivo de mídia independente

Para adicionar um arquivo de mídia independente, clique no ícone + na barra superior do aplicativo e selecione "Objeto de Mídia".

Clique em "selecionar um arquivo" para escolher um arquivo do seu computador. Em um dispositivo móvel, clicar neste botão dará a opção de tirar uma foto diretamente com a câmera do seu dispositivo.

Opcionalmente,

- insira uma descrição do arquivo de mídia em "título"
- insira uma data
- defina o arquivo de mídia como privado (o que o tornará visível apenas para usuários com autorização suficiente)

Clique em "adicionar" para fazer o upload do arquivo e criar o objeto de mídia.

## Adicionar um novo arquivo de mídia e vinculá-lo a outro objeto

Os seguintes tipos de objeto no Gramps podem ter objetos de mídia anexados: pessoas, famílias, eventos, lugares, fontes e citações.

Na visualização de detalhes de qualquer objeto, clique no botão azul de editar no canto inferior direito (se você não vê-lo, seu usuário não tem permissões de edição). Clique na aba "galeria" e clique no botão azul +.

Uma caixa de diálogo será aberta que oferece os mesmos campos descritos na seção anterior. Clique em "salvar" para fazer o upload do arquivo, adicionar um novo objeto de mídia e vinculá-lo ao objeto visualizado.

## Reconhecimento de texto (OCR)

Se o administrador do servidor ativou o suporte a OCR, um botão "Reconhecimento de Texto" aparecerá abaixo da imagem na visualização de detalhes de um objeto de mídia.

Clique em "Reconhecimento de Texto", escolha o idioma do texto mostrado na imagem e, em seguida, clique em "Executar". A imagem é processada com [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) e o texto reconhecido é exibido abaixo.

Se seu usuário tiver permissões de edição, clique em "Salvar como Nota" para criar uma nova nota (do tipo "Transcrição") contendo o texto reconhecido e vinculá-la ao objeto de mídia.

!!! dica
    A precisão do OCR depende fortemente da qualidade da imagem e do idioma selecionado. Se o resultado parecer errado, experimente um idioma diferente – por exemplo, documentos históricos em alemão muitas vezes precisam da variante Fraktur em vez do alemão simples.
