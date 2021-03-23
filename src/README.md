## Turtlebots

#### Actividades sesión 3 (para sábado 27):

1) Vuelve este workspace funcional y crea un paquete de ROS con tu nombre (dependencia rospy).


2) El equipo de Perception ha terminado de entrenar la red neuronal encargada de identificar objetos para la competencia, esta tiene como output una coordenada **(x,y,z)**. Así que VantTec necesita que tú, como miembro de Turtlebots, transmitas este output al equipo de control. Crea los nodos *perception_uuv* y *control_uuv*, luego transmite un ROS message type *geometry_msgs/Point* (output de la red neuronal) por medio de un tópico */perception_to_control*. Para probar que funciona, transmite alguna cordenada (la que quieras) y cuando la recibas printea en la terminal: "La coordenada es: [coordenada escogida]". 

