def reformat_string(s):
    result = []
    alpha_index = 0  # Index to track the alphabetical characters
    
    # Create a list of only alphabetical characters
    alpha_chars = [char for char in s if char.isalpha()]
    
    # Iterate through the original string
    for char in s:
        if char.isalpha():
            # Alternate between uppercase and lowercase
            if alpha_index % 2 == 0:
                result.append(alpha_chars[alpha_index].upper())
            else:
                result.append(alpha_chars[alpha_index].lower())
            alpha_index += 1
        else:
            # Keep non-alphabetical characters unchanged
            result.append(char)
    
    return ''.join(result)


print(reformat_string("hello world!"))# Testing
print(reformat_string("Za^B8g@E2jH*kWl!MoPqXr7YvT1c$Fs3Ud9IwZ&yX0pLkV6sHqN^tB4rA+oZ%gFj"))  
