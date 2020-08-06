#!/usr/bin/env python3

import os

email = input('Your email: ')

os.system('ssh-keygen -t rsa -C "{}"'.format(email))

print('Done')

