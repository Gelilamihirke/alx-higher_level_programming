class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size

    def get_size(self):
        """Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    def set_size(self, new_size):
        """Set the size of the square.

        Args:
            new_size (int): The new size for the square.
        """
        if not isinstance(new_size, int):
            raise TypeError("size must be an integer")
        elif new_size < 0:
            raise ValueError("size must be >= 0")
        self.__size = new_size

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2
