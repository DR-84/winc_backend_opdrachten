ajax_vitesse_1972_05_12 = [
    {"full_name": "Heinz Stuy", "id": 1, "team_name": "Ajax"},
    {"full_name": "Horst Blankenburg", "id": 2, "team_name": "Ajax"},
    {"full_name": "Barry Hulshoff", "id": 3, "team_name": "Ajax"},
    {"full_name": "Gerrie Mühren", "id": 4, "team_name": "Ajax"},
    {"full_name": "Ruud Krol", "id": 5, "team_name": "Ajax"},
    {"full_name": "Wim Suurbier", "id": 6, "team_name": "Ajax"},
    {"full_name": "Johan Neeskens", "id": 7, "team_name": "Ajax"},
    {"full_name": "Sjaak Swart", "id": 8, "team_name": "Ajax"},
    {"full_name": "Arie Haan", "id": 9, "team_name": "Ajax"},
    {"full_name": "Johan Cruyff", "id": 10, "team_name": "Ajax"},
    {"full_name": "Dick van Dijk", "id": 11, "team_name": "Ajax"},
    {"full_name": "Johnny Rep", "id": 12, "team_name": "Ajax"},
    {"full_name": "Dick Beukhof", "id": 13, "team_name": "Vitesse"},
    {"full_name": "Nico Kunst", "id": 14, "team_name": "Vitesse"},
    {"full_name": "Ben Gerritsen", "id": 15, "team_name": "Vitesse"},
    {"full_name": "Willy Melchers", "id": 16, "team_name": "Vitesse"},
    {"full_name": "Ben Bosma", "id": 17, "team_name": "Vitesse"},
    {"full_name": "Bram van Kerkhof", "id": 18, "team_name": "Vitesse"},
    {"full_name": "Herman Veenendaal", "id": 19, "team_name": "Vitesse"},
    {"full_name": "Willy Veenstra", "id": 20, "team_name": "Vitesse"},
    {"full_name": "Co Prins", "id": 21, "team_name": "Vitesse"},
    {"full_name": "Theo Rutten", "id": 22, "team_name": "Vitesse"},
    {"full_name": "Henk Vleeming", "id": 23, "team_name": "Vitesse"},
    {"full_name": "Henk Hofs", "id": 24, "team_name": "Vitesse"},
    {"full_name": "John Meeuwsen", "id": 25, "team_name": "Vitesse"},
]

goal_list = [
    {"id": 7, "time": 10},
    {"id": 7, "time": 28},
    {"id": 10, "time": 32},
    {"id": 10, "time": 42},
    {"id": 10, "time": 47},
    {"id": 11, "time": 49},
    {"id": 11, "time": 51},
    {"id": 4, "time": 63},
    {"id": 3, "time": 70},
    {"id": 19, "time": 75},
    {"id": 10, "time": 78},
    {"id": 11, "time": 81},
    {"id": 7, "time": 88},
]


# -------------- opdracht 1------------------


def who_won(goals, players):
    team1 = []
    team2 = []
    for goal in goals:
        for player in players:
            team = player["team_name"]
            if goal["id"] == player["id"]:
                if team in team1 or len(team1) == 0:
                    team1.append(team)
                else:
                    team2.append(team)

    if len(team1) > len(team2):
        winner = team1
        loser = team2
    else:
        winner = team2
        loser = team1

    win_points = str(len(winner))
    lose_points = str(len(loser))
    print(winner[0], "wint van", loser[0], "met", win_points, "-", lose_points)


# -------------- opdracht 2------------------


def print_match_report(goals, players):
    home = 0
    away = 0
    for goal in goals:
        score_time = goal["time"]
        for player in players:
            if goal["id"] == player["id"]:
                player_scored = player["full_name"]
                score_time = goal["time"]
                team = player["team_name"]
                if team == "Ajax":
                    home += 1
                else:
                    away += 1
                print(
                    "in de",
                    str(score_time) + "e minuut scoort",
                    player_scored,
                    "voor",
                    team,
                    ", het is",
                    str(home),
                    "-",
                    str(away),
                )


print_match_report(goal_list, ajax_vitesse_1972_05_12)
who_won(goal_list, ajax_vitesse_1972_05_12)
