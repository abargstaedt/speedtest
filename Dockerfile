FROM python:3
RUN pip install speedtest-cli
ADD ./speedtest.py /
CMD [ "python", "./speedtest.py" ]
