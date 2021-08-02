# 실행시킨 폴더 안에 설치됨.

import subprocess
import os

os.system('cd jupyternootebook')
subprocess.call('git clone https://github.com/nikdubois/vsftpd-2.3.4-infected.git', shell = True)
os.system('sudo apt-get install build-essential')
os.system('cp -f /vsftpd-2.3.4-infected/Makefile Makefile2.txt')
os.system('cd vsftpd-2.3.4-infected')
os.system('make')