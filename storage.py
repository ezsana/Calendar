#  saving and loading files (after you implement it)
import ui
import calendar


def schedule():
    lines = read_from_file().split('\n')
    new_lines = []
    for i in lines[:-1]:
        x = i.split(' / ')
        new_lines.append(x)
    meeting_times = [int(n[1]) for n in new_lines]
    print(meeting_times)
    labels = ['Enter meeting title: ', 'Enter start time: ', 'Enter duration in hours (1 or 2): ']
    add_meeting = []
    for l in range(len(labels)):
        if l == 0:
            answer = ui.simple_input(labels[l])
        else:
            if l == 1:
                while True:
                    answer = ui.integer_input(labels[l])
                    if answer not in range(8, 18):
                        ui.simple_print('Between 8-17 hours please.')
                        continue
                    elif answer in meeting_times:
                        ui.simple_print('You have an existing meeting at this time.')
                        continue
                    else:
                        break
            if l == 2:
                while True:
                    answer = ui.integer_input(labels[l])
                    if answer not in range(1, 3):
                        ui.simple_print('1 or 2 hours meeting?')
                        continue
                    else:
                        break
            answer = str(answer)
        add_meeting.append(answer)
    add_meeting[-1] = add_meeting[-1] + ' hour(s)'
    meeting = ' / '.join(add_meeting)
    with open('/home/zsana/python/Calendar/store_datas.csv', "a") as file:
        file.write(meeting + '\n')
    ui.simple_print('Meeting added.')


def cancel():
    ui.simple_print('Cancel an existing meeting.')
    lines = read_from_file().split('\n')
    new_lines = []
    for i in lines[:-1]:
        x = i.split(' / ')
        new_lines.append(x)
    meeting_times = []
    for n in new_lines:
        meeting_times.append(n[1])
    while True:
        meeting_to_cancel = ui.integer_input('Enter the start time: ')
        if str(meeting_to_cancel) not in meeting_times:
            ui.simple_print('There\'s no meeting at that time.')
            continue
        else:
            for n in new_lines:
                if str(meeting_to_cancel) == n[1]:
                    new_lines.remove(n)
            break
    write_to_file(new_lines)
    ui.simple_print('Meeting cancelled.')


def read_from_file():
    with open('/home/zsana/python/Calendar/store_datas.csv', 'r') as f:
        lines = f.read()
    return lines


def write_to_file(lines):
    with open('/home/zsana/python/Calendar/store_datas.csv', 'w') as f:
        for l in lines:
            row = ' / '.join(l)
            f.write(row + '\n')


def edit_meeting():
    lines = read_from_file().split('\n')
    new_lines = []
    for i in lines[:-1]:
        x = i.split(' / ')
        new_lines.append(x)
    titles = []
    for n in new_lines:
        titles.append(n[0])
    while True:
        edit_meeting = ui.simple_input('Which meeting would you like to edit? ')
        if edit_meeting not in titles:
            ui.simple_print('There is no such meeting.')
            continue
        else:
            for meeting in new_lines:
                if edit_meeting == meeting[0]:
                    new_lines.remove(meeting)
            break
    write_to_file(new_lines)
    schedule()


def total_meeting_duration():
    lines = read_from_file().split('\n')
    new_lines = []
    for i in lines[:-1]:
        x = i.split(' / ')
        new_lines.append(x)
    times = [t[-1] for t in new_lines]
    time = [int(time[0]) for time in times]
    total_time = sum(time)
    return (str(total_time) + ' hour(s)')


def meetings_arranged_by_time():
    lines = read_from_file().split('\n')
    new_lines = []
    for i in lines[:-1]:
        x = i.split(' / ')
        new_lines.append(x)
    N = len(new_lines)
    for i in range(N):
        for j in range(N-1):
                if int(new_lines[j][1]) > int(new_lines[j+1][1]):
                    temp = new_lines[j+1]
                    new_lines[j+1] = new_lines[j]
                    new_lines[j] = temp
    for l in new_lines:
        ui.simple_print(' / '.join(l) + '\n')