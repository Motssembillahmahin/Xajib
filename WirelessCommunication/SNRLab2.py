import math
n = [4, 3]
R_SI = 15  # R_IR = Ratio of Signal to Interference
io = 6  # io = co_channel
N = 0
for value in n:
    N += value
for i in n:
    Q = math.sqrt(3*N);
    print(f'n : {i}')
    print(f'Frequency Reuse Factor {Q}')
    SI = 10*(math.log(((1/io) * (Q**i)), 10))
    print(f'Signal to interference ratio : {round(SI, 2)} dB')
    if SI < R_SI:
        k = 2; j = 2;
        N = (k**2) + (k*j) + (j**2)
        Q = math.sqrt(3*N)
        print(f'n : {i}')
        print(f'Frequency Reuse Factor {Q} ')
        SI1 = 10*(math.log(((1/io) * (Q**i)), 10));
        print(f'Signal to interference ratio : {round(SI1, 2)} dB')


