# STEP 1 Modélisation des Produits et Composition

class Ingredient:
    def __init__(self, name):
        self.name = name


class Pizza:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.ingredients = []  # Initialize the ingredients list
    
    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)
    
    def afficher_ingredients(self):
        for ingredient in self.ingredients:
            print(ingredient.name)



# Créer des ingrédients
tomato = Ingredient("Tomato")
cheese = Ingredient("Cheese")
pepperoni = Ingredient("Pepperoni")
mushroom = Ingredient("Mushroom")
onion = Ingredient("Onion")
olive = Ingredient("Olive")
ham = Ingredient("Ham")
pineapple = Ingredient("Pineapple")
bacon = Ingredient("Bacon")

# Créer des pizzas
margarita = Pizza("Margarita", 13.90)
margarita.add_ingredient(tomato)
margarita.add_ingredient(cheese)
margarita.add_ingredient(olive)
margarita.add_ingredient(onion)
margarita.add_ingredient(mushroom)

pepperoni_pizza = Pizza("Pepperoni", 11.90)
pepperoni_pizza.add_ingredient(tomato)
pepperoni_pizza.add_ingredient(cheese)
pepperoni_pizza.add_ingredient(pepperoni)

#Fonction pour afficher les pizzas, leur taille, leur prix ainsi que leurs ingrédients
def afficher_pizzas(pizzas):
    for pizza in pizzas:
        print(f"Name: {pizza.name}", pizza.price)
        print("Ingredients:")
        for ingredient in pizza.ingredients:
            print(f"- {ingredient.name}")
        print("Available sizes: M, L, XL \n")
        print()  # Add a blank line between pizzas


# Afficher les pizzas disponibles
pizzas = [margarita, pepperoni_pizza]
afficher_pizzas(pizzas)



class Drink:
    def __init__(self, name, volume, price):
        self.name = name
        self.volume = volume
        self.price = price

cocacola = Drink("Coca-Cola", 500, 2)
sprite = Drink("Sprite", 500, 2)
# STEP 2 :  Gestion des Commandes (Agrégation)

lvide=[]

class Order: 
    def __init__(self, order_id, lvide):
        self.order_id = order_id
        self.products = lvide
    
    def add_product(self, product):
        self.products.append(product)
    
    def total(self):
        total = 0
        for product in self.products:
            total = total + product.price
        return total

order = Order(1, [])
order.add_product(margarita)
order.add_product(sprite)
print(f"Total order price: {order.total()} euros")

# STEP 3 :  Factory et Pattern Matching pour la Création des Produits
