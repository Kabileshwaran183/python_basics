PLACEHOLDER = "[name]"


with open("/Users/arunb/Desktop/PYTHON COURSE 100days/programs/turtle/files/mail merging/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("/Users/arunb/Desktop/PYTHON COURSE 100days/programs/turtle/files/mail merging/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"/Users/arunb/Desktop/PYTHON COURSE 100days/programs/turtle/files/mail merging/Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)

