import os
import subprocess
import platform

def WindowsPackageInstall():
    print("\nClone Vcpkg Package Manager...")
    os.system('git clone https://github.com/microsoft/vcpkg.git ./vendor')

    currentFolderPath = os.getcwd()
    print("\nCurrent Directory Path : " + currentFolderPath)

    print("\nGenerate Vcpkg execute file... ")
    subprocess.call([currentFolderPath + '/vendor/bootstrap-vcpkg.bat'])

    vcpkg = currentFolderPath + '/vendor/vcpkg.exe '

    print("\nInstall ThirdParty Libraries... ")
    os.system(vcpkg + 'install vulkan:x64-windows')
    os.system(vcpkg + 'install glm:x64-windows')
    os.system(vcpkg + 'install glfw3:x64-windows')
    os.system(vcpkg +'integrate install')

def MacPackageInstall():
    os.system("brew install glfw")
    os.system("brew install glm")

operatingSystem = platform.system()
print("OS : " + operatingSystem)

if operatingSystem == "Windows" :
    WindowsPackageInstall()
elif operatingSystem == "Darwin" :
    MacPackageInstall()
elif operatingSystem == "Linux" :
    print()

