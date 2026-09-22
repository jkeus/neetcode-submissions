from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        cubes = defaultdict(list)

        for i, row in enumerate(board):
            for k, val in enumerate(row):
                
                if val == ".":
                    continue

                if i in rows:
                    if val in rows[i]:
                        return False
                rows[i].append(val)
                
                
                if k in cols:
                    if val in cols[k]:
                        return False
                cols[k].append(val)
                
                loc = str(i // 3) + ":" + str(k // 3)
                if loc in cubes:
                    if val in cubes[loc]:
                        return False
                cubes[loc].append(val)

        return True