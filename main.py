import getpass
import os
import platform
import sys

ARCH = platform.machine()
OS = platform.system()

compatibly = False


def move_files():
    os.mkdir(f"/home/{getpass.getuser()}/.infinity/")
    os.rename(f'{ARCH}-{OS}-Infinity.exe', '/home/{getpass.getuser()}/.infinity/{ARCH}-{OS}-Infinity.exe')
    os.rename('Infinity.desktop', f'/home/{getpass.getuser()}/Desktop/Infinity.desktop')
    os.rename('infinity.json', f"/home{getpass.getuser()}/.infinity/infinity.json")


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
    check_compatibility()
    move_files()
    print("Finished installing Infinity")


if __name__ == '__main__':
    main()
