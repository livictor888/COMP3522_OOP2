class Document:
    """
    Represents a document which consists of:
    - heading: The first line of the document, a string
    - body: The rest of the document, a string
    - author: a string
    - formatter: a function that takes in heading, body and author and
    returns a formatted string
    """
    def __init__(self, doc_file, author="Unknown"):
        with open(doc_file, mode='r', encoding='utf-8') as document:
            self.heading = document.readline()
            self.body = document.read()
        self.author = author
        # This is the strategy that we will change later
        self.formatter = None

    def format_and_write(self, dest_file):
        formatted_document = self.formatter(self.heading, self.author, self.body)
        with open(dest_file, mode='w', encoding='utf-8') as output_doc:
            output_doc.write(formatted_document)

# strategy in function format
def paragraph_formatter(heading, author, body):
    """
    Returns a formatted document string where the body is broken down
    into paragraphs
    :param heading: a string
    :param author: a string
    :param body: a string
    :precondition body: must be a string where each sentence is on a
    separate line.
    :return: a string, formatted document
    """

    formatted_doc_list = [heading]
    formatted_doc_list.append(author)
    lines = [line for line in body.split('\n')]
    num_lines_in_para = 6
    para = ""
    for line in lines:
        if num_lines_in_para > 5:
            formatted_doc_list += [para, "\n\n"]
            num_lines_in_para = 0
            para = ""

        para = ''.join((para, line))
        num_lines_in_para += 1
    formatted_doc = ''.join((formatted_doc_list))
    return formatted_doc

# strategy in class format
class BulletPointFormatter:

    def __init__(self, bullet_unicode='\u2022'):
        self.bullet = bullet_unicode


    def __call__(self, heading, author, body):
        formatted_doc_list = [heading]
        lines = [' '.join((self.bullet, line)) for line in body.split('\n')]
        formatted_doc_list += lines
        formatted_doc_list.append(author)
        formatted_doc = '\n'.join(formatted_doc_list)
        return formatted_doc



def main():
    doc = Document("sample_doc.txt", "OOP2 Student")

    #doc.formatter = paragraph_formatter #use function formatter

    # use class as a formatter. Class overrides __call__ so object can be called like a function
    b = BulletPointFormatter()
    doc.formatter = b
    doc.format_and_write("para_sample_doc.txt")


if __name__ == '__main__':
    main()