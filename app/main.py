import sys


def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")
    i = input()
    print(i + ": command not found")


if __name__ == "__main__":
    main()
