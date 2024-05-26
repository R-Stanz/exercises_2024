songs_str_ls = input().split(" ")
songs_int_ls = [int(i) for i in songs_str_ls]

set_of_songs = set([i for i in range(4)])

for i in set_of_songs:
    if (i not in songs_int_ls):
        print(i)
        break
