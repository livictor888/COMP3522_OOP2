"""
This module is responsible for containing anything
related to Teams of students.
"""


class Team:
    """
    This implementation of Team showcases the use of variable argument
    list parameters. Check out the add_members() method.

    Builds on top of teams_default_arguments.py
    """

    def __init__(self, team_name="Team Ninja", team_members=None):
        """
        Initializes a team with the given name and members, or default
        values if not privided
        :param team_name: a string
        :param team_members: a list
        """
        if team_members == None:
            team_members = []
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

    def __iter__(self):
        """
        Implements the iter protocol. This returns an iterator over the
        team member list allowing us to use this object as part of a for
        loop.
        :return: An Iterator.
        """
        return iter(self.members)

    def add_members(self, *args):
        """
        Adds the given members to the list of members in the team.
        Implements the variable argument list paramater *args that can
        accept any number of arguments.
        :param args: a variable number of strings
        """
        for person in args:
            print("appending:", person)
            self.members.append(person)


def main():
    x_men = Team("X-Men", ["Professor Xavier", "Cyclops", "Storm",
                           "Jean"])
    print(x_men)
    x_men.add_members("Nightcrawler", "Wolverine", "Rogue")
    print(x_men)
    additional_members = ["Beast", "Gambit", "Jubilee"]
    x_men.add_members(*additional_members)
    print(x_men)


if __name__ == '__main__':
    main()
