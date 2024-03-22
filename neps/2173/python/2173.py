def main():
    ini_info = input().split(" ")
    n, m = [int(i) for i in ini_info]

    cities_links = [[] for i in range(n)]
    linked_cities = []

    for i in range(m):

        input_road = input().split(" ")
        city_a, city_b = [int(i) for i in input_road]
        
        if ((city_a == city_b) or (city_a > n) or (city_b > n)): 
            return print("-1")

        if ((city_b not in cities_links[city_a-1]) or
                (city_a not in cities_links[city_b-1])):

            cities_links[city_a-1] += [city_b]
            cities_links[city_b-1] += [city_a]


        if (city_a not in linked_cities):
            linked_cities += [city_a]

        if (city_b not in linked_cities):
            linked_cities += [city_b]

    for i in range(len(cities_links)):

        city_links = cities_links[i]

        if ((len(city_links) < len(linked_cities) - 1) 
                and (len(city_links) > 0)):

            for city in linked_cities:

                if ((city not in city_links) and (city != i+1)):
                    return print(city, i+1)

    return print("-1")

if __name__ == "__main__":
    main()
