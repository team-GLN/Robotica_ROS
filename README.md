# Proyecto Final del curso de Robotica Industrial Aplicada
## ROS
*Master Universitario en Digital Manufacturing*

Desarrollado por:
* Nekane Berasategui
* Goiatz Ezpeleta
* Laura Zambrano

### Contenido
### Introducción

El ejercicio a programar consiste en la aplicación roboticá común de PICK&PLACE. Sin embargo, previamente se han tenido que preparar y tener en cuenta las diferentes fases para poder realizar los ejercicios:

Primeramente se ha instalado el simulador de UR Gazebo a traves del paquete de ROS *sudo apt-get install ros-kinetic-universal-robot.* A la hora de hacer los ejercicios, se lanza este simulador así como el planificador MoveIt!; el cual sirve para planificar y ejecutar trayectorias. Consiste en un conjunto de paquetes. Para planificar trayectorias también se puede utilizar el visualizador RViz. Para interaccionar con MoveIt! Además de lanzar el visualizador es necesario lanzar también el plugin. En RViz podemos ver que las trayectorias pueden generar colisiones. Esto es debido a que la escena del RViz tiene suelo y la de MoveIt! no. Esto hace que haya que modificar la escena. Para ello es necesario modificar el URDF (formato de lenguaje) para añadir una mesa. Se modifica la última parte *world_joint*.


