# Fundamentos de Internet 

## 1. Del Cliente al Servidor

Cuando se escribe www.youtube.com en el navegador y se presiona Enter, se lleva a cabo un proceso paso a paso basado en el modelo de cliente-servidor.

Qué hace el cliente (navegador): El navegador web actúa como el cliente, encargado de solicitar la información requerida. Al ingresar la URL, el navegador procesa el nombre de dominio para iniciar la solicitud.

Qué papel cumple el DNS: La computadora realiza una consulta a un servidor DNS (Domain Name System). Este servidor DNS se encarga de buscar y traducir el nombre de dominio www.youtube.com a una dirección IP pública.

Qué ocurre con la dirección IP: Una vez que el servidor DNS localiza y retorna la dirección IP pública real del servidor, el navegador obtiene la ubicación numérica exacta a la cual debe conectarse.

Cómo entra en juego el protocolo HTTP/HTTPS: La transferencia de datos se rige mediante el protocolo HTTP o su variante segura HTTPS, la cual encripta la información en ambos extremos para brindar mayor seguridad. El navegador emite un HTTP request haciendo uso de métodos como GET para obtener los recursos de la página.

Qué hace el servidor: El servidor, que consiste en una computadora con hardware especializado cuyo único propósito es responder a las solicitudes de los clientes, recibe la petición HTTP a través de la dirección IP. El servidor procesa dicha solicitud y devuelve un HTTP response que contiene los archivos necesarios, los contenidos web y el código de estado correspondiente (como el 200 de éxito), permitiendo que el navegador muestre el video en la pantalla.  


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

| Tipo de API | Formato de datos usado | Nivel de Flexibilidad | Dificultad de implementación | Uso actual (Alta / Media / Baja) |
|-------------|------------------------|------------------------|-------------------------------|-----------------------------------|
| REST        |         JSON           |         Media          |              Baja             |               Alto                |
| SOAP        |         XML            |         Baja           |              Alta             |               Baja                |
| GraphQL     |         JSON           |         Alta           |              Media            |               Media               |

**¿Cuál es más apropiada para una startup moderna? ¿Por qué?**

REST es la más apropiada para iniciar debido a su madurez como estándar de la industria, a menos que las necesidades específicas de la plataforma de reservas exijan la selección precisa de datos que ofrece GraphQL.

## 4. Explorando APIs con Postman
 
### 4.1 Selección de la API
- **Nombre de la API:** https://www.chess.com/news/view/published-data-api 
- **Descripción:** Esta API almacena la información de los jugadores de Chess.com como su nombre, estadísticas de partidas y sobre torneos.

### 4.2 Configuración en Postman
- **Nombre de la colección:** Chess.com
- **Solicitudes agregadas:**
  - GET Player data
  - GET Player stats
  - GET List of tournaments participated by player

### 4.3 Ejecución y análisis

|      Solicitud        | Método |               Endpoint               | Código de estado |                      Notas                      |
|-----------------------|--------|--------------------------------------|------------------|-------------------------------------------------|
| GET Player data       |   GET  |{{base_url}}/player/hikaru            |      200 OK      |Devuelve la información del perfil del jugador   |
| GET Player stats      |   GET  |{{base_url}}/player/hikaru/stats      |      200 OK      |Muestra las estadísticas detalladas y de juego   |
|GET List of tournaments|   GET  |{{base_url}}/player/hikaru/tournaments|      200 OK      |Retorna el listado de torneos jugados por jugador|

### 4.4 Explicación técnica

Esta es una REST API que devuelve respuestas con el formato JSON-LD, en esta se almacena la información de los jugadores de Chess.com como su nombre, estadísticas de partidas y sobre torneos.

#### GET Player data
- **Método HTTP:** GET
- **Endpoint:** {{base_url}}/player/hikaru (utilizando una variable de entorno para la raíz https://api.chess.com/pub)
- **Parámetros / body:** No requiere cuerpo (body). Utiliza un parámetro de ruta (path parameter) para especificar el nombre de usuario.
- **Descripción de la respuesta:** Retorna un objeto JSON con los datos generales del perfil público del jugador (como su ID, avatar, nombre, ubicación y estatus de cuenta).

#### GET Player stats
- **Método HTTP:** GET
- **Endpoint:** {{base_url}}/player/hikaru/stats
- **Parámetros / body:** Ninguno en el cuerpo, incluye el nombre del usuario en la ruta.
- **Descripción de la respuesta:** Devuelve un JSON estructurado con las estadísticas detalladas de juego.

#### GET List of tournaments participated by player
- **Método HTTP:** GET
- **Endpoint:** {{base_url}}/player/hikaru/tournaments
- **Parámetros / body:** Ninguno.
- **Descripción de la respuesta:** Entrega una respuesta en formato JSON con el listado de los torneos en los que el usuario ha participado, clasificados por su estado actual.

**Ejemplo de código o fragmento JSON con la respuesta**

{
    "player_id": 1694236,
    "url": "https://www.chess.com/member/hikaru",
    "username": "hikaru",
    "title": "GM",
    "followers": 1452300,
    "country": "https://api.chess.com/pub/country/US",
    "status": "premium"
}


**¿Qué aprendiste del proceso?**

A través de esta práctica comprendí de forma aplicada cómo interactúan un cliente como Postman y un servidor web a través de peticiones y respuestas HTTP. Aprendí la importancia de estructurar correctamente las solicitudes utilizando una URL base mediante variables de entorno.


### 4.5 Reflexión final

Aprendí que una API es un medio de comunicación esencial que permite a dos aplicaciones distintas interactuar utilizando protocolos de internet, siendo HTTP el más común. Comprendí que las APIs web (como REST, que es el estándar de la industria) se apoyan en las características base de HTTP para que el cliente y el servidor intercambien datos estructurados, habitualmente en formato JSON.   
Por otro lado, Postman me ayudó a comprender de forma práctica la comunicación entre cliente y servidor al permitirme consumir y probar APIs de manera sencilla. Mediante esta herramienta pude construir y enviar peticiones personalizadas y probar distintos métodos sin la necesidad de desarrollar una interfaz completa