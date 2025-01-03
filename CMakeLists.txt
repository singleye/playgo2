cmake_minimum_required(VERSION 3.10)

project(playgo2)

add_subdirectory(experiments/dds)


# c/c++ sdk2 only support Linux
if(LINUX)
    add_subdirectory(experiments/sdk2)
endif()
