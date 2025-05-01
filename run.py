import json


def check_capacity(max_capacity: int, guests: list) -> bool:
    timeline = []

    for guest in guests:
        check_in = guest["check-in"]
        check_out = guest["check-out"]
        timeline.append((check_in, 1))
        timeline.append((check_out, -1))

    timeline.sort(key=lambda x:(x[0], x[1]))

    guest_in = 0
    for i, j in timeline:
        guest_in += j
        if guest_in > max_capacity:
            return False
    return True


if __name__ == "__main__":
    max_capacity = int(input())
    n = int(input())


    guests = []
    for _ in range(n):
        guest_json = input()
        guest_data = json.loads(guest_json)
        guests.append(guest_data)


    result = check_capacity(max_capacity, guests)
    print(result)
