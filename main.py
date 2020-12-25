import platform
import sys
import os

compatibly = False


def move_files(userName):
    os.rename('Infinity', '/bin/Infinity')
    os.rename('Infinity.desktop', f'/home/{userName}/Desktop/Infinity.desktop')


def check_compatibility():
    global compatibly
    if platform.machine() == 'x86_64' or platform.machine() == 'x86':
        compatibly = True
        print("CPU architecture is supported")
    else:
        print("CPU architecture:", platform.machine(), "isn't supported")
        compatibly = False
    if platform.system() == 'Linux':
        compatibly = True
        print("Operating system is supported")
    else:
        print("Operating system:", platform.system(), "isn't supported")
    if compatibly:
        print("Infinity is supported on your device")
        print("Setting up Infinity...")
    else:
        print("Don't worry if your device doesn't support Infinity.")
        print("This is just the proof of concept and will hopefully work better soon")
        sys.exit(0)


def main():
    print("Your user name should be:")
    os.system('echo $USER')
    userName = input("\nEnter you user name: ")
    check_compatibility()
    move_files(userName)
    print("Finished installing Infinity")


if __name__ == '__main__':
    main()
