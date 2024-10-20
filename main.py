import random

size = 11

def create_matrix(size):
    
    my_matrix = []
    
    # create a matrix with 11 rows
    for i in range(size):
        
        # add new row
        my_matrix.append([])
        
        # in this row add 11 elements
        for j in range(size):
            
            found_element = False
            
            # we try to find an element that is not on our left or above
            while not found_element:
                element = random.randint(1,4)
                
                # if we are not on the first column
                if j >= 1:
                    if element != my_matrix[i][j-1]:
                        # if we are not on the first row
                        if i >= 1:
                            if element != my_matrix[i-1][j]:
                                my_matrix[i].append(element)
                                found_element = True
                
                # if we are on the first column, compare only with the element above
                if j == 0 and i >= 1: 
                    if element != my_matrix[i-1][j]:
                                my_matrix[i].append(element)
                                found_element = True
                
                # if we are on the first row, compare only with the element on the left
                if i == 0 and j >= 1:
                    if element != my_matrix[i][j-1]:
                                my_matrix[i].append(element)
                                found_element = True
                
                # if we are on the first position in matrix, just add a random element
                if i==0 and j==0:
                    my_matrix[i].append(element)
                    found_element = True
    
    # print the matrix content in console
    for i in range(size):
        for j in range(size):
            print(my_matrix[i][j], end="  ")
        print("\n")

    
create_matrix(size)