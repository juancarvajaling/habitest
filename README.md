# Habi - Prueba Técnica
Se implementarán dos microservicios que Habi desea tener. El primero para que los usuarios externos puedan consultar los inmuebles disponibles almacenados en la base de datos. El segundo para que los usuarios puedan darle “Me gusta” a un inmueble en específico. Este último su impletación será solo conceptual.

## Consideraciones Técnicas
Estas consideraciones son iniciales. La implementación final podría diferir al encontrarse dificultades en este primer diseño.

### Bibliotecas
La bibliotecas más relevantes que se usarán en este proyecto son:
- [http](https://docs.python.org/3/library/http.html#module-http): se utilizará para crear el servidor HTTP y manejar las peticiones de los usuarios.
- [MySQL connector/python](https://dev.mysql.com/doc/connector-python/en/connector-python-introduction.html): se utilizará para manejar la conexión a la base de datos y la ejecución de los queries.
- [jsonchema](https://python-jsonschema.readthedocs.io/en/latest/): servirá para validar los parámetros de búsqueda de las peticiones y para validar la respuestas que el servidor va a retornar.

### Estructura del proyecto
Para implementar la solución, los siguientes módulos serán creados:
- **server**: tendrá la implementación del servidor, el manejo de las peticiones y el llamado a los métodos que atenderán las peticiones.
- **database**: implementará la conexión a la base de datos y la ejecución de los queries.
- **propertyfinder**: atenderá las peticiones para buscar una propiedad. 
