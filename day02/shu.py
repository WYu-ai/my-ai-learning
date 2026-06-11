import math
def q(a,b,c):
    delta=b**2-4*a*c
    if delta<0:
        return None
    sqrt_delta=math.sqrt(delta)
    x1=(-b+sqrt_delta)/(2*a)
    x2=(-b-sqrt_delta)/(2*a)
    return x1,x2
print('q(2,3,1)=',q(2,3,1))
print('q(1,3,-4)=',q(1,3,-4))
if q(2,3,1)!=(-0.5,-1.0):
    print('测试失败')
elif q(1,3,-4)!=(1.0,-4.0):
    print('测试失败')
else:
    print('测试成功')