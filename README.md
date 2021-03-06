# Proyecto Final de Robótica Industrial Aplicada
## ROS
*Máster Universitario en Digital Manufacturing*

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
El ejercicio a programar consiste en la aplicación robótica común de PICK & PLACE. En este caso, se coge una pieza de una mesa y se deja en otra.

En primer lugar, se ha creado un nuevo workspace llamado *ros*. A continuación se crea un paquete para el ejercicio 1 con el comando  ```catkin_create_pkg ejercicio_1 rospy``` dentro de la carpeta *src*.

Las acciones de ROS se programan mediante nodos, los cuales son la unidad ejecutable de ROS. Es el *Máster* el que supervisa la comunicación entre nodos. Es lo primero que se lanza y siempre tiene que estar lanzado (```roscore```). 

Para visualizar estas modificaciones, se debe lanzar el simulador de UR Gazebo que el cálculo de geometría, a traves del comando ```roslaunch ur_gazebo ur5.launch```. A su vez, cada vez que se ejecuta un cambio se deben detener todas las terminales que se esten ejecuatando, y posteriormente compilar y refrescar la información nueva a traves de ```catkin build``` y a continuación ```source devel/setup.bash``` . 

Es necesario instalar una serie de complementos, librerias, APIs, etc. para realizar el desarrollo del ejercicio. Por un lado, se ha bajado una copia del código fuente de Ros de Universal Robots en el workspace para modificar el URDF.

Para ello, se ha modificado la parte *world_joint* del URDF para añadir dos mesas, una sobre la que esta el robot y realiza el pick y otra en perpendicular (en forma de L) donde se realiza el place (ver URDF 1).

```
<!-- MESA 2 -->
    <joint name="table_joint_2" type="fixed">
        <parent link="world"/>
        <child link="table_2"/>
    </joint>

    <link name="table_2">
        <visual>
            <origin xyz="0.5 1 0.37" rpy="0 0 0"/>
            <geometry>
                <box size="0.5 1.5 0.74"/>
            </geometry>
        </visual>
        <collision>
            <origin xyz="0.5 1 0.37" rpy="0 0 0"/>
            <geometry>
                <box size="0.5 1.5 0.74"/>
            </geometry>
        </collision>
```

La primera mesa está situada en el origen y sus dimensiones son 1.5x0.5x0.74m. La segunda mesa está situada a 0.5m en X y 1m en Y y sus dimensiones son 0.5x1.5x0.74m, tal como se observa en la siguiente foto.
    
 <p align="center">
    <img src = /Fotos/1.jpg width="350">
</p>

Además se lanza el nodo "rqt joint trajectory controller" para mover las articulaciones (joints) del robot de forma independiente mediante el siguiente comando ```rosrun rqt_joint_trajectory_controller rqt_joint_trajectory_controller --force-discover```, y encontrar la posición segura.

Los valores en espacio de joints elegidos como posición segura se definen a continuación en la tabla:

| Joints            | Valores      | 
| :----------------:|:------------:|
| elbow_joint       | 0.69         |      
| shoulder_lift_join| -2.00        |                                        
| shoulder_pan_joint| 2.35         |                                   
| wrist_1_joint     | -0.69        |                               
| wrist_2_joint     | -1.57        | 
| wrist_3 joint     | 0.50         |

safe_pose = [2.35, -2, 0.69, -0.69, -1.57, 0]

Para la comunicación entre ROS y MoveIt que se llevará a cabo mediante lenguaje Python, es necesario importar la librería de *moveit_commander*. 

```py
import rospy
import moveit_commander
import time
from tf import transformations
from geometry_msgs.msg import Pose
```

También se ha importado la librería Time para las esperas, mediante la línea ```time.sleep(T)```. En este caso se le ha dado un valor de 2.

El siguiente paso a seguir es generar un nuevo archivo en blanco el cual tendrá el script en python. La lógica que sigue el código es la siguiente:

* Se desplaza a la posición Pick arriba: [0, 0, 1, -2.36, 1.57, 0]
* Se desplaza a la posición Pick abajo:[0, 0, 0.85, -2.36, 1.57, 0]
* Espera 2 segundos
* Vuelve a subir. Se desplaza a la posicion pick arriba:[0, 0, 1, -2.36, 1.57, 0]
* Se desplaza al punto Place arriba:[0.5, 0.7, 1, -2.36, 1.57, 0]
* Se desplaza al punto Place abajo:[0.5, 0.7, 0.85, -2.36, 1.57, 0]
* Espera 2 segundos.
* Vuelve a subir a la posición a Place arriba.

Este ciclo pick & place se ha incluido dentro de un ciclo ```for``` donde se realizan N repeticiones, según el valor que se le asigne a dicha variable (en este caso de 5). 

```py
for i in range (rep):

	print "PICK"
	pick_arriba = [0, 0, 1,-2.36, 1.57, 0]
	ur_group.set_pose_target(pick_arriba)
	plan = ur_group.plan()
	ur_group.execute( plan )

	pick_abajo = [0, 0, 0.85,-2.36, 1.57, 0]
	ur_group.set_pose_target(pick_abajo)
	plan = ur_group.plan()
	ur_group.execute( plan )

	time.sleep(2)
```

Se aclara que, en este script se ha definido la posición segura en joints mediante el siguiente vector ```safe_pose = [2.35, -2, 0.69, -0.69, -1.57, 0]```. Esta posición segura se alcanza  al inicio y al final del programa en espacio de joints.

Para que el script de Python sea ejecutable, se dan permisos de ejecuciòn mediante el comando   ```chmod +x script_1.py ```.
Se vuelve a compilar y refrescar la información nueva a través de ```catkin build``` y ```source devel/setup.bash```. 

También se lanza el planificador MoveIt!, el cual sirve para planificar y ejecutar trayectorias en espacio cartesiano con ```roslaunch ur5_moveit_config ur5_moveit_planning_execution.launch sim:=true```. 

Además, se utiliza RViz de lanzar el visualizador es necesario lanzar también el plugin ```roslaunch ur5_moveit_config moveit_rviz.launch config:=true```. En RViz podemos ver que las trayectorias pueden generar colisiones. Esto es debido a que la escena del RViz tiene suelo y la de MoveIt! no. Esto hace que haya que modificar la escena. 

 Y por ùltimo, se lanza el nodo creado con el comando ```rosrun ejercicio_1 script_1.py```. La siguiente foto muestra la ejecuaciòn de todas las terminales lanzadas.
 
 <p align="center">
    <img src = /Fotos/2.jpg width="450">
</p>
 
### Ejercicio 2

En este ejercicio se va a simular que el robot coge una pieza de una posición y la deja en otra posición del grid. Para comenzar se ha tomado como base el ejercicio anterior y se realizan los mismos pasos de creaciòn de paquete, utilizaciòn de Gazebo, MoveIT, RViz y rqt joint trajectory controller, modificaciòn del URDF para una mesa mas grande, creaciòn de un script en python, etc.

Se ha tomado como base las posiciones iniciales del ejercicio anterior

* Pose de approach (Pose pick del ejercicio 1): [0, 0, 1, -2.36, 1.57, 0]
* Posicion inicial de la bandeja (Place): [0.5, 0.7, 1, -2.36, 1.57, 0]
* Posición segura de inicio y final de programa en espacio de joints: safe_pose = [2.35, -2, 0.69, -0.69, -1.57, 0]

Se han definido los parametros de filas, columnas, Distancia horizontal y Distancia vertical como variables del codigo en Python para facilitar su uso en caso de requerir modificaciòn en el valor
```py
filas = 3
columnas = 3
paso_horizontal = 0.1
paso_vertical = 0.15
```
También, se han agregado dos ciclos ```for``` para recorrer la rejilla, el primero da el paso por las columnas, manteniendo la fila constante, y después se incrementa el contador para pasar a la siguiente fila. Además de crear los dos contadores ```i``` y ```j``` que controlan el recorrido y se incrementan en cada paso.

De modo que el nodo Python realizar los siguientes pasos:

1. Se mueve en espacio de joints a la posición “safe”
```py
print "Safe point"
safe_point = [2.35, -2, 0.69, -0.69, -1.57, 0]
ur_group.set_joint_value_target(safe_point)
rospy.loginfo( 'Planning movement' )
plan = ur_group.plan()
rospy.loginfo( 'Executing pl1an' )
ur_group.execute( plan )
raw_input('Pause')
```
2. Realiza un movimiento de approach en espacio cartesiano a la posición de cogida.
```py
for i in range (filas):
    for j in range (columnas):

        print "PICK"
        pick_arriba = [0, 0, 1,-2.36, 1.57, 0]
        ur_group.set_pose_target(pick_arriba)
        plan = ur_group.plan()
        ur_group.execute( plan )
```
3. Baja en Z para coger el objeto, y subir en Z de nuevo.
```py

        pick_abajo = [0, 0, 0.85,-2.36, 1.57, 0]
        ur_group.set_pose_target(pick_abajo)
        plan = ur_group.plan()
        ur_group.execute( plan )

        time.sleep(2)

        ur_group.set_pose_target(pick_arriba)
        plan = ur_group.plan()
        ur_group.execute( plan )
```
4. Realiza un movimiento de approach en espacio cartesiano a la primera posición del grid
```py
print "Place"
        place_arriba = [0.5+i*paso_horizontal, 0.7+j*paso_vertical, 1,-2.36, 1.57, 0]
        ur_group.set_pose_target(place_arriba)
        plan = ur_group.plan()
        ur_group.execute( plan )
```
5. Bajar en Z para dejar el objeto, y subir en Z de nuevo
```py
        place_abajo = [0.5+i*paso_horizontal, 0.7+j*paso_vertical, 0.85,-2.36, 1.57, 0]
        ur_group.set_pose_target(place_abajo)
        plan = ur_group.plan()
        ur_group.execute( plan )

        time.sleep(2)

        ur_group.set_pose_target(place_arriba)
        plan = ur_group.plan()
        ur_group.execute( plan )
```
6. Mover de nuevo a la posición de cogida (approach + bajar + subir)
7. Dejar el objeto en la siguiente posición del grid
8. Ir repitiendo el ciclo hasta completar todas las posiciones del grid

Estos utlimos pasos se realizan a medida que se va incrementando el valor de los contadores y recorriendo todas las posiciones de la rejilla.

Ademas, se han realizado modificaciones sobre los parametros iniciales. Primero se han llevado a cabo añadiendo 4 filas, y un paso horizontal de 0.08 no ha dado problemas. Sin embargo, también se ha desplazado el origen un metro  hacia la derecha (+x) y ha dado error porque el robot no ha alcanzado esta posición por lo que se ha interrumpido el programa.

### Ejercicio 3

#### *MoveIt! tiene en cuenta los elementos de la escena para asegurar que las trayectorias que se generan no tienen ninguna colisión con los elementos de la escena.*

Se ha modificado el URDF para añadir un tercer obstáculo entre las dos mesas en forma de L. Este obstáculo tiene  las siguientes dimensiones: 0.4x0.4x1m y se encuentra en la posición x,y,z "0.5 0.5 1"

Al planificar trayectorias, en algunos casos el robot ha hecho movimientos curisos debido a la dificultad de alcanzar la posición, daba vueltas innecesarias para alcanzar los puntos. En casos en los que directamente no ha podido conseguir generar la trayectoria, el programa ha dejado de ejecutarse.

### Conclusiones

Al ser un entorno de trabajo abstracto para nosotras, nos hemos encontrado con varios problemas: nos ha dado problemas la máquina virtual. Además nos ha llevado mucho tiempo solventar que aparezca la segunda mesa. La razón principal ha sido que no se detenían todos los terminales activos para modificar el URDF.
