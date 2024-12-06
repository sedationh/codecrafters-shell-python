import sys


def main():
    # Uncomment this block to pass the first stage
    commands = ["echo", "type"]

    while True:
        sys.stdout.write("$ ")
        command = input()
        if command == "exit 0":
            break
        # start with echo
        if command.startswith("echo"):
            sys.stdout.write(command[5:] + "\n")
            continue
        # start with type
        if command.startswith("type"):
            # type <command>
            command = command[5:]
            if command in commands:
                sys.stdout.write(f"{command} is a shell builtin\n")
            else:
                sys.stdout.write(f"{command}: not found\n")
            continue


if __name__ == "__main__":
    main()
