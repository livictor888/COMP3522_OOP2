"""
This module is responsible for containing anything
related to Teams of students.
"""
class Team:
    """
    This implementation of Team showcases the use of default parameters
    in the __init__ method.

    Builds on top of teams_iterable.py
    """

    def __init__(self, team_name="Team Ninja", team_members=None):
        """
        Initializes a team with the given name and members, or default
        values if not provided
        :param team_name: a string
        :param team_members: a list
        """
        if team_members == None:
            team_members = [] #prevents team_members defaulting to the same [] list for every instance
            team_members.append('person')
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


def main():
    # initialize a team with default values
    my_team = Team()
    print(my_team)

    my_team = Team()
    print(my_team)

    my_team = Team(team_name="Chipmunks", team_members=['Alvin', 'Theodore'])
    print(my_team)

    my_team = Team(team_name="Turtles", team_members=['Leo', 'Ralph', 'Dona', 'Mike'])
    print(my_team)

    my_team = Team()
    print(my_team)


if __name__ == '__main__':
    main()
