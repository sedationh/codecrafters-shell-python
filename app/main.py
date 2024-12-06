import sys


def main():
    # Uncomment this block to pass the first stage
    while True:
        sys.stdout.write("$ ")
        command = input()
        if command == "exit 0":
            break
        # start with echo
        if command.startswith("echo"):
            sys.stdout.write(command[5:] + "\n")
            continue

        sys.stdout.write(f"{command}: command not found\n")


if __name__ == "__main__":
    main()
