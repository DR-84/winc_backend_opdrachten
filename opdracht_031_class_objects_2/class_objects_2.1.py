# is het idee van de opdracht dat we onze code/functions uit "return value"
# herschrijven? of gaat het het om het eind resultaat.

# -------------- opdracht 1------------------


class Player:
    def __init__(self, name, num, team):
        self.full_name = name
        self.id = num
        self.team = team


class Goals:
    def __init__(self, num, minute):
        self.id = num
        self.minute = minute


player_list = [
    Player("Heinz Stuy", 1, "AFC Ajax"),
    Player("Horst Blankenburg", 2, "AFC Ajax"),
    Player("Barry Hulshoff", 3, "AFC Ajax"),
    Player("Gerrie Mühren", 4, "AFC Ajax"),
    Player("Ruud Krol", 5, "AFC Ajax"),
    Player("Wim Suurbier", 6, "AFC Ajax"),
    Player("Johan Neeskens", 7, "AFC Ajax"),
    Player("Sjaak Swart", 8, "AFC Ajax"),
    Player("Arie Haan", 9, "AFC Ajax"),
    Player("Johan Cruyff", 10, "AFC Ajax"),
    Player("Dick van Dijk", 11, "AFC Ajax"),
    Player("Johnny Rep", 12, "AFC Ajax"),
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


goal_list = [
    Goals(7, 10),
    Goals(7, 28),
    Goals(10, 32),
    Goals(10, 42),
    Goals(10, 47),
    Goals(11, 49),
    Goals(11, 51),
    Goals(4, 63),
    Goals(3, 70),
    Goals(19, 75),
    Goals(10, 78),
    Goals(11, 81),
    Goals(7, 88),
]

home_team = "Ajax"


def who_won(goals, players):
    team1_goals = []
    team2_goals = []
    for goal in goals:
        for player in players:
            team = player.team
            if goal.id == player.id:
                if team in team1_goals or len(team1_goals) == 0:
                    team1_goals.append(team)
                else:
                    team2_goals.append(team)

    if len(team1_goals) > len(team2_goals):
        winner = team1_goals
        loser = team2_goals
    else:
        winner = team2_goals
        loser = team1_goals

    win_points = str(len(winner))
    lose_points = str(len(loser))
    return f"{winner[0]} wint van {loser[0]} met {win_points}-{lose_points}."


def get_goal_info(players, goal):
    for player in players:
        if goal.id == player.id:
            minute = goal.minute
            player_name = player.full_name
            team_name = player.team
            return {
                "minute": minute,
                "player_name": player_name,
                "team_name": team_name,
            }


def print_match_report(items):
    for item in items:
        print(item)


def generate_match_report(players, goals):
    report_lines = []
    home = 0
    away = 0
    for goal in goals:
        goals_full_info = []
        goals_full_info.append(get_goal_info(players, goal))
        for goals in goals_full_info:
            if goals["team_name"] is home_team:
                home += 1
            if goals["team_name"] is not home_team:
                away += 1
            line = f"In de {goals['minute']}e minuut "
            line += f"scoort {goals['player_name']} voor "
            line += f"{goals['team_name']} het is {home}-{away}."

            report_lines.append(line)
    report_lines.append(who_won(goal_list, player_list))
    return report_lines


print_match_report(generate_match_report(player_list, goal_list))
