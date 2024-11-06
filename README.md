# EFI Flask - Backend:

Este repositorio contiene únicamente la parte backend del proyecto. Para poder ver y utilizar todas las funciones del proyecto, 
también necesitarás configurar la versión frontend, disponible en nuestro segundo repositorio.

A continuación, detallamos el proceso de instalación y el uso correcto de la API.

* Clonación del Repositorio
  1. Abre la terminal y crea un nuevo directorio con el siguiente comando: mkdir <nombre_del_directorio> 
  2. Ingresa al directorio recién creado: cd <nombre_del_directorio>
  3. Clona el repositorio con: git clone git@github.com:tom1mvp/EFI_Backend.git

* Creación de Entorno Virtual e Instalación de Dependencias
  1. Crea un entorno virtual para el proyecto Flask: python3 -m venv <nombre_del_entorno>
  2. Activa el entorno virtual: source <nombre_del_entorno>/bin/activate
  3. Instala las dependencias del archivo requirements.txt: pip install -r requirements.txt

* Configuración de la Base de Datos
  1. Encender los servicios de xampp
  2. Abre http://localhost en tu navegador.
  3. Crea una base de datos llamada db_sportia.
 
# Uso de la API
Con el repositorio clonado y el servidor activado, la API estará lista para recibir solicitudes.  A continuación se describen algunos de los endpoints y métodos disponibles:

* Crear un Usuario
  * Método: POST
  * Endpoint: /api/users
  * Cabecera de la solicitud: Authorization: Token <tu_token_de_autenticacion>
  * Cuerpo de la solicitud:
      {
  "Username": "nombre_de_usuario",
  "Password_hash": "password_hasheada"
}

* Eliminar un Usuario
    * Método: DELETE
    * Endpoint: /api/users/<id_usuario>
    * Cabecera de la solicitud: Authorization: Token <tu_token_de_autenticacion>
    * Respuesta: Código de estado 200, indicando que el usuario fue eliminado con éxito.

* Actualizar un Usuario
    * Método: PUT
    * Endpoint: /api/users/<id_usuario>
    * Cabecera de la solicitud: Authorization: Token <tu_token_de_autenticacion>
    * Cuerpo de la solicitud:
      {
      "Username": "Nuevo nombre"
      }
