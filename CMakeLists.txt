cmake_minimum_required(VERSION 3.1)

# Cmake 구성할때 인자로 넘겨줘야하나 편의상 변수로 설정.
# M1 Mac Architecture 설정
# set(CMAKE_OSX_ARCHITECTURES arm64)
 
# vcpkg 툴체인 경로 설정 
# CMAKE_TOOLCHAIN_FILE도 프로젝트 구성할 때, 인자로 넣어주는 것이 좋습니다. -DCMAKE_TOOLCHAIN_FILE=경로
if(NOT DEFINED CMAKE_TOOLCHAIN_FILE)
  set(CMAKE_TOOLCHAIN_FILE "./vendor/scripts/buildsystems/vcpkg.cmake"
      CACHE STRING "")
endif()

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