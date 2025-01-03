project(sdk-cpp LANGUAGES C CXX)
cmake_minimum_required(VERSION 3.10)

if (NOT TARGET CycloneDDS-CXX::ddscxx)
find_package(CycloneDDS-CXX REQUIRED)
endif()

if (NOT TARGET CycloneDDS::ddsc)
find_package(CycloneDDS REQUIRED)
endif()

#find_package(CycloneDDS-CXX REQUIRED)
## Convenience function, provided by the idlc backend for CXX that generates a CMake
## target for the given IDL file. The function calls idlc to generate
## source files and compiles them into a library.
#idlcxx_generate(TARGET ddscxxHelloWorldData_lib FILES HelloWorldData.idl WARNINGS no-implicit-extensibility)
#
#add_executable(ddscxxHelloworldPublisher publisher.cpp)
#add_executable(ddscxxHelloworldSubscriber subscriber.cpp)
#
## Link both executables to IDL data type library and ddscxx.
#target_link_libraries(ddscxxHelloworldPublisher ddscxxHelloWorldData_lib CycloneDDS CXX::ddscxx)
#target_link_libraries(ddscxxHelloworldSubscriber ddscxxHelloWorldData_lib CycloneDDS CXX::ddscxx)
#
#set_property(TARGET ddscxxHelloworldPublisher PROPERTY CXX_STANDARD 11)
#set_property(TARGET ddscxxHelloworldSubscriber PROPERTY CXX_STANDARD 11)

add_executable(list_topics list_topics.cpp)
target_link_libraries(list_topics CycloneDDS-CXX::ddscxx)
set_property(TARGET list_topics PROPERTY CXX_STANDARD 17)

add_executable(list_topics_c list_topics.c)
target_link_libraries(list_topics_c CycloneDDS::ddsc)
