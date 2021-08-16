cmake_minimum_required(VERSION 3.1)

#Cmake Arch을 명시해줘야함. 원래는  Cmake 구성할때 인자로 넘겨주는 것잊 좋은데 임시로, 여기에 변수로 셋팅하도록하자.
# 윈도우나 인텔 맥의 경우 아키텍쳐를 바꿔줘야함. ( arm M1 맥에서만 필요한 것으로 보임. )
set(CMAKE_OSX_ARCHITECTURES arm64)

project(learning-vulkan LANGUAGES CXX)

list(APPEND CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/cmake)

find_package(Vulkan REQUIRED)
find_package(glfw3 3.3 REQUIRED)
find_package(glm REQUIRED)

add_executable(vulkan-test "src/main.cpp")

target_link_libraries(vulkan-test PRIVATE
Vulkan::Vulkan
glfw
glm::glm
)