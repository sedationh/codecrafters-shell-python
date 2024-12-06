import subprocess
import sys
import shutil


def main():
    while True:
        sys.stdout.write("$ ")
        command = input()

        builtin_commands = ["echo", "type", "exit"]

        if command == "exit 0":
            break
        # start with echo
        if command.startswith("echo"):
            sys.stdout.write(command[5:] + "\n")
            continue
        # start with type
        if command.startswith("type"):
            # type <command>
            sub_command = command[5:]
            if sub_command in builtin_commands:
                sys.stdout.write(f"{sub_command} is a shell builtin\n")
            else:
                result = shutil.which(sub_command)
                if result:
                    sys.stdout.write(f"{sub_command} is {result}\n")
                else:
                    sys.stdout.write(f"{sub_command}: not found\n")
            continue
        if command.split() and shutil.which(command.split()[0]):
            # Execute the command with arguments
            args = command.split()
            result = subprocess.run(args)
            continue

        sys.stdout.write(f"{command}: command not found\n")


if __name__ == "__main__":
    main()
