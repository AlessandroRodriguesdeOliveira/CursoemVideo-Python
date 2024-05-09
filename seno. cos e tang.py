from math import sin, cos, tan, radians

a = float(input('Ângulo:'))
e = radians(a)
b = sin(e)
c = cos(e)
d = tan(e)
print('O ângulo tem seno {:.2f}, cosseno {:.2f} e tangente {:.2f}'.format(b, c, d))