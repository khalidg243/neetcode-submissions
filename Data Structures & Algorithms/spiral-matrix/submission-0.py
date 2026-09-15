class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        l , r = 0, len(matrix[0])
        top , bottom = 0 , len(matrix)


        while l < r and top < bottom:
            # Top left to right
            for i in range(l,r):
                ans.append(matrix[top][i])
            top += 1

            # Right top to bottom
            for i in range(top, bottom):
                ans.append(matrix[i][r - 1])
            r -= 1

            if not (l < r and top < bottom):
                break
            
            # Bottom right to left
            for i in range(r - 1 , l - 1, -1):
                ans.append(matrix[bottom - 1][i])
            bottom -= 1

            # left bottom to top
            for i in range(bottom - 1, top - 1, -1):
                ans.append(matrix[i][l])
            l += 1

        return ans