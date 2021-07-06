def solution(people, limit):
    people.sort()
    cnt = 0
    s, e = 0, len(people) - 1
    while s <= e:
        if people[s] + people[e] <= limit:
            s += 1
            e -= 1
            cnt += 1
        else:
            e -= 1
            cnt += 1

    answer = cnt
    return answer