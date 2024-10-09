import json
# STEP 1 Modélisation des Produits et Composition
#Création de la classe Ingrédient
class Ingredient:
    def __init__(self, nom):
        self.nom = nom

#Création de la classe Pizza

class Pizza:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix
        self.garnitures = []
    
    def add_ingredient(self, ingredient):
        self.garnitures.append(ingredient)
    
    def afficher_garnitures(self):
        for ingredient in self.garnitures:
            print(ingredient.nom)
    
    def __str__(self):
        garnitures_str = ", ".join([ingredient.nom for ingredient in self.garnitures])
        return f"Pizza: {self.nom}, Prix: {self.prix} euros, Garnitures: {garnitures_str}"




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
        print(f"nom: {pizza.nom}", pizza.prix)
        print("garnitures:")
        for ingredient in pizza.garnitures:
            print(f"- {ingredient.nom}")
        print("Available tailles: M, L, XL \n")
        print()  # Add a blank line between pizzas


# Afficher les pizzas disponibles
pizzas = [margarita, pepperoni_pizza]
afficher_pizzas(pizzas)



class Boisson:
    def __init__(self, nom, volume, prix):
        self.nom = nom
        self.volume = volume
        self.prix = prix

    def __str__(self):
        return f"Boisson: {self.nom}, Volume: {self.volume}ml, Prix: {self.prix} euros"

cocacola = Boisson("Coca-Cola", 500, 2)
sprite = Boisson("Sprite", 500, 2)
# STEP 2 :  Gestion des Commandes (Agrégation)

lvide=[]

class Order: 
    def __init__(self, order_id):
        self.order_id = order_id
        self.produits = []
    
    def add_product(self, product):
        self.produits.append(product)
    
    def total(self):
        total = 0
        for product in self.produits:
            total = total + product.prix
        return total

order = Order(1)
order.add_product(margarita)
order.add_product(sprite)
print(f"Total order prix: {order.total()} euros")


# STEP 3 :  Factory et Pattern Matching pour la Création des Produits
class ProductFactory:
    def create_product(self, product_type, *args):
        match product_type:
            case "Pizza":
                return self.create_pizza(*args)
            case "boisson":
                return self.create_boisson(*args)
            case _:
                raise ValueError(f"Unknown product type: {product_type}")
    
    def create_pizza(self, nom, prix):
        pizza = Pizza(nom, prix)
        return pizza
    
    def create_boisson(self, nom, volume, prix):
        return Boisson(nom, volume, prix)

# Lecture du fichier commandes.json et menu.json
def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

menu = load_json('menu.json')
commandes = load_json('commandes.json')

factory = ProductFactory()

available_boissons = {boisson['nom']: boisson for boisson in menu['boissons']}

# Traitement des commandes
for commande in commandes:
    order = Order(commande['commande_id'])
    
    for item in commande['items']:
        if item in available_boissons:
            boisson_info = available_boissons[item]
            boisson = factory.create_product("boisson", boisson_info['nom'], boisson_info['volume'], boisson_info['prix'])
            order.add_product(boisson)
        else:
            pizza = factory.create_product("Pizza", item, 12.0)  # Prix par défaut si non fourni
            order.add_product(pizza)
    
    print(f"Total pour la commande {order.order_id}: {order.total()} euros")
    for produit in order.produits:
        print(produit)
    print()  # Ajoute une ligne vide entre les commandes