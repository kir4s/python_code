import math
an = float(input('digite o ângulo que deseja: '))
seno = math.sin(math.radians(an))
print('O ângulo de {} tem o seno de {}'.format(an, seno))
cos = math.cos(math.radians(an))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(an, cos))
tang = math.tan(math.radians(an))
print('O ângul de {} tem a TANGENTE de {:.2f}'.format(an, tang))