# Configuración para alojar múltiples árboles

Por defecto, Gramps Web solo permite acceder a una única base de datos de árbol familiar (“árbol”), especificada en el archivo de configuración.

Sin embargo, a partir de la versión 0.7.0 del backend de la API de Gramps Web, también es posible servir múltiples árboles desde una única instalación. Sin embargo, cada usuario está (actualmente) vinculado a un solo árbol, por lo que esta configuración no es adecuada para compartir árboles entre usuarios, sino para alojar múltiples instancias aisladas de Gramps Web.

## Habilitar soporte para múltiples árboles

Para habilitar el soporte para múltiples árboles, la opción de configuración `TREE` debe establecerse en un único asterisco `*`, por ejemplo, en un archivo de configuración:

```python
TREE = "*"
```

Esto hará que todos los árboles en el directorio de la base de datos de Gramps del servidor sean accesibles (dadas las suficientes permisos de usuario). El ID del árbol es el nombre del subdirectorio. Puedes listar los árboles existentes (nombres e IDs) con el comando

```bash
python -m gramps_webapi --config /app/config/config.cfg tree list
```

Además, debes establecer la opción de configuración `MEDIA_PREFIX_TREE` en `True` para asegurar que los archivos multimedia se almacenen en subcarpetas separadas. ¡De lo contrario, los usuarios podrán acceder a archivos multimedia que pertenecen a un árbol para el cual no tienen permiso!

## Agregar una cuenta de usuario a un árbol específico

Para agregar un usuario a un árbol específico, simplemente añade la opción de línea de comandos `--tree TREEID` al comando de agregar usuario. También puedes hacer un POST al endpoint `/users/` con la propiedad `tree` establecida en la carga útil JSON.

Los nombres de usuario y las direcciones de correo electrónico deben ser únicos en *todos* los árboles.

## Crear un nuevo árbol

Para crear un nuevo árbol, se recomienda hacer un POST al endpoint `/trees/` en lugar de usar la CLI de Gramps. Esto utilizará un UUIDv4 como ID de árbol, lo que proporciona una seguridad adicional ya que el nombre no puede ser adivinado. Actualmente, solo se admite SQLite para los árboles recién creados.

## Autorizar

Para autorizar (obtener un token), solo son necesarios el nombre de usuario y la contraseña, como en el modo de un solo árbol, ya que el ID del árbol es conocido para cada usuario, por lo que no es necesario proporcionarlo.

## Migrar archivos multimedia existentes

Si deseas migrar una instancia existente de Gramps Web a soporte para múltiples árboles y estás utilizando archivos multimedia locales, simplemente puedes moverlos a una subcarpeta de la ubicación original con el ID del árbol como nombre.

Si estás utilizando archivos multimedia alojados en S3, puedes usar el script proporcionado en el directorio `scripts` del repositorio `gramps-web-api`:

```bash
python scripts/s3_rename.py BUCKET_NAME TREE_ID
```

Esto asume que las claves de acceso relevantes ya están configuradas como variables de entorno.

## Migrar base de datos de usuarios existente

Si deseas habilitar el soporte para múltiples árboles y reutilizar usuarios existentes, necesitas asignarlos a un árbol específico. Puedes usar el siguiente comando proporcionado para este propósito,

```bash
python -m gramps_webapi --config /app/config/config.cfg user fill-tree TREE_ID
```

## Personalizar el frontend

La página de registro accesible desde la página de inicio de sesión no funciona en una configuración de múltiples árboles, ya que se necesita especificar un árbol para el registro. Por lo tanto, es recomendable establecer `hideRegisterLink` en `true` en la [configuración del frontend](frontend-config.md).
