dict = {
    '2': {
        '0.01': 0.153,
        '0.005': 0.105,
        '0.002': 0.065,
        '0.001': 0.046
    },
    '4': {
        '0.01': 0.869,
        '0.005': 0.701,
        '0.002': 0.535,
        '0.001': 0.439
    },
    '5': {
        '0.01': 1.36,
        '0.005': 1.13,
        '0.002': 0.900,
        '0.001': 0.762
    },
    '10': {
        '0.01': 4.46,
        '0.005': 3.96,
        '0.002': 3.43,
        '0.001': 3.09
    },
    '20': {
        '0.01': 12.0,
        '0.005': 11.1,
        '0.002': 10.1,
        '0.001': 9.41
    },
    '24': {
        '0.01': 15.3,
        '0.005': 14.2,
        '0.002': 13.0,
        '0.001': 12.2
    },
    '40': {
        '0.01': 29.0,
        '0.005': 27.3,
        '0.002': 25.7,
        '0.001': 24.5
    },
    '70': {
        '0.01': 56.1,
        '0.005': 53.7,
        '0.002': 51.0,
        '0.001': 49.2
    },
    '100': {
        '0.01': 84.1,
        '0.005': 80.9,
        '0.002': 77.4,
        '0.001': 75.2
    }
}
C = input('Enter the trunked Channel : ')

GOS = 0.005
AU = 0.1  # AU = Traffic Intensity offered by each user


def CalculateValue():
    try:
        # U = Total number of user
        # A = Total offer Traffic
        A = dict[C][str(GOS)]
        U = A / AU
        U = 1 if U < 1 else round(U)
        print(f'Total Number of user {U} users')
    except KeyError:
        print('The trunked channel is not in the table')


CalculateValue()
