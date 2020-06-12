from pathlib import Path
import os
import re
import subprocess
import time


def get_speedtest():
    response = subprocess.Popen('speedtest-cli --simple',
                                shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')

    ping = re.findall(r'Ping:\s(.*?)\s', response, re.MULTILINE)
    download = re.findall(r'Download:\s(.*?)\s', response, re.MULTILINE)
    upload = re.findall(r'Upload:\s(.*?)\s', response, re.MULTILINE)

    return [
        ping[0].replace(',', '.'),
        download[0].replace(',', '.'),
        upload[0].replace(',', '.')
    ]


[ping, download, upload] = get_speedtest()

with open('speedtest.csv', 'a+') as f:

    if os.stat('speedtest.csv').st_size == 0:
        f.write('Date,Time,Ping (ms),Download (Mbit/s),Upload (Mbit/s)\r\n')

    f.write('{},{},{},{},{}\r\n'.format(time.strftime('%m/%d/%y'),
                                        time.strftime('%H:%M'), ping, download, upload))
