# Report functions
def count_games(file_name):
    number = len(open(file_name).readlines())
    return number


def decide(file_name, year):
    year = str(year)
    if year in open(file_name).read():
        return True
    else:
        return False


def get_latest(file_name):
    data = [word.split('\t') for word in open(file_name, "r").readlines()]
    year = 2018
    counter = 0
    while counter < year:
        for a in data:
            if str(year) in a:
                return a[0]
        year -= 1
        counter += 1


def count_by_genre(file_name, genre):
    data = [word.split('\t') for word in open(file_name, "r")]
    a = 0
    gameGenre = []
    while a < len(open(file_name).readlines()):
        gameGenre.append(data[a][3])
        a += 1
    return len(set(gameGenre))


def get_line_number_by_title(file_name, title):
    data = [word.split('\t') for word in open(file_name, "r")]
    number = 0
    for a in data:
        number += 1
        if title in a:
            return number


def get_genres(file_name):
    data = [word.split('\t') for word in open(file_name, "r")]
    a = 0
    gameGenre = []
    while a < len(open(file_name).readlines()):
        gameGenre.append(data[a][3])
        a += 1
    gameGenre = set(gameGenre)
    gameGenre = sorted(gameGenre)
    return gameGenre


def get_most_played(file_name):
    data = [word.split('\t') for word in open(file_name, "r")]
    a = 0
    copiesSold = []
    while a < len(open(file_name).readlines()):
        copiesSold.append(float(data[a][1]))
        a += 1
    number = copiesSold.index(max(copiesSold))
    return data[number][0]


def sum_sold(file_name):
    data = [word.split('\t') for word in open(file_name, "r")]
    a = 0
    sumSold = []
    while a < len(open(file_name).readlines()):
        sumSold.append(float(data[a][1]))
        a += 1
    number = sum(sumSold)
    return number


def get_selling_avg(file_name):
    data = [word.split('\t') for word in open(file_name, "r")]
    a = 0
    avgSold = []
    while a < len(open(file_name).readlines()):
        avgSold.append(float(data[a][1]))
        a += 1
    number = sum(avgSold) / len(open(file_name).readlines())
    return number


def count_longest_title(file_name):
    data = [word.split('\t') for word in open(file_name, "r")]
    a = 0
    longestName = []
    while a < len(open(file_name).readlines()):
        longestName.append(len(data[a][0]))
        a += 1
    number = max(longestName)
    return number


def get_date_avg(file_name):
    data = [word.split('\t') for word in open(file_name, "r")]
    a = 0
    avgSold = []
    while a < len(open(file_name).readlines()):
        avgSold.append(float(data[a][2]))
        a += 1
    number = sum(avgSold) / len(open(file_name).readlines())
    if (sum(avgSold) % len(open(file_name).readlines())) / len(open(file_name).readlines()) > 0.5:
        number += 1
    return int(number)


def get_game(file_name, title):
    data = [word.split('\t') for word in open(file_name, "r")]
    for a in data:
        if title in a:
            return a
    return "There is no game " + title + ". Check the spelling."

