
from typing import List

def encode(strs: List[str]) -> str:
    x = ""
    for string in strs:
        if x == "":
            x += string
        else:
            y = "," + string
            x += y
    

    return x


def decode(s: str) -> List[str]:
    s += ","
    result = []
    x = ""
    for char in s:
        if char != ',':
            x += char
        else:
            result.append(x)
            x = ""
    return result

# test case
print(encode(["hello", "world"])) # hello,world
print(decode("hello,world")) # ["hello", "world"]