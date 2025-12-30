from collections import defaultdict


def pigeon_sort(arr: list[tuple[str, int]], max_rating: int) -> list[tuple[str, int]]:
    rating_store = defaultdict(list)
    for name, rating in arr:
        rating_store[rating].append((name, rating))
    print(rating_store)
    return [player for i in range(max_rating, 0, -1) if i in rating_store for player in rating_store[i]]



if __name__ == '__main__':
    chess_players = [
        ('Гукеш Доммараджу', 2758),
        ('Фабиано Каруана', 2786),
        ('Уэсли Со', 2753),
        ('Магнус Карлсен', 2839),
        ('Дин Лижэнь', 2780),
        ('Ян Непомнящий', 2771),
        ('Аниш Гири', 2760),
        ('Вишванатан Ананд', 2754),
        ('Алиреза Фирузджа', 2777),
        ('Хикару Накамура', 2780),

    ]

    print(pigeon_sort(chess_players, 3000))
