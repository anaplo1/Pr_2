with open('/Users/anaplo1/Documents/Python projects/Pr 2/Task 12/test.txt') as file_in:
    text = file_in.read()
    mass = ['0']*len(text)
    newText = ''

    for i in range(len(text)):
        mass[i] = text[i]

    count = 0
    symbolCounter = True

    for i in range(len(mass)):
        if mass[i] == '>' and mass[i+1] == '>' and mass[i+2] == '>':
            symbolCounter = False
            print(symbolCounter)
        if mass[i] == '\"' and symbolCounter:
            count += 1
            if count % 2 == 0:
                mass[i] = '»'
            else:
                mass[i] = '«'

    for i in range(len(mass)):
        newText += mass[i]

    print(mass)

with open("/Users/anaplo1/Documents/Python projects/Pr 2/Task 12/test.txt", "w") as file_out:
    file_out.write(newText)