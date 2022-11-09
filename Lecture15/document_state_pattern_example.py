import abc
from datetime import datetime

class Document:

    def __init__(self, content, state):
        self.doc_state = state
        self.doc_state.document = self
        self.content = content
        self.date_published = None

    def change_state(self, state):
        self.doc_state = state
        self.doc_state.document = self

    def render(self):
        self.doc_state.render()

    def publish(self, user_type: str):
        self.doc_state.publish(user_type)


class DocumentState(abc.ABC):

    def __init__(self):
        self._document = None

    @property
    def document(self):
        return self._document

    @document.setter
    def document(self, value):
        self._document = value

    @abc.abstractmethod
    def render(self):
        pass

    @abc.abstractmethod
    def publish(self, user_type: str):
        pass


class DocumentDraftState(DocumentState):

    def render(self):
        print(f"----DRAFT----\n{self.document.content}")

    def publish(self, user_type: str):
        print("DRAFT has been sent to the administrator for review.")
        self.document.change_state(DocumentModerationState())


class DocumentModerationState(DocumentState):
    def render(self):
        print(f"----MODERATION----\n{self.document.content}")

    def publish(self, user_type: str):
        if user_type == "admin":
            self.render()
            approval = input("Do you approve of the content?")
            if approval.lower() == 'y':
                print("Document approved and published!")
                self.document.change_state(DocumentPublishedState())
                self.document.date_published = datetime.now()
            else:
                print("Document not approved")
                self.document.change_state(DocumentDraftState())
        else:
            print("Error! Only an admin can approve")


class DocumentPublishedState(DocumentState):
    def render(self):
        print(f"----PUBLISHED: {self.document.date_published}----\n{self.document.content}")

    def publish(self, user_type: str):
        time_diff = datetime.now() - self.document.date_published
        if time_diff.total_seconds()/3600 > 24:
            self.document.change_state(DocumentDraftState())


def main():
    doc_draft_state = DocumentDraftState()
    my_doc = Document("This is an object that has multiple states", doc_draft_state)
    my_doc.render()
    my_doc.publish("writer")
    print("\n")
    my_doc.render()
    my_doc.publish("writer")
    my_doc.publish("admin")
    print("\n")
    my_doc.render()
    my_doc.publish("admin")


if __name__ == '__main__':
    main()

