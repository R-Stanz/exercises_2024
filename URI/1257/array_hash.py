def hash_a_line(line, string, pos = 0, hash_val = 0):
    if (len(string) > pos):
        hash_val += ord(string[pos]) - ord('A') + line + pos
        return hash_a_line(line, string, pos + 1, hash_val)

    return hash_val


test_cases = int(input())
results = []

for k in range(test_cases):
    numb_of_lines = int(input())
    result = 0

    for l in range(numb_of_lines):
        string = input()
        result += hash_a_line(l, string)

    results += [result]

for i in results:
    print(i)
