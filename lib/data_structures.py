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
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    spicy_emoji = '🌶'
    formatted_foods = [
        f"{food['name']} ({food['cuisine']}) | Heat Level: {spicy_emoji * food['heat_level']}"
        for food in spicy_foods
    ]
    for formatted_food in formatted_foods:
        print(formatted_food)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    matching_foods = [food for food in spicy_foods if food['cuisine'].lower() == cuisine.lower()]
    
    if matching_foods:
        return matching_foods[0]
    else:
        return None

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    return print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):
    if not spicy_foods:
        return 0 
    total_heat_level = sum(food['heat_level'] for food in spicy_foods)
    return total_heat_level / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    return spicy_foods + [spicy_food]
