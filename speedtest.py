from pathlib import Path
import os
import re
import subprocess
import time


def parse_response(res):
    ping = re.findall(r'Ping:\s(.*?)\s', res, re.MULTILINE)
    download = re.findall(r'Download:\s(.*?)\s', res, re.MULTILINE)
    upload = re.findall(r'Upload:\s(.*?)\s', res, re.MULTILINE)

    return (
        ping[0].replace(',', '.'),
        download[0].replace(',', '.'),
        upload[0].replace(',', '.')
    )


def write_data(ping, download, upload):
    with open('./data/speedtest.csv', 'a+') as f:

        if os.stat('./data/speedtest.csv').st_size == 0:
            f.write('Date,Time,Ping (ms),Download (Mbit/s),Upload (Mbit/s)\n')

        f.write('{},{},{},{},{}\n'.format(time.strftime('%Y-%m-%d'),
                                          time.strftime('%H:%M:%S'), ping, download, upload))


res = subprocess.Popen('speedtest-cli --simple',
                       shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')

if res:
    print(res)
    (ping, download, upload) = parse_response(res)
else:
    (ping, download, upload) = (0.0, 0.0, 0.0)

write_data(ping, download, upload)
