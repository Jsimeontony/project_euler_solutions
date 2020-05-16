# this function display a board as an output
def display_board(board):

    print( '  |    |')
    print( ' ' + board[7] +   '| ' + board[8] + '  |' + board[9])
    print( '  |    | ')
    print( '-------------')
    print( ' ' +board[4] +    '| ' + board[5] + '  |' + board[6])
    print( '  |    |')
    print( '-------------')
    print( ' ' +board[1] +    '| ' + board[2] + '  |' + board[3])
    print( '  |    |')

test_board = ['x' ,'o','x','o','x','o','x','o','x'] * 9
display_board(test_board)

    #print('\n' * 100) # it makes new-line

    #display_board(test_board)

def player_input():
     marker = ''
     while marker != 'x' and marker != 'o':
         marker = input(' player1 : choose x or o')

         if marker == 'x':
             return ('x', 'o')
         else:
             return ('o' , 'x')

player1_marker , player2_marker = player_input()


def place_marker( board , marker , position):
    marker =  board[position]

place_marker(test_board , 'anthony' , 8)
