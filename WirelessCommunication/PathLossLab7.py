
import math

# Given values
hre = 2  # Height of the receiving antenna (meters)
hte = 100  # Height of the transmitting antenna (meters)
fc = 900  # Frequency (MHz)
d = 4  # Distance between antennas (kilometers)


def AnothlerSln():
    # Calculate a_hre
    a_hre = 3.2 * (math.log10(11.75 * hre)) ** 2 - 4.97
    # Calculate path loss
    Lp = 69.55 + 26.16 * math.log10(fc) - 13.82 * math.log10(hte) - a_hre + (
            44.9 - 6.55 * math.log10(hte)) * math.log10(d)

    print('Path loss: %.2f' % Lp)


def MineSln():
    P_4 = 10 * math.log((((3e+8) ** 2) / ((((4 * math.pi) ** 2) * (4000 ** 2) * ((9e+8) ** 2)))), 10)
    P_100 = 20 * math.log((100 / 4000), 10)
    P_2 = 20 * math.log((2 / 4000), 10)
    Total = P_4 + P_100 + P_2
    print(f'The path loss of the cellular system is {round(Total, 2)} dB')


MineSln()
