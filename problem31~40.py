# 35 Factory 함수 사용하기
def one(n):
    def two():
        return n*n
    return two

a = one(2)
b = one(3)
c = one(4)

print()