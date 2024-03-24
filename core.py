from abc import abstractmethod
import os

class CMD:
    def __init__(self, cmd_list):
        self.cmd_list = dict({'to cancel': 'echo "cancel"'},**cmd_list) 

    @classmethod
    def execute_command(cls,cmd):
        print(f"Executing base: {cmd}")
        print('\n')
        os.system(cmd)

    def add_options(self, option, cmd):
      self.cmd_list[option] = cmd

    @abstractmethod
    def default_data():
        pass

    def execute(self):
        prompt_message = "Select a command: "
        options = list(self.cmd_list.keys())

        while True:
            for i, option in enumerate(options, start=0):
                print(f"{i} -> {option}")

            try:
                choice = int(input(prompt_message))
                if 0 <= choice <= len(options):
                    option = options[choice]
                    cmd = self.cmd_list.get(option)
                    if cmd:
                        self.execute_command(cmd)
                        break
                    else:
                        print("Command not found.")
                else:
                    print("Invalid choice. Please select a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")