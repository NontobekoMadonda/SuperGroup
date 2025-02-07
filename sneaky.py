def find_duplicates(outcomes):
    seen = set()
    duplicates = []
    
    for outcome in outcomes:
        if outcome in seen:
            duplicates.append(outcome)
            if len(duplicates) == 2:  # We only need two duplicates
                break
        else:
            seen.add(outcome)
    
    return duplicates


print(find_duplicates([0, 3, 2, 1, 3, 2]))  # for Testing
print(find_duplicates([123456, 234567, 123347, 456789, 567890, 678901, 789012, 890123, 901234, 112233, 223344, 334455, 789012, 222234, 123347]))  # Output: [123347, 789012]
