first_line = input().split(" ")
num_of_cities, num_of_stretches, num_visited_cities = [int(i) for i in first_line]

cities_by_time = {}
times = []
for i in range(num_of_stretches):
    stretch_info = input().split(" ")
    city_a, city_b, time = [int(u) for u in stretch_info]

    if (time not in cities_by_time):
        cities_by_time[time] = set()
        times += [time]

    cities_by_time[time].add(city_a)
    cities_by_time[time].add(city_b)


times = sorted(times)
smallest_time = -1
for i in range(len(times)):
    time = times[i]
    for u in range(i):

        prev_time = times[u]
        if (prev_time != time):
            cities_by_time[time] = cities_by_time[time].union(cities_by_time[prev_time])

    if (len(cities_by_time[time]) >= num_visited_cities):
        smallest_time = time
        break

print(smallest_time)
