#  printing data, asking user for input


def print_menu(title, list_options):
    '''
    ['Schedule a new meeting',
                'Cancel an existing meeting',
                'Quit']
    '''
    print(title)
    for option in list_options:
        print(option)


def get_inputs(list_labels):
    inputs = []
    for l in range(len(list_labels)):
        inputs.append(input(list_labels[l]))
    return inputs


def print_error_message(message):
    print(message)


def simple_print(to_print):
    print(to_print)


def simple_input(question):
    x = input(question)
    return x


def integer_input(question):
    while True:
        x = input(question)
        try:
            x = int(x)
        except ValueError:
            print('Please write a number.')
        else:
            break
    return x