execute_process(COMMAND "/home/ivan5d/turtlebots/build/turtlebots_sim/turtlebot3/turtlebot3_example/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/ivan5d/turtlebots/build/turtlebots_sim/turtlebot3/turtlebot3_example/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
