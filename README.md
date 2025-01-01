# playgo2

This project has some programs to play with unitree go2 quadruped robot.

* doggy: under development. It will act as a dog to play with the human around.

# Setup environemnt

## Build opencv with gstreamer

In order to capture video through opencv, you need to build opencv with gstreamer support. Here is how you can do it:

```
cd deps
tar zxf opencv-4.10.0.tar.tgz
tar zxf opencv_contrib-4.10.0.tar.gz
cd opencv-4.10.0
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=<replace_with_your_prefix_dir> INSTALL_PYTHON_EXAMPLES=ON -D INSTALL_C_EXAMPLES=OFF -D OPENCV_ENABLE_NONFREE=ON -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-4.10.0/modules -D PYTHON_EXECUTABLE=$(which python) -D BUILD_opencv_python2=OFF -D CMAKE_INSTALL_PREFIX=$(python -c "import sys; print(sys.prefix)") -D PYTHON3_EXECUTABLE=$(which python) -D PYTHON3_INCLUDE_DIR=$(python -c "from distutils.sysconfig import get_python_inc; print(get_python_inc())") -D PYTHON3_PACKAGES_PATH=$(python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())") -D WITH_GSTREAMER=ON -D WITH_OPENGL=ON -D BUILD_EXAMPLES=ON ..
make
make install
```
