"""
This module is responsible for containing anything
related to Teams of students.
"""
class Team:
    """
    This implementation of Team adheres to the 'sized protocol' and
    implements the __len__ method.

    Builds on top of teams.py
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

    def __len__(self):
        """
        Returns the number of people in the team
        :return:
        """
        return len(self.members)


def main():
    x_men = Team("X-Men", ["Professor Xavier", "Cyclops", "Storm",
                           "Jean"])
    print(x_men)

    # sized protocol in action
    print(f"Number of members: {len(x_men)}")


if __name__ == '__main__':
    main()
