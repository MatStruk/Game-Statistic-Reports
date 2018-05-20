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
    a = 0
    b = 1
    gameGenre = sorted(gameGenre)
    return gameGenre

