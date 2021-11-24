from typing import Generator

def Become_easier(value: int, i: int) -> Generator:
    while value > 1:
        while value % i == 0:
            value //= i
            yield i
        i += 1

result = []
for item in Become_easier(15, 2):
    result += str(item)
print(result)







