def SciNotation(num, sig):
    x = '%.2e' % num  # <-- Instead of 2, input sig here
    x = x.split('e')
    if (x[1])[0] == "-":
        return x[0] + " x 10^" + x[1].lstrip('0')
    else:
        return x[0] + " x 10^" + (x[1])[1:].lstrip('0')


import math


def math_calculation():
    PT = 50  # Transmitter power | W
    fc = 900  # Carrier Frequency | MHz
    lamda = 1 / 3
    d = 100
    L = 1
    GT = 1  # Gain of transmitter
    GR = 1  # Gain of receiver
    print('Answer of section A of the question')
    PT_dBm = round(10 * math.log((50 * 10 ** 3), 10))
    print(f'Transmitter power in dBm {PT_dBm} dBm')
    print('\n')
    print('Answer of section B of the question')
    PT_dBW = round(10 * math.log(50, 10))
    print(f'Transmitter power in dBm {PT_dBW} dBW')
    FirstValue = (PT * GT * GR * (lamda ** 2))
    secondVale = ((4 * math.pi) ** 2) * (d ** 2) * L
    PR = (FirstValue / secondVale) * 1000  # Received Power | W
    PR_dBm = round(10 * math.log(PR, 10), 2)
    print(f'Received Power {PR_dBm} dB')
    PR_10 = PR_dBm + 20 * math.log((100 / 10000), 10)
    print(f'When receiver power in 10km distance, received power at 10 km distance {round(PR_10, 2)} dB')


math_calculation()
