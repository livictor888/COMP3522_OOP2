""" This module depicts some ways to read and write to a file."""

def read_sample_txt():
    """
    Reads data from sample1.txt. This method contains instructions to
    manually open and close a file. It also demonstrates how to reset
    the file pointer if we want to read multiple times.
    """
    print("Reading sample.txt")
    print("----------------")
    #Step1: Open a file
    my_text_file = open("sample.txt", mode='r', encoding='utf-8')

    #Step2: File operations
    data = my_text_file.read()
    print(f"File Data:\n{data}")

    # This won't print anything since the file pointer is at the end
    # of the file
    data = my_text_file.read()
    print(f"Printing Data again: {data}")

    # reset the file pointer to the beginning of the file
    # the file pointer can be reset to any custom location as needed.
    my_text_file.seek(0)
    data = my_text_file.read()
    print(f"Printing data after seeking to the beginning:\n{data}")

    #Step3: Close the file
    my_text_file.close()


def read_sample_txt_with():
    """
    Reads data from sample1.txt. This method utilizes the with block to
    do so. A with block allows us to safely conduct file operations. If
    there is any exception, the file is closed automatically. It also
    demonstrates how to reset the file pointer if we want to read
    multiple times.
    """
    print("\nReading the sample.txt file using a with block")
    print("----------------------------------------------")
    with open("sample.txt", mode='r') as my_text_file:
        data = my_text_file.read()
        print(f"File Data:\n{data}")
        # cursor is at the end of the file
        data = my_text_file.read()
        print(f"Printing Data again: {data}")
        my_text_file.seek(0)
        data = my_text_file.read()
        print(f"Printing data after seeking to the beginning:\n{data}")


def write_sample2_write_mode(data):
    """
    Writes data to a file by opening the file in write mode. In this mode
    if the file does not exist, it gets created. IMPORTANT: If the file
    has any pre-existing data in it, opening the file in write mode will
    overwrite any existing data in that file.
    :param data: a string
    """
    print("Writing to sample2.txt using write mode")
    with open("sample2.txt", mode='w') as my_text_file:
        my_text_file.write(data)


def write_sample3_append_mode(*args):
    """
    Writes data to a file by opening the file in append mode. In this
    mode, if the file does not exist, it gets created. More importantly,
    if the file has any pre-existing data, opening the append mode will
    not overwrite this data. Any calls to file.write() will add the data
    to the end. (Unless you change the file pointer using file.seek()
    :param args: Variable list argument, any number of string arguments.
    """
    print("Writing tp sample3.txt using append mode")
    with open("sample3.txt", mode='a') as my_text_file:
        for line in args:
            my_text_file.write(line)


def main():
    # read from sample.txt
    # read_sample_txt()

    # # read from sample.txt using the with block
    read_sample_txt_with()

    # # write to sample2.txt using write mode, file gets created if it
    # # doesnt exist
    write_sample2_write_mode("This is some test data\n that is being "
                             "written")
    #
    # # write to sample2.txt again using write mode, file gets overwritten.
    write_sample2_write_mode("The file got overwritten with this text.")

    # Write using append mode to sample3.txt, file gets created if it
    # doesn't exist.
    write_sample3_append_mode("This is line 01", "This is line 02"
                              , "This is line 03")

    # Let's append some more lines using append mode, this will not
    # overwrite the file. This time lets add line breaks using \n
    write_sample3_append_mode("\nThis is line 04\n", "This is line05\n")


if __name__ == '__main__':
    main()

