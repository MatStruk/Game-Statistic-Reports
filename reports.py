# Report functions
def count_games(file_name):
    try:
        f = open(file_name)
        number = len(f.readlines())
    finally:
        f.close()
    return number


def decide(file_name, year):
    year = str(year)
    try:
        f = open(file_name)
        if year in f.read():
            return True
        else:
            return False
    finally:
        f.close()


def get_latest(file_name):
    try:
        f = open(file_name)
        data = [word.split('\t') for word in f.readlines()]
        year = 2018
        counter = 0
        while counter < year:
            for a in data:
                if str(year) in a:
                    return a[0]
            year -= 1
            counter += 1
    finally:
        f.close()


def count_by_genre(file_name, genre):
    try:
        f = open(file_name)
        data = [word.split('\t') for word in f.readlines()]
        gameGenre = []
        for a in data:
            if genre in a:
                gameGenre.append(a[0])
        return len(set(gameGenre))
    finally:
        f.close()


def get_line_number_by_title(file_name, title):
    try:
        f = open(file_name)
        data = [word.split('\t') for word in f.readlines()]
        number = 0
        for a in data:
            number += 1
            if title in a:
                return number
    finally:
        f.close()


def get_genres(file_name):
    try:
        f = open(file_name)
        data = [word.split('\t') for word in f.readlines()]
        a = 0
        gameGenre = []
        while a < len(data):
            gameGenre.append(data[a][3])
            a += 1
        gameGenre = set(gameGenre)
        gameGenre = sorted(gameGenre)
        return gameGenre
    finally:
        f.close()


def get_most_played(file_name):
    try:
        f = open(file_name)
        data = [word.split('\t') for word in f.readlines()]
        a = 0
        copiesSold = []
        while a < len(data):
            copiesSold.append(float(data[a][1]))
            a += 1
        number = copiesSold.index(max(copiesSold))
        return data[number][0]
    finally:
        f.close()


def sum_sold(file_name):
    try:
        f = open(file_name)
        data = [word.split('\t') for word in f.readlines()]
        a = 0
        sumSold = []
        while a < len(data):
            sumSold.append(float(data[a][1]))
            a += 1
        number = sum(sumSold)
        return number
    finally:
        f.close()


def get_selling_avg(file_name):
    try:
        f = open(file_name)
        data = [word.split('\t') for word in f.readlines()]
        a = 0
        avgSold = []
        while a < len(data):
            avgSold.append(float(data[a][1]))
            a += 1
        number = sum(avgSold) / len(open(file_name).readlines())
        return number
    finally:
        f.close()


def count_longest_title(file_name):
    try:
        f = open(file_name)
        data = [word.split('\t') for word in f.readlines()]
        a = 0
        longestName = []
        while a < len(data):
            longestName.append(len(data[a][0]))
            a += 1
        number = max(longestName)
        return number
    finally:
        f.close()


def get_date_avg(file_name):
    try:
        f = open(file_name)
        data = [word.split('\t') for word in f.readlines()]
        a = 0
        avgSold = []
        while a < len(data):
            avgSold.append(float(data[a][2]))
            a += 1
        number = sum(avgSold) / len(data)
        if (sum(avgSold) % len(data) / len(data)) > 0.5:
            number += 1
        return int(number)
    finally:
        f.close()


def get_game(file_name, title):
    try:
        f = open(file_name)
        data = [word.split('\t') for word in f.readlines()]
        for a in data:
            if title in a:
                return a
        return "There is no game " + title + ". Check the spelling."
    finally:
        f.close()


def sort_abc(file_name):
    ...


def when_was_top_sold_fps(file_name):
    ...