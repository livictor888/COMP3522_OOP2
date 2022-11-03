"""
This module depicts the use of the Proxy Pattern. MovieDatabaseProxy
acts as a a proxy to MovieDatabase. Refer to the
movie_database_proxy_uml.png diagram while reading this code.
"""
import movie_database
import pathlib


class MovieDatabaseProxy:
    """
    A Proxy to movie database, MovieDatabaseProxy implements the same
    inteface as MovieDatabase and checks the users access level before
    allowing interactions with the database. Responsible for raising
    exceptions if the user is not authorized.
    """

    def __init__(self, access_level, name, connect_on_startup=True):
        """
        Initialize the MovieDatabase with the given name. Checks the
        users access level first and raises an exception if the user does not
        have access or if the file path is incorrect.
        :param access_level: a string
        :param name: a string, file path
        :param connect_on_startup: a bool
        """
        self.access_level = access_level
        if pathlib.Path(name).suffix == ".db" and \
                (access_level == "moderator" or access_level == "member"):
            self.database = movie_database.MovieDatabase(name,
                                                         connect_on_startup)
        else:
            raise Exception("Check filename or access level. Guests cannot "
                            "connect to the database.")

    def connect(self):
        """
        Connects to the database if the user has access, raises an
        exception otherwise.
        """
        if self.access_level == "moderator" or self.access_level == "member":
            self.database.connect()
        else:
            raise Exception("Not authorized. Guests cannot connect to the "
                            "database.")

    def close_connection(self):
        """
        Closes the connection to the database if the user has access,
        raises an exception otherwise
        """
        if self.access_level == "moderator" or self.access_level == "member":
            self.database.close_connection()
        else:
            raise Exception("Not authorized. Guests cannot close connection")

    def insert(self, title, director, language, release_year):
        """
        Inserts movie details into the database if the user has access,
        raises an exception otherwise
        :param title: a string
        :param director: a string
        :param language: a string
        :param release_year: an int
        """
        if self.access_level == "moderator":
            self.database.insert(title, director, language, release_year)
        else:
            raise Exception("Not authorized. Guests and members cannot insert "
                            "data, only moderators can.")

    def view(self):
        """
        Retrieves all the data from the movie database if the user has
        access, raises an exception otherwise
        :return: a list
        """
        if self.access_level == "moderator" or self.access_level == "member":
            return self.database.view()
        else:
            raise Exception("Not authorized. Guests cannot view the database.")

    def delete(self, movie_id):
        """
        Deletes the specified movie from the database if the user has
        access, raises an exception otherwise
        :param movie_id: an int
        """
        if self.access_level == "moderator":
            self.database.delete(movie_id)
        else:
            raise Exception("Not authorized. Guests and members cannot delete "
                            "data, only moderators can.")

    def search(self, title="", director="", language="", release_year=""):
        """
        Retrieves all movies that match the given details from the
        database if the user has access, raises an exception otherwise
        :param title:
        :param director:
        :param language:
        :param release_year:
        :return:
        """
        if self.access_level == "moderator" or self.access_level == "member":
            return self.database.search(title, director, language,
                                        release_year)
        else:
            raise Exception("Not authorized. Guests cannot search the "
                            "database.")


def main():
    try:
        print("------ Demonstrating moderator access to database ------")
        database = MovieDatabaseProxy("moderator", "movies.db", True)
        database.insert("Shrek", "Andrew Adamson", "ENG", 2001)
        print(database.view())
        database.close_connection()

        print("------ Demonstrating member access to database ------")
        database = MovieDatabaseProxy("member", "movies.db", True)
        print(database.search(language="ENG"))
        database.close_connection()

        print("------ Demonstrating guest access to database ------")
        database = MovieDatabaseProxy("guest", "movies.db", True)
        print(database.search(language="ENG"))
        database.close_connection()

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
