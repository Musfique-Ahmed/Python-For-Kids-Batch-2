# This module contains functions for basic string manipulation.

def reverse_string(s):
    """Returns the reverse of a string."""
    return s[::-1]

def is_palindrome(s):
    """
    Checks if a string is a palindrome.
    (A palindrome reads the same forwards and backwards)
    """
    cleaned_s = "".join(char.lower() for char in s if char.isalnum())
    return cleaned_s == cleaned_s[::-1]
