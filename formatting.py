def format_labels(players):
    formatted_lines = []
    for player in players:
        number = str(player[0]).ljust(4)
        first_name = player[1].ljust(10)
        last_name = player[2].ljust(12)
        team_coach = f"{player[3]} - {player[4]}"

        formatted_lines.append(f"{number} {first_name} {last_name} {team_coach}\n")
    
    return formatted_lines