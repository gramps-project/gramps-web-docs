# Configuración del desarrollo backend

Esta página enumera los pasos necesarios para comenzar a desarrollar [Gramps Web API](https://github.com/gramps-project/gramps-web-api/), el backend (componente del servidor) de Gramps Web.


## Requisitos previos

La configuración de desarrollo recomendada utiliza Visual Studio Code con devcontainers. Este enfoque creará un entorno de desarrollo preconfigurado con todas las herramientas que necesitas. Para comenzar, necesitarás los siguientes ingredientes:

- [Docker](https://docs.docker.com/get-docker/)
- [Visual Studio Code](https://code.visualstudio.com/) con la [extensión Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) instalada
- [Git](https://git-scm.com)

Puedes usar Linux, macOS o Windows como tu sistema operativo.


## Comenzando

1. Abre el [repositorio de Gramps Web API](https://github.com/gramps-project/gramps-web-api) y haz clic en "fork"
2. Clona tu repositorio bifurcado en tu máquina local usando Git
3. Abre el repositorio clonado en Visual Studio Code. Cuando se te pida, selecciona "Reabrir en Contenedor" o abre manualmente la paleta de comandos (Ctrl+Shift+P o Cmd+Shift+P) y selecciona "Dev Containers: Rebuild and Reopen in Container".
4. Espera a que el contenedor de desarrollo se construya y se inicie. Esto puede tardar unos minutos, especialmente la primera vez.


## Tareas

Si solo estás modificando el código del backend, no necesitas necesariamente iniciar un servidor web: las pruebas unitarias utilizan un cliente de prueba de Flask que permite simular solicitudes a la API sin necesidad de un servidor en funcionamiento.

Sin embargo, ejecutar un servidor es útil si

- quieres probar tus cambios con solicitudes HTTP reales (ver [consultas manuales](queries.md)), 
- quieres previsualizar el impacto de los cambios en toda la aplicación Gramps Web, o
- también quieres hacer cambios simultáneos en el frontend (ver [configuración de desarrollo del frontend](../frontend/setup.md)).

Ejecutar el servidor se simplifica en el contenedor de desarrollo mediante tareas predefinidas. Puedes ejecutar estas tareas desde la paleta de comandos (Ctrl+Shift+P o Cmd+Shift+P) seleccionando "Tasks: Run Task" y luego eligiendo una de las siguientes:
- "Serve Web API" - inicia el servidor de desarrollo de Flask en el puerto 5555 con el registro de depuración habilitado
- "Start Celery worker" - inicia un trabajador de Celery para procesar tareas en segundo plano.


## Depuración

La depuración puede ser a veces un desafío, especialmente al intentar rastrear comportamientos complejos o identificar problemas sutiles. Para facilitar esto, puedes depurar tanto una instancia de API en ejecución como casos de prueba individuales directamente dentro de Visual Studio Code.

### Depurando la Gramps Web API

Para depurar la API en ejecución:

1. Abre Visual Studio Code y ve a la vista **Ejecutar y Depurar**.  
2. Selecciona la configuración **"Web API"** del menú desplegable.  
3. Comienza la depuración.  
4. Cuando envíes solicitudes al backend (ya sea manualmente o a través de la GUI de Gramps Web), la ejecución se pausará en cualquier punto de interrupción que hayas establecido en el código.  
   Esto te permite inspeccionar variables, el flujo de control y otros detalles en tiempo de ejecución.

### Depurando Casos de Prueba

Para depurar un caso de prueba específico:

1. Abre el archivo de prueba que deseas depurar (por ejemplo, `test_people.py`).  
2. En Visual Studio Code, abre la vista **Ejecutar y Depurar**.  
3. Elige la configuración **"Archivo de Prueba Actual"**.  
4. Comienza la depuración: la ejecución se detendrá en cualquier punto de interrupción establecido dentro de ese archivo de prueba.  

Esta configuración te permite avanzar a través de la lógica de prueba, examinar los valores de las variables y comprender mejor las fallas de las pruebas o los resultados inesperados.
