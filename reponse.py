"""
Exercice 1 : Classe Abstraite Simple

Créez une classe abstraite Shape avec une méthode abstraite area().
Implémentez deux classes dérivées : Circle et Rectangle.
Chaque classe devra implémenter sa propre version de la méthode area().
"""
import math
import pytest

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
# Test du code
circle = Circle(5)
assert pytest.approx(circle.area(), 0.01) == 78.54

rectangle = Rectangle(4, 6)
assert rectangle.area() == 24

# Test pour vérifier que la classe Shape ne peut pas être instanciée
try:
    Shape()
except TypeError as e:
    assert str(e) == "Subclasses must implement this method"

"""
Exercice 2 : Surcharge d'Opérateurs

Créez une classe BankAccount avec un solde initial.
Surchargez les opérateurs + et - pour permettre d’ajouter ou retirer de l’argent du compte bancaire en utilisant ces opérateurs.
"""
class BankAccount():
    def __init__(self, balance):
        self.balance = balance

    def __add__(self, amount):
        self.balance += amount
        return self

    def __sub__(self, amount):
        self.balance -= amount
        return self

account = BankAccount(100)
account += 50  # Ajoute 50 euros
assert account.balance == 150

account -= 20  # Retire 20 euros
assert account.balance == 130


"""
Exercice 3 : Décorateurs

Créez un décorateur @check_positive qui vérifie si le nombre passé en argument à une fonction est positif. 
Si le nombre est négatif, levez une exception ValueError.
"""

def check_positive(func):
    def wrapper(x):
        if x < 0:
            raise ValueError("Le nombre doit être positif")
        return func(x)
    return wrapper

@check_positive
def double(x):
    return x*2

assert double(5) ==10


try: 
    double(-1)
except ValueError:
    print("Le nombre doit être positif")
    

"""
Exercice 4 : Propriétés (Property)
Créez une classe Car avec un attribut privé speed.
Utilisez le décorateur @property pour lire la vitesse et un setter pour la modifier. 
La vitesse ne peut pas dépasser 200 km/h (et doit être > 0), sinon une exception ValueError est levée.
""" 
class Car():
    def __init__(self):
        self._speed = 0

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if value <= 0 or value > 200:
            raise ValueError("Vitesse non valide")
        self._speed = value

car = Car()
car.speed = 120
assert car.speed == 120

try:
    car.speed = 250  # Doit lever une exception
except ValueError:
    print("Vitesse non valide")
    

"""
Exercice 5 : Gestion des Exceptions
Créez une classe Person qui prend un nom et un âge en entrée.
Utilisez une exception personnalisée InvalidAgeError pour lever une erreur si l’âge est négatif ou supérieur à 150 ans.
"""

class AgeError(Exception):
    def __init__(self, message="L'âge doit être compris entre 0 et 150"):
        super().__init__(message)

class Person:
    def __init__(self, name, age):
        if age < 0 or age > 150:
            raise AgeError()
        self.name = name
        self.age = age


try:
    personne = Person("Alice", -5)  # Ceci va déclencher l'exception
except AgeError as e:
    print(f"Erreur : {e}")


    
    
    
"""Exercice 6 : Singleton et context manager
Implémentez un pattern Singleton pour une classe DatabaseConnection qui garantit qu’il n’existe qu’une seule instance de connexion à la base de données.
L'instance de cette classe doit permettre de créer un context (qui, lui, n'est pas unique), et qui permet d'ajouter une entrée (id, data), de la supprimer par id, ou de drop toutes les lignes.
Les opérations doivent être exécutées (flush) une fois le context fermé.
"""
class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.entries = []  # Utiliser self.entries pour stocker les données
        return cls._instance

    def __enter__(self):
        return DbContext(self)

    def __exit__(self, exc_type, exc_value, traceback):
        self.flush()  # Flushing data when exiting the context

    def add_entry(self, entry):
        self.entries.append(entry)

    def remove_by_id(self, entry_id):
        self.entries = [entry for entry in self.entries if entry["id"] != entry_id]

    def drop_all(self):
        self.entries = []

    def flush(self):
        print("Flushed data:", self.entries)

class DbContext:
    def __init__(self, db):
        self.db = db

    def __enter__(self):
        return self.db

    def __exit__(self, exc_type, exc_value, traceback):
        self.db.flush()  # Flush data on exit




"""
Exercice 7 : Factory Pattern
Créez une factory pour générer des objets Circle ou Rectangle (héritant d'une classe abstraite Shape) en fonction d’un paramètre passé à une méthode create.
Vous devez pouvoir choisir quelle forme créer en fonction des paramètres fournis.
"""
class ShapeFactory():
    @staticmethod
    def create(shape, **kwargs):
        if shape == "circle":
            return Circle(**kwargs)
        elif shape == "rectangle":
            return Rectangle(**kwargs)
        else:
            raise ValueError("Forme non valide")

"""
Exercice 8 : Décorateurs avec Paramètres
Créez un décorateur @timeout_limit qui prend un paramètre indiquant une limite de temps en secondes (timeout).
Si une fonction prend plus de temps que cette limite pour s’exécuter, le décorateur devra lever une exception TimeoutError.

Exercice 8 Bonus : Avec un thread 
Même chose, mais le décorateur prend un paramètre supplémentaire raise_exception, ayant la valeur par défaut à False.
Si la valeur est True, vous devez lever une exception même si la fonction n'est pas terminée (vous devez interrompre l'action en cours).
"""
import time
import pytest

class TimeoutError(Exception):
    def __init__(self, message="Timeout Error"):
        super().__init__(message)

def timeout_limit(timeout, raise_exception=False):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            elapsed = end - start
            if elapsed > timeout:
                if raise_exception:
                    raise TimeoutError()
                else:
                    raise TimeoutError("Function execution time exceeded")
            return result
        return wrapper
    return decorator

@timeout_limit(1, raise_exception=True)  # Par exemple, 1 seconde de timeout
def long_running_function():
    time.sleep(2)  # Simule une exécution longue


"""
Exercice 9 : Opérateurs Avancés
Créez une classe Matrix et surchargez les opérateurs + et * pour permettre l'addition et la multiplication de matrices.
Gérez les exceptions si les matrices ne sont pas de tailles compatibles.*
"""
class Matrix:
    def __init__(self, matrix):
        self.values = matrix  # Utiliser self.values pour stocker les valeurs

    def __add__(self, other):
        if len(self.values) != len(other.values) or len(self.values[0]) != len(other.values[0]):
            raise ValueError("Les matrices doivent être de même taille")
        return Matrix([[self.values[i][j] + other.values[i][j] for j in range(len(self.values[0]))] for i in range(len(self.values))])

    def __mul__(self, other):
        if len(self.values[0]) != len(other.values):
            raise ValueError("Les matrices doivent être de tailles compatibles")
        return Matrix([[sum(self.values[i][k] * other.values[k][j] for k in range(len(self.values[0]))) for j in range(len(other.values[0]))] for i in range(len(self.values))])


"""
Exercice 10 : Classes abstraites & Factory 
Créez une classe abstraite Animal avec une méthode abstraite speak().
Implémentez des classes dérivées Dog et Cat.
Ensuite, implémentez une factory AnimalFactory qui génère une instance de Dog ou Cat en fonction des paramètres d'entrée.
Les paramètres sont :
animal_type : une chaîne de caractères contenant soit "dog" soit "cat" (ou autre).
name : une chaîne de caractères contenant le nom de l'animal.
"""
class Animal():
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

class AnimalFactory():
    @staticmethod
    def create(animal_type, name):
        if animal_type == "dog":
            return Dog(name)
        elif animal_type == "cat":
            return Cat(name)
        else:
            raise ValueError("Type d'animal non valide")

"""Exercice 11 : Surcharge d'Opérateurs (Comparaison)

Créez une classe Product avec des attributs name et price.
Surchargez les opérateurs de comparaison (==, <, >, etc.) pour comparer des objets Product en fonction de leur prix.

Exercice 11 Bonus : Surcharge d'Opérateurs (Comparaison Avancée)

Créez une fonction top_products(products, k) qui prend en paramètre une liste de produits et un entier k, et qui retourne les k produits les plus chers.
"""
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.price == other.price

    def __lt__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.price < other.price

    def __gt__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.price > other.price

    def __le__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.price <= other.price

    def __ge__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.price >= other.price

    def __ne__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.price != other.price

    @staticmethod
    def top_product(products, k):
        sorted_products = sorted(products, key=lambda product: product.price, reverse=True)
        return sorted_products[:k]


"""Exercice 12 : Propriétés et Gestion d’Exceptions

Créez une classe Account avec une propriété balance.
Si un dépôt est inférieur à 0 ou si un retrait rend le solde négatif, une exception ValueError doit être levée.
Utilisez le décorateur @property pour gérer les accès et modifications du solde.


account = Account()
account.balance = 100

try:
    account.balance -= 150  # Doit lever une exception
except ValueError:
    print("Solde insuffisant")
"""
class Account:
    def __init__(self, initial_balance=0):
        if initial_balance < 0:
            raise ValueError("Le solde initial ne peut pas être négatif")
        self._balance = initial_balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Le solde ne peut pas être négatif")
        self._balance = value

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Le montant déposé ne peut pas être négatif")
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Le montant retiré ne peut pas être négatif")
        if amount > self._balance:
            raise ValueError("Solde insuffisant")
        self.balance -= amount

    def __iadd__(self, amount):
        self.deposit(amount)
        return self

    def __isub__(self, amount):
        self.withdraw(amount)
        return self



# Exemple d'utilisation
try:
    account = Account(500)
    account.balance -= 150  # Doit lever une exception
except ValueError:
    print("Solde insuffisant")

"""Exercice 13 : Surcharge d'Opérateurs

Créez une classe Vector représentant un vecteur mathématique à deux dimensions.
Implémentez les opérations de +, -, et *.


v1 = Vector(1, 2)
v2 = Vector(3, 4)

v3 = v1 + v2
assert v3.x == 4 and v3.y == 6

v4 = v1 * 2
assert v4.x == 2 and v4.y == 4
"""
class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

v1 = Vector(1, 2)
v2 = Vector(3, 4)

v3 = v1 + v2
assert v3.x == 4 and v3.y == 6

v4 = v1 * 2
assert v4.x == 2 and v4.y == 4

"""
Exercice 14 : Mock et Monkey-Patch
Créez une classe MockFunction qui prend une return_value à la création et se comporte comme une fonction en retournant cette valeur.
Créez une fonction patch qui permet de remplacer une fonction par un mock pour la durée d'un contexte (with).
La fonction patch doit être un context manager, et tant que l’on est dans le contexte, c’est la fonction mockée qui est appelée.
"""
class MockFunction():
    def __init__(self, return_value):
        self.return_value = return_value

    def __call__(self):
        return self.return_value

class patch():
    def __init__(self, original_function, return_value):
        self.original_function = original_function
        self.return_value = return_value

    def __enter__(self):
        self.original_function = MockFunction(self.return_value)
        return self.original_function

    def __exit__(self, exc_type, exc_value, traceback):
        pass
"""
Exercice 15 : Classes Génériques et Méthodes Statistiques
Créez une classe générique Statistics qui accepte une liste de nombres et fournit des méthodes pour calculer la moyenne, la médiane et la variance des données.
Utilisez le module statistics pour vous aider.
"""
from statistics import mean, median, variance

class Statistics:
    def __init__(self, data):
        self.data = data

    def mean(self):
        return sum(self.data) / len(self.data)

    def median(self):
        data = sorted(self.data)
        n = len(data)
        if n % 2 == 0:
            return (data[n // 2 - 1] + data[n // 2]) / 2
        else:
            return data[n // 2]

    def variance(self):
        mean_value = self.mean()
        return sum((x - mean_value) ** 2 for x in self.data) / len(self.data)



stats = Statistics([10, 20, 30, 40])
assert stats.mean() == mean([10, 20, 30, 40])
"""
Exercice 16 : Vecteurs et Calculs
Créez une classe Vector3D représentant un vecteur en trois dimensions.
Implémentez la méthode pour calculer la norme, l’addition et le produit scalaire entre deux vecteurs 3D.
Utilisez la surcharge des opérateurs pour ces opérations.
"""
class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norm(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __add__(self, other):
        if not isinstance(other, Vector3D):
            raise TypeError("Addition only supported between Vector3D instances.")
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def dot(self, other):
        if not isinstance(other, Vector3D):
            raise TypeError("Dot product only supported between Vector3D instances.")
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __mul__(self, other):
        if not isinstance(other, Vector3D):
            raise TypeError("Multiplication only supported between Vector3D instances.")
        return self.dot(other)

