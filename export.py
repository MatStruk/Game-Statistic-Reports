import reports


def export_report(file):
    filename = open("export_report.txt", "w")
    filename.write(str(reports.count_games(file)) + "\n")
    filename.write(str(reports.decide(file, 2005)) + "\n")
    filename.write(str(reports.get_latest(file)) + "\n")
    filename.write(str(reports.count_by_genre(file, "eh")) + "\n")
    filename.write(str(reports.get_line_number_by_title(file, "Diablo III")) + "\n")
    filename.write(str(reports.get_genres(file)) + "\n")
    filename.write(str(reports.get_most_played) + "\n")
    filename.write(str(reports.sum_sold("game_stat.txt")) + "\n")
    filename.write(str(reports.get_selling_avg("game_stat.txt")) + "\n")
    filename.write(str(reports.count_longest_title("game_stat.txt")) + "\n")
    filename.write(str(reports.get_date_avg("game_stat.txt")) + "\n")
    pass




export_report("game_stat.txt")
