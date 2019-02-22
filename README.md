# [TFM] Generador de historias servidor

Las historias tiene mucho más impacto si la relacionamos con elementos de la realidad. El uso de dispositivos móviles y de técnicas como la geolocalización o la realidad aumentada nos permiten ampliar una historia, relacionando parte de la misma con lugares y objetos existentes en la realidad. Este tipo de narrativas tiene un potencial importante en aplicaciones como son la educación o el turismo donde la información extra que obtienen los jugadores puede ser usada en los proceso de aprendizaje y también como fuerte motivador para visitar lugar de interés.

El objetivo del proyecto es desarrollar un sistema que permita diseñar historias interactivas que se integren en un juego con el que los jugadores puedan completar retos, buscar y coleccionar objetos, hablar con personajes virtuales y todo ello mientras exploran el mundo físico que esta a su alrededor.

El editor facilitará el diseño de las experiencias y generara ficheros de configuración que puedan ser usados en una aplicación móvil que permita coordinar y vivir las experiencias de juego previamente diseñadas.

## Rutas implementadas

### Rutas de usuario

- Ruta: /

- Ruta: /nueva_historia

- Ruta: /monitorizacion

- Ruta: /rutas

### Rutas GET auxiliares

- Ruta: /rest/status

- Ruta: /historia/<id>

- Ruta: /mision/<id>

- Ruta: /misiones_asociadas/<id_historia>

- Ruta: /rest/list/historia

- Ruta: /rest/list/mision

### Rutas POST

- Ruta: /rest/historia/<post_id>
