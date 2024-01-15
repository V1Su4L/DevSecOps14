import os
import datetime

# path = os.getcwd()
#
# os.system('mkdir hodi && cd hodi && date  > hello.txt') # we can run all terminal ncommands in python

url = 'https://github.com/hothaifa96/DevSecOps14'

folder_name = str(datetime.datetime.now().date())  # date
print(folder_name)

commands = [f'git clone {url}',
            f'mv {url[url.rfind("/") + 1:]} {folder_name}']

for command in commands:
    os.system(command)
