class Driver:
    def __init__(self, name, laps):
        self.name = name
        self.laps = laps
        self.total = sum(laps)

    def __lt__(self, other):
        return self.total < other.total

array = []
n, m = [int(x) for x in input().split()]
for i in range(n):
    name = input()
    time = [int(x) for x in input().split()]
    array.append(Driver(name, time))


print(min(array).name)






