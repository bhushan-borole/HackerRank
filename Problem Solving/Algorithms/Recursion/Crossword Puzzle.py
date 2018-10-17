# https://www.hackerrank.com/challenges/crossword-puzzle/problem

import copy

raw_board = list()
for _ in range(10):
    raw_board.append(input())
    
raw_words = input().split(';')

def test_board(board, words):
    buff = len(words[0])
    possible_boards = list()
    
    # puts into horizontal space
    for rr in range(10):
        for cc in range(10-buff+1):
            if all([(wl==bl or bl=='-') for (wl,bl) in zip(words[0], board[rr][cc:cc+buff])]):
                temp_board = copy.deepcopy(board)
                temp_board[rr] = temp_board[rr][:cc]+words[0]+temp_board[rr][cc+buff:]
                possible_boards.append(temp_board)
                
    # puts into vertical space
    for rr in range(10-buff+1):
        for cc in range(10):
            if all([(wl==bl or bl=='-') for (wl,bl) in zip(words[0], [x[cc] for x in board[rr:rr+buff]])]):
                temp_board = copy.deepcopy(board)
                for ii in range(buff):
                    temp_board[rr+ii] = temp_board[rr+ii][:cc]+words[0][ii]+temp_board[rr+ii][cc+1:]
                possible_boards.append(temp_board)

    if (len(words) <= 1) or not possible_boards:
        return possible_boards
    else:
        return_boards = list()
        for entry in possible_boards:
            return_boards += test_board(entry, words[1:])
        return return_boards
                
result = test_board(raw_board, raw_words)

for entry in result[0]:
    print(entry)
