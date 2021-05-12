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

ROS es un software d eprogramación de robots que es compatible con la mayoría de los robots que se encuentran en el mercado. Esto es una ventaja en un mundo en el que cada marca tiene su propio lenguaje de programación y permite no ser experto en cada uno de ellos para poder trabajar con varias marcas.

Se van a analizar y programar diferentes ejercicios de situaciones típicas que se encuentran en la industria. Sin embargo, previamente se han tenido que preparar y tener en cuenta las diferentes fases que se analizarán a continuación para poder realizar los ejercicios:

Primeramente se ha instalado el simulador de UR Gazebo a traves del paquete de ROS *sudo apt-get install ros-kinetic-universal-robot.* A la hora de hacer los ejercicios, se lanza este simulador así como el planificador MoveIt! (es en un conjunto de paquetes); el cual sirve para planificar y ejecutar trayectorias en espacio cartesiano. Para la comunicación entre ROS y MoveIt que se llevará a cabo mediante lenguaje Python, es necesario tener instalado el paquete *moveit_commander* porque ofrece una interfaz de Python. El siguiente paso a seguir es generar un nuevo paquete para obtener el script, *rospy*.

Como planificador de trayectorias también se puede utilizar el visualizador RViz. Para interaccionar con MoveIt! Además de lanzar el visualizador es necesario lanzar también el plugin. En RViz podemos ver que las trayectorias pueden generar colisiones. Esto es debido a que la escena del RViz tiene suelo y la de MoveIt! no. Esto hace que haya que modificar la escena. Para ello es necesario modificar el URDF (formato de lenguaje) para añadir una mesa. Se modifica la última parte *world_joint*. Para realizar los ejercicios de pick&place, es necesario añadir una segunda mesa para simular coger objetos y depositarlos.

Los movimientos del ejercicio se programan en un nodo de ROS. Un nodo es la unidad ejecutable de ROS, comunica los dos entre sí. La comunicación se da atraves de dos nodos, el *Publisher* y el *Subscriber*. Y los buses en los cuales los nodos intercambian mensajes son *Topics*. Siempre tiene que estar lanzado el Máster (*roscore*).

Una vez se ha tenido esto en cuenta, es posible comenzar con los ejercicios.

### Ejercicio 1

El ejercicio a programar consiste en la aplicación roboticá común de PICK&PLACE, en el que un robot coje un objeto de un punto fijo y lo deposita en otro.
Se dispone de dos mesas para comenzar con los ejercicios. Es necesario definir una posición segura en espacio de joints: 
 *Safe Point:[-pi/4, -pi/2, 0,-3*pi/4, pi/2, 0]

El ciclo pick&place que se propone es el siguiente: 
1. El robot vaya a la posición XYZ [500, 0, 250] RxRyRz [0, 180, 0], baje 250mm hasta quedarse en Z=0, espere 1 segundo y vuelva a subir a la posición previa.
2. El robot vaya a la posición XYZ [500, 250, 250] RxRyRz [0, 180, 0], baje 250mm hasta quedarse en Z=0, espere 1 segundo y vuelva a subir a la posición previa.
3. El robot vuelva a la posición segura.

### Ejercicio 2

### Ejercicio 3


