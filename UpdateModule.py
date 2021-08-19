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
    # print("Input Target Architecture : (ex : arm64-osx, x64-osx) : ")
    # arch = input()
    print("\nClone Vcpkg Package Manager...")
    os.system('git clone https://github.com/microsoft/vcpkg.git ./vendor')

    currentFolderPath = os.getcwd()
    print("\nCurrent Directory Path : " + currentFolderPath)

    print("\nGenerate Vcpkg execute file... ")
    subprocess.call([currentFolderPath + '/vendor/bootstrap-vcpkg.sh'])

    vcpkg = currentFolderPath + '/vendor/vcpkg '

    print("\nInstall ThirdParty Libraries... ")
    os.system(vcpkg + 'install vulkan:x64-osx')
    os.system(vcpkg + 'install glm:x64-osx')
    os.system(vcpkg + 'install glfw3:x64-osx')

    os.system(vcpkg + 'install vulkan:arm64-osx')
    os.system(vcpkg + 'install glm:arm64-osx')
    os.system(vcpkg + 'install glfw3:arm64-osx')

    os.system(vcpkg +'integrate install')

operatingSystem = platform.system()
print("OS : " + operatingSystem)

if operatingSystem == "Windows" :
    WindowsPackageInstall()
elif operatingSystem == "Darwin" :
    MacPackageInstall()
elif operatingSystem == "Linux" :
    print()

