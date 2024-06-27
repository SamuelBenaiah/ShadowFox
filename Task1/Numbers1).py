def format_number(number, format_spec):
    formatted_string = format(number, format_spec)
    return formatted_string
number = 145
format_spec = 'o'
result = format_number(number, format_spec)
print(result)
