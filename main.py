import sys, os
import pathlib

def walker(path):
    """
    Walks through path folders and count files
    folders and collect files byte
    """
    files_ = []
    dirs_ = []
    bytes_ = []

    for root, dirs, files in os.walk(path):
        files_.append(files)
        dirs_.append(dirs)
        for file in files:
            if pathlib.PurePath(root).name == ".git":
                continue
            with open(os.path.join(root, file), "r", encoding="utf8") as auto:
                    bytes_.append(auto.read())
    yield files_
    yield dirs_
    yield bytes_

def compare(first, second):
    """
    Compares two path and collect data
    """
    a,b,c = walker(first)
    d,e,f = walker(second)
    print(a,b)
    

def main():
    compare(sys.argv[1], sys.argv[2])
    pass

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: didiff <pathToFirstDir> <pathToSecondDir>")
        sys.exit(1)

    if sys.argv[1] == sys.argv[2]:
        print("Dir's are the same!")
    else:
        main()
