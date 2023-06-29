a = int(input())
b = int(input())
c = int(input())
way1 = a + b + c
way2 = 2 * (a + b)
way3 = 2 * (a + c)
way4 = 2 * (b + c)
print(min(way1, way2, way3, way4))
