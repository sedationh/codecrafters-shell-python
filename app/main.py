import subprocess
import sys
import shutil
import os


def main():
    while True:
        sys.stdout.write("$ ")
        command = input()

        builtin_commands = ["echo", "type", "exit", "pwd"]

        match command.split():
            case ["exit", "0"]:
                break
            case ["echo", *args]:
                sys.stdout.write(" ".join(args) + "\n")
            case ["type", sub_command]:
                if sub_command in builtin_commands:
                    sys.stdout.write(f"{sub_command} is a shell builtin\n")
                else:
                    result = shutil.which(sub_command)
                    if result:
                        sys.stdout.write(f"{sub_command} is {result}\n")
                    else:
                        sys.stdout.write(f"{sub_command}: not found\n")
            case ["pwd"]:
                sys.stdout.write(f"{os.getcwd()}\n")
            case [sub_command, *args] if shutil.which(sub_command):
                # Execute the command with arguments
                subprocess.run([sub_command, *args])
            case _:
                sys.stdout.write(f"{command}: command not found\n")


if __name__ == "__main__":
    main()
