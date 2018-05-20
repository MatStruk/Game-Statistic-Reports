import reports

def export_report(file):
    filename = open("export_report.txt", "w")
    filename.write(str(reports.count_games(file)) + "\n")
    filename.write(str(reports.decide(file, 2005)) + "\n")
    filename.write(str(reports.get_latest(file)) + "\n")
    filename.write(str(reports.count_by_genre(file, "eh")) + "\n")
    filename.write(str(reports.get_line_number_by_title(file, "Diablo III")) + "\n")
    filename.write(str(reports.get_genres(file))  + "\n")
    pass


export_report("game_stat.txt")