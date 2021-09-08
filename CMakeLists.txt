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

# Check Vulkan GLSLC EXE
message(STATUS "Vulkan_GLSLC_EXECUTABLE : ${Vulkan_GLSLC_EXECUTABLE}")
message(STATUS "Vulkan_GLSLANG_VALIDATOR_EXECUTABLE  : ${Vulkan_GLSLANG_VALIDATOR_EXECUTABLE}")

function(add_shader SHADER INPUT_EXTENSION)
    set(shaderFile  ${CMAKE_CURRENT_SOURCE_DIR}/shaders/${SHADER}${INPUT_EXTENSION})
    set(outputFile ${CMAKE_CURRENT_SOURCE_DIR}/shaders/${SHADER}.spv)
    add_custom_command(
        TARGET ${TargetName} POST_BUILD
        COMMAND ${Vulkan_GLSLC_EXECUTABLE} ${shaderFile} -o ${outputFile}
    )
endfunction(add_shader)

# Find All shaders
file(GLOB vertex-shaders ${CMAKE_CURRENT_SOURCE_DIR}/shaders/*.vert)
file(GLOB fragment-shaders ${CMAKE_CURRENT_SOURCE_DIR}/shaders/*.frag)
file(GLOB compute-shaders ${CMAKE_CURRENT_SOURCE_DIR}/shaders/*.comp)

# Compile All shaders
foreach(vertex-shader ${vertex-shaders})
		get_filename_component(pathName ${vertex-shader} NAME_WE)
		get_filename_component(extension ${vertex-shader} EXT)
		add_shader(${pathName} ${extension})
endforeach(vertex-shader)

foreach(fragment-shader ${fragment-shaders})
		get_filename_component(pathName ${fragment-shader} NAME_WE)
		get_filename_component(extension ${fragment-shader} EXT)
		add_shader(${pathName} ${extension})
endforeach(fragment-shader)

foreach(compute-shader ${compute-shaders})
		get_filename_component(pathName ${compute-shader} NAME_WE)
		get_filename_component(extension ${compute-shader} EXT)
		add_shader(${pathName} ${extension})
endforeach(compute-shader)
