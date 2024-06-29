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

# Function to read content from a file
def read_file(file_path):
    with open(file_path, 'r', encoding='latin-1') as file:
        return file.read()

# Example usage:
file_path = r"C:\Users\arunb\Desktop\PYTHON COURSE 100days\programs\Ambattur - Ayyapakkam Road - Oasis .txt"  # Replace with the actual path to your file
input_paragraph = read_file(file_path)
output_paragraph = process_paragraph(input_paragraph)
print(output_paragraph)