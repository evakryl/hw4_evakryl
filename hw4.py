def read_file_to_list(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()


def is_valid_input(user_input):
    return len(user_input.split()) >= 3


def write_lines_to_script(script_file, line, prompt):
    if line.strip() == '$$$':
        user_input = input(prompt)
        while not is_valid_input(user_input):
            print("wrong input. please try again. use at least 3 words.")
            user_input = input(prompt)
        script_file.write(user_input + "\n")
    else:
        script_file.write(line)


def main():
    lines_character_1 = read_file_to_list('chapter1.txt')
    lines_character_2 = read_file_to_list('chapter2.txt')

    with open('script_output.txt', 'w') as script_file:
        for line1, line2 in zip(lines_character_1, lines_character_2):
            write_lines_to_script(script_file, line1, "write a line for chapter 1: ")
            write_lines_to_script(script_file, line2, "write a line for chapter 2: ")

    print("script is finally done!")


main()
