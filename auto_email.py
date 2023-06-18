import os
from time import sleep
from message_creator import to_msg

email_header = 'Hello,\nI have reviewed your work and here are the final checklist items:\n\n'

checklist = [
    "Double-check work for any typos",
    "Tested the code on multiple devices",
    "Documented your code for future reference",
    "Discussed your changes with community for feedback"
    ]

checklist_index = [i for i in range(len(checklist))]
d = {key: value for key, value in zip(checklist_index, checklist)}

print(f'From {checklist_index[0]} to {checklist_index[-1]}, choose values that are \033[31;1mNOT\033[0m okay.\n')
for key, value in d.items():
    print(f'{key}: {value}\n')
print('\nExample: 0, 2, 3')

values = str(input("> ")).split(", ")

try:
    int_values = [int(value) for value in values]
except ValueError as err:
    print(f'\033[31;1mError\033[0m: Only numeric values are expected\nShutting down . . .')
    sleep(1)
    quit()

final_email = email_header
for key, value in d.items():
    if key in int_values:
        final_email += f'[ ] {key + 1}. {d[key]}\n\n'
    else:
        final_email += f'[X] {key + 1}. {d[key]}\n\n'

if 'email_template.msg' in os.listdir():
    open('email_template.msg', 'w').close()
    to_msg(final_email)
else:
    to_msg(final_email)
