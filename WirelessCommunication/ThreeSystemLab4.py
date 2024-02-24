GOS = 0.02  # Probability of blocking
AU = 0.1  # Traffic intensity per user


def Calculation(A, cells):
    # U = Number of users that can be
    # supported per cell
    U = A / AU
    return U * cells

# System A
NumSubsSys_A = Calculation(45, 98)
print(f'The total number of subscriber that can be '
      f'supported by System A is equal to'
      f' {NumSubsSys_A}')
# System B
NumSubsSys_B = Calculation(88, 49)
print(f'The total number of subscriber that can be '
      f'supported by System B is equal to'
      f' {NumSubsSys_B}')
# System C
NumSubsSys_C = Calculation(12, 394)
print(f'The total number of subscriber that can be '
      f'supported by System C is equal to'
      f' {NumSubsSys_C}')

dict = {
    'A': NumSubsSys_A,
    'B': NumSubsSys_B,
    'C': NumSubsSys_C
}


for value in dict:
    print('Since there is two million in the given urban '
          'area and the total number of cellular subscriber'
          f'in system {value} is equal to {dict[value]},'
          f'the percentage market penetration is equal to '
          f'{round((dict[value]/2000000)*100, 2)}%')

print(f'The market penetration of the three system '
      f'combined is equal to {round(((NumSubsSys_A+NumSubsSys_B+NumSubsSys_C)/2000000)*100, 2)}%')