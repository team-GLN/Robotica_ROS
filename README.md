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
- [Conclusiones](https://github.com/team-GLN/Robotica_ROS/blob/UR/README.md#conclusiones)


### Introducción

ROS es un software de programación de robots que es compatible con la mayoría de los robots que se encuentran en el mercado. Esto es una ventaja en un mundo en el que cada marca tiene su propio lenguaje de programación y permite no ser experto en cada uno de ellos para poder trabajar con varias marcas.

Se van a analizar y programar diferentes ejercicios de situaciones típicas que se encuentran en la industria. Sin embargo, previamente se han tenido que preparar y tener en cuenta las diferentes fases que se analizarán a continuación para poder realizar los ejercicios.


### Ejercicio 1

El ejercicio a programar consiste en la aplicación roboticá común de PICK&PLACE. En este caso, coge la pieza en una mesa y lo deposita en otra.

En primer lugar se ha creado un nuevo workspace llamado *ros*. A continuación se crea un paquete para el ejercicio 1 con el comando  ```catkin_create_pkg ejercicio_1 rospy``` dentro de *src*.

Es necesario instalar el simulador de UR Gazebo para hacer el cálculo de geometria a traves del paquete de ROS ```sudo apt-get install ros-kinetic-universal-robot``` y a la hora de lanzar el simulador con ```roslaunch ur_gazebo ur5.launch```. Así como el planificador MoveIt! el cual sirve para planificar y ejecutar trayectorias en espacio cartesiano con ```roslaunch ur5_moveit_config ur5_moveit_planning_execution.launch sim:=true```. 

Los movimientos del ejercicio se programan en nodos de ROS. Un nodo es la unidad ejecutable de ROS. Es el *Máster* el que supervisa la comunicación entre nodos. Es lo primero que se lanza y siempre tiene que estar lanzado (*roscore*). Para la comunicación entre ROS y MoveIt que se llevará a cabo mediante lenguaje Python, es necesario tener instalado el paquete *moveit_commander* porque ofrece una interfaz de Python. El siguiente paso a seguir es generar un nuevo archivo en blanco el cual contendra el script.

Como planificador de trayectorias también se puede utilizar el visualizador de datos de Ros, RViz. Para que RViz interaccione con MoveIt! además de lanzar el visualizador es necesario lanzar también el plugin ```roslaunch ur5_moveit_config moveit_rviz.launch config:=true```. En RViz podemos ver que las trayectorias pueden generar colisiones. Esto es debido a que la escena del RViz tiene suelo y la de MoveIt! no. Esto hace que haya que modificar la escena. 

Es necesario modificar la última parte *world_joint* del URDF (formato de lenguaje) para añadir una mesa. Sin embargo, durante esta fase de modificaciones, hay que detener todos los terminales y posteriormente activarlos a traves de ```catkin build``` y a continuación ```source devel/setup.bash``` . 





Para realizar los ejercicios de pick&place, es necesario añadir una segunda mesa para simular coger objetos y depositarlos. Para ello hay que modificar el URDF. La configuración de las mesas que hemos considerado es con forma de L. La segunda mesa está situada a 0.5m del origen en X y las dimensiones de ambas son 1.5x0.5x0.74m.


    
  <p align="center">
    <img src = /Fotos/1.jpg width="350">
</p>


Los valores de joint elegidos se definen a continuación en la tabla:

| Joints            | Valores      | 
| :----------------:|:------------:|
| elbow_joint       | 0.69         |      
| shoulder_lift_join| -2           |                                        
| shoulder_pan_joint| 2.35         |                                   
| wrist_1_joint     | -0.69        |                               
| wrist_2_joint     | -1.57        | 
| wrist_3 joint     | 0.5          |

Además es necesario declarar una posición segura de inicio y final de programa en espacio de joints:

* safe_pose = [2.35, -2, 0.69, -0.69, -1.57, 0]

El ciclo pick&place en posiciones cartersianas que se propone es el que se ve a continuación el cual se ha incluido dentro de un ciclo ```for``` donde a las repetiones  N  se le ha dado un valor de 5.
* posición Pick arriba: [0, 0, 1, -2.36, 1.57, 0]
* Posición Pick abajo:[0, 0, 0.85, -2.36, 1.57, 0]
* Espera 2 segundos
* Vuelve a subir. Pick arriba:[0, 0, 1, -2.36, 1.57, 0]
* Place arriba:[0.5, 0.7, 0.85, -2.36, 1.57, 0]
* Place abajo:[0.5, 0.7, 1, -2.36, 1.57, 0]
* Espera 2 segundos.


```
rep=5

for i in range (rep):
	pick_arriba = [0, 0, 1,-2.36, 1.57, 0]
        pick_abajo = [0, 0, 0.85,-2.36, 1.57, 0]
	time.sleep(2)
	pick_arriba = [0, 0, 1,-2.36, 1.57, 0]
	place_arriba = [0.5, 0.7, 1,-2.36, 1.57, 0]
	place_abajo = [0.5, 0.7, 0.85,-2.36, 1.57, 0]
	time.sleep(2)
        place_arriba = [0.5, 0.7, 1,-2.36, 1.57, 0] 
```   


### Ejercicio 2

#### *En este ejercicio se va a simular que el robot coge una pieza de una posición y la deja en otra posición del grid.*

* Pose de inicio:
* Posiciones de la bandeja:
* filas: 3
* columnas: 3
* Distancia horizontal de la rejilla: 0.05
* Distancia vertical de la rejilla: 0.05
* Antes de comenzar el ciclo de pick&place, el robot debera ir a una posición 50mm por encima de la pose de inicio.
* Posición segura de inicio y final de programa en espacio de joints: [-45º, -90º, 0º -135º, 90º, 0º]
* Movimiento de approach en espacio cartesiano
* Bajar en Z para coger el objeto y subir en Z
* Movimiento de approach a la primera posicion del grid
* Bajar en Z para dejar el objeto y subir en Z
* Mover de nuevo a la posición de cogida

*Verificación de las posiciones

### Ejercicio 3

#### *MoveIt! tiene en cuenta los elementos de la escena para asegurar que las trayectorias que se generan no tienen ninguna colisión con los elementos de la escena. Cogiendo como punto inicial del ejercicio anterior [0º, -45º, -90º, -135º, 90º, 0º], modifica la URDF para añadir obstáculos.*

Se ha añadido un tercer obstáculo entre las dos mesas modificando el URDF una vez más, de tal manera que al robot le resulte más complicado alcanzar la segunda mesa. Como conclusión 

### Conclusiones

Al ser un entorno de trabajo abstracto para nosotras, nos hemos encontrado con varios problemas: nos ha dado problemas la máquina virtual. Además nos ha llevado mucho tiempo solventar que aparezca la segunda mesa. La razón principal ha sido que no se detenian todos los terminales activos para modificar el URDF.
