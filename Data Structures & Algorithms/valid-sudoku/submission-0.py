class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # A board is valid if
        # no numbers repeat within the same row
        # no numbers repeat within the same col
        # no numbers repeat within the same box
        # you do not need to see all numbers within any row/col/box


        # Pseudocode:
        # Look at each cell, determining which row, col, and box it belongs to, 
        # and if we've seen that cell's number there before
        # if we have -> return False
        # if all cells pass -> return True 


        # Given: Board will always be 9x9 -> 9 rows, 9 cols, 9 boxes 
        boxes = defaultdict(set) # store the numbers seen in each box so far (boxes 1 - 9)
        rows = defaultdict(set)
        cols = defaultdict(set)

        numRows = 9
        numCols = 9


        # how to find the box? 
        # rows 0 - 2, with cols 0-2 corrospond to box 0
        # rows 0 - 2, with cols 3-5 corrospond to box 1
        # rows 0 - 2, with cols 6-8 corrospond to box 2 
        # boxIndex = (row // 3) + (col // 3)

        for row in range (numRows):
            for col in range (numCols):
                cell = board[row][col]
                if cell in rows[row]: 
                    print(f"Found dupe cell in row {row}\n")
                    return False
                if (cell != '.'):
                    rows[row].add(cell)
                
                if cell in cols[col]:
                    print(f"Found dupe cell {cell} in col {col}\n")
                    return False
                if (cell != '.'):
                    cols[col].add(cell)
                    
                boxCoord = ((row // 3), (col // 3))
                
                if cell in boxes[boxCoord]:
                    print(f"Found dupe cell {cell} in box {boxCoord}, {boxes[boxCoord]}\n")
                    return False

                if (cell != '.'):
                    boxes[boxCoord].add(cell)
                print(f"Added cell {cell} in box {boxCoord}, {boxes[boxCoord]}\n")

        return True
                



        