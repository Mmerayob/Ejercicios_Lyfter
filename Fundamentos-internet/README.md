# Fundamentos de Internet 

## 1. Del Cliente al Servidor

Cuando se escribe www.youtube.com en el navegador y se presiona Enter, se lleva a cabo un proceso paso a paso basado en el modelo de cliente-servidor.

Qué hace el cliente (navegador): El navegador web actúa como el cliente, encargado de solicitar la información requerida. Al ingresar la URL, el navegador procesa el nombre de dominio para iniciar la solicitud.

Qué papel cumple el DNS: La computadora realiza una consulta a un servidor DNS (Domain Name System). Este servidor DNS se encarga de buscar y traducir el nombre de dominio www.youtube.com a una dirección IP pública.

Qué ocurre con la dirección IP: Una vez que el servidor DNS localiza y retorna la dirección IP pública real del servidor, el navegador obtiene la ubicación numérica exacta a la cual debe conectarse.

El establecimiento de la conexión (TCP y TLS): Antes de enviar la información, ocurren dos pasos de red fundamentales: primero, el navegador realiza un Handshake TCP para abrir un canal de comunicación confiable y ordenado con el servidor; y segundo, debido a que se utiliza HTTPS, se ejecuta un Handshake TLS para negociar y establecer un canal cifrado y seguro en ambos extremos que proteja los datos en tránsito.

Cómo entra en juego el protocolo HTTP/HTTPS: La transferencia de datos se rige mediante el protocolo HTTP o su variante segura HTTPS, la cual encripta la información en ambos extremos para brindar mayor seguridad. El navegador emite un HTTP request haciendo uso de métodos como GET para obtener los recursos de la página.

Qué hace el servidor: El servidor, que consiste en una computadora con hardware especializado cuyo único propósito es responder a las solicitudes de los clientes, recibe la petición HTTP a través de la dirección IP. El servidor procesa dicha solicitud y devuelve un HTTP response que contiene los archivos necesarios y el código de estado correspondiente (como el 200 de éxito). Cabe destacar que el video no llega en una sola respuesta; las páginas web modernas realizan un promedio de más de 70 solicitudes independientes de forma asíncrona para cargar los componentes visuales, scripts y fragmentos de video multimedia necesarios para que este aparezca y se reproduzca en la pantalla.  


## 2. Frontend y Backend en acción

En una app web para agendar citas médicas el frontend correspondería a toda la parte del desarrollo web que abarca todo lo que el usuario ve y con lo que interactúa directamente en su navegador. Las tecnologías usadas en el frontend son Javascript, CSS y HTML.
Javascript: Es el lenguaje de programación encargado de definir cómo funcionan las interacciones del usuario de la página.
HTML: Es un lenguaje de etiquetas encargado de definir la estructura de la página.
CSS: Es un lenguaje de estilo encargado de definir el estilo visual de la página.

Por otra parte el Backend corresponde al servidor web y a la lógica de negocio (todo lo que no se ve directamente, encargado de procesar la disponibilidad de los médicos, validar credenciales, y gestionar la base de datos con la información de los pacientes y las citas). Tres tecnologías usadas en el backend podrían ser Node.js con Express, Python con Django o FastAPI y Java con Spring Boot.

La comunicación entre el frontend y el backend se lleva a cabo mediante los siguientes conceptos clave:
API (Application Programming Interface): Funciona como el puente de comunicación digital. El frontend utiliza APIs web para solicitar o modificar información sin intervención humana directa.   
HTTP / HTTPS: Es el protocolo de transferencia estándar de internet que regula cómo viajan los mensajes. Cuando un paciente presiona el botón de "Agendar cita", el navegador cifra y envía la orden mediante este protocolo.   
Request / Response (Solicitud y Respuesta):El frontend envía un request HTTP al servidor, especificando un método (como POST para crear una nueva cita o GET para consultar horarios) junto con los datos necesarios en formato JSON dentro del cuerpo (body). El backend procesa la solicitud consultando la base de datos y devuelve un response HTTP que incluye un código de estado (por ejemplo, un 200 de éxito o un 400 de error) y la información solicitada para que el frontend la refleje en la pantalla.   


## 3. REST vs SOAP vs GraphQL

| Tipo de API | Formato de datos usado             | Nivel de Flexibilidad | Dificultad de implementación | Uso actual (Alta / Media / Baja) |
|-------------|------------------------------------|------------------------|-------------------------------|------------------------------- |
| REST        |      JSON (u otros formatos)       |         Media          |              Baja             |               Alta             |
| SOAP        |              XML                   |         Baja           |              Alta             |               Baja             |
| GraphQL     |JSON (lenguaje de consultas propio) |         Alta           |              Media            |               Media            |

**¿Cuál es más apropiada para una startup moderna? ¿Por qué?**

REST es la más apropiada para iniciar debido a su madurez como estándar de la industria, a menos que las necesidades específicas de la plataforma de reservas exijan la selección precisa de datos que ofrece GraphQL.
Algunas de las ventajas que proporciona REST son las siguientes:
- Al ser el estándar indiscutible de la industria, la curva de aprendizaje es mínima.
- Cuenta con una integración nativa y probada con herramientas de documentación (como Swagger/OpenAPI) y pruebas (como Postman), lo que simplifica la colaboración diaria entre los equipos de frontend y backend.
- En un sistema de reservas, las consultas para verificar disponibilidad (por ejemplo, GET /disponibilidad o la lista de servicios/horarios) son altamente repetitivas por parte de múltiples usuarios. REST permite aprovechar de forma directa el almacenamiento en caché estándar de HTTP (mediante navegadores, proxies o CDNs), lo que optimiza el rendimiento de la plataforma y reduce drásticamente la carga sobre la base de datos.

## 4. Explorando APIs con Postman
 
### 4.1 Selección de la API
- **Nombre de la API:** JSONPlaceholder [https://jsonplaceholder.typicode.com/]
- **Descripción:** Esta es una REST API pública y gratuita, que esta diseñanada para ser usada cuando se ocupen datos de ejemplo para crear tutoriales, ejemplos de código, aprendizaje o pruebas.

### 4.2 Configuración en Postman
- **Nombre de la colección:** JSONPlaceholder
- **Solicitudes agregadas:**
  - GET - users
  - POST - new user 
  - DELETE - delete user

### 4.3 Ejecución y análisis

|      Solicitud      | Método |      Endpoint       | Código de estado |                            Notas                                 |
|---------------------|--------|----------------------------------------|------------------------------------------------------------------|
| GET - users         |  GET   |{{base_url}}/users   |      200 OK      |Devuelve la lista de usuarios. Headers: content-type confirma formato JSON y cache-control (max-age=43200) junto con etag indican política de caché y validación de versiones.|

| POST - new user     |  POST  |{{base_url}}/users   |   201 Created    |Crea un nuevo usuario. Headers: location indica la URL exacta del recurso creado y content-type especifica la respuesta en JSON.|

|DELETE - delete user | DELETE |{{base_url}}/users/1 |      200 OK      |Elimina el usuario según el id. Headers: content-type confirma respuesta JSON vacía y etag gestiona el estado del recurso simulado.|

### 4.4 Explicación técnica

JSONPlaceholder es una API de tipo RESTful (Representational State Transfer) diseñada para actuar como un servidor mock (simulado) para pruebas de desarrollo, prototipos y aprendizaje. Además, funciona sobre HTTPS, lo que garantiza que las solicitudes y respuestas viajen cifradas. Tanto las solicitudes que aceptan datos como las respuestas devueltas por el servidor utilizan estrictamente el formato JSON.

La API permite ejecutar el ciclo de operaciones CRUD completas utilizando los métodos HTTP estándar: GET para consultar, POST para simular la creación, PUT y PATCH para actualizar, y DELETE para eliminar datos de prueba. Estas operaciones se ejecutan sin persistencia real en la base de datos subyacente, devolviendo respuestas simuladas realistas con sus respectivos códigos de estado HTTP.

Asimismo, los datos dentro de la API se organizan a través de rutas y recursos comunes en el desarrollo web, tales como publicaciones (/posts), comentarios (/comments), álbumes (/albums), fotos (/photos), tareas (/todos) y usuarios (/users).

#### GET users
- **Método HTTP:** GET
- **Endpoint:** {{base_url}}/users
- **Parámetros / body:** Ninguno, esta es una petición de solo lectura.
- **Descripción de la respuesta:** Retorna un arreglo en formato JSON con la lista completa de los 10 usuarios simulados del sistema, incluyendo sus datos personales.

#### POST new user
- **Método HTTP:** POST
- **Endpoint:** {{base_url}}/users
- **Parámetros / body:** Requiere un cuerpo en formato JSON (raw) que incluye un objeto con los datos del nuevo usuario a registrar (id, name, username, email, address, phone, website y company)
- **Descripción de la respuesta:** Devuelve un código de estado 201 Created junto con un objeto JSON que replica los datos enviados del usuario recién creado, asignándole de forma simulada su identificador (id: 11) y la ruta de ubicación en la cabecera Location.

#### DELETE delete user 
- **Método HTTP:** DELETE
- **Endpoint:** {{base_url}}/users/1
- **Parámetros / body:** Utiliza un parámetro de ruta (/1) para especificar el identificador único del usuario que se desea eliminar, pero no requiere ningún body.
- **Descripción de la respuesta:** Retorna un código de estado 200 OK junto con un objeto JSON vacío ({}), simulando de forma exitosa la eliminación del recurso en el servidor.

**Ejemplo de código o fragmento JSON con la respuesta**

```json
{
    "id": 11,
    "name": "Manfred Merayo",
    "username": "Mmerayo",
    "email": "Mmerayo@gmail.com",
    "address": {
        "street": "Example road",
        "suite": "Apt. 556",
        "city": "Cartago",
        "zipcode": "30501",
        "geo": {
            "lat": "-37.3159",
            "lng": "81.1496"
        }
    },
    "phone": "8830-6745",
    "website": "example.org",
    "company": {
        "name": "Lyfter",
        "catchPhrase": "Multi-layered client-server neural-net",
        "bs": "harness real-time e-markets"
    }
} 
```

**¿Qué aprendiste del proceso?**

A través de esta práctica comprendí de forma aplicada cómo interactúan un cliente como Postman y un servidor web a través de peticiones y respuestas HTTP. Aprendí la importancia de estructurar correctamente las solicitudes utilizando una URL base mediante variables de entorno.


### 4.5 Reflexión final

Aprendí que una API es un medio de comunicación esencial que permite a dos aplicaciones distintas interactuar utilizando protocolos de internet, siendo HTTP el más común. Comprendí que las APIs web (como REST, que es el estándar de la industria) se apoyan en las características base de HTTP para que el cliente y el servidor intercambien datos estructurados, habitualmente en formato JSON.   
Por otro lado, Postman me ayudó a comprender de forma práctica la comunicación entre cliente y servidor al permitirme consumir y probar APIs de manera sencilla. Mediante esta herramienta pude construir y enviar peticiones personalizadas y probar distintos métodos sin la necesidad de desarrollar una interfaz completa