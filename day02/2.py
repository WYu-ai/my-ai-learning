def my_abs(x):
    if not isinstance(x,(int,float)):
       raise TypeError('输入错误')
    if x>=0:
       return x
    else:
       return -x
print(my_abs('99'))