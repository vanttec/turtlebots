#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/ivan5d/turtlebots/src/turtlebots_sim/turtlebot3/turtlebot3_example"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/ivan5d/turtlebots/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/ivan5d/turtlebots/install/lib/python2.7/dist-packages:/home/ivan5d/turtlebots/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/ivan5d/turtlebots/build" \
    "/usr/bin/python2" \
    "/home/ivan5d/turtlebots/src/turtlebots_sim/turtlebot3/turtlebot3_example/setup.py" \
     \
    build --build-base "/home/ivan5d/turtlebots/build/turtlebots_sim/turtlebot3/turtlebot3_example" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/ivan5d/turtlebots/install" --install-scripts="/home/ivan5d/turtlebots/install/bin"
