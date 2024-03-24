from core import CMD

class MainCMD(CMD):
    @classmethod
    def execute_command(cls, cmd):
        print(f"Chose inctance: {cmd}")
        print('\n')

        from olivia import OliviaCMD
        from olivia11 import OliviaPython11CMD

        factory = {
            'olivia': OliviaCMD,
            'py11': OliviaPython11CMD
        }

        _cmd = factory[cmd]
        if not cmd:
            return None

        default_data = _cmd.default_data()
        print('default_data', default_data)
        cmdInstance = _cmd(default_data)
        cmdInstance.execute()


if __name__ == "__main__":
    COMMAND_PATH = './'
    oliviaCMD = MainCMD(dict(
        {
            '[olivia]': f"olivia",
            '[py11]': f"py11",
        }
    ))
    oliviaCMD.execute()
