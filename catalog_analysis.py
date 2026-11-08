import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155,
     "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]


def average_rating(movies):
    score_count = 0
    for i in range(len(movies)):
        score = movies[i]
        score_count += score["rating"]
    overage = round(score_count / len(movies), 1)
    return (overage)


def catalog_age_stats(movies, current_year=2026):
    ages = []
    for movie in movies:
        year = movie["year"]
        ages.append(current_year - year)

    oldest = max(ages)
    newest = min(ages)
    average = math.ceil(sum(ages) / len(ages))

    return (oldest, newest, average)


def duration_in_hours(minutes):
    hours = minutes // 60
    min = minutes % 60
    return (f"{hours}ч" ' ' f"{min}м")


def rating_tier(rating):
    if rating >= 9:
        return 'шедевр'
    elif rating >= 7:
        return 'хорошо'
    return 'средне' if rating >= 5 else "слабо"


def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"


for movie in movies:
    if 'comedy' in movie["genres"]:
        continue
    print(movie["title"])

count = 0
while count < len(movies):
    if (movies[count]["rating"]) > 9:
        print('шедевр', (movies[count]["title"]))
        break
    else:
        count += 1
else:
    print("Шедевров не найдено")

    
def count_long_movies(movies, threshold=120):
    count=0
    for movie in movies:
        if movie["duration_min"]>threshold:
            count+=1
    return count

def normalize_title(title):
    changed_words = []
    title = title.split()
    for i in title:
         changed_words.append(i[0].upper()+i[1:])
    return(" ".join(changed_words))

def make_slug(title):
    lower_title = title.lower()
    return lower_title.replace(" ", "-")

def format_report_line(movie):
    title = normalize_title(movie["title"])
    year = movie["year"]
    rating = movie["rating"]
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))

    return f'"{title}" ({year}) — {rating}/10, {duration}, жанры: {genres}'

def titles_sorted_by_rating(movies):
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)

    titles = []
    for movie in sorted_movies:
        titles.append(movie["title"])
    return titles

def top_n_by_rating(movies, n=3):
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)

    top = []
    for movie in sorted_movies[:n]:
        top.append((movie["title"], movie["rating"]))
    return top

def count_by_genre(movies):
    counts = {}
    for movie in movies:
        for genre in movie["genres"]:
            counts[genre] = counts.get(genre, 0) + 1
    return counts


def actor_filmography(movies):
    filmography = {}
    for movie in movies:
        for actor in movie["actors"]:
            if actor not in filmography:
                filmography[actor] = []
            filmography[actor].append(movie["title"])
    return filmography


def ratings_above_average(movies):
    average = average_rating(movies)
    return {
        movie["title"]: movie["rating"]
        for movie in movies
        if movie["rating"] > average
    }

def all_genres(movies):
    genres = set()
    for movie in movies:
        genres.update(movie["genres"])
    return genres


def common_actors(movie1, movie2):
    actors1 = set(movie1["actors"])
    actors2 = set(movie2["actors"])
    return actors1 & actors2


def genres_only_in_one(movies_a, movies_b):
    return all_genres(movies_a) - all_genres(movies_b)
