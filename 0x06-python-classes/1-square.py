#!/usr/bin/python3
class Square:
    """Represents a square."""

    def __init__(self, size):
        """Initialize a new Square.

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
        self.__size = new_size

    def area(self):
        """Compute the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
