## Prepara tu base de datos de Gramps

Si estás utilizando Gramps Desktop, hay dos pasos para preparar tu base de datos y asegurarte de que todo funcione sin problemas en lo siguiente. Si estás migrando desde un programa de genealogía diferente, puedes omitir este paso.

1. Verifica y repara la base de datos
    - Opcional: crea una copia de seguridad de la base de datos exportando a Gramps XML
    - Ejecuta la [herramienta de verificación y reparación de base de datos](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database). Esto corrige algunas inconsistencias internas que podrían llevar a problemas en Gramps Web.
2. Convierte las rutas de medios a relativas
    - Usa el Administrador de Medios de Gramps para [convertir todas las rutas de medios de absolutas a relativas](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Convert_paths_from_relative_to_absolute). Ten en cuenta que incluso con rutas relativas, cualquier archivo de medios fuera de tu directorio de medios de Gramps no funcionará correctamente cuando se sincronice con Gramps Web.

## Importar datos genealógicos

Para importar un árbol genealógico existente, utiliza la página "Importar" y sube un archivo en cualquiera de los formatos de archivo soportados por Gramps &ndash; consulta [Importar desde otro programa de genealogía](https://www.gramps-project.org/wiki/index.php/Import_from_another_genealogy_program) en la Wiki de Gramps.

Si ya usas Gramps Desktop, se recomienda encarecidamente utilizar el formato Gramps XML (`.gramps`) para asegurar que tus árboles en línea y fuera de línea utilicen los mismos identificadores y puedan ser [sincronizados](sync.md).

## ¿Por qué no hay soporte para el paquete Gramps XML?

Mientras que Gramps XML (`.gramps`) es el formato preferido para importar datos, el *paquete* Gramps XML (`.gpkg`) no es soportado por Gramps Web. Esto se debe a que las rutinas de importación y exportación para archivos de medios no son adecuadas para su uso en un servidor web.

Para importar los archivos de medios que pertenecen a un archivo `.gramps` importado, consulta la siguiente sección.

## Importar archivos de medios

Si has subido un árbol genealógico y necesitas subir los archivos de medios correspondientes, puedes usar el botón "importar archivo de medios" en la página "Importar".

Se espera un archivo ZIP con los archivos de medios faltantes dentro. La estructura de carpetas en el archivo ZIP no tiene que ser la misma que la estructura de carpetas dentro de la carpeta de medios de Gramps, ya que los archivos se emparejan con objetos de medios por su suma de verificación.

Ten en cuenta que esta función solo funciona para archivos que tienen la suma de verificación correcta en la base de datos de Gramps (lo cual debería asegurarse ejecutando la herramienta de verificación y reparación en el primer paso).

Al mover a Gramps Web desde un programa de genealogía diferente que incluya archivos de medios, se recomienda primero importar todo en Gramps Desktop, que tiene más opciones para asociar archivos de medios existentes con un árbol importado.
