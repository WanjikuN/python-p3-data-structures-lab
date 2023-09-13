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
    name_list=[]
    for food in spicy_foods:
        # print (food)
        name= [value for key, value in food.items()]
        name_list.append(name[0])
    return name_list
       
# get_names(spicy_foods)
def get_spiciest_foods(spicy_foods):
    x=[food for food in spicy_foods if food['heat_level'] > 5 ]
    return x
        
# get_spiciest_foods(spicy_foods)
def print_spicy_foods(spicy_foods):

    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶'*food['heat_level']}" )

# print_spicy_foods(spicy_foods)
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
        x=[food for food in spicy_foods if food["cuisine"] == cuisine ]
        return x[0]
# get_spicy_food_by_cuisine(spicy_foods,"Thai")
def print_spiciest_foods(spicy_foods):
    x=get_spiciest_foods(spicy_foods)
    return print_spicy_foods(x)
# print_spiciest_foods(spicy_foods)
def get_average_heat_level(spicy_foods):
    level=[]
    value= 0
    for food in spicy_foods:
        # print (food)
        name= [value for key, value in food.items()]
        level.append(name[2])
        value += name[2]
    # print(level)
    # print(value)
    # print(len(level))
    return int(value/len(level))
# get_average_heat_level(spicy_foods)
def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)

    return spicy_foods
# create_spicy_food(spicy_foods, {
#                 'name': 'Griot',
#                 'cuisine': 'Haitian',        
#                 'heat_level': 10,
#             })
