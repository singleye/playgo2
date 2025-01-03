cmake_minimum_required(VERSION 3.10)

project(experiment_gstreamer)

set(CMAKE_CXX_STANDARD 14)

find_package(PkgConfig REQUIRED)
pkg_check_modules(GSTREAMER REQUIRED gstreamer-1.0)
include_directories(
    ${GLIB_INCLUDE_DIRS}
    ${GSTREAMER_INCLUDE_DIRS}
)

message("gstreamer include directories: " ${GSTREAMER_INCLUDE_DIRS})
message("gstreamer libraries: " ${GSTREAMER_LIBRARIES})
add_executable(basic-tutorial-1 basic-tutorial-1.c)
target_link_libraries(basic-tutorial-1 ${GSTREAMER_LIBRARIES})
