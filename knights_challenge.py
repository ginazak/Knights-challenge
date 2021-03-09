def knight(start, end, moves):
    """ A knight is able to move to all squares of a chessboard atleast once -
    This function checks whether the knight is able to reach the given end-position from a given start-position in at most the given number of moves.
    The 'start' and 'end' inputs are alphanumerics. Moves is a positive integer.
    The output is a bool.

    /* Code to find minimum steps to reach a position
    * taken from geeksforgeeks post
    * Accessed 06-10-21
    * https://www.geeksforgeeks.org/minimum-steps-reach-target-knight/
    */
    """ 

    #  'Start' and 'end' input converted to a number format
    dict_to_numbers = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
    }

    x = dict_to_numbers[start[0]]
    y = int(start[1])
    a = dict_to_numbers[end[0]]
    b = int(end[1])
    
    end_position = (a,b)
    prev_visited = [(x,y)]  

    #  Set of 8 potential positions accessible to each position within 1 move, 
    #  Where for position [a,b] the next move will be [a + setA(item), b + setB(item)]
    set_x = [2, 2, -2, -2, 1, 1, -1, -1] 
    set_y = [1, -1, 1, -1, 2, -2, 2, -2]     

    # Internal function to check whether any potential move [p,q] is valid - i.e. lies within the 8 x 8 chessboard
    def isValid(x, y): 
        if (x >= 1 and x <= 8 and 
            y >= 1 and y <= 8):  
            return True
        else:
            return False    

    def recursive(moves):
        if moves >= 1:
            for i in (range(len(prev_visited))):
                for j in range(8):
                    (x,y) = prev_visited[[i][0]]
                    x +=  set_x[j] 
                    y +=  set_y[j]

                    #  Check whether final position has been reached in the given number of moves 
                    if (x,y) == end_position:
                        return True
                    #  if moves remaining, generate and check validity of next circle of 8 possible positions for current position.
                    #  Add unvisited (and valid) next positions into the queue                        
                    elif not isValid(x, y) or (x,y) in prev_visited:
                        False
                    else:  
                        prev_visited.append((x, y))
                    j += 1
            return recursive(moves-1)
                 
        else: 
            return False

    return recursive(moves)