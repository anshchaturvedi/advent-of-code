def solution():
    times = [62737565]
    distances = [644102312401023]

    ans = 0

    for time, record_distance in zip(times, distances):
        num_ways = 0
        for i in range(time):
            distance_travelled = i * (time - i)
            if distance_travelled > record_distance:
                num_ways += 1

        if ans == 0:
            ans = num_ways
        else:
            ans *= num_ways

    return ans


if __name__ == "__main__":
    print(solution())
