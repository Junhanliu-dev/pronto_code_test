
from Command import Command
from errors.CommandParsingError import CommandParsingException


class CommandHelper:
    """
    The helper method to transform string of commands to each individual command
    """
    @classmethod
    def transform_command(cls, command: str) -> list[tuple[Command, int]]:
        """

        :param command:
        :return:
        Returns list of commands. Each command consists command enum and steps
        """
        if command.strip() == '':
            raise CommandParsingException(command)

        command_list: list[tuple[Command, int]] = []
        # split command string to each single command and check valid or not
        commands: list[str] = command.split(',')

        for command in commands:
            first_instruction = command[0].strip().upper()

            if not Command.has_value(first_instruction):
                raise CommandParsingException(command, 'Command is invalid, should be one of F,B,R,L')

            command_enum: Command = Command(first_instruction)
            try:
                steps: int = int(command[1:])

                if steps <= 0:
                    raise CommandParsingException(command, "steps should be larger than 0")

                full_instruction = (command_enum, steps)
                command_list.append(full_instruction)

            except ValueError as e:
                raise CommandParsingException(command, str(e))
            except CommandParsingException as e:
                raise e
            except Exception as e:
                print(e)

        return command_list


