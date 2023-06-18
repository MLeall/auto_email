# Checklist e-mail generator

This script generates an email based on your predefined checklist. The email is saved as an Outlook MSG file.

### Prerequisites

You just need to have Python 3.x installed.

## Usage

The idea of this code is to automate a checklist that is extensively used. You need to populate the `checklist` variable in `auto_email.py` once and then you are good to go. Be sure to use your own `email_header` inside `auto_email.py` as well. There is already a GPT generated checklist sample for testing. Here is the final text output:

```
Hello,
I have reviewed your work and here are the final checklist items:

[X] 1. Double-check work for any typos

[ ] 2. Tested the code on multiple devices

[X] 3. Documented your code for future reference

[X] 4. Discussed your changes with community for feedback
```
The output will be a outlook email file named `email_template.msg`. There is no need to delete this file after use, it'll be replaced by the next one.

Follow the `instructions.md` to use. Pretty simple straightfoward.

### Contribuition

Feel free to contribuite with your ideas. This is the first release, I have plans to create an script to read the checklist from some file and automate the process of populating the `checklist` variable.