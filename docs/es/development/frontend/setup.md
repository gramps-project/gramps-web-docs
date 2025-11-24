# Configuración del desarrollo frontend

Esta página describe los pasos necesarios para comenzar con el desarrollo frontend.

## Requisitos previos

La configuración de desarrollo recomendada utiliza Visual Studio Code con devcontainers. Este enfoque creará un entorno de desarrollo preconfigurado con todas las herramientas que necesitas.

Consulta [Configuración del desarrollo backend](../backend/setup.md#prerequisites) para los requisitos previos necesarios.

## Empezando

1. Abre el [repositorio frontend de Gramps Web](https://github.com/gramps-project/gramps-web) y haz clic en "fork"
2. Clona tu repositorio bifurcado en tu máquina local usando Git
3. Abre el repositorio clonado en Visual Studio Code. Cuando se te solicite, selecciona "Reabrir en Contenedor" o abre manualmente la paleta de comandos (Ctrl+Shift+P o Cmd+Shift+P) y selecciona "Dev Containers: Rebuild and Reopen in Container".
4. Espera a que el contenedor de desarrollo se construya y se inicie. Esto puede tardar unos minutos, especialmente la primera vez.

## Ejecutando el servidor de desarrollo frontend

Para ejecutar el servidor de desarrollo frontend y previsualizar el impacto de tus cambios en el navegador, puedes usar las tareas predefinidas en el contenedor de desarrollo.

Para que esto funcione, primero necesitas iniciar una instancia del [backend de la API de Gramps Web](../backend/setup.md#tasks). La forma más fácil de hacer esto es usar el contenedor de desarrollo backend y [ejecutar la tarea "Serve Web API"](../backend/setup.md#tasks) en una ventana separada de VS Code.

Una vez que el backend esté en funcionamiento, puedes ejecutar el servidor de desarrollo frontend seleccionando "Tasks: Run Task" desde la paleta de comandos (Ctrl+Shift+P o Cmd+Shift+P) y luego eligiendo "Serve Gramps Web frontend".

Esto iniciará el servidor de desarrollo frontend en el puerto 8001, al que puedes acceder en tu navegador en `http://localhost:8001`. El navegador se recargará automáticamente cuando realices cambios en el código frontend, lo que te permitirá ver el impacto de tus cambios de inmediato.
