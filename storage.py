#  saving and loading files (after you implement it)
import ui
import calendar


def schedule():
    ui.simple_print('Schedule a new meeting.')
    labels = ['Enter meeting title: ', 'Enter start time: ', 'Enter duration in hours (1 or 2): ']
    add_meeting = []
    for l in range(len(labels)):
        if l == 0:
            answer = ui.simple_input(labels[l])
        else:
            answer = str(ui.integer_input(labels[l]))
        add_meeting.append(answer)
    add_meeting[-1] = add_meeting[-1] + ' hour(s)'
    meeting = ' / '.join(add_meeting)
    with open('/home/zsana/python/Calendar/store_datas.csv', "a") as file:
        file.write(meeting + '\n')
    ui.simple_print('Meeting added.')
    '''

def cancel():
    ui.simple_print('Cancel an existing meeting.')

    Enter the start time: 13
    ERROR: There is no meeting starting at that time!
    Enter the start time: 12
    Meeting cancelled.
    '''


def read_from_file():
    with open('/home/zsana/python/Calendar/store_datas.csv', 'r') as f:
        lines = f.read()
    return lines