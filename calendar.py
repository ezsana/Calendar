# main program
import sys
import ui
import storage


def choose():
    inputs = ui.get_inputs(['Please choose between the options: '])
    user_choice = inputs[0]
    if user_choice == 's':
        ui.simple_print('Your choice: s')
        storage.schedule()
    elif user_choice == 'c':
        ui.simple_print('Your choice: c')
        storage.cancel()
    elif user_choice == 'm':
        ui.simple_print('Your schedule for the day: ')
        print(storage.read_from_file())
    elif user_choice == 'q':
        ui.simple_print('Your choice: q')
        sys.exit()
    else:
        raise KeyError('There is no such option.')


def handle_menu():
    options = [ 's: Schedule a new meeting',
                'c: Cancel an existing meeting',
                'm: Your meetings',
                'q: Quit']
    ui.print_menu('Menu', options)


def main():
    while True:
        handle_menu()
        try:
            choose()
        except KeyError as err:
            ui.print_error_message(str(err))


if __name__ == '__main__':
    main()
