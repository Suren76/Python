# Function call: find_long_word("filename.txt")
# Function output: "LongestWord"


def find_long_word(file_name):

    try:

        file = open(file_name)
        max_word = str()

        for line in file.readlines():

            line = line.split(" ")
            for word in line:

                if len(word) > len(max_word):
                    max_word = word

        if max_word == "":

            raise IOError

    except FileNotFoundError:

        return ("{}: file not found".format(file_name))

    except IOError:

        return ("Your file is empty")

    else:

        return (max_word)


print(find_long_word("random_text.txt"))
