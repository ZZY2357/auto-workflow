#!/usr/bin/env python3

import os

name = input('Your name: ')
email = input('Your email: ')
isColorful = input('Do you want to enable the git color? [Y/n] ')

os.system('git config --global user.name "{}"'.format(name))
os.system('git config --global user.email "{}"'.format(email))

if isColorful != 'n':
    os.system('git config --global color.ui true')
else:
    os.system('git config --global color.ui false')

print('Done')

