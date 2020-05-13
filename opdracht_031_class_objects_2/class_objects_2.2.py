# -------------- opdracht 2------------------


class Team:
    def __init__(self, name, trainer, players):
        self.name = name
        self.trainer = trainer
        self.players = players

    def get_clubname(self):
        print(self.name)
        return self.name

    def get_trainername(self):
        print(self.trainer.name)
        return self.trainer.name

    def get_playernames(self):
        for player in self.players:
            print(player.name)
            return player.name


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

    def get_trainer_name(self):
        return self.name

    def get_trainer_team(self):
        return self.team


class Player:
    def __init__(self, name, number, team):
        self.name = name
        self.number = number
        self.team = team


class Goal:
    def __init__(self, name, minute):
        self.name = name
        self.minute = minute

    def print_goal(self, team):
        print(
            "In de {}e minuut scoort {} voor {},".format(
                self.minute, self.name, self.team.name
            )
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

    def generate_match_report(self):
        home = 0
        away = 0
        print(
            "Op {} speelde {} tegen {} in {} in Amsterdam.".format(
                self.date, self.home.name, self.away.name, self.location.stadium
            )
        )
        print("Er waren {} bezoekers aanwezig in het stadion.".format(self.attendance))
        print("De wedstrijd werd gefloten door {}.".format(self.referee.name))
        print(
            "De trainer voor {} was {}.".format(self.home.name, self.home.trainer.name)
        )
        print(
            "De trainer voor {} was {}.".format(self.away.name, self.away.trainer.name)
        )
        for goal in self.goals:
            for player in self.home.players:
                if goal.name in player.name:
                    home += 1
                    print(
                        "In de {}e minuut scoort {} voor {}, het is {} - {}.".format(
                            goal.minute, goal.name, self.home.name, home, away
                        )
                    )
                else:
                    away += 1
                    print(
                        "In de {}e minuut scoort {} voor {}, het is {} - {}.".format(
                            goal.minute, goal.name, self.away.name, home, away
                        )
                    )

        print("AFC Ajax wint van Vitesse met 12-1")


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
# hometeam data
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
# location class
location = Locatie("Amsterdam", "het De Meer stadion", hometeam)
# referee class
referee = Scheidsrechter("Joop Vervoort")
# game class
wedstrijd = Wedstrijd(
    "19 mei 1972", location, referee, hometeam, awayteam, goals_in_game_named, 6000
)


wedstrijd.generate_match_report()
awayteam.get_clubname()
awayteam.get_trainername()
awayteam.get_playernames()
# goals_in_game_numbered = [
#     Goal(7, 10),
#     Goal(7, 28),
#     Goal(10, 32),
#     Goal(10, 42),
#     Goal(10, 47),
#     Goal(11, 49),
#     Goal(11, 51),
#     Goal(4, 63),
#     Goal(3, 70),
#     Goal(19, 75),
#     Goal(10, 78),
#     Goal(11, 81),
#     Goal(7, 88),
# ]
#
