
class CommandParsingException(Exception):

    def __init__(self, command, message: str = "the command your entered is invalid"):
        self.message = message
        self.command: str = command
        super().__init__(self.message)
