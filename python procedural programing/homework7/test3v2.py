# Function call: file_to_list("filename.txt")
# Function output: ["Content", "of", "file"]


def file_to_list(file_name):

    try:

        file = open(file_name)

        #  Երկուսն էլ տող֊տող են կարդում, պահանջի տեսանկյունից 1֊ինը սխալ է՞։

        # 1
        #lines_in_list = [[line] for line in file.readlines()]

        #  2
        lines = len(file.readlines())
        file.seek(0)
        lines_in_list = [[file.readline()] for _ in range(lines)]

        if lines_in_list == []:
            raise IOError

    except FileNotFoundError:

        return ("{}: file not found".format(file_name))

    except IOError:

        return ("Your file is empty")

    else:

        return (lines_in_list)


print(file_to_list("random_text.txt"))
