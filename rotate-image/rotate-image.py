class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
    
        for layer in range(N//2):
            first = layer
            last = N - 1 - layer
            for i in range(first, last):
                offset = i - first

                top = matrix[first][i] ## save top

                ## left -> top
                matrix[first][i] = matrix[last - offset][first]

                ## bottom -> left
                matrix[last - offset][first] = matrix[last][last - offset]

                ## right -> bottom
                matrix[last][last - offset] = matrix[i][last]

                ## top -> right
                matrix[i][last] = top