# Comprobar y verificar datos

La sección de **Procesamiento del Árbol Genealógico** en la [configuración de administración](settings.md) contiene dos herramientas que verifican el árbol genealógico: una para problemas técnicos en la base de datos y otra para datos implausibles.

## Comprobar y Reparar Base de Datos

Esta herramienta verifica la base de datos de Gramps en busca de inconsistencias internas y repara las que puede – análoga a la herramienta [Comprobar y Reparar Base de Datos](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) en Gramps Desktop.

Haz clic en **Comprobar y Reparar** y espera a que el indicador de progreso se complete. El resultado se muestra debajo del botón:

- Si no se encontraron errores, se muestra un mensaje de confirmación.
- Si se encontraron errores, se muestra un resumen de las reparaciones aplicadas.

Ejecuta esta herramienta si encuentras errores o comportamientos inesperados que puedan ser causados por inconsistencias en la base de datos, como relaciones faltantes entre objetos.

## Verificar los Datos

Mientras que [Comprobar y Reparar Base de Datos](#check-and-repair-database) busca inconsistencias *técnicas*, esta herramienta busca datos *implausibles* – análoga a la herramienta [Verificar los Datos](https://gramps-project.org/wiki/index.php/Gramps_5.0_Wiki_Manual_-_Tools#Verify_the_Data) en Gramps Desktop. Informa sobre cosas que no son imposibles, pero que son lo suficientemente improbables como para merecer una segunda revisión, como una madre de 12 años o una persona que vivió hasta los 130.

Bajo **Opciones** puedes ajustar los umbrales que utilizan las pruebas – edad máxima, edad mínima y máxima para casarse o tener hijos, número máximo de hijos, y así sucesivamente – así como si estimar fechas faltantes o inexactas y si informar fechas inválidas como el 31 de febrero. Las opciones que cambias se recuerdan en tu navegador para la próxima ejecución; **Restablecer** restaura los valores predeterminados.

Haz clic en **Verificar los Datos** para comenzar. La verificación se ejecuta como una tarea en segundo plano, y los hallazgos se enumeran luego bajo **Resultados de Verificación de Datos**. Esta herramienta no cambia nada: solo informa lo que encuentra.

!!! nota
    Un hallazgo no es prueba de un error. Vidas largas y grandes diferencias de edad ocurren, así que trata los resultados como una lista de cosas a verificar en lugar de una lista de cosas a reparar.
