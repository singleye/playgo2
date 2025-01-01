# install cyclonedds

```
cd deps
tar zxf cyclonedds-cxx-0.10.4.tar.gz
cd cyclonedds-cxx-0.10.4
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=<your_prefix_dir> -DCMAKE_PREFIX_PATH=<your_prefix_dir> -DENABLE_SHM=YES -DENABLE_TYPE_DISCOVERY=YES -DENABLE_TOPIC_DISCOVERY=YES  ..
make
make install
```
