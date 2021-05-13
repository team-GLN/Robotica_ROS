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

ROS es un software de programación de robots que es compatible con la mayoría de los robots que se encuentran en el mercado. Esto es una ventaja en un mundo en el que cada marca tiene su propio lenguaje de programación y permite no ser experto en cada uno de ellos para poder trabajar con varias marcas.

Se van a analizar y programar diferentes ejercicios de situaciones típicas que se encuentran en la industria. Sin embargo, previamente se han tenido que preparar y tener en cuenta las diferentes fases que se analizarán a continuación para poder realizar los ejercicios:


### Ejercicio 1Primeramente se ha creado un nuevo workspace *ros*. A continuación se crea un paquete *src.

Es necesario instalar el simulador de UR Gazebo para hacer el cálculo de geometria a traves del paquete de ROS ```sudo apt-get install ros-kinetic-universal-robot```. A la hora de hacer los ejercicios, se lanza este simulador con ```roslaunch ur_gazebo ur5.launch``` así como el planificador MoveIt! (es en un conjunto de paquetes); el cual sirve para planificar y ejecutar trayectorias en espacio cartesiano con ```roslaunch ur5_moveit_config ur5_moveit_planning_execution.launch sim:=true```. Para la comunicación entre ROS y MoveIt que se llevará a cabo mediante lenguaje Python, es necesario tener instalado el paquete *moveit_commander* porque ofrece una interfaz de Python. El siguiente paso a seguir es generar un nuevo paquete para obtener el script, *rospy*.

Los movimientos del ejercicio se programan en un nodo de ROS. Un nodo es la unidad ejecutable de ROS, comunica los dos entre sí. La comunicación se da atraves de dos nodos, el *Publisher* (*talker*) y el *Subscriber* (*listener*). Y los buses en los cuales los nodos intercambian mensajes son *Topics*. Siempre tiene que estar lanzado el Máster (*roscore*).

Como planificador de trayectorias también se puede utilizar el visualizador de datos de Ros,RViz. Para interaccionar con MoveIt! Además de lanzar el visualizador es necesario lanzar también el plugin ```roslaunch ur5_moveit_config moveit_rviz.launch config:=true```. En RViz podemos ver que las trayectorias pueden generar colisiones. Esto es debido a que la escena del RViz tiene suelo y la de MoveIt! no. Esto hace que haya que modificar la escena. Para ello es necesario modificar el URDF (formato de lenguaje) para añadir una mesa. Se modifica la última parte *world_joint*. Para realizar los ejercicios de pick&place, es necesario añadir una segunda mesa para simular coger objetos y depositarlos.
Primeramente se ha creado un nuevo workspace *ros*. A continuación se crea un paquete *src.

Es necesario instalar el simulador de UR Gazebo para hacer el cálculo de geometria a traves del paquete de ROS ```sudo apt-get install ros-kinetic-universal-robot```. A la hora de hacer los ejercicios, se lanza este simulador con ```roslaunch ur_gazebo ur5.launch``` así como el planificador MoveIt! (es en un conjunto de paquetes); el cual sirve para planificar y ejecutar trayectorias en espacio cartesiano con ```roslaunch ur5_moveit_config ur5_moveit_planning_execution.launch sim:=true```. Para la comunicación entre ROS y MoveIt que se llevará a cabo mediante lenguaje Python, es necesario tener instalado el paquete *moveit_commander* porque ofrece una interfaz de Python. El siguiente paso a seguir es generar un nuevo paquete para obtener el script, *rospy*.

Los movimientos del ejercicio se programan en un nodo de ROS. Un nodo es la unidad ejecutable de ROS, comunica los dos entre sí. La comunicación se da atraves de dos nodos, el *Publisher* (*talker*) y el *Subscriber* (*listener*). Y los buses en los cuales los nodos intercambian mensajes son *Topics*. Siempre tiene que estar lanzado el Máster (*roscore*).

Como planificador de trayectorias también se puede utilizar el visualizador de datos de Ros,RViz. Para interaccionar con MoveIt! Además de lanzar el visualizador es necesario lanzar también el plugin ```roslaunch ur5_moveit_config moveit_rviz.launch config:=true```. En RViz podemos ver que las trayectorias pueden generar colisiones. Esto es debido a que la escena del RViz tiene suelo y la de MoveIt! no. Esto hace que haya que modificar la escena. Para ello es necesario modificar el URDF (formato de lenguaje) para añadir una mesa. Se modifica la última parte *world_joint*. Para realizar los ejercicios de pick&place, es necesario añadir una segunda mesa para simular coger objetos y depositarlos.

El ejercicio a programar consiste en la aplicación roboticá común de PICK&PLACE, en el que un robot coge un objeto de un punto fijo y lo deposita en otro.
Se dispone de dos mesas para comenzar con los ejercicios. Es necesario definir una posición segura en espacio de joints: [-45º, -90º, 0º -135º, 90º, 0º]
 
 *Safe Point* en equivalente en radianes:[-pi/4, -pi/2, 0,-3*pi/4, pi/2, 0]

El ciclo pick&place que se propone es el siguiente: 
1. Posición XYZ [500, 0, 250] RxRyRz [0, 180, 0], baje 250mm hasta quedarse en Z=0, espere 1 segundo y vuelva a subir a la posición previa.
2. Posición XYZ [500, 250, 250] RxRyRz [0, 180, 0], baje 250mm hasta quedarse en Z=0, espere 1 segundo y vuelva a subir a la posición previa.
3. El robot vuelva a la posición segura.

Las variables que definen estas posiciones son las siguientes:
```py
#Declaracion de posiciones globales
posPrePick = p[0.500, 0.000, 0.250, 0, pi, 0] #herramienta arriba en el punto de pick
posPick = p[0.500, 0.000, 0.000, 0, pi, 0] #herramienta abajo en el punto de pick
posPrePlace = p[0.500, 0.250, 0.250, 0, pi, 0]#herramienta arriba en el punto de place
posPlace = p[0.500, 0.250, 0.000, 0, pi, 0]#herramienta abajo en el punto de place
```

El robot se mueve a la posición segura mediante movej ...### hay que confirmar que sea como en el UR...


### Ejercicio 2

En este ejercicio se va a simular que el robot coge una pieza de una posición y la deja en otra posición del grid. 

Pose de inicio:

Tamaño de la rejilla:
* filas: 2
* columnas: 3

Distancia horizontal de la rejilla: 0.01

Distancia vertical de la rejilla: 0.01

Antes del desbarbado, el robot debera ir a una posición 50mm por encima de la pose de desbarbado.

### Ejercicio 3

MoveIt! tiene en cuenta los elementos de la escena para asegurar que las trayectorias que se generan no tienen ninguna colisión con los elementos de la escena. Cogiendo como punto inicial del ejercicio anterior [0º, -45º, -90º, -135º, 90º, 0º], modifica la URDF para añadir obstáculos.

Se han experimentado añadiendo distintos obstáculos y se ha analizado como se modifican las trayectorias.
