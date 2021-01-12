# Function call: copy("input.txt", "neworexistingfile.txt")
# Function output: The process is successfully done.

def copy(input_file, new_file):
    try:

        file = open(input_file)
        new_file = open(new_file, "w")

        add_text = file.read()
        new_file.write(add_text)

        if file.read() == "":
            raise IOError

    except FileNotFoundError:

        return ("{} file not found".format(input_file))

    except IOError:

        return ("Your file is empty")

    else:
        return "The process is successfully done."


print(copy("random_text.txt", "random_text1.txt"))
