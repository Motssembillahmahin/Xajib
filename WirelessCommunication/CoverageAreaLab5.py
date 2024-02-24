import math
AU = 0.02 # GOS
area = 1300 # coverage area | sq miles
N = 7
radius = 4 # miles
allocated_spectrum = 40000 # MHz
BW = 60 # MHz
A = 0.03 # offered traffic intensity | Earling


print('Answer of question A')
CellArea = 2.5981*(radius)**2
Number_Cell = math.floor(1300/CellArea)
print(f'The area of cell can be shown {CellArea}')
print(f'Total number of cells are {Number_Cell}')
print('\n')
print('Answer of question B')
Number_channel_per_cell = math.floor(allocated_spectrum/(BW*N))
print(f'The total Number of channel per cell {Number_channel_per_cell}')
print('\n')
print('Answer of question C')
intensity_per_cell = 84
print(f'According to the table of erling B chart'
      f' trucked '
      f'channel {Number_channel_per_cell} and '
      f'GOS is {AU} '
      f'traffic {intensity_per_cell}')

print('\n')
print('Answer of question D')
maximum_carried_traffic = Number_Cell * intensity_per_cell
print(f'Maximum carried traffic {maximum_carried_traffic} Erlangs')

print('\n')
print('Answer of question E')
Total_number_user = maximum_carried_traffic/A
print(f'Total Number of user {round(Total_number_user)} users')
print('\n')
print('Answer of question F')
print(f'Number of per channel {math.floor(Total_number_user/Number_channel_per_cell*N)} '
      f'mobiles/channel')
print('\n')
print('Answer of question g')
print(f'The theoretical maximum number of served mobiles'
      f' is the number of available channels in the system'
      f' {Number_Cell*Number_channel_per_cell}')