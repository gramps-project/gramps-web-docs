# Importar archivos multimedia

Si has [importado un árbol genealógico](import.md) y necesitas subir los archivos multimedia correspondientes, utiliza **Importar archivos multimedia** en la sección de Datos de la [configuración de administración](settings.md). Se espera un archivo ZIP que contenga los archivos multimedia faltantes. Los archivos se emparejan con los objetos multimedia en tu árbol de una de dos maneras:

- **Por suma de verificación.** Para los objetos multimedia que tienen una suma de verificación – como es el caso de los árboles importados desde Gramps Desktop – se utiliza el archivo con la suma de verificación coincidente, independientemente de su nombre o la estructura de carpetas en el archivo ZIP. Esto solo funciona si las sumas de verificación en la base de datos de Gramps son correctas, lo cual asegura ejecutar la herramienta de verificación y reparación.
- **Por ruta.** Los objetos multimedia sin una suma de verificación – como es típico después de una importación GEDCOM – se emparejan por su ruta: el archivo ZIP debe contener el archivo bajo exactamente la ruta relativa almacenada en el objeto multimedia.

Si las rutas almacenadas en tu archivo GEDCOM son absolutas (por ejemplo `C:\Users\...\photo.jpg`), el emparejamiento por ruta no funcionará. En este caso, se recomienda primero importar todo en Gramps Desktop, que tiene más opciones para asociar archivos multimedia existentes con un árbol importado, y luego pasar a Gramps Web como se describe en [Proveniente de Gramps Desktop](import.md#coming-from-gramps-desktop).

## Estado del archivo multimedia

La sección de **Datos** de la [configuración de administración](settings.md) muestra:

- El número total de objetos multimedia en el árbol y si alguno carece de una suma de verificación
- El número de objetos multimedia cuyo archivo asociado falta en el servidor

Una marca de verificación verde indica que todo está en orden. Si se detectan problemas, se muestran enlaces a los objetos afectados. Las sumas de verificación faltantes ocurren típicamente cuando se importaron datos de un formato como GEDCOM que incluye referencias multimedia pero no los archivos reales. Los archivos faltantes pueden ser subidos como se describe arriba.
