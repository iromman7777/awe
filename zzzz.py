"""
a = int(input())
b = 0
c = 100
d = 0
e = 50
while a!=e:
    b = b +1
    e = (c + d)//2
    if a < e:
        c = e
    if a > e:
        d = e
print("{}번 만에 찾았습니다".format(b))

2차원 리스트
a = [[1,2,3], [4,5,6]]
print(a[1][2])
딕셔너리
a = {'kkk': 170, 'age': 100, 'velue': 200}
print(a['kkk'])
함"""
def add_test(x, y):
    return x + y
print(add_test(1, 3))
