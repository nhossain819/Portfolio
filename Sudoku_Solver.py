"""
DESCRIPTION:
The following program takes in a sudoku board in terms of its rows and returns a completed sudoku puzzle.
"""
#Input the sudoku board here using zeros instead of blanks.
row1 = [0 , 0 , 0 , 2 , 6 , 0 , 7 , 0 , 1]
row2 = [6 , 8 , 0 , 0 , 7 , 0 , 0 , 9 , 0]
row3 = [1 , 9 , 0 , 0 , 0 , 4 , 5 , 0 , 0]
row4 = [8 , 2 , 0 , 1 , 0 , 0 , 0 , 4 , 0]
row5 = [0 , 0 , 4 , 6 , 0 , 2 , 9 , 0 , 0]
row6 = [0 , 5 , 0 , 0 , 0 , 3 , 0 , 2 , 8]
row7 = [0 , 0 , 9 , 3 , 0 , 0 , 0 , 7 , 4]
row8 = [0 , 4 , 0 , 0 , 5 , 0 , 0 , 3 , 6]
row9 = [7 , 0 , 3 , 0 , 1 , 8 , 0 , 0 , 0]


#The function show_board prints the sudoku puzzle.
def show_board():
    print(row1)
    print(row2)
    print(row3)
    print(row4)
    print(row5)
    print(row6)
    print(row7)
    print(row8)
    print(row9)


#sudoku_solver is a function with nested functions that inserts missing values when there is only one possible value per box.
#sudoku_solver is run numerous times until all boxes are filled.
def sudoku_solver(row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9):

    #XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    #ROW, COLUMN, AND SQUARE VARIABLE DECLARATION

    #all_rows is a list of all boxes of all rows.
    all_rows = list(row1 + row2 + row3 + row4 + row5 + row6 + row7 + row8 + row9)


    #The function 'columns' creates a list of lists containing all columns sequentially.
    def columns(all_rows_list , column_number):
        column = []
        column.append(all_rows_list[column_number - 1])
        column.append(all_rows_list[column_number + 9 - 1])
        column.append(all_rows_list[column_number + (9 * 2) - 1])
        column.append(all_rows_list[column_number + (9 * 3) - 1])
        column.append(all_rows_list[column_number + (9 * 4) - 1])
        column.append(all_rows_list[column_number + (9 * 5) - 1])
        column.append(all_rows_list[column_number + (9 * 6) - 1])
        column.append(all_rows_list[column_number + (9 * 7) - 1])
        column.append(all_rows_list[column_number + (9 * 8) - 1])
        return column


    #The variables column1-column9 contain the columns of the board accordingly.
    column1 = columns(all_rows , 1)
    column2 = columns(all_rows , 2)
    column3 = columns(all_rows , 3)
    column4 = columns(all_rows , 4)
    column5 = columns(all_rows , 5)
    column6 = columns(all_rows , 6)
    column7 = columns(all_rows , 7)
    column8 = columns(all_rows , 8)
    column9 = columns(all_rows , 9)


    #The variables square1-square9 contain the three-by-three- squares of the board.

    #Square1: top row, left
    square1 = [row1[0], row1[1], row1[2], row2[0], row2[1], row2[2], row3[0], row3[1], row3[2]]
    #Square2: top row, middle
    square2 = [row1[3], row1[4], row1[5], row2[3], row2[4], row2[5], row3[3], row3[4], row3[5]]
    #Square3: top row, right
    square3 = [row1[6], row1[7], row1[8], row2[6], row2[7], row2[8], row3[6], row3[7], row3[8]]

    #Square4: middle row, left
    square4 = [row4[0], row4[1], row4[2], row5[0], row5[1], row5[2], row6[0], row6[1], row6[2]]
    #Square5: middle row, middle
    square5 = [row4[3], row4[4], row4[5], row5[3], row5[4], row5[5], row6[3], row6[4], row6[5]]
    #Square6: middle row, right
    square6 = [row4[6], row4[7], row4[8], row5[6], row5[7], row5[8], row6[6], row6[7], row6[8]]

    #Square7: bottom row, left
    square7 = [row7[0], row7[1], row7[2], row8[0], row8[1], row8[2], row9[0], row9[1], row9[2]]
    #Square8: bottom row, middle
    square8 = [row7[3], row7[4], row7[5], row8[3], row8[4], row8[5], row9[3], row9[4], row9[5]]
    #Square9: bottom row, right
    square9 = [row7[6], row7[7], row7[8], row8[6], row8[7], row8[8], row9[6], row9[7], row9[8]]


    #XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    #ANALYSIS

    #The function 'possible_values_by_row_column_square' provides all possible values for a single box based on its row, column, and square.
    def possible_values_by_row_column_square(row, column, square):
        row_value_list = []
        for row_element in row:
            if row_element == 0:
                continue
            else:
                row_value_list.append(row_element)
        row_framelist = list(range(1,10))
        row_possible_value_list = []
        for element in row_framelist:
            if element in row_value_list:
                continue
            else:
                row_possible_value_list.append(element)
        column_value_list = []
        for column_element in column:
            if column_element == 0:
                continue
            else:
                column_value_list.append(column_element)
        column_framelist = list(range(1,10))
        column_possible_value_list = []
        for element in column_framelist:
            if element in column_value_list:
                continue
            else:
                column_possible_value_list.append(element)
        square_value_list = []
        for square_element in square:
            if square_element == 0:
                continue
            else:
                square_value_list.append(square_element)
        square_framelist = list(range(1,10))
        square_possible_value_list = []
        for element in square_framelist:
            if element in square_value_list:
                continue
            else:
                square_possible_value_list.append(element)
        final_framelist = list(range(1,10))
        final_possible_value_list = []
        for element in final_framelist:
            if (element in row_possible_value_list) and (element in column_possible_value_list) and (element in square_possible_value_list):
                final_possible_value_list.append(element)
            else:
                continue
        return final_possible_value_list


    #XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    #ROW1 POSSIBLE VALUES
    possible_values_box1 = possible_values_by_row_column_square(row1, column1, square1)
    possible_values_box2 = possible_values_by_row_column_square(row1, column2, square1)
    possible_values_box3 = possible_values_by_row_column_square(row1, column3, square1)
    possible_values_box4 = possible_values_by_row_column_square(row1, column4, square2)
    possible_values_box5 = possible_values_by_row_column_square(row1, column5, square2)
    possible_values_box6 = possible_values_by_row_column_square(row1, column6, square2)
    possible_values_box7 = possible_values_by_row_column_square(row1, column7, square3)
    possible_values_box8 = possible_values_by_row_column_square(row1, column8, square3)
    possible_values_box9 = possible_values_by_row_column_square(row1, column9, square3)

    #ROW2 POSSIBLE VALUES
    possible_values_box10 = possible_values_by_row_column_square(row2, column1, square1)
    possible_values_box11 = possible_values_by_row_column_square(row2, column2, square1)
    possible_values_box12 = possible_values_by_row_column_square(row2, column3, square1)
    possible_values_box13 = possible_values_by_row_column_square(row2, column4, square2)
    possible_values_box14 = possible_values_by_row_column_square(row2, column5, square2)
    possible_values_box15 = possible_values_by_row_column_square(row2, column6, square2)
    possible_values_box16 = possible_values_by_row_column_square(row2, column7, square3)
    possible_values_box17 = possible_values_by_row_column_square(row2, column8, square3)
    possible_values_box18 = possible_values_by_row_column_square(row2, column9, square3)

    #ROW3 POSSIBLE VALUES
    possible_values_box19 = possible_values_by_row_column_square(row3, column1, square1)
    possible_values_box20 = possible_values_by_row_column_square(row3, column2, square1)
    possible_values_box21 = possible_values_by_row_column_square(row3, column3, square1)
    possible_values_box22 = possible_values_by_row_column_square(row3, column4, square2)
    possible_values_box23 = possible_values_by_row_column_square(row3, column5, square2)
    possible_values_box24 = possible_values_by_row_column_square(row3, column6, square2)
    possible_values_box25 = possible_values_by_row_column_square(row3, column7, square3)
    possible_values_box26 = possible_values_by_row_column_square(row3, column8, square3)
    possible_values_box27 = possible_values_by_row_column_square(row3, column9, square3)

    #ROW4 POSSIBLE VALUES
    possible_values_box28 = possible_values_by_row_column_square(row4, column1, square4)
    possible_values_box29 = possible_values_by_row_column_square(row4, column2, square4)
    possible_values_box30 = possible_values_by_row_column_square(row4, column3, square4)
    possible_values_box31 = possible_values_by_row_column_square(row4, column4, square5)
    possible_values_box32 = possible_values_by_row_column_square(row4, column5, square5)
    possible_values_box33 = possible_values_by_row_column_square(row4, column6, square5)
    possible_values_box34 = possible_values_by_row_column_square(row4, column7, square6)
    possible_values_box35 = possible_values_by_row_column_square(row4, column8, square6)
    possible_values_box36 = possible_values_by_row_column_square(row4, column9, square6)

    #ROW5 POSSIBLE VALUES
    possible_values_box37 = possible_values_by_row_column_square(row5, column1, square4)
    possible_values_box38 = possible_values_by_row_column_square(row5, column2, square4)
    possible_values_box39 = possible_values_by_row_column_square(row5, column3, square4)
    possible_values_box40 = possible_values_by_row_column_square(row5, column4, square5)
    possible_values_box41 = possible_values_by_row_column_square(row5, column5, square5)
    possible_values_box42 = possible_values_by_row_column_square(row5, column6, square5)
    possible_values_box43 = possible_values_by_row_column_square(row5, column7, square6)
    possible_values_box44 = possible_values_by_row_column_square(row5, column8, square6)
    possible_values_box45 = possible_values_by_row_column_square(row5, column9, square6)

    #ROW6 POSSIBLE VALUES
    possible_values_box46 = possible_values_by_row_column_square(row6, column1, square4)
    possible_values_box47 = possible_values_by_row_column_square(row6, column2, square4)
    possible_values_box48 = possible_values_by_row_column_square(row6, column3, square4)
    possible_values_box49 = possible_values_by_row_column_square(row6, column4, square5)
    possible_values_box50 = possible_values_by_row_column_square(row6, column5, square5)
    possible_values_box51 = possible_values_by_row_column_square(row6, column6, square5)
    possible_values_box52 = possible_values_by_row_column_square(row6, column7, square6)
    possible_values_box53 = possible_values_by_row_column_square(row6, column8, square6)
    possible_values_box54 = possible_values_by_row_column_square(row6, column9, square6)

    #ROW7 POSSIBLE VALUES
    possible_values_box55 = possible_values_by_row_column_square(row7, column1, square7)
    possible_values_box56 = possible_values_by_row_column_square(row7, column2, square7)
    possible_values_box57 = possible_values_by_row_column_square(row7, column3, square7)
    possible_values_box58 = possible_values_by_row_column_square(row7, column4, square8)
    possible_values_box59 = possible_values_by_row_column_square(row7, column5, square8)
    possible_values_box60 = possible_values_by_row_column_square(row7, column6, square8)
    possible_values_box61 = possible_values_by_row_column_square(row7, column7, square9)
    possible_values_box62 = possible_values_by_row_column_square(row7, column8, square9)
    possible_values_box63 = possible_values_by_row_column_square(row7, column9, square9)

    #ROW8 POSSIBLE VALUES
    possible_values_box64 = possible_values_by_row_column_square(row8, column1, square7)
    possible_values_box65 = possible_values_by_row_column_square(row8, column2, square7)
    possible_values_box66 = possible_values_by_row_column_square(row8, column3, square7)
    possible_values_box67 = possible_values_by_row_column_square(row8, column4, square8)
    possible_values_box68 = possible_values_by_row_column_square(row8, column5, square8)
    possible_values_box69 = possible_values_by_row_column_square(row8, column6, square8)
    possible_values_box70 = possible_values_by_row_column_square(row8, column7, square9)
    possible_values_box71 = possible_values_by_row_column_square(row8, column8, square9)
    possible_values_box72 = possible_values_by_row_column_square(row8, column9, square9)

    #ROW9 POSSIBLE VALUES
    possible_values_box73 = possible_values_by_row_column_square(row9, column1, square7)
    possible_values_box74 = possible_values_by_row_column_square(row9, column2, square7)
    possible_values_box75 = possible_values_by_row_column_square(row9, column3, square7)
    possible_values_box76 = possible_values_by_row_column_square(row9, column4, square8)
    possible_values_box77 = possible_values_by_row_column_square(row9, column5, square8)
    possible_values_box78 = possible_values_by_row_column_square(row9, column6, square8)
    possible_values_box79 = possible_values_by_row_column_square(row9, column7, square9)
    possible_values_box80 = possible_values_by_row_column_square(row9, column8, square9)
    possible_values_box81 = possible_values_by_row_column_square(row9, column9, square9)

    #All possible values per row.
    row1_possible_values = [possible_values_box1, possible_values_box2, possible_values_box3, possible_values_box4, possible_values_box5, possible_values_box6, possible_values_box7, possible_values_box8, possible_values_box9]
    row2_possible_values = [possible_values_box10, possible_values_box11, possible_values_box12, possible_values_box13, possible_values_box14, possible_values_box15, possible_values_box16, possible_values_box17, possible_values_box18]
    row3_possible_values = [possible_values_box19, possible_values_box20, possible_values_box21, possible_values_box22, possible_values_box23, possible_values_box24, possible_values_box25, possible_values_box26, possible_values_box27]
    row4_possible_values = [possible_values_box28, possible_values_box29, possible_values_box30, possible_values_box31, possible_values_box32, possible_values_box33, possible_values_box34, possible_values_box35, possible_values_box36]
    row5_possible_values = [possible_values_box37, possible_values_box38, possible_values_box39, possible_values_box40, possible_values_box41, possible_values_box42, possible_values_box43, possible_values_box44, possible_values_box45]
    row6_possible_values = [possible_values_box46, possible_values_box47, possible_values_box48, possible_values_box49, possible_values_box50, possible_values_box51, possible_values_box52, possible_values_box53, possible_values_box54]
    row7_possible_values = [possible_values_box55, possible_values_box56, possible_values_box57, possible_values_box58, possible_values_box59, possible_values_box60, possible_values_box61, possible_values_box62, possible_values_box63]
    row8_possible_values = [possible_values_box64, possible_values_box65, possible_values_box66, possible_values_box67, possible_values_box68, possible_values_box69, possible_values_box70, possible_values_box71, possible_values_box72 ]
    row9_possible_values = [possible_values_box73, possible_values_box74, possible_values_box75, possible_values_box76, possible_values_box77, possible_values_box78, possible_values_box79, possible_values_box80, possible_values_box81]

    #solve_rows replaces missing values in each row with the correct value.
    def solve_rows():
        framelist = list(range(9))
        for i in framelist:
            if (row1[i] == 0) and (len(row1_possible_values[i]) == 1):
                row1[i] = row1_possible_values[i][0]
            if (row2[i] == 0) and (len(row2_possible_values[i]) == 1):
                row2[i] = row2_possible_values[i][0]
            if (row3[i] == 0) and (len(row3_possible_values[i]) == 1):
                row3[i] = row3_possible_values[i][0]
            if (row4[i] == 0) and (len(row4_possible_values[i]) == 1):
                row4[i] = row4_possible_values[i][0]
            if (row5[i] == 0) and (len(row5_possible_values[i]) == 1):
                row5[i] = row5_possible_values[i][0]
            if (row6[i] == 0) and (len(row6_possible_values[i]) == 1):
                row6[i] = row6_possible_values[i][0]
            if (row7[i] == 0) and (len(row7_possible_values[i]) == 1):
                row7[i] = row7_possible_values[i][0]
            if (row8[i] == 0) and (len(row8_possible_values[i]) == 1):
                row8[i] = row8_possible_values[i][0]
            if (row9[i] == 0) and (len(row9_possible_values[i]) == 1):
                row9[i] = row9_possible_values[i][0]
    solve_rows()
#The end of the function sudoku_solver

#Prints the original board for comparison
print('Original Board')
show_board()
print(' ')

#Run the sudoku_solver function numerous times to ensure all boxes are filled with correct values.
runs_until_solved = list(range(10))
for run in runs_until_solved:
    sudoku_solver(row1, row2, row3, row4, row5, row6, row7, row8, row9)

#Print the final solved sudoku board
print('Solved Board')
show_board()

#The End
