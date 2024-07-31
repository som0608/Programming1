from turtle import *
import random

# Drawing Sudoku squares using turtle.
# /----------------------------------------------------------------------------------------------/
penup()

# Move the pointer to the bottom left of the starting position of the squares.
goto(-200, -200)

pendown()

# Draw the frame of the squares, 450 per side.
for i in range(4):
    pensize(4)
    forward(450)
    left(90)

# Draw inner lines in the squares.

# Draw vertical lines of the internal lines.
for i in range(9):

    # Draw the third lines with a bold line.
    if i % 3 == 2:
        pensize(4)
    
    # Draw another lines.
    else:
        pensize(1)
    if i % 2 == 0:
        forward(450/9)
        left(90)
        forward(450)
        right(90)
    else:
        forward(450/9)
        right(90)
        forward(450)
        left(90)

# Draw horizontal lines of the internal lines.
for i in range(9):

    # Draw the third lines with a bold line.
    if i % 3 == 2:
        pensize(4)

    # Draw another lines.
    else:
        pensize(1)
    if i % 2 == 0:
        right(90)
        forward(450/9)
        right(90)
        forward(450)
    else:
        left(90)
        forward(450/9)
        left(90)
        forward(450)

# /----------------------------------------------------------------------------------------------/

# Create the definition that making a correct answer to a Sudoku.
# Assign each 3 x 3 block as one, and assign a number to each as follows;
#  ______________
# | 1  | 2  | 3  |
# |____|____|____|
# | 4  | 5  | 6  |
# |____|____|____|
# | 7  | 8  | 9  |
# |____|____|____|

# The numbers in the 3x3 squares within each block are written in the list of lists.

count = 0

# Create a dictionary with a list of numbers that can be selected for the square of each block, using the block number as a key.
d_block = {}
for i in range(1,10):
    d_block[i] = [j for j in range(1, 10)]

# First fit the numbers into the squares in blocks 1, 5, and 9 since these blocks do not interfere with each other.
# Argument 'a' is a block number.
def block159(a, count):
    # program pick numbers at random from the list 'f' and then remove the selected numbers from the list.
    # The numbers program pick will be added to the list 'l_'.
    f = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    l_ = []
    count += 1
    for i in range(3):
        l_row = []
        for j in range(3):
            number = random.choice(f)
            f.remove(number)
            l_row.append(number)
        l_.append(l_row)
    return l_


# Second fit the numbers into the squares in blocks 2 and 6. Blocks 2 and 6 do not interfere with each other.
# Each is filled with one block that already has a number filled in horizontally and vertically.
# Therefore get a list of already filled blocks as an argument.
def block26(a, list1, list5, count):
    l_ = []
    l_spare = []
    count += 1
    for i in range(3):
        l_row = []

        # Numbers with same row of blocks 'list1[i]' that are already filled cannot be picked,
        # so they are removed from the list 'd_block[a]' of numbers that can be selected.
        for k in list1[i]:
            flag1 = k in d_block[a]
            if flag1 == True:
                d_block[a].remove(k)
        
        # Numbers with same column of blocks 'list5[k][j]' that are already filled cannot be picked
        # so they are removed from the list 'd_block[a]' of numbers that can be selected.
        for j in range(3):
            for k in range(3):
                flag2 = list5[k][j] in d_block[a]
                if flag2 == True:
                    d_block[a].remove(list5[k][j])

            # If there are no numbers available for selection, start over again.
            if len(d_block[a]) == 0:
                d_block[a] = [i for i in range(1,10)]
                return block26(a, list1, list5, count)
            
            # Select a number at random from a list of possible numbers 'd_block[a].
            number = random.choice(d_block[a])
            l_row.append(number)
            l_spare.append(number)

            # If the numbers that omitted because they are in the same column are not in the same row,
            # they are returned to the possibles number list 'd_block[a]'
            # since they are available for selection when the next square's number in next column will be selected.
            for k in range(3):
                flag2 = True
                for l in list1[i]:
                    flag1 = list5[k][j] in l_spare
                    if list5[k][j] == l:
                        flag2 = False
                        break
                    elif flag1 == True:
                        flag2 = False
                        break
                if flag2 == True:
                    d_block[a].append(list5[k][j])

            # Remove the selected numbers from the possible number list 'd_block[a]'.
            d_block[a].remove(number)

        # The numbers program pick will be added to the list 'l_'.
        l_.append(l_row)

        # If numbers omitted because they are in the same row are available for selection in the next row,
        # add it to the possible number list 'd_block[a]'.
        for k in list1[i]:
            flag1 = True
            if k in l_spare:
                flag1 = False
            if flag1 == True:
                d_block[a].append(k)
    
    return l_


# Third fit the numbers into the squares in blocks 4.
# This block has one vertical block 1 and two horizontal blocks 5&6 that already have numbers filled.
# Therefore get a list of already filled blocks as an argument.
def block4(a, list1, list5, list6, count):
    l_ = []
    l_spare = []
    count += 1

    # If too many recursions are made, start over from blocks 1, 5, and 9 in def make_block().
    if count > 15:
        return False
    
    # Numbers with same row of blocks 'list5[i] and list6[i]' that are already filled cannot be picked,
    # so they are removed from the list 'd_block[a]' of numbers that can be selected.
    for i in range(3):
        l_row = []
        for k in range(3):
            flag1 = list5[i][k] in d_block[a]
            flag2 = list6[i][k] in d_block[a]
            if flag1 == True:
                d_block[a].remove(list5[i][k])
            if flag2 == True:
                d_block[a].remove(list6[i][k])
        
        # Numbers with same column of blocks 'list1[k][j]' that are already filled cannot be picked
        # so they are removed from the list 'd_block[a]' of numbers that can be selected.
        for j in range(3):
            for k in range(3):
                flag3 = list1[k][j] in d_block[a]
                if flag3 == True:
                    d_block[a].remove(list1[k][j])

            # If there are no numbers available for selection, start over again.
            if len(d_block[a]) == 0:
                d_block[a] = [i for i in range(1,10)]
                return block4(a, list1, list5, list6, count)
            
            # Select a number at random from a list of possible numbers 'd_block[a].
            number = random.choice(d_block[a])
            l_row.append(number)
            l_spare.append(number)
        
            # If the numbers that omitted because they are in the same column are not in the same row,
            # they are returned to the possibles number list 'd_block[a]'
            # since they are available for selection when the next square's number in next column will be selected.
            for k in range(3):
                flag6 = True
                for l in range(3):
                    flag5 = list1[k][j] in l_spare
                    if flag5 == True:
                        flag6 = False
                        break
                    elif list1[k][j] == list5[i][l] or list1[k][j] == list6[i][l]:
                        flag6 = False
                        break
                if flag6 == True:
                    d_block[a].append(list1[k][j])

            # Remove the selected numbers from the possible number list 'd_block[a]'.
            d_block[a].remove(number)

        l_.append(l_row)

        # If numbers omitted because they are in the same row are available for selection in the next row,
        # add it to the possible number list 'd_block[a]'.
        for k in list5[i]:
            flag7 = True
            if k in l_spare:
                flag7 = False
            if flag7 == True:
                d_block[a].append(k)
        for k in list6[i]:
            flag8 = True
            if k in l_spare:
                flag8 = False
            if flag8 == True:
                d_block[a].append(k)
    
    return l_


# Fourth fit the numbers into the squares in blocks 8.
# This block has two vertical blocks 2&5 and one horizontal block 9 that already have numbers filled.
# Therefore get a list of already filled blocks as an argument.
def block8(a, list2, list5, list9, count):
    l_ = []
    l_spare = []
    count += 1

    # If too many recursions are made, start over from blocks 1, 5, and 9 in def make_block().
    if count > 15:
        return False
    
    # Numbers with same row of blocks 'list9[i]' that are already filled cannot be picked,
    # so they are removed from the list 'd_block[a]' of numbers that can be selected.
    for i in range(3):
        l_row = []
        for k in list9[i]:
            flag1 = k in d_block[a]
            if flag1 == True:
                d_block[a].remove(k)

        # Numbers with same column of blocks 'list2[k][j] and list5[k][j]' that are already filled cannot be picked
        # so they are removed from the list 'd_block[a]' of numbers that can be selected.
        for j in range(3):
            for k in range(3):
                flag2 = list2[k][j] in d_block[a]
                flag3 = list5[k][j] in d_block[a]
                if flag2 == True:
                    d_block[a].remove(list2[k][j])
                if flag3 == True:
                    d_block[a].remove(list5[k][j])

            # If there are no numbers available for selection, start over again.
            if len(d_block[a]) == 0:
                d_block[a] = [i for i in range(1,10)]
                return block8(a, list2, list5, list9, count)
            
            # Select a number at random from a list of possible numbers 'd_block[a].
            number = random.choice(d_block[a])
            l_row.append(number)
            l_spare.append(number)
        
            # If the numbers that omitted because they are in the same column are not in the same row,
            # they are returned to the possibles number list 'd_block[a]'
            # since they are available for selection when the next square's number in next column will be selected.
            for k in range(3):
                flag1 = list2[k][j] in l_spare
                flag2 = list2[k][j] in list9[i]
                flag3 = list5[k][j] in l_spare
                flag4 = list5[k][j] in list9[i]
                if flag1 == flag2 == False:
                    d_block[a].append(list2[k][j])
                if flag3 == flag4 == False:
                    d_block[a].append(list5[k][j])

            # Remove the selected numbers from the possible number list 'd_block[a]'.
            d_block[a].remove(number)

        l_.append(l_row)

        # If numbers omitted because they are in the same row are available for selection in the next row,
        # add it to the possible number list 'd_block[a]'.
        for k in list9[i]:
            flag1 = True
            if k in l_spare:
                flag1 = False
            if flag1 == True:
                d_block[a].append(k)
    
    return l_


# Fifth fit the numbers into the squares in blocks 3 and 7. Blocks 3 and 7 do not interfere with each other.
# Each is filled with two blocks that already have numbers filled in horizontally and vertically.
# Therefore get a list of already filled blocks as an argument.
def block37(a, list1, list2, list6, list9, count):
    l_ = []
    l_spare = []
    count += 1

    # If too many recursions are made, start over from blocks 1, 5, and 9 in def make_block().
    if count > 20:
        return False
    
    # Numbers with same row of blocks 'list1[i] and list2[i]' that are already filled cannot be picked,
    # so they are removed from the list 'd_block[a]' of numbers that can be selected.
    for i in range(3):
        l_row = []
        for k in list1[i]:
            flag1 = k in d_block[a]
            if flag1 == True:
                d_block[a].remove(k)
        for k in list2[i]:
            flag1 = k in d_block[a]
            if flag1 == True:
                d_block[a].remove(k)

        # Numbers with same column of blocks 'list6[k][j] and list9[k][j]' that are already filled cannot be picked
        # so they are removed from the list 'd_block[a]' of numbers that can be selected.
        for j in range(3):
            for k in range(3):
                flag2 = list6[k][j] in d_block[a]
                flag3 = list9[k][j] in d_block[a]
                if flag2 == True:
                    d_block[a].remove(list6[k][j])
                if flag3 == True:
                    d_block[a].remove(list9[k][j])

            # If there are no numbers available for selection, start over again.
            if len(d_block[a]) == 0:
                d_block[a] = [i for i in range(1,10)]
                return block37(a, list1, list2, list6, list9, count)
            
            # Select a number at random from a list of possible numbers 'd_block[a].
            number = random.choice(d_block[a])
            l_row.append(number)
            l_spare.append(number)

            # If the numbers that omitted because they are in the same column are not in the same row,
            # they are returned to the possibles number list 'd_block[a]'
            # since they are available for selection when the next square's number in next column will be selected.
            for k in range(3):
                flag4 = list6[k][j] in l_spare
                flag5 = list6[k][j] in list1[i]
                flag6 = list6[k][j] in list2[i]
                flag7 = list9[k][j] in l_spare
                flag8 = list9[k][j] in list1[i]
                flag9 = list9[k][j] in list2[i]
                if flag4 == flag5 == flag6 == False:
                    d_block[a].append(list6[k][j])
                if flag7 == flag8 == flag9 == False:
                    d_block[a].append(list9[k][j]) 

            # Remove the selected numbers from the possible number list 'd_block[a]'.
            d_block[a].remove(number)

        l_.append(l_row)

        # If numbers omitted because they are in the same row are available for selection in the next row,
        # add it to the possible number list 'd_block[a]'.
        for k in list1[i]:
            flag1 = True
            if k in l_spare:
                flag1 = False
            if flag1 == True:
                d_block[a].append(k)
        for k in list2[i]:
            flag1 = True
            if k in l_spare:
                flag1 = False
            if flag1 == True:
                d_block[a].append(k)
    
    return l_

# /----------------------------------------------------------------------------------------------/

# Draw numbers in the squares using turtle.
# The position of the block is specified by the arguments a and b.
def write_number(list, a, b):
    d = {}
    for m in range(5):

        # Randomly select squares to display
        k = random.randint(0,8)

        # Ignore if a number is already displayed in that square.
        # If not shown, draw numbers in the squares.
        flag = k in d
        if flag == False:
            d[k] = k
            j = k % 3
            l = k // 3

            # Specify the location of squares.
            goto((-200 + 50*a + 50*j) + 25, (250 - 50*b - 50*l) - 38)
            # Draw a number.
            write(list[l][j], False, "center", ("Sans", 15, "bold"))

# /----------------------------------------------------------------------------------------------/

# Fill the blocks with numbers in the order of block 1, 5, 9, 2, 6, 4, 8, 3 and 7.
def make_block(count):

    l1 = block159(1, count)
    l5 = block159(5, count)
    l9 = block159(9, count)
    l2 = block26(2, l1, l5, count)
    l6 = block26(6, l5, l9, count)

    l4 = block4(4, l1, l5, l6, count)

    # If too many recursions are made, start over the first.
    if l4 == False:
        count = 0
        d_block = {}
        for i in range(1,10):
            d_block[i] = [j for j in range(1, 10)]
        return make_block(count)

    l8 = block8(8, l2, l5, l9, count)

    # If too many recursions are made, start over the first.
    if l8 == False:
        count = 0
        d_block = {}
        for i in range(1,10):
            d_block[i] = [j for j in range(1, 10)]
        return make_block(count)

    l3 = block37(3, l1, l2, l6, l9, count)

    # If too many recursions are made, start over the first.
    if l3 == False:
        count = 0
        d_block = {}
        for i in range(1,10):
            d_block[i] = [j for j in range(1, 10)]
        return make_block(count)

    l7 = block37(7, l8, l9, l1, l4, count)

    # If too many recursions are made, start over the first.
    if l7 == False:
        count = 0
        d_block = {}
        for i in range(1,10):
            d_block[i] = [j for j in range(1, 10)]
        return make_block(count)

    # print('l1 is ', l1)
    # print('l2 is ', l2)
    # print('l3 is ', l3)
    # print('l4 is ', l4)
    # print('l5 is ', l5)
    # print('l6 is ', l6)
    # print('l7 is ', l7)
    # print('l8 is ', l8)
    # print('l9 is ', l9)

    penup()

    # Draw numbers in the squares using turtle.
    write_number(l1, 0, 0)
    write_number(l2, 3, 0)
    write_number(l3, 6, 0)
    write_number(l4, 0, 3)
    write_number(l5, 3, 3)
    write_number(l6, 6, 3)
    write_number(l7, 0, 6)
    write_number(l8, 3, 6)
    write_number(l9, 6, 6)

# /----------------------------------------------------------------------------------------------/

# Implementation
make_block(count)

done()
