# Proyecto Final del curso de Robotica Industrial Aplicada
## ROS
*Master Universitario en Digital Manufacturing*

Desarrollado por:
* Nekane Berasategui
* Laura Zambrano
* Goiatz Ezpeleta


### Contenido
- [Introducción](https://github.com/team-GLN/Robotica_ROS/blob/main/README.md#introducci%C3%B3n)
- [Ejercicio 1](https://github.com/team-GLN/Robotica_ROS/blob/main/README.md#ejercicio-1)
- [Ejercicio 2](https://github.com/team-GLN/Robotica_ROS/blob/UR/README.md#ejercicio-2)
- [Ejercicio 3](https://github.com/team-GLN/Robotica_ROS/blob/UR/README.md#ejercicio-3)

### Introducción

El ejercicio a programar consiste en la aplicación roboticá común de PICK&PLACE. Sin embargo, previamente se han tenido que preparar y tener en cuenta las diferentes fases para poder realizar los ejercicios:

Primeramente se ha instalado el simulador de UR Gazebo a traves del paquete de ROS *sudo apt-get install ros-kinetic-universal-robot.* A la hora de hacer los ejercicios, se lanza este simulador así como el planificador MoveIt!; el cual sirve para planificar y ejecutar trayectorias en espacio cartesiano. Consiste en un conjunto de paquetes. Para la comunicación entre ROS y MoveIt que se llevará a cabo mediante lenguaje Python, es necesario tener instalado el paquete *moveit_commander* porque ofrece una interfaz de Python. Es necesario crear un nuevo paquete para obtener el script, *rospy*.

Como planificador de trayectorias también se puede utilizar el visualizador RViz. Para interaccionar con MoveIt! Además de lanzar el visualizador es necesario lanzar también el plugin. En RViz podemos ver que las trayectorias pueden generar colisiones. Esto es debido a que la escena del RViz tiene suelo y la de MoveIt! no. Esto hace que haya que modificar la escena. Para ello es necesario modificar el URDF (formato de lenguaje) para añadir una mesa. Se modifica la última parte *world_joint*.

### Ejercicio 1

### Ejercicio 2

### Ejercicio 3


