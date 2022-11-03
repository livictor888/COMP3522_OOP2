"""
This module houses the code to perform sql queries on a database.
"""
import sqlite3


class MovieDatabase:
    """
    The MovieDatabase class allows users to connect and create a movies
    database while performing simple data manipulation tasks.
    The columns that make up each row are:

    1. PRIMARY KEY (integer, key)
    2. TITLE (text)
    3. DIRECTOR (text)
    4. RELEASE_YEAR (integer)

    All changes are committed immediately.
    """

    def __init__(self, name, connect_on_startup=True):
        """
        Initializes the database object and may establish a connection
        to the database based on the arguments.
        :param name: a string, path to the database file.
        :param connect_on_startup: a bool, will establish connection if
        True.
        """
        self.name = name
        self.db_connection = None
        self.cursor = None

        if connect_on_startup:
            self.connect()

    def connect(self):
        """
        Establishes a connection to the database and instantiates the
        cursor as well. If the movies table or the file does not exist,
        it creates one.
        """
        self.db_connection = sqlite3.connect(self.name)
        self.cursor = self.db_connection.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS movies (id INTEGER PRIMARY KEY, "
            "title text, director text, language text, release_year integer)"
        )
        self.db_connection.commit()

    def close_connection(self):
        """
        Closes the connection to the database preventing further changes.
        """
        self.db_connection.close()

    def insert(self, title, director, language, release_year):
        """
        Inserts a row into the movies database. Refer to the column
        headings in the class comments to see what the movies database
        is composed of.
        :param title: a string
        :param director: a string
        :param language: a string, ISO language code
        :param release_year: an int
        :return:
        """
        self.cursor.execute("INSERT INTO movies VALUES (NULL,?,?,?,?)",
                            (title, director, language, release_year))
        self.db_connection.commit()

    def view(self):
        """
        Retrieves all the rows in the movies table.
        :return: a list of rows.
        """
        self.cursor.execute("SELECT * FROM movies")
        rows = self.cursor.fetchall()
        return rows

    def delete(self, movie_id):
        """
        Deletes a row specified by the key in the movies table.
        :param movie_id: an int
        """
        self.cursor.execute("DELETE FROM movies WHERE id=?",(movie_id,))
        self.db_connection.commit()

    def search(self, title="", director="", language="", release_year=""):
        """
        Retrieves the rows that match any combination of the given
        parameters.
        :param title: a string
        :param director: a string
        :param language: a string, ISO language code
        :param release_year: an int
        :return: a list of rows
        """
        self.cursor.execute(
            "SELECT * FROM movies WHERE title=? OR director=? "
            "OR language=? OR release_year=?",
            (title, director, language, release_year))
        return self.cursor.fetchall()
