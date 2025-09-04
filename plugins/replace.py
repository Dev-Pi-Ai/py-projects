from os import sys

try:
    with open(sys.argv[1], 'r') as og, open(sys.argv[2], 'w') as edit:
        og = og.readlines()
        for line in og:
            line = line.split(" ")
            line_print = ""
            for i in line:
                if i == sys.argv[3]:
                    i = sys.argv[4]
                elif sys.argv[3] in i:
                    i = list(i)
                    for j in range(len(i)):
                        if i[j] == sys.argv[3]:
                            i[j] = sys.argv[4]
                    i = ''.join(i)

                edit.write(i + ' ')
except FileNotFoundError:
    print(f'Please ensure that "{sys.argv[1]} exists and is in the current directory.')
except IndexError:
    print('Please use provide an input file, an output file, the character to replace, and the character to replace it with.')