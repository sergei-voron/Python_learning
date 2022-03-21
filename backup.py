#!/usr/bin/env python3

import os
import sys
import time

# print(sys.argv())

"""
1. The files and directories to be backed up are specified in a list.
Example on Windows:
source = ['"C:\\My Documents"']
Example on Mac OS X and Linux:
"""
# source = [input('Please enter the source directory path: ')]
source = ['./backup']

# print(source)

"""
Notice we have to use double quotes inside a string for names with spaces in it.  We could have also used
a raw string by writing [r'C:\My Documents'].

2. The backup must be stored in a main backup directory
Example on Windows:
target_dir = 'E:\\Backup'
Example on Mac OS X and Linux:
"""

# target_dir = input('Please enter the target directory path: ')
target_dir = './backup_new'

# print(target_dir)

# Remember to change this to which folder you will be using

# Create target directory if it is not present
if not os.path.exists(target_dir):
    os.mkdir(target_dir)  # make directory

"""
3. The files are backed up into a zip file.
Note to Windows Users

Instead of double backslash escape sequences, you can also use raw strings. For example, use 'C:\\Documents' or 
r'C:\Documents'. However, do not use 'C:\Documents' since you end up using an unknown escape sequence \D.
"""

# print(target)

# 4. The current day is the name of the subdirectory in the main directory.
today = f"{target_dir}{os.sep}{time.strftime('%Y.%m.%d')}"
# The current time is the name of the zip archive.
now = time.strftime('%H%M%S')

# The name of the zip file
target = f"{today}{os.sep}{now}.zip"

# Take a comment from the user to create the name of the zip file
comment = input('Enter a comment --> ')
# Check if a comment was entered
if len(comment) == 0:
    target = f"{today}{os.sep}{now}.zip"
else:
    target = f"{today}{os.sep}{now}_{comment.replace(' ', '_')}.zip"

# Create the subdirectory if it isn't already there
if not os.path.exists(today):
    os.mkdir(today)
    print(f'Successfully created directory {today}')


def cmd_args():
    args = ""
    for arg in sys.argv[1:]:
        args = f"{args} {arg}"
    return args


# 5. We use the zip command to put the files in a zip archive
zip_command = f"zip -r {target} {' '.join(source)} {cmd_args()}"
# Run the backup
print(f'Zip command is: {zip_command}')
print('Running:')

if os.system(zip_command) == 0:
    print(f'Successful backup to target')
else:
    print('Backup FAILED')
