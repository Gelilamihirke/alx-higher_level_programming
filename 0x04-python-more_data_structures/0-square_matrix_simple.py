#!/user/bin/python3
def square_matrix_simple(matrix=[]):
    # Check if matrix is empty or not
    if matrix:
        # Get the dimensions of the matrix
        rows = len(matrix)
        cols = len(matrix[0])

        # Create a new matrix to store the squared values
        new_matrix = [[0] * cols for _ in range(rows)]

        # Iterate through each element in the matrix
        for i in range(rows):
            for j in range(cols):
                # Calculate the square of the element and store it in the new matrix
                new_matrix[i][j] = matrix[i][j] ** 2

        return new_matrix
    else:
        # If the input matrix is empty, return an empty matrix
        return []
