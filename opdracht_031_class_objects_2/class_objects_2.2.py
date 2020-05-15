# -------------- opdracht 2------------------
class Team:
    def __init__(self, name, trainer, players):
        self.name = name
        self.trainer = trainer
        self.players = players

    # overbodig
    def get_clubname(self):
        return self.name

    # overbodig
    def get_trainername(self):
        return self.trainer.name

    # playername_is_in_team
    def get_playernames(self):
        # player_list = []
        # for player in self.players:
        #     player_list.append(player.name)
        # return player_list
        return [player.name for player in self.players]

    def get_specific_name(self, index):
        return self.players[index].name


class Scheidsrechter:
    def __init__(self, name):
        self.name = name


class Locatie:
    def __init__(self, city, stadium, hometeam):
        self.city = city
        self.stadium = stadium
        self.hometeam = hometeam


class Trainer:
    def __init__(self, name, team):
        self.name = name
        self.team = team


class Player:
    def __init__(self, name, number, team):
        self.name = name
        self.number = number
        self.team = team


class Goal:
    def __init__(self, name, minute):
        self.name = name
        self.minute = minute
        self.homepoints = []
        self.awaypoints = []

    def print_goal(self, home, away):
        if self.name in home.get_playernames():
            print(
                f"In de {self.minute}e minuut scoort {self.name} voor {home.get_clubname()}, het is {self.homepoints} - {self.awaypoints}."
            )
        if self.name in away.get_playernames():
            print(
                f"In de {self.minute}e minuut scoort {self.name} voor {away.get_clubname()}, het is {self.homepoints} - {self.awaypoints}."
            )

    def print_winner(self, goals, home, away):
        list_lgt = len(goals) - 1
        if goals[list_lgt].homepoints > goals[list_lgt].awaypoints:
            home_teamname = home.get_clubname()
            away_teamname = away.get_clubname()
            print(
                f"{home_teamname} wint van {away_teamname} met {goals[list_lgt].homepoints}-{goals[list_lgt].awaypoints}"
            )


class Wedstrijd:
    def __init__(self, date, location, referee, home, away, goals, attendance):
        self.date = date
        self.location = location
        self.referee = referee
        self.home = home
        self.away = away
        self.goals = goals
        self.attendance = attendance

    def print_match_report(self):

        line = []
        line.append(
            f"Op {self.date} speelde {self.home.name} tegen {self.away.name} in {self.location.stadium} in Amsterdam."
        )
        line.append(f"Er waren {self.attendance} bezoekers aanwezig in het stadion.")
        line.append(f"De wedstrijd werd gefloten door {self.referee.name}.")
        line.append(f"De trainer voor {self.home.name} was {self.home.trainer.name}.")
        line.append(f"De trainer voor {self.away.name} was {self.away.trainer.name}.")
        for single_line in line:
            print(single_line)
        for goal in self.goals:
            goal.print_goal(self.home, self.away)
        Goal.print_winner(self, self.goals, self.home, self.away)


# hometeam data
trainer_hometeam = Trainer("Ștefan Kovács", "AFC ajax")
hometeam_players = [
    Player("Heinz Stuy", 1, "AFC ajax"),
    Player("Horst Blankenburg", 2, "AFC ajax"),
    Player("Barry Hulshoff", 3, "AFC ajax"),
    Player("Gerrie Mühren", 4, "AFC ajax"),
    Player("Ruud Krol", 5, "AFC ajax"),
    Player("Wim Suurbier", 6, "AFC ajax"),
    Player("Johan Neeskens", 7, "AFC ajax"),
    Player("Sjaak Swart", 8, "AFC ajax"),
    Player("Arie Haan", 9, "AFC ajax"),
    Player("Johan Cruyff", 10, "AFC ajax"),
    Player("Dick van Dijk", 11, "AFC ajax"),
    Player("Johnny Rep", 12, "AFC ajax"),
]
# give data to team class
hometeam = Team("AFC ajax", trainer_hometeam, hometeam_players)
# awayteam data
trainer_awayteam = Trainer("Cor Brom", "Vitesse")
awayteam_players = [
    Player("Dick Beukhof", 13, "Vitesse"),
    Player("Nico Kunst", 14, "Vitesse"),
    Player("Ben Gerritsen", 15, "Vitesse"),
    Player("Willy Melchers", 16, "Vitesse"),
    Player("Ben Bosma", 17, "Vitesse"),
    Player("Bram van Kerkhof", 18, "Vitesse"),
    Player("Herman Veenendaal", 19, "Vitesse"),
    Player("Willy Veenstra", 20, "Vitesse"),
    Player("Co Prins", 21, "Vitesse"),
    Player("Theo Rutten", 22, "Vitesse"),
    Player("Henk Vleeming", 23, "Vitesse"),
    Player("Henk Hofs", 24, "Vitesse"),
    Player("John Meeuwsen", 25, "Vitesse"),
]
# give data to team class
awayteam = Team("Vitesse", trainer_awayteam, awayteam_players)
# goals
goals_in_game_named = [
    Goal("Johan Neeskens", 10),
    Goal("Johan Neeskens", 28),
    Goal("Johan Cruyff", 32),
    Goal("Johan Cruyff", 42),
    Goal("Johan Cruyff", 47),
    Goal("Dick van Dijk", 49),
    Goal("Dick van Dijk", 51),
    Goal("Gerrie Mühren", 63),
    Goal("Barry Hulshoff", 70),
    Goal("Herman Veenendaal", 75),
    Goal("Johan Cruyff", 78),
    Goal("Dick van Dijk", 81),
    Goal("Johan Neeskens", 88),
]


def count_points_for_teams(goals, home, away):
    i = 0
    homepoints = 0
    awaypoints = 0
    for point in goals:
        if point.name in home.get_playernames():
            homepoints += 1
            goals_in_game_named[i].homepoints = homepoints
            goals_in_game_named[i].awaypoints = awaypoints
            i += 1
        if point.name in away.get_playernames():
            awaypoints += 1
            goals_in_game_named[i].homepoints = homepoints
            goals_in_game_named[i].awaypoints = awaypoints
            i += 1


# location class
location = Locatie("Amsterdam", "het De Meer stadion", hometeam)
# referee class
referee = Scheidsrechter("Joop Vervoort")
# game class
wedstrijd = Wedstrijd(
    "19 mei 1972", location, referee, hometeam, awayteam, goals_in_game_named, 6000
)


count_points_for_teams(goals_in_game_named, hometeam, awayteam)
wedstrijd.print_match_report()
