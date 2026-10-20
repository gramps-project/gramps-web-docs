Hay dos formas de agregar un nuevo archivo multimedia (una imagen, archivo de audio, archivo de video o cualquier otro archivo), y los archivos multimedia existentes se pueden vincular a nuevos objetos a medida que se crean:

## Agregar un nuevo archivo multimedia independiente

Para agregar un archivo multimedia independiente, haz clic en el ícono + en la barra superior de la aplicación y selecciona "Objeto multimedia".

Haz clic en "seleccionar un archivo" para seleccionar un archivo de tu computadora. En un dispositivo móvil, al hacer clic en este botón tendrás la opción de tomar una foto directamente con la cámara de tu dispositivo.

Opcionalmente,

- ingresa una descripción del archivo multimedia en "título"
- ingresa una fecha
- establece el archivo multimedia como privado (lo que lo hará visible solo para usuarios con la autorización suficiente)

Haz clic en "agregar" para subir el archivo y crear el objeto multimedia.

## Agregar un nuevo archivo multimedia y vincularlo a otro objeto

Los siguientes tipos de objetos en Gramps pueden tener objetos multimedia adjuntos: personas, familias, eventos, lugares, fuentes y citas.

En la vista de detalles de cualquier objeto, haz clic en el botón azul de editar en la esquina inferior derecha (si no lo ves, tu usuario no tiene permisos de edición). Haz clic en la pestaña "galería" y haz clic en el botón azul +.

Se abrirá un diálogo que ofrece los mismos campos que se describieron en la sección anterior. Haz clic en "guardar" para subir el archivo, agregar un nuevo objeto multimedia y vincularlo al objeto visualizado.

## Fotos de perfil

La primera imagen en la galería de una persona se utiliza como su foto de perfil. En modo de edición, está marcada con una insignia de "Foto de perfil". Para usar una imagen diferente, muévela a la primera posición con los botones de flecha en las miniaturas de la galería.

Si una persona no tiene medios aún, el modo de edición muestra un marcador de **Agregar foto de perfil** en su lugar. Haz clic en él para subir un nuevo archivo multimedia o seleccionar uno existente.

## Vincular archivos multimedia existentes al crear un objeto

Cuando creas una nueva persona, familia, evento, lugar, fuente o cita, el formulario tiene una sección "Medios". Allí puedes seleccionar uno o más objetos multimedia existentes, que se vinculan al nuevo objeto cuando lo guardas.

Cuando creas una persona junto con sus eventos de nacimiento y muerte, los objetos multimedia seleccionados se vinculan solo a la persona, no a los eventos.

## Reconocimiento de texto (OCR)

Si el administrador del servidor ha habilitado el soporte de OCR, aparece un botón de "Reconocimiento de texto" debajo de la imagen en la vista de detalles de un objeto multimedia.

Haz clic en "Reconocimiento de texto", elige el idioma del texto mostrado en la imagen y luego haz clic en "Ejecutar". La imagen se procesa con [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) y el texto reconocido se muestra a continuación.

Si tu usuario tiene permisos de edición, haz clic en "Guardar como Nota" para crear una nueva nota (de tipo "Transcripción") que contenga el texto reconocido y vincularla al objeto multimedia.

!!! consejo
    La precisión del OCR depende en gran medida de la calidad de la imagen y del idioma seleccionado. Si el resultado parece incorrecto, intenta con un idioma diferente; por ejemplo, los documentos históricos alemanes a menudo necesitan la variante Fraktur en lugar del alemán estándar.
