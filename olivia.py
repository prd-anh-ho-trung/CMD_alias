from core import CMD

class OliviaCMD(CMD):
    @staticmethod
    def default_data():
        COMMAND_PATH =  '/home/anh/dev/command/resource/olivia/'
        return dict(
            {
                '[olivia]': f"sh {COMMAND_PATH}olivia.sh",
                '[client]': f"sh {COMMAND_PATH}client.sh",
                '[core]': f"sh {COMMAND_PATH}core.sh",
                '[queue]': f"sh {COMMAND_PATH}queue.sh",
                '[proxy]': f"sh {COMMAND_PATH}proxy.sh",
            }
        )
