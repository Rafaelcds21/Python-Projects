from random import sample

list = []

num_min = int(input('Enter the lowest number from the list: '))
num_max = int(input('Enter the highest number from the list: '))

for i in range(num_min, num_max+1):
    list.append(i)

qtde_sample = int(input('Enter the number of numbers to be drawn:'))

numbers_drawn = sample(list, qtde_sample)

print(numbers_drawn)
