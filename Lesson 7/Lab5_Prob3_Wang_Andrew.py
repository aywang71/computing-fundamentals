alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
string = input('Enter a string:').upper()

letters = {}

for i in range(len(string)):
    if string[i] in alphabet:
        letters[string[i]] = string.count(string[i])

print('Dictionary:', letters)
l = input('Choose a letter:').upper()
print('Frequency count of that letter:', letters[l])
del letters[l]

print('Dictionary after that letter removed:', letters)
c = list(letters.keys())
c.sort()
print('Letters sorted:', c)
