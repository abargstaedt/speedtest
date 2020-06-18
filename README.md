This script produces a `./data/speedtest.csv` file with a line of *speedtest* results added for each invokation like this:

```
Date,Time,Ping (ms),Download (Mbit/s),Upload (Mbit/s)
2020-06-12,22:32:00,33.721,96.45,7.29
2020-06-12,22:35:21,34.773,153.01,7.17
2020-06-13,00:06:33,35.099,75.69,7.19
```

Load the image from *Docker Hub* and run the container providing your [timezone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones):

```
docker run -e TZ=Europe/Berlin -v ${PWD}/data:/data --name speedtest --rm abargstaedt/speedtest
```
