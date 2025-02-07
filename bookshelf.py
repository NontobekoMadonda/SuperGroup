from collections import Counter

def can_organize_books(shelf):
    count = Counter(shelf)
    
    # Check if all counts are greater than 1
    for copies in count.values():
        if copies < 2:
            return "NO"
    
    return "YES"

# Example usage
print(can_organize_books([5, 5, 3, 3, 2, 2]))  # testing
print(can_organize_books([1, 2, 3, 4, 4, 3, 2, 1]))  # testing
print(can_organize_books([1, 1, 1, 2, 2, 2, 3, 3, 3]))  # testing
print(can_organize_books([1234567, 1234567, 2345678, 2345678, 3456789, 3456789, 1234567, 2345678, 3456789, 4567890, 4567890, 5678901, 5678901, 6789012, 6789012, 1234567, 2345678, 3456789, 4567890, 5678901, 4567890, 5678901]))
