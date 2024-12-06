import sys
import os


def main():
    while True:
        sys.stdout.write("$ ")
        command = input()

        builtin_commands = ["echo", "type", "exit"]
        PATH = os.environ.get("PATH", "").split(":")

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
            if command in builtin_commands:
                sys.stdout.write(f"{command} is a shell builtin\n")
            else:
                result = None
                for dir in PATH:
                    new_var = os.path.join(dir, command)
                    if os.path.exists(new_var):
                        result = new_var
                        break
                if result:
                    sys.stdout.write(f"{command} is {result}\n")
                else:
                    sys.stdout.write(f"{command}: not found\n")
            continue

        sys.stdout.write(f"{command}: command not found\n")


if __name__ == "__main__":
    main()
