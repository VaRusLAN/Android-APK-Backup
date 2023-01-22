import os
from subprocess import run


def main():
    folder = "packages"
    files = os.listdir(folder)
    package_list = []
    for file in files:
        if file.endswith(".apk"):
            package_list.append(f"./{folder}/{file}")
    packages = " ".join(package_list)
    command = f"adb install-multi-package {packages}"
    run(command, shell=True)


if __name__ == "__main__":
    main()
