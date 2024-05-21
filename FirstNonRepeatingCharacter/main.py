def first_non_repeating_letter(string):
    string_lower = string.lower()

    for char in string:
        if string_lower.count(char.lower()) == 1:
            return char
        
    return ''