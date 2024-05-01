input()
queue = input().split(" ")
queue = [int(i) for i in queue]

input()
exited = input().split(" ")
exited = set([int(i) for i in exited])

answer = ""
first_is_printed = False
for identifier in queue:
    if (identifier not in exited):

        if (first_is_printed):
            answer += " " 
        else:
            first_is_printed = not first_is_printed

        answer += str(identifier)

print(answer)
