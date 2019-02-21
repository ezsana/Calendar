# main program
import sys
import ui
import storage


def choose():
    inputs = ui.get_inputs(['Please choose between the options: '])
    user_choice = inputs[0]
    if user_choice == 's':
        ui.simple_print('Schedule a new meeting.')
        storage.schedule()
    elif user_choice == 'c':
        storage.cancel()
    elif user_choice == 'm':
        ui.simple_print('Your schedule for the day:\n')
        storage.meetings_arranged_by_time()
    elif user_choice == 'e':
        ui.simple_print('Your schedule for the day: ')
        ui.simple_print(storage.read_from_file())
        storage.edit_meeting()
    elif user_choice == 't':
        ui.simple_print(storage.total_meeting_duration())
    elif user_choice == 'q':
        ui.simple_print('Your choice: q')
        sys.exit()
    else:
        raise KeyError('There is no such option.')


def handle_menu():
    options = [ 's: Schedule a new meeting',
                'c: Cancel an existing meeting',
                'm: Your meetings',
                'e: Edit a meeting',
                't: Total meeting duration',
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
