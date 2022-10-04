"""
This module is responsible for containing anything
related to Teams of students.
"""
class Team:
    """
    This implementation of Team allows us to use the for loop syntax to
    iterate over the team member list.

    Builds on top of teams_container.py
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

    def __iter__(self):
        """
        Implements the iter protocol. This returns an iterator over the
        team member list allowing us to use this object as part of a for
        loop.
        :return: An Iterator.
        """
        return iter(self.members)


def main():
    x_men = Team("X-Men", ["Professor Xavier", "Cyclops", "Storm",
                           "Jean"])
    print(x_men)

    # sized protocol in action
    print(f"Number of members: {len(x_men)}")

    #Container protocol in action
    print(f"Is Cyclops part of the X-men? {'Cyclops' in x_men}")

    # iter protocol in action
    print("The X-Men:")
    for person in x_men:
        print(person)


if __name__ == '__main__':
    main()
