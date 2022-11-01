"""
This module depicts the factory pattern in action as it generates
different kinds of users for a hypothetical website.
"""
import enum
import abc
from datetime import  datetime


class Permission(enum.Enum):
    """
    This enum specifies the different distinct permission types.
    """
    READ = 0,
    LIKE = 1,
    SHARE = 2,
    FLAG = 3,
    WRITE = 4


class User(abc.ABC):
    """
    Defines the User interface. This is the Product that the Factory
    Pattern creates. A user has a username, password, date_joined and a
    list of permissions.
    """

    @abc.abstractmethod
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.date_joined = datetime.now()
        self.permissions = None
        self.password = password

    def authenticate(self, password_input: str) -> bool:
        return password_input == self.password

    def get_profile(self) -> tuple:
        return self.username, self.date_joined

    def __str__(self):
        return f"Username: {self.username}, Date Joined: {self.date_joined}"

class Reader(User):
    """
    This type of user can Read, Like, Share and Flag posts.
    """

    def __init__(self, username: str, password: str) -> None:
        super().__init__(username, password)
        self.permissions = (Permission.READ)

    def __str__(self):
        return f"Reader User: {super().__str__()}"

class Guest(User):
    """
    This type of user can Read, Like, Share and Flag posts.
    """

    def __init__(self, username: str, password: str) -> None:
        super().__init__(username, password)
        self.permissions = (Permission.READ, Permission.LIKE, Permission.SHARE,
                            Permission.FLAG)

    def __str__(self):
        return f"Guest User: {super().__str__()}"


class Member(User):
    """
    This type of user can Read, Write, Like, Share, and Flag posts
    """

    def __init__(self, username:str, password: str) -> None:
        super().__init__(username, password)
        self.permissions = (Permission.READ, Permission.LIKE, Permission.SHARE,
                            Permission.FLAG, Permission.WRITE)

    def __str__(self):
        return f"Member User: {super().__str__()}"


class UserFactory(abc.ABC):
    """
    The UserFactory class is the base class that the rest of the system
    depends on. It defines a factory interface that creates a user.
    """

    @abc.abstractmethod
    def create_user(self) -> User:
        pass


class ReaderUserFactory(UserFactory):
    """
    The GuestFactory is responsible for creating Guests USer Accounts.
    """

    def create_user(self) -> User:
        return Reader(None, None)

class GuestUserFactory(UserFactory):
    """
    The GuestFactory is responsible for creating Guests USer Accounts.
    """

    def create_user(self) -> User:
        return Guest(None, None)


class MemberUserFactory(UserFactory):
    """
    The MemberUSerFactory is responsible for creating Member User
    Accounts
    """

    def create_user(self) -> User:
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        return Member(username, password)


class Forum:
    """
    The Client system in the factory pattern. Depends on the UserFactory
    class to create user accounts.
    """

    def __init__(self, name):
        self.name = name
        self.users = []

    def add_user(self, factory):
        """
        This function doesn't know what kind of factory it will receive
        As a result it doesn't depend on the concrete MemberUserFactory or GuestUserFactory
        to create the user
        """
        user = factory.create_user()
        self.users.append(user)


def get_user_factory() -> UserFactory:
    """
    get_user_factory is responsible for displaying the account
    creation menu and returning the appropriate user factory.
    """
    print("Welcome! Do you want to make an account or continue as a guest?")
    print("1. Make Account")
    print("2. Continue as Guest")
    print("3. Continue as Reader")
    choice = int(input("Enter your choice (1-3)"))
    if choice == 1:
        factory_class = MemberUserFactory
    elif choice == 2:
        factory_class = GuestUserFactory
    else:
        factory_class = ReaderUserFactory
    return factory_class()


def main():
    """
    main is acting as the ForumController
    prompting user for the type of user to create and passing factory to Forum
    """
    my_forum = Forum("Discussion Forum")

    my_forum.add_user(get_user_factory())
    my_forum.add_user(get_user_factory())
    my_forum.add_user(get_user_factory())

    for user in my_forum.users:
        print(user)


if __name__ == '__main__':
    main()