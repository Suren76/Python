# Function call: read_file("filename.txt", ["Some", "text", "or", 5, 9])
# Function output: The writing process is successfully done

def read_file(file_name, add_list):
    try:

        file = open(file_name, "r+")
        file.writelines(add_list)

    except FileNotFoundError:

        return ("{} file not found".format(file_name))

    except TypeError:
        file.seek(0)
        for val in add_list:

            file.writelines(str(val))

        return "The writing process is successfully done"

    else:

        return "The writing process is successfully done"


print(read_file("random_text.txt", ["Some", "text", "or", 5, 9]))
