# Function call: file_to_list("filename.txt")
# Function output: ["Content", "of", "file"]


def file_to_list(file_name):

    try:

        file = open(file_name)

        lines_in_list = [[line] for line in file.readlines()]

        if lines_in_list == []:
            raise IOError

    except FileNotFoundError:

        return ("{}: file not found".format(file_name))

    except IOError:

        return ("Your file is empty")

    else:

        return (lines_in_list)


print(file_to_list("random_text.txt"))
