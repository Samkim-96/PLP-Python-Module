import os

file =open('samkim.txt', 'r')
print(file.read())


# Write an file
newFile =open('kimani.txt', 'w')
newFile.write('This is my second name')

# os.remove('samkim.txt')

# error handling exception
try:
    file = open('samuel.txt', 'r')
    print(file.read())
except FileNotFoundError:
    print('Ooops! the file doesnt exist')
finally:
    print('Try another file name')