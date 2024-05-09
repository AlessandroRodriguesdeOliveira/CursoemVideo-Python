from random import randint
a = randint(0, 5)
from time import sleep
print(('\033[0;33m-=-\033[m')*20)
print('\033[0;34mVou pensar em um  número entre 0 e 5. Tente adivinhar...\033[m')
print(('\033[0;33m-=-\033[m')*20)
b = str(input('Em que número eu pensei?'))
print('\033[0;35mPROCESSANDO...\033[m')
sleep(2.5)
if a == b:
    print('\033[1;30mUAU, você acertou!\033[m')
else:
    print('\033[0;31mHAHAHAH, você errou!\033[m')
