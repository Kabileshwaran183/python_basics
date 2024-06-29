def process_paragraph(paragraph):
    result = ''
    current_number = ''
    for char in paragraph:
        if char.isdigit():
            current_number += char
        else:
            if current_number:
                result += current_number
                current_number = ''
                if char != ',' and char != '-':
                    result += '\n'
            result += char
    if current_number:
        result += current_number + '\n'
    return result

# Example usage:
input_paragraph = input("enter the string:")
output_paragraph = process_paragraph(input_paragraph)
print(output_paragraph)