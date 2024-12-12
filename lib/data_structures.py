spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    fetch_names = []
    for spicy_food in spicy_foods:
        fetch_names.append(spicy_food['name'])
    return fetch_names

def get_spiciest_foods(spicy_foods):
    fetch_spiciest_foods = []
    for spicy_food in spicy_foods:
        if spicy_food["heat_level"] > 5:
            fetch_spiciest_foods.append(spicy_food)
    return fetch_spiciest_foods

def print_spicy_foods(spicy_foods):
    for spicy_food in spicy_foods:
        print (spicy_food['name'] + " (" + spicy_food['cuisine'] + ") | Heat Level: " + "🌶" * spicy_food['heat_level'])
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for spicy_food in spicy_foods:
        if spicy_food['cuisine'] == cuisine:
            return spicy_food

def print_spiciest_foods(spicy_foods):
    for spicy_food in get_spiciest_foods(spicy_foods):
        print (spicy_food['name'] + " (" + spicy_food['cuisine'] + ") | Heat Level: " + "🌶" * spicy_food['heat_level'])

def get_average_heat_level(spicy_foods):
    total_heat_level = 0
    for spicy_food in spicy_foods:
        total_heat_level += spicy_food['heat_level']
    return total_heat_level / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods