def max_time(time_periods):
    return (max[y for (x, y) in time_periods])

def min_time(time_periods):
    return (min[x for (x, y) in time_periods])

def index_val(time_periods):
    for (x, y) in time periods:
        if y == max_time(timeperiods):
            return(time_periods.index((x, y)))

def Can_he_take_all_the_pictures(time_Periods, t, T):
    z = max_time(time_periods)
    u = index_val(time_periods)
    time_periods.pop(u)
    q = min_time(time_periods)
    if (all([(b - a) >= t for (a, b) in time_periods])):
        if z - q >= T:
            return ("Yes")
        else:
            return ("No")
    else:
         return ("No")

if __name__ == "__main__":
    n, t = map(int,input().split())
    T = n * t
    time_periods = []
    for i in range(n):
        a, b = map(int,input().split())
        time_periods.append((a, b))

    print(Can_he_take_all_the_pictures(time_periods, t, T)

