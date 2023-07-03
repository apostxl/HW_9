from commands import COMMANDS, good_bye, no_command


def command_handler(text: str):
    for command, kword in COMMANDS.items():
        if text.startswith(kword):
            return command, text.replace(kword, '').strip()
    return no_command, None


def main():
    print("Type 'hello' for help.\n")
    while True:
        user_input = input('Enter your command: ').lower()
        command, data = command_handler(user_input)
        print(command(data))
        if command == good_bye:
            break


if __name__ == '__main__':
    main()

dct_contacts = dict()


def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except KeyError:
            return '\nEnter user name please.\n'
        except ValueError:
            return '\nSecond argument must be a number.\n'
        except IndexError:
            return '\nGive me name and phone please.\n'
    return inner


def from_txt_to_dict(file, mode):
    with open(file, mode) as fh:
        for line in fh:
            text = line.strip().split(':')
            dct_contacts[text[0]] = text[1]

    return dct_contacts


def hello(*args):
    with open('hello.txt') as fh:
        return fh.read()


@input_error
def add(*args):
    list_of_param = args[0].split()
    name = list_of_param[0].capitalize()
    number = int(list_of_param[1])

    with open('contacts.txt', 'a') as fh:
        fh.write(f'{name}:{number}\n')
    return '\nThe contact was save.\n'


@input_error
def change(*args):
    dct = from_txt_to_dict('contacts.txt', 'r')
    list_of_param = args[0].split()
    name = list_of_param[0].capitalize()
    number = int(list_of_param[1])
    dct[name] = int(number)
    with open('contacts.txt', 'w') as fh:
        fh.write('')
        for key, value in dct.items():
            fh.write(f'{key}:{value}\n')

    return '\nThe number was changed.\n'


@input_error
def phone(*args):
    dct = from_txt_to_dict('contacts.txt', 'r')
    list_of_param = args[0].split()
    name = list_of_param[0].capitalize()
    phone = dct[name]

    return f'\n{phone}\n'


def show_all(*args):
    with open('contacts.txt') as fh:
        text = '\n'
        for line in fh.readlines():
            text += line
        if len(text) < 2:
            return '\nThe phone book is empty.\n'

    return text


def good_bye(*args):
    return '\nGood bye!\n'


def clear(*args):
    confirmation = input(
        '\nAre you sure you want to clear your phone book? If yes type "clear": ').lower()

    if confirmation == 'clear':
        with open('contacts.txt', 'w') as fh:
            fh.write('')
        return '\nThe phone book has been cleared.\n'

    return '\nThe phone book has not been cleared.\n'


def no_command(*args):
    return '\nUnknown command! Try again.\n'


COMMANDS = {
    hello: 'hello',
    good_bye: 'exit',
    add: 'add',
    change: 'change',
    clear: 'clear',
    phone: 'phone',
    show_all: 'show all',
}
