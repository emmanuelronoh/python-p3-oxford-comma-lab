# oxford_comma.py

def oxford_comma(items):
    '''Formats a list of items according to the Oxford comma rules.'''
    if len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return f"{items[0]} and {items[1]}"
    elif len(items) == 3:
        return f"{items[0]}, {items[1]}, and {items[2]}"
    else:
        # For more than three elements
        return ', '.join(items[:-1]) + ', and ' + items[-1]
