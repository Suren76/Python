# Function call: read_file("filename.txt")
# Function output: Content of file

def read_file(file_name):
    try:

        file = open(file_name)

        return (file.read())

    except FileNotFoundError as Error:
        print(Error)
        next_step = input("Creat new file (c) or exit (e) ")
        if next_step == 'c':
            file = open(file_name, "w")
            return "File created"
        if next_step == 'e':
            exit()

print(read_file("random_text.txt"))