print("Hello world")

print("file 1 __name__ = %s" % __name__)

# __name__ = "__main__"

if __name__ == "__main__":
    print("File1 is being run directly")
else:
    print("File1 is being imported")