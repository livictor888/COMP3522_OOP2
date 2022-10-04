import file_1

print("file 2 __name__ = %s" % __name__)

# __name__ = "__main__"

if __name__ == "__main__":
    print("File2 is being run directly")
else:
    print("File2 is being imported")