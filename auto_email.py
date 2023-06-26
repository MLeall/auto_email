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

print(f'From {checklist_index[0] + 1} to {checklist_index[-1] + 1}, choose values that are \033[31;1mNOT\033[0m okay.\n')
for key, value in d.items():
    print(f'{key+1}: {value}\n')
print('\nExample: 1, 2, 4')

while True:
    values = str(input("> ")).split(", ")
    try:
        int_values = [int(value) - 1 for value in values]
        break
    except ValueError:
        print('\033[31;1mError\033[0m: Only numeric values are expected. Try again.')
        
while True:
    q = input('Just false checkboxes or all checkboxes? (0 or 1)\n> ')
    try:
        q = int(q)
        if not q in [0, 1]:
            print('\033[31;1mError\033[0m: Only `0` or `1` are expected. Try again.')
        else:
            if q == 1:
                is_full = True
                break
            else:
                is_full = False
                break
    except ValueError:
        print('\033[31;1mError\033[0m: Only numeric values are expected. Try again.')

final_email = email_header

if is_full:
    for key, value in d.items():
        if key in int_values:
            final_email += f'[ ] {key + 1}. {d[key]}\n\n'
        else:
            final_email += f'[X] {key + 1}. {d[key]}\n\n'
else:
    for key, value in d.items():
        if key in int_values:
            final_email += f'[ ] {key + 1}. {d[key]}\n\n'
        else:
            pass

if 'email_template.msg' in os.listdir():
    open('email_template.msg', 'w').close()
    to_msg(final_email)
else:
    to_msg(final_email)

print('All done. Check your directory for `email_template.msg`.')