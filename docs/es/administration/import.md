# Importar datos

Puedes llevar un árbol genealógico existente a Gramps Web subiendo un archivo exportado desde otro programa de genealogía, desde un servicio en línea o desde Gramps Desktop.

La importación tiene su propia página, disponible para los propietarios del árbol y administradores. Ábrela con **Importar árbol genealógico** en la sección **Datos** de la [configuración de administración](settings.md) (icono de usuario en la barra superior de la aplicación ▸ Administración). Mientras el árbol aún esté vacío, el botón **Importar árbol genealógico** de la tarjeta "Comenzar" en la página de inicio, en el árbol genealógico y en las listas también te lleva allí.

## Qué archivo usar

| Procedente de | Exporta tu árbol como | Extensión de archivo |
|---|---|---|
| Otro programa de genealogía o servicio en línea | GEDCOM | `.ged` |
| Gramps Desktop | Gramps XML | `.gramps` |
| GeneWeb | GeneWeb | `.gw` |
| Pro-Gen | Pro-Gen | `.def` |
| Una hoja de cálculo | Gramps CSV | `.csv` |
| Una libreta de direcciones | vCard | `.vcf` |

GEDCOM es el formato de intercambio común que casi todos los programas de genealogía y servicios en línea pueden exportar. Busca una opción de "Exportar" o "Descargar" en tu programa o en el sitio web, y elige GEDCOM si se te ofrecen varios formatos. La página del Wiki de Gramps [Importar desde otro programa de genealogía](https://www.gramps-project.org/wiki/index.php/Import_from_another_genealogy_program) tiene notas sobre programas específicos.

Si usas Gramps Desktop, elige Gramps XML (`.gramps`) en lugar de GEDCOM. Este lleva todos los datos de Gramps sin pérdida, y tus árboles en línea y fuera de línea mantienen los mismos identificadores, por lo que pueden ser [sincronizados](sync.md). Consulta [Procedente de Gramps Desktop](#coming-from-gramps-desktop) a continuación.

## Importar un archivo de árbol genealógico

1. Abre la página de Importación como se describió anteriormente.
2. Bajo "Importar árbol genealógico", elige tu archivo y haz clic en **Importar**. Se muestra el progreso de la carga.
3. El archivo se lee primero, y se muestra un cuadro de diálogo "Confirmar importación" que indica cuántos objetos contiene (personas, familias, eventos, lugares, etc.), y el [informe](#the-import-report) del importador si lo tiene. Aún no se ha añadido nada a tu árbol. Verifica que los conteos parezcan plausibles, luego haz clic en **Importar** para continuar, o **Cancelar** para abortar sin cambiar nada. Si tu árbol ya contiene personas, el cuadro de diálogo advierte que importar los mismos datos nuevamente crea duplicados.
4. La importación se ejecuta en segundo plano y se muestra un indicador de progreso. Una vez que se importan los datos, se actualiza el índice de búsqueda, lo que puede tardar un tiempo para un árbol grande. Si la importación falla, se muestra la razón.
5. Si el árbol aún no tiene una persona principal, se te ofrece elegir una.

Cuando la importación haya terminado, verifica el resultado: compara el número de personas en el panel de **Estadísticas** en la página de inicio con el número en tu antiguo programa, y abre una familia que conozcas bien para ver que los padres, hijos, fechas y lugares se hayan transferido como se esperaba. Si el archivo hace referencia a fotos u otros archivos multimedia, añádelos a continuación, bajo [Importar archivos multimedia](import-media.md) en la misma página.

!!! warning
    Una importación regular es puramente aditiva: siempre crea nuevos objetos y nunca actualiza o elimina los existentes, incluso para objetos que ya existen en tu árbol bajo el mismo ID o manejador de Gramps. Importar el mismo archivo dos veces – o importar un archivo que se superponga con datos ya en el árbol – duplicará cada objeto coincidente en lugar de fusionarlo o omitirlo.

    Si necesitas traer cambios realizados en otro lugar a un árbol que ya fue importado, utiliza [Restaurar desde copia de seguridad](backups.md#restore-from-backup) en su lugar, que reemplaza el árbol para que coincida con el archivo subido en lugar de añadirle. Esto requiere un archivo Gramps XML o una copia de seguridad de Gramps Web.

## El informe de importación

Los importadores informan lo que no pudieron importar completamente, por ejemplo, líneas GEDCOM que no entendieron, referencias a registros que faltan en el archivo, o un formato de archivo obsoleto. El informe se muestra bajo **Informe**, tanto en el cuadro de diálogo de confirmación como después de la importación. Léelo antes de confirmar: a menudo explica problemas que de otro modo solo notarías más tarde en el árbol.

No todos los mensajes son un problema: muchos archivos GEDCOM contienen datos específicos del programa que se informan pero se mantienen, consulta [Datos específicos del programa](#program-specific-data). Utiliza los botones junto al informe para copiarlo o descargarlo como un archivo de texto, por ejemplo, para pedir ayuda en el [foro](../help/help.md).

## Cuotas de uso

El administrador del servidor puede establecer límites para tu árbol (ver [Configuración del servidor](../install_setup/configuration.md)). La parte superior de la sección **Datos** muestra el uso actual en relación con estos límites:

- **Personas** – el número de objetos de persona en el árbol frente al máximo configurado (∞ si es ilimitado)
- **Almacenamiento multimedia** – tamaño total de los archivos multimedia subidos frente a la cuota de almacenamiento configurada (∞ si es ilimitado)

Una importación que exceda el límite en el número de personas es rechazada en su totalidad.

## Archivos GEDCOM

Se pueden importar archivos GEDCOM 5.5.1 y GEDCOM 7. Hay algunas cosas a tener en cuenta.

### Codificación de caracteres

Un archivo GEDCOM 5.5.1 declara su codificación de caracteres en su encabezado. Se admiten codificaciones UTF-8, UTF-16, ANSEL y Windows (ANSI). Si los nombres con acentos u otros caracteres especiales se ven distorsionados después de la importación (por ejemplo, `MÃ¼ller` en lugar de `Müller`), es probable que el archivo se haya exportado con una codificación diferente a la que declara. Exporta el archivo nuevamente desde tu antiguo programa, eligiendo UTF-8 si se te ofrece una opción, y [comienza de nuevo](#starting-over).

Los archivos GEDCOM 7 deben estar siempre codificados como UTF-8; otros archivos son rechazados con un error de "Archivo GEDCOM no válido".

### Datos específicos del programa

Muchos programas añaden sus propias extensiones a GEDCOM que otros programas no entienden. Gramps no elimina silenciosamente esos datos: las líneas que no puede interpretar se recopilan en una nota del tipo "importación GEDCOM", adjunta a la persona, familia u otro objeto al que pertenecen. Revisa estas notas para ver si algo importante no se ha transferido.

### Archivos multimedia

Un archivo GEDCOM contiene referencias a archivos multimedia (como fotos o documentos escaneados), pero no los archivos en sí. Después de la importación, los objetos multimedia existen en tu árbol, pero sus archivos faltan, lo que se muestra bajo [Estado del archivo multimedia](import-media.md#media-file-status). Para añadir los archivos, consulta [Importar archivos multimedia](import-media.md).

## Procedente de Gramps Desktop

Si estás utilizando Gramps Desktop, hay dos pasos para preparar tu base de datos y asegurarte de que todo funcione sin problemas en lo siguiente.

1. Verificar y reparar la base de datos
    - Opcional: crea una copia de seguridad de la base de datos exportando a Gramps XML
    - Ejecuta la [herramienta de Verificar y reparar base de datos](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database). Esto corrige algunas inconsistencias internas que podrían causar problemas en Gramps Web.
2. Convertir rutas de medios a relativas
    - Utiliza el Gestor de Medios de Gramps para [convertir todas las rutas de medios de absolutas a relativas](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Convert_paths_from_relative_to_absolute). Ten en cuenta que incluso con rutas relativas, cualquier archivo multimedia fuera de tu directorio de medios de Gramps no funcionará correctamente cuando se sincronice con Gramps Web.

Luego exporta tu árbol a Gramps XML (`.gramps`), impórtalo como se describió anteriormente y [sube tus archivos multimedia](import-media.md). Para seguir trabajando en el mismo árbol en tu computadora y en la web, utiliza el [complemento de sincronización de Gramps Web](sync.md).

### ¿Por qué no hay soporte para el paquete Gramps XML?

Si bien Gramps XML (`.gramps`) es el formato preferido para importar datos, el paquete Gramps XML (`.gpkg`) no es compatible con Gramps Web. Esto se debe a que las rutinas de importación y exportación para archivos multimedia no son adecuadas para su uso en un servidor web.

## Problemas comunes

**"Formato no soportado".** Solo se pueden importar las extensiones de archivo listadas [arriba](#which-file-to-use). Si tu programa o servicio en línea te dio un archivo ZIP, descomprímelo y sube el archivo `.ged` que hay dentro.

**Todo aparece dos veces.** El mismo archivo fue importado dos veces. Dado que las importaciones nunca fusionan, [comienza de nuevo](#starting-over).

**Caracteres especiales distorsionados.** Consulta [Codificación de caracteres](#character-encoding).

**Faltan fotos.** Consulta [Importar archivos multimedia](import-media.md).

### Comenzar de nuevo

Si una importación salió mal, o deseas corregir algo en tu antiguo programa e importar nuevamente, primero vacía el árbol utilizando [Eliminar todos los objetos](#delete-all-objects), luego importa el archivo corregido. Ten en cuenta que esto también elimina cualquier cambio que hayas realizado en Gramps Web desde la importación.

### Eliminar todos los objetos

!!! danger
    Eliminar objetos es **irreversible**. Haz una [copia de seguridad](backups.md) antes de continuar.

**Eliminar todos los objetos** se encuentra en la sección **Zona de peligro** de la [configuración de administración](settings.md). Hacer clic en **Eliminar** abre un cuadro de diálogo donde puedes elegir eliminar:

- **Todos los objetos** – limpia completamente el árbol
- **Tipos de objetos específicos** – por ejemplo, solo eventos o solo objetos multimedia

Se te pedirá que te autentiques nuevamente (inicies sesión de nuevo) para confirmar la acción. La eliminación se ejecuta como una tarea en segundo plano y se muestra un indicador de progreso.

!!! warning
    Eliminar solo un subconjunto de tipos de objetos (en lugar de todos los objetos a la vez) puede tardar mucho tiempo para árboles grandes, ya que el servidor debe verificar y actualizar todas las relaciones entre objetos.
