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

El ejercicio a programar consiste en la aplicación roboticá común de PICK & PLACE. En este caso, se coge una pieza de una mesa y lo deposita en otra.

En primer lugar, se ha creado un nuevo workspace llamado *ros*. A continuación se crea un paquete para el ejercicio 1 con el comando  ```catkin_create_pkg ejercicio_1 rospy``` dentro de la carpeta *src*.

Las acciones en ROS se programan mediante nodos, la cual es la unidad ejecutable de ROS. Es el *Máster* el que supervisa la comunicación entre nodos. Es lo primero que se lanza y siempre tiene que estar lanzado (```roscore```). 

A su vez, es necesario instalar una serie de complementos, librerias, APIs, etc. para realizar el desarrollo del ejercicio. Por un lado, se bajo una copia del codgio fuente del ros de universal robots para modificar el URDF.

Para ello, se modifico la parte *world_joint* del URDF para añadir dos mesas, una sobre la que esta el robot y realiza el pick y otra en perpendicular (en forma de L) donde se realiza el place. 

Para visualizar estas modificaciones, se debe lanzar el simulador de UR Gazebo que el cálculo de geometria, a traves del comando ```roslaunch ur_gazebo ur5.launch```

A su vez, cada vez que se ejecute un cambio se deben detener todos los terminales que se esten ejecuatando, y posteriormente compilar y refrescar la información nueva a traves de ```catkin build``` y a continuación ```source devel/setup.bash``` . 

Como se menciono anteriomente, para realizar los ejercicios de pick & place se configuraron dos mesas en forma de L,  para simular coger objetos y depositarlos. La primera mesa está situada en el origen y sus dimensiones son 1.5x0.5x0.74m. La segunda mesa está situada a 0.5m en X y 1m en Y y sus dimensiones son 0.5x1.5x0.74m.
    
  <p align="center">
    <img src = /Fotos/1.jpg width="350">
</p>

Ademas se lanza el nodo rqt joint trajectory controller para mover las articulaciones (joints) del robot de forma independiente mediante el siguiente comando ```rosrun rqt_joint_trajectory_controller rqt_joint_trajectory_controller --force-discover```, y encontrar la posición segura.

Los valores en espacio de joints elegidos como posición segura se definen a continuación en la tabla:

| Joints            | Valores      | 
| :----------------:|:------------:|
| elbow_joint       | 0.69         |      
| shoulder_lift_join| -2.00         |                                        
| shoulder_pan_joint| 2.35         |                                   
| wrist_1_joint     | -0.69        |                               
| wrist_2_joint     | -1.57        | 
| wrist_3 joint     | 0.50         |

Para la comunicación entre ROS y MoveIt que se llevará a cabo mediante lenguaje Python, es necesario tener utilizar la libreria de *moveit_commander*. El siguiente paso a seguir es generar un nuevo archivo en blanco el cual contendra el script en python. La logica que sigue el codigo es la siguiente 

* Se desplaza a la posición Pick arriba: [0, 0, 1, -2.36, 1.57, 0]
* Se desplaza a la posición Pick abajo:[0, 0, 0.85, -2.36, 1.57, 0]
* Espera 2 segundos
* Vuelve a subir. Se desplaza a la posicion pick arriba:[0, 0, 1, -2.36, 1.57, 0]
* Se desplaza al punto Place arriba:[0.5, 0.7, 0.85, -2.36, 1.57, 0]
* Se desplaza al punto Place abajo:[0.5, 0.7, 1, -2.36, 1.57, 0]
* Espera 2 segundos.
* Vuelve a subir a la posición a Place arriba.

Este ciclo pick & place se realiza alcanza las posiciones (en espacios cartersianos) definidos anteriormente. Ademas se a incluido dentro de un ciclo ```for``` donde se realizan N repeticiones, segun el valor que se le asigne a dicha variable (en este caso de 5).

Se aclara que, en este script se ha definido la posiciòn segura en joints mediante el siguiente vector ```safe_pose = [2.35, -2, 0.69, -0.69, -1.57, 0]```. Esta posición segura es alcanzada  al inicio y final de programa en espacio de joints.

Para que el script Python sea ejecutable, se les dan permisos de ejecuciòn mediante el comando   ```chmod +x script_1.py ```.
Nuevamente se compila y refresca la información nueva a traves de ```catkin build``` y ```source devel/setup.bash```. 

Al igual que se lanza el planificador MoveIt!, el cual sirve para planificar y ejecutar trayectorias en espacio cartesiano con ```roslaunch ur5_moveit_config ur5_moveit_planning_execution.launch sim:=true```. 

 Y luego se lanza el nodo creado con el comando ```rosrun ejercicio_1 script_1.py```
 
 <p align="center">
    <img src = /Fotos/2.jpg width="450">
</p>
 
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

Se ha añadido un tercer obstáculo entre las dos mesas desplazando la segunda mesa. De tal manera que al robot le resulte más complicado alcanzar la segunda mesa. 

### Conclusiones

Al ser un entorno de trabajo abstracto para nosotras, nos hemos encontrado con varios problemas: nos ha dado problemas la máquina virtual. Además nos ha llevado mucho tiempo solventar que aparezca la segunda mesa. La razón principal ha sido que no se detenian todos los terminales activos para modificar el URDF.
