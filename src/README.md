## Turtlebots

#### Actividad 2: 

<p align="left">
  <img src="https://github.com/vanttec/turtlebots/blob/5ef8b54bc3199e1bc85476b46d7c725b161ff31f/src/images/uv.png" width="400" height="240" align="center"/>
</p>

La competencia de RoboBoat tomará lugar en línea y se necesita que cada equipo envíe un simulador de su usv desplegado en Gazebo, pues ahí se mostrarán los retos de la competencia. 

1) Modifica *scripts/perception_uuv* para volverlo un subscriber del tópico */r200/camera/color/image_raw* proveniente del simulador.     
2) Crea el launch file *launch/turtlebots.launch* que despliegue *vtec_s3_description/upload.launch* y el rosnode *perception_uuv* modificado. 

#### Comentarios:
Para comprobar corre: 
```
roslaunch uv_worlds lake.launch
roslaunch [nombre] turtlebots.launch 
```
