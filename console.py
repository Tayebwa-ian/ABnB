import cmd
"""The console Module
Description:
    This is provides shell like functionalities to run commands in this project
    More explicitly it provides a prompt to run basic commands
    commands that interact with the overall project
"""


class HBNBCommand(cmd.Cmd):
    """Customised AirBnB console (command prompt)
    Description:
        Functions under this class run several commands input via the prompt
    """
    prompt = "(hbnb) "

    def do_prompt(self, value) -> None:
        """Change the default prompt to a new provided value
        Args:
            Value: new prompt string to use
        Return: None
        """
        self.prompt = value + ": "

    def help_prompt(self) -> None:
        """Text to display when help command in run with prompt cmd"""
        print("Change the default prompt to a new provided value\n")

    def do_quit(self, value) -> bool:
        """Exits the program"""
        return True

    def help_quit(self) -> None:
        """Text to display when help command in run with quit cmd"""
        print("Quit command to exit the program\n")

    def do_EOF(self, value) -> bool:
        """Exits the program"""
        return True

    def help_EOF(self) -> None:
        """Text to display when help command in run with EOF cmd"""
        print("EOF command to exit the program\n")

    def emptyline(self) -> None:
        """Execute nothing on pressing an empty line + ENTER"""
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
