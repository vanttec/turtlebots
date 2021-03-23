## Turtlebots

#### Actividad 1: 

1) Baja los cambios, vuelve este workspace funcional y crea un paquete de ROS con tu nombre (dependencia rospy).

<p align="left">
  <img src="https://github.com/vanttec/turtlebots/blob/main/src/images/image2.jpg" width="400" height="240" align="left"/>
</p>

<p align="center">
  <img src="https://github.com/vanttec/turtlebots/blob/main/src/images/image3.png" width="400" height="240" align="center"/>

2) El equipo de Perception ha terminado de entrenar la red neuronal encargada de identificar boyas para la competencia, esta tiene como output una coordenada **(x,y,z)** del centro de cada una. Así que VantTec necesita que tú, como miembro de Turtlebots, transmitas este output al equipo de control. Crea los nodos *perception_uuv* y *control_uuv*, luego transmite un ROS message type *geometry_msgs/Point* (output de la red neuronal) por medio de un tópico */perception_to_control*. Para probar que funciona, transmite alguna cordenada (la que quieras) y cuando la recibas printea en la terminal: "La coordenada es: [coordenada escogida]". 

Hint: Toda la documentación que necesites sobre ROS la encontrarás en su wiki.  
