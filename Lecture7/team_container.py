"""
This module is responsible for containing anything
related to Teams of students.
"""
class Team:
    """
    This implementation of Team adheres to the 'contains protocol' and
    implements the __contains__ method. This enables us to use
    "_____  in team_object" as syntax.

    Builds on top of teams_sized.py
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

    def __contains__(self, item):
        """
        Implements the container protocol. This checks if the given
        item is in the object or not.
        :param item: a string (team members name)
        :return: True if found, False otherwise.
        """
        found = False
        for person in self.members:
            if item == person:
                found = True
                break
        return found



def main():
    x_men = Team("X-Men", ["Professor Xavier", "Cyclops", "Storm",
                           "Jean"])
    print(x_men)

    # sized protocol in action
    print(f"Number of members: {len(x_men)}")

    #Container protocol in action
    print(f"Is Cyclops part of the X-men? {'Cyclops' in x_men}")


if __name__ == '__main__':
    main()
