This script produces a `./data/speedtest.csv` file with a line of *speedtest* results added for each invokation like this:

```
Date	Time	Ping (ms)	Download (Mbit/s)	Upload (Mbit/s)
2020-06-13	12:30:25	39.344	62.84	5.01
2020-06-13	12:45:25	37.155	71.26	7.29
2020-06-13	13:00:26	36.38	69.76	6.67
2020-06-13	13:15:25	35.591	84.68	7.18
2020-06-13	13:30:25	34.531	79.09	7.08
2020-06-13	13:45:25	36.315	111.46	7.32
2020-06-13	14:00:25	35.602	66.97	7.16
2020-06-13	14:15:25	35.74	64.98	7.12
```

Load the image from *Docker Hub* and run the container providing your [timezone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones):

```
docker run -e TZ=Europe/Berlin -v ${PWD}/data:/data --rm abargstaedt/speedtest
```
