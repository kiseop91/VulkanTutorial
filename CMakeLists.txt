cmake_minimum_required(VERSION 3.1)
list(APPEND CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/cmake)

set(TargetName vulkan_tutorial)
project(learning-vulkan LANGUAGES CXX)

find_package(Vulkan REQUIRED)
find_package(glfw3 CONFIG REQUIRED)
find_package(glm CONFIG REQUIRED)

add_executable(${TargetName} "src/main.cpp")

target_compile_features(${TargetName} PRIVATE cxx_std_17)
target_link_libraries(${TargetName} PRIVATE
    Vulkan::Vulkan
    glfw
    glm::glm
)