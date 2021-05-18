import sys, os

def compare(first, second):
    firstbytes = []
    for root, dirs, files in os.walk(first):
        for file in files:
            with open(os.path.join(root, file), "r", encoding="utf8") as auto:
                    firstbytes.append(auto.read(4096))

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