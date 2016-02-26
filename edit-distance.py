import sys

class Memo:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.subproblems = [[-1 for x in range(cols)] for y in range(rows)]

    def setValue(self, row, col, val):
        self.subproblems[row][col] = val

    def setValueFromTuple(self, pos, val):
        self.setValue(pos[0], pos[1], val)

    def getValue(self, row, col):
        return self.subproblems[row][col]

    def getValueFromTuple(self, pos):
        return self.getValue(pos[0], pos[1])

    def isSolved(self, row, col):
        return not (self.getValue(row, col) == -1)

##########################################
#   _ _ _ _ _ _ _ _ _ _ _ _ _ _
# | 0 1 2 3 4 ..... len(word2)  |
# | 1                           |
# | 2                           |
# | 3                           |
# | 4                           |
# | ....                        |
# | len(word1)                  |
#   _ _ _ _ _ _ _ _ _ _ _ _ _ _
#
##########################################
def edit_distance(word1, word2):
    memo = Memo(len(word1) + 1, len(word2) + 1) # problem of size len(word1) * len(word2)
    for i in range(len(word1) + 1): # initialize row 0 and column 0
        memo.setValue(i, 0, i)
    for i in range(len(word2) + 1):
        memo.setValue(0, i, i)
    # For each row, iterate through all the columns
    for row in range(1, len(word1) + 1):
        for col in range(1, len(word2) + 1):
            # 3 subproblems for edit distance: delete from word 1, delete from word 2, or mutate/same character
            subproblems = [(row - 1, col - 1), (row - 1, col), (row, col - 1)]
            results = map(lambda x: [x, memo.getValueFromTuple(x) + 1], subproblems)
            if word1[row - 1] == word2[col - 1]:
                results[0][1] -= 1
            # Now we have values plus a transition cost for each subproblem. Take minimum.
            best = min([x[1] for x in results])
            memo.setValue(row, col, best)
    # Finally, return the finished problem.
    return memo.getValue(len(word1), len(word2))

if __name__ == "__main__":
    args = sys.argv[1:]

    if not len(args) == 2 or args[0] is None or args[1] is None:
        print("Usage: python edit_distance.py <first-word> <second-word>")
        sys.exit(0)
    first, second = args[0], args[1]
    print edit_distance(first, second)
