import time

time_split = time.ctime().split(' ')

times = time_split[1] + '-' +time_split[3] + '-' +time_split[4]


print(times)