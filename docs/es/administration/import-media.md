# Importar archivos multimedia

Si has [importado un árbol genealógico](import.md) y necesitas subir los archivos multimedia correspondientes, utiliza **Importar archivos multimedia** en la [página de importación](import.md), debajo de la importación del árbol genealógico. Se espera un archivo ZIP que contenga los archivos multimedia que faltan. La carga solo es posible una vez que el árbol contiene objetos multimedia, ya que los archivos se emparejan con objetos multimedia existentes; un archivo de árbol genealógico solo hace referencia a sus archivos multimedia, así que impórtalo primero.

Los archivos se emparejan con los objetos multimedia en tu árbol de una de dos maneras:

- **Por suma de verificación.** Para los objetos multimedia que tienen una suma de verificación – como es el caso de los árboles importados desde Gramps Desktop – se utiliza el archivo con la suma de verificación coincidente, independientemente de su nombre o la estructura de carpetas en el archivo ZIP. Esto solo funciona si las sumas de verificación en la base de datos de Gramps son correctas, lo cual asegura ejecutar la herramienta de verificación y reparación.
- **Por ruta o nombre de archivo.** Los objetos multimedia sin una suma de verificación – como es típico después de una importación GEDCOM – se emparejan por la ruta relativa almacenada en el objeto multimedia. Si ningún archivo en el ZIP tiene esa ruta, se emparejan solo por el nombre del archivo, ignorando mayúsculas y minúsculas (desde Gramps Web API 3.26). Esto también funciona para rutas absolutas de otros programas, como `C:\Users\...\Family\grandpa.jpg`, por lo que puedes simplemente poner todos los archivos en el archivo ZIP. Un nombre de archivo solo se utiliza si es único, tanto en el archivo ZIP como entre los objetos multimedia que aún no tienen un archivo.

Después de la carga, el resultado indica cuántos objetos multimedia encontraron un archivo, y lista aquellos para los cuales el archivo ZIP no tenía archivo, con su ID de Gramps y la ruta almacenada. Utiliza esta lista para encontrar los archivos que faltan, luego sube otro archivo ZIP solo con estos – los archivos que ya están en el servidor no se ven afectados.

Si varios objetos multimedia tienen el mismo nombre de archivo en diferentes carpetas, el emparejamiento por nombre de archivo no funciona para ellos. O recrea la estructura de carpetas a partir de las rutas almacenadas en el archivo ZIP, o importa todo en Gramps Desktop primero, que tiene más opciones para asociar archivos multimedia existentes con un árbol importado, y luego muévete a Gramps Web como se describe en [Procedente de Gramps Desktop](import.md#coming-from-gramps-desktop).

## Estado del archivo multimedia

La sección **Datos** de la [configuración de administración](settings.md) muestra:

- El número total de objetos multimedia en el árbol y si alguno carece de una suma de verificación
- El número de objetos multimedia cuyo archivo asociado falta en el servidor

Una marca de verificación verde indica que todo está en orden. Si se detectan problemas, se muestran enlaces a los objetos afectados. Las sumas de verificación faltantes ocurren típicamente cuando los datos se importaron desde un formato como GEDCOM que incluye referencias multimedia pero no los archivos reales. Los archivos que faltan se pueden subir como se describió anteriormente.
