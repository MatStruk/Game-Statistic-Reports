import reports


print(reports.count_games("game_stat.txt"))
print(reports.decide("game_stat.txt", 2005))
print(reports.get_latest("game_stat.txt"))
print(reports.count_by_genre("game_stat.txt", "eh"))
print(reports.get_line_number_by_title("game_stat.txt", "Diablo III"))
print(reports.get_genres("game_stat.txt"))
# Printing functions
