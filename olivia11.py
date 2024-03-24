from core import CMD

class OliviaPython11CMD(CMD):
    @staticmethod
    def default_data():
        COMMAND_PATH =  '/home/anh/dev/command/resource/olivia/'
        return dict(
            {
                '[olivia11]': f"sh {COMMAND_PATH}olivia11.sh",
                '[core]11': f"sh {COMMAND_PATH}core11.sh",
            }
        )
