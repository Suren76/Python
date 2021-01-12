# Function call: write_text_in_file("filename.txt", "text")
# Function output: Text should be wrote in the file.

def write_text_in_file(file_name, add_text):

    try:

        file = open(file_name, "r+")

        file.write(add_text)

    except FileNotFoundError:

        return ("{} file not found".format(file_name))

    else:

        file.seek(0)
        return (file.read())

        file.close()


print(write_text_in_file("random_text.txt", "random text"))
