Hay dos formas de agregar un nuevo archivo multimedia (una imagen, archivo de audio, archivo de video o cualquier otro archivo):

## Agregar un nuevo archivo multimedia independiente

Para agregar un archivo multimedia independiente, haz clic en el ícono + en la barra superior de la aplicación y selecciona "Objeto Multimedia".

Haz clic en "seleccionar un archivo" para seleccionar un archivo de tu computadora. En un dispositivo móvil, al hacer clic en este botón se te dará la opción de tomar una foto directamente con la cámara de tu dispositivo.

Opcionalmente,

- ingresa una descripción del archivo multimedia en "título"
- ingresa una fecha
- establece el archivo multimedia como privado (lo que lo hará visible solo para usuarios con autorización suficiente)

Haz clic en "agregar" para subir el archivo y crear el objeto multimedia.

## Agregar un nuevo archivo multimedia y vincularlo a otro objeto

Los siguientes tipos de objetos en Gramps pueden tener objetos multimedia adjuntos: personas, familias, eventos, lugares, fuentes y citas.

En la vista de detalles de cualquier objeto, haz clic en el botón azul de editar en la esquina inferior derecha (si no lo ves, tu usuario no tiene permisos de edición). Haz clic en la pestaña "galería" y haz clic en el botón azul +.

Se abrirá un diálogo que ofrece los mismos campos que se describieron en la sección anterior. Haz clic en "guardar" para subir el archivo, agregar un nuevo objeto multimedia y vincularlo al objeto visualizado.

## Reconocimiento de texto (OCR)

Si el administrador del servidor ha habilitado el soporte de OCR, aparecerá un botón de "Reconocimiento de Texto" debajo de la imagen en la vista de detalles de un objeto multimedia.

Haz clic en "Reconocimiento de Texto", elige el idioma del texto mostrado en la imagen y luego haz clic en "Ejecutar". La imagen se procesa con [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) y el texto reconocido se muestra a continuación.

Si tu usuario tiene permisos de edición, haz clic en "Guardar como Nota" para crear una nueva nota (del tipo "Transcripción") que contenga el texto reconocido y vincularla al objeto multimedia.

!!! tip
    La precisión del OCR depende en gran medida de la calidad de la imagen y del idioma seleccionado. Si el resultado parece incorrecto, prueba con un idioma diferente; por ejemplo, los documentos históricos alemanes a menudo necesitan la variante Fraktur en lugar del alemán estándar.
