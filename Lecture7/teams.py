"""
This module is responsible for containing anything related to Teams of
students.
"""
class Team:
    """
    This represents a simple team of students. Each object is made up
    of a team name, and a list of members. This forms the base for
    implementing a number of protocols.
    """

    def __init__(self, team_name, team_members):
        """
        Initializes a team with the given name and members
        :param team_name: a string
        :param team_members: a list
        """
        self.name = team_name
        self.members = team_members

    def __str__(self):
        team_list = ""
        for person in self.members:
            team_list += person + " "
        return f"Team: {self.name}\nMembers: {team_list}"


def main():
    x_men = Team("X-Men", ["Professor Xavier", "Cyclops", "Storm",
                           "Jean"])
    print(x_men)


if __name__ == '__main__':
    main()
