cmake_minimum_required(VERSION 3.1)

# 해당 변수는 preset으로 옮길 예정
# set(CMAKE_OSX_ARCHITECTURES arm64)
 
project(learning-vulkan LANGUAGES CXX)

list(APPEND CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/cmake)

find_package(Vulkan REQUIRED)
find_package(glfw3 CONFIG REQUIRED)
find_package(glm CONFIG REQUIRED)

add_executable(vulkan-test "src/main.cpp")

target_link_libraries(vulkan-test PRIVATE
Vulkan::Vulkan
glfw
glm::glm
)