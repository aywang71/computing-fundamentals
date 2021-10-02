numbers = [int(input('Enter an integer from 1 to 10:'))]

while input('Enter another integer?[y/n]') == 'y':
    numbers.append(int(input('Enter an integer from 1 to 10:')))

print('Number list:', numbers)

print('Largest element:', max(numbers))
print('Smallest element:', min(numbers))
print('Sum of all elements:', sum(numbers))
print('Length of list:', len(numbers))
print('Average:', sum(numbers)/len(numbers))

numbers.reverse()
print('List reversed:', numbers)

numbers.insert(0, numbers[-1])
numbers.pop(-1)
print('Last element moved to front:', numbers)
