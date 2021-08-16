#define GLFW_INCLUDE_VULKAN
#include <GLFW/glfw3.h>

/*
GLFW/glfw3.h 헤더를 살펴보면,
#define GLFW_INCLUDE_VULKAN
이 전처리기가 명시되어있으면, 벌칸 헤더파일을 포함하도록 되어있다.
#if defined(GLFW_INCLUDE_VULKAN)
  #include <vulkan/vulkan.h>
#endif /* Vulkan header 
*/
//#include <vulkan/vulkan.h>

#include <iostream>
#include <stdexcept>
#include <cstdlib>

const uint32_t WIDTH = 800;
const uint32_t HEIGHT = 600;

class HelloTriangleApplication{
public:
void run() {
    initWindow();
    initVulkan();
    mainLoop();
    cleanup();
}
private:
    void initWindow() {

        glfwInit();
        glfwWindowHint(GLFW_CLIENT_API, GLFW_NO_API);
        glfwWindowHint(GLFW_RESIZABLE, GLFW_FALSE);

        window = glfwCreateWindow(WIDTH, HEIGHT, "Vulkan", nullptr, nullptr);
    }
    void initVulkan() {}
    void mainLoop(){
        while(!glfwWindowShouldClose(window)){
            glfwPollEvents();
        }
    }
    void cleanup(){
        glfwDestroyWindow(window);
        glfwTerminate();
    }

private:
    GLFWwindow* window;
};

int main() { 
    HelloTriangleApplication app;
    std::cout << " Hello Test ! \n";
    try{
        app.run();
    }
    catch(const std::exception& e){
        std::cerr<< e.what() << std::endl;
        return EXIT_FAILURE;
    }
    return EXIT_SUCCESS;
}