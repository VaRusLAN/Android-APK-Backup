import os
from subprocess import run
import re


def get_path_and_names() -> list[tuple[str, str]]:
    command = "adb shell pm list packages -3 -f"
    result = run(command, shell=True, capture_output=True)
    packages = result.stdout.decode().splitlines()
    paths = []
    names = []
    pattern = r"(?<=package:)(.*(?=\=))\=(.*)"
    regex = re.compile(pattern)
    for package in packages:
        result = regex.search(package)
        paths.append(result.group(1))
        names.append(result.group(2))
    tuples = list(zip(paths, names))
    return tuples


def main():
    # Get paths and names
    tuples = get_path_and_names()
    # Make folder for packages
    folder = "packages"
    os.makedirs(folder, exist_ok=True)
    # Extract apks
    for path, name in tuples:
        command = f"adb pull {path} ./{folder}/{name}.apk"
        run(command, shell=True)


if __name__ == "__main__":
    main()
