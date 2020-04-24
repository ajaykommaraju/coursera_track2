#synatx for opening a file
'''file = open('c:/Users/kkumar19/Documents/coursera_python_track2/network.py')
print(file.read())
file.close()'''
#syntax for opening a file with section
'''with open('c:/Users/kkumar19/Documents/coursera_python_track2/network.py') as file:
    for line in file:
        print(line.upper().strip())'''
# code sort the line
'''file = open('c:/Users/kkumar19/Documents/coursera_python_track2/network.py')
lines = file.readlines()
lines.sort()
print(lines)'''

#code to open a file in write mode (w) mode ..if you open in w mode the content will lost.
'''with open('c:/Users/kkumar19/Documents/coursera_python_track2/test.txt','w') as file:
    file.write("It was a dark and a stromy night")'''

#code to open a file in appned mode (a) mode ..if you opne in a mode conten will append at last
with open('c:/Users/kkumar19/Documents/coursera_python_track2/test.txt','a') as file:
    file.write("It was a dark and stromy night")
