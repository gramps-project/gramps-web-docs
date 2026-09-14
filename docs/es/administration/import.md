# Importar datos

Puedes llevar un árbol genealógico existente a Gramps Web subiendo un archivo exportado desde otro programa de genealogía, desde un servicio en línea o desde Gramps Desktop.

La importación se encuentra en la sección **Datos** de la [Configuración de administración](settings.md) (ícono de usuario en la barra superior de la aplicación ▸ Administración), que está disponible para los propietarios del árbol y administradores. Mientras el árbol aún esté vacío, el botón **Importar árbol familiar** en la tarjeta "Comenzar" de la página de inicio también te lleva allí.

## Qué archivo usar

| Procedente de | Exporta tu árbol como | Extensión de archivo |
|---|---|---|
| Otro programa de genealogía o servicio en línea | GEDCOM | `.ged` |
| Gramps Desktop | Gramps XML | `.gramps` |
| GeneWeb | GeneWeb | `.gw` |
| Pro-Gen | Pro-Gen | `.def` |
| Una hoja de cálculo | Gramps CSV | `.csv` |
| Un libro de direcciones | vCard | `.vcf` |

GEDCOM es el formato de intercambio común que casi todos los programas de genealogía y servicios en línea pueden exportar. Busca una opción de "Exportar" o "Descargar" en tu programa o en el sitio web, y elige GEDCOM si se te ofrecen varios formatos. La página de la Wiki de Gramps [Importar desde otro programa de genealogía](https://www.gramps-project.org/wiki/index.php/Import_from_another_genealogy_program) tiene notas sobre programas específicos.

Si usas Gramps Desktop, elige Gramps XML (`.gramps`) en lugar de GEDCOM. Lleva todos los datos de Gramps sin pérdida, y tus árboles en línea y fuera de línea mantienen los mismos identificadores, por lo que pueden ser [sincronizados](sync.md). Consulta [Procedente de Gramps Desktop](#coming-from-gramps-desktop) a continuación.

## Importar un archivo de árbol familiar

1. Abre la sección **Datos** de la configuración de administración.
2. En "Importar árbol familiar", elige tu archivo y haz clic en **Importar**.
3. El archivo se analiza primero, y un cuadro de diálogo "Confirmar importación" muestra cuántos objetos contiene (personas, familias, eventos, lugares, etc.). Aún no se ha añadido nada a tu árbol. Verifica que los conteos parezcan plausibles, luego haz clic en **Importar** para continuar, o **Cancelar** para abortar sin cambiar nada.
4. La importación se ejecuta en segundo plano y se muestra un indicador de progreso. Una vez que se importan los datos, se actualiza el índice de búsqueda, lo que puede tardar un tiempo para un árbol grande.

Cuando la importación haya terminado, verifica el resultado: compara el número de personas en el panel de **Estadísticas** en la página de inicio con el número en tu antiguo programa, y abre una familia que conozcas bien para ver que los padres, hijos, fechas y lugares se hayan transferido como se esperaba.

!!! warning
    Una importación regular es puramente aditiva: siempre crea nuevos objetos y nunca actualiza o elimina los existentes, incluso para objetos que ya existen en tu árbol bajo el mismo ID o identificador de Gramps. Importar el mismo archivo dos veces – o importar un archivo que se superponga con datos ya en el árbol – duplicará cada objeto coincidente en lugar de fusionarlo o omitirlo.

    Si necesitas incorporar cambios realizados en otro lugar a un árbol que ya fue importado, utiliza [Restaurar desde copia de seguridad](settings.md#restore-from-backup) en su lugar, que reemplaza el árbol para que coincida con el archivo subido en lugar de agregarle. Esto requiere un archivo Gramps XML.

Si se ha establecido un límite en el número de personas para tu árbol (ver [Cuotas de uso](settings.md#usage-quotas)), una importación que lo exceda se rechaza en su totalidad.

## Archivos GEDCOM

Se pueden importar archivos GEDCOM 5.5.1 y GEDCOM 7. Hay algunas cosas a tener en cuenta.

### Codificación de caracteres

Un archivo GEDCOM 5.5.1 declara su codificación de caracteres en su encabezado. Se admiten las codificaciones UTF-8, UTF-16, ANSEL y Windows (ANSI). Si los nombres con acentos u otros caracteres especiales se ven distorsionados después de la importación (por ejemplo, `MÃ¼ller` en lugar de `Müller`), es probable que el archivo se haya exportado con una codificación diferente a la que declara. Exporta el archivo nuevamente desde tu antiguo programa, eligiendo UTF-8 si se ofrece una opción, y [comienza de nuevo](#starting-over).

Los archivos GEDCOM 7 deben estar siempre codificados como UTF-8; otros archivos son rechazados con un error de "Archivo GEDCOM no válido".

### Datos específicos del programa

Muchos programas añaden sus propias extensiones a GEDCOM que otros programas no entienden. Gramps no descarta silenciosamente tales datos: las líneas que no puede interpretar se recopilan en una nota del tipo "importación GEDCOM", adjunta a la persona, familia u otro objeto al que pertenecen. Revisa estas notas para ver si algo importante no se transfirió.

### Archivos multimedia

Un archivo GEDCOM contiene referencias a archivos multimedia (como fotos o documentos escaneados), pero no los archivos en sí. Después de la importación, los objetos multimedia existen en tu árbol, pero sus archivos faltan, lo que se muestra bajo [Estado de archivos multimedia](settings.md#media-file-status). Para agregar los archivos, consulta [Importar archivos multimedia](#import-media-files) a continuación.

## Procedente de Gramps Desktop

Si estás usando Gramps Desktop, hay dos pasos para preparar tu base de datos y asegurarte de que todo funcione sin problemas en lo siguiente.

1. Verificar y reparar la base de datos
    - Opcional: crea una copia de seguridad de la base de datos exportando a Gramps XML
    - Ejecuta la [herramienta de verificación y reparación de base de datos](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database). Esto corrige algunas inconsistencias internas que podrían causar problemas en Gramps Web.
2. Convertir rutas multimedia a relativas
    - Usa el Administrador de medios de Gramps para [convertir todas las rutas multimedia de absolutas a relativas](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Convert_paths_from_relative_to_absolute). Ten en cuenta que incluso con rutas relativas, cualquier archivo multimedia fuera de tu directorio de medios de Gramps no funcionará correctamente cuando se sincronice con Gramps Web.

Luego exporta tu árbol a Gramps XML (`.gramps`), impórtalo como se describe arriba y sube tus archivos multimedia como se describe en la siguiente sección. Para seguir trabajando en el mismo árbol en tu computadora y en la web, utiliza el [complemento de sincronización de Gramps Web](sync.md).

### ¿Por qué no hay soporte para el paquete Gramps XML?

Si bien Gramps XML (`.gramps`) es el formato preferido para importar datos, el paquete Gramps XML (`.gpkg`) no es compatible con Gramps Web. Esto se debe a que las rutinas de importación y exportación para archivos multimedia no son adecuadas para su uso en un servidor web.

## Importar archivos multimedia

Si has importado un árbol familiar y necesitas subir los archivos multimedia correspondientes, utiliza **Importar archivos multimedia** en la sección de Datos de la configuración de administración. Se espera un archivo ZIP que contenga los archivos multimedia faltantes. Los archivos se emparejan con objetos multimedia en tu árbol de una de dos maneras:

- **Por suma de verificación.** Para objetos multimedia que tienen una suma de verificación – como es el caso de los árboles importados desde Gramps Desktop – se utiliza el archivo con la suma de verificación coincidente, independientemente de su nombre o la estructura de carpetas en el archivo ZIP. Esto solo funciona si las sumas de verificación en la base de datos de Gramps son correctas, lo que asegura la ejecución de la herramienta de verificación y reparación.
- **Por ruta.** Los objetos multimedia sin una suma de verificación – como es típico después de una importación GEDCOM – se emparejan por su ruta: el archivo ZIP debe contener el archivo bajo exactamente la ruta relativa almacenada en el objeto multimedia.

Si las rutas almacenadas en tu archivo GEDCOM son absolutas (por ejemplo, `C:\Users\...\photo.jpg`), el emparejamiento por ruta no funcionará. En este caso, se recomienda primero importar todo en Gramps Desktop, que tiene más opciones para asociar archivos multimedia existentes con un árbol importado, y luego pasar a Gramps Web como se describe en [Procedente de Gramps Desktop](#coming-from-gramps-desktop).

## Problemas comunes

**"Formato no soportado".** Solo se pueden importar las extensiones de archivo listadas [arriba](#which-file-to-use). Si tu programa o servicio en línea te dio un archivo ZIP, descomprímelo y sube el archivo `.ged` que hay dentro.

**Todo aparece dos veces.** El mismo archivo fue importado dos veces. Dado que las importaciones nunca fusionan, [comienza de nuevo](#starting-over).

**Caracteres especiales distorsionados.** Consulta [Codificación de caracteres](#character-encoding).

**Faltan fotos.** Consulta [Importar archivos multimedia](#import-media-files).

### Comenzando de nuevo

Si una importación salió mal, o quieres corregir algo en tu antiguo programa e importar de nuevo, primero vacía el árbol utilizando [Eliminar todos los objetos](settings.md#delete-all-objects) en la Zona de peligro de la configuración de administración, luego importa el archivo corregido. Ten en cuenta que esto también elimina cualquier cambio que hayas realizado en Gramps Web desde la importación.
