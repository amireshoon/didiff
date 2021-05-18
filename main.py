import sys

def main():
    pass

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: didiff <pathToFirstDir> <pathToSecondDir>")
        sys.exit(1)

    if sys.argv[1] == sys.argv[2]:
        print("Dir's are the same!")
    else:
        main()