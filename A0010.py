import math
a, b, c = map(int, input().split())
print(math.ceil(a / 2) + math.ceil(b / 2) + math.ceil(c / 2))

# tepaga qarab yaxlitlash
# print(math.ceil(4.3)) # 5
# print(math.ceil(4.8)) # 5

# pastga qarab yaxlitlash
# print(math.floor(4.3)) # 4
# print(math.floor(4.8)) # 4