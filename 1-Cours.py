import sys
import os

class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def get_city(self, city):
        try:
            if not os.path.exists("./csv"):
                return "Directory not found: ./csv"
            
            # Ouverture du fichier en mode lecture
            with open("./csv/vw7RczKZ.csv", "r") as file:
                print("File found")
                for line in file:
                    line = line.strip()
                    # Convertir les noms de ville en minuscules pour la comparaison
                    if line.lower().startswith(city.lower() + ","):
                        return line
                return "City not found"
        except FileNotFoundError as e:
            print(e)
            return "File not found: ./csv/vw7RczKZ.csv"

    def get_department(self, department):
        try:
            if not os.path.exists("./csv"):
                return "Directory not found: ./csv"
            
            with open("./csv/vw7RczKZ.csv", "r") as file:
                print("File found")
                cities = []
                for line in file:
                    line = line.strip()
                    # L'ordre des colonnes est: Nom de la ville, Numéro du département, Pays, Population
                    # On veut afficher les noms de ville qui sont dans le même numéro de département
                    if line.split(",")[1] == department:
                        # Ajoute uniquement le nom de la ville à la liste
                        cities.append(line.split(",")[0])
                return ", ".join(cities) if cities else "No cities found for the given department"
        except FileNotFoundError as e:
            print(e)
            return "File not found: ./csv/vw7RczKZ.csv"
    
    def add_city(self, city, department, country, population):
        try:
            if not os.path.exists("./csv"):
                os.makedirs("./csv")  # Créer le répertoire si nécessaire
            
            with open("./csv/vw7RczKZ.csv", "a") as file:
                file.write(f"{city},{department},{country},{population}\n")
                return "City added"
        except FileNotFoundError as e:
            print(e)
            return "File not found: ./csv/vw7RczKZ.csv"
        except Exception as e:
            print(e)
            return "An error occurred while adding the city"
    
    def delete_city(self, city):
        try:
            if not os.path.exists("./csv"):
                return "Directory not found: ./csv"
            
            with open("./csv/vw7RczKZ.csv", "r") as file:
                lines = file.readlines()
            
            with open("./csv/vw7RczKZ.csv", "w") as file:
                found = False
                for line in lines:
                    if not line.lower().startswith(city.lower() + ","):
                        file.write(line)
                    else:
                        found = True
                return "City deleted" if found else "City not found"
        except FileNotFoundError as e:
            print(e)
            return "File not found: ./csv/vw7RczKZ.csv"
        
    def delete_department(self, department):
        try:
            if not os.path.exists("./csv"):
                return "Directory not found: ./csv"
            
            with open("./csv/vw7RczKZ.csv", "r") as file:
                lines = file.readlines()
            
            with open("./csv/vw7RczKZ.csv", "w") as file:
                found = False
                for line in lines:
                    # Sépare la ligne en colonnes
                    columns = line.strip().split(",")
                    if columns[1] == department:
                        # Remplacer le numéro de département par une chaîne vide
                        columns[1] = ""
                        found = True
                    # Réécrire la ligne avec les informations modifiées
                    file.write(",".join(columns) + "\n")
                return "Department deleted" if found else "Department not found"
        except FileNotFoundError as e:
            print(e)
            return "File not found: ./csv/vw7RczKZ.csv"
        
    def delete(self, identifier):
        try: 
            if not os.path.exists("./csv"):
                return "Directory not found: ./csv"
            
            with open("./csv/vw7RczKZ.csv", "r") as file:
                lines = file.readlines()
            
            with open("./csv/vw7RczKZ.csv", "w") as file:
                found = False
                for line in lines:
                    columns = line.strip().split(",")
                    if columns[0].lower() == identifier.lower():
                        # Remplacer le nom de la ville par une chaîne vide
                        columns[0] = ""
                        found = True
                    elif columns[1] == identifier:
                        # Remplacer le numéro de département par une chaîne vide
                        columns[1] = ""
                        found = True
                    
                    # Réécrire la ligne avec les informations modifiées
                    file.write(",".join(columns) + "\n")
                return "City or department deleted" if found else "City or department not found"
        except FileNotFoundError as e:
            return "File not found: ./csv/vw7RczKZ.csv"


    
    def save_to_csv(data, filename="db.csv"):
        try:
            with open(filename, "w", newline='') as file:
                writer = csv.writer(file)
                # Écrire les en-têtes, si nécessaire
                writer.writerow(["City", "Department", "Country", "Population"])  # Modifier selon vos besoins
                # Écrire les données
                for row in data:
                    writer.writerow(row)
            print(f"Data successfully written to {filename}")
        except Exception as e:
            print(f"An error occurred while writing to {filename}: {e}")



if __name__ == "__main__":
    # Récupérer les arguments passés en ligne de commande
    if len(sys.argv) > 2:
        command = sys.argv[1]
        parameter = sys.argv[2]
        
        city_instance = City(name="", population=0)  # Crée une instance de la classe City

        if command == "get_city":
            result = city_instance.get_city(parameter)
            print(result)
        elif command == "get_department":
            result = city_instance.get_department(parameter)
            print(result)
        elif command == "add_city":
            # Récupérer les paramètres supplémentaires pour add_city
            if len(sys.argv) >= 6:
                city, department, country, population = sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]
                result = city_instance.add_city(city, department, country, population)
                print(result)
            else:
                print("Usage: python script.py add_city <city> <department> <country> <population>")
        elif command == "delete_city":
            result = city_instance.delete_city(parameter)
            print(result)
        elif command == "delete_department":
            result = city_instance.delete_department(parameter)
            print(result)
        elif command == "delete":
            if len(sys.argv) >= 3:
                identifier = sys.argv[2]  # Un seul paramètre pour le nom de la ville ou le département
                result = city_instance.delete(identifier)
                print(result)
            else:
                print("Usage: python script.py delete <city or department>")


        else:
            print("Invalid command. Usage: python script.py <get_city|get_department|add_city|delete_city|delete_department> <parameters>")
    else:
        print("Usage: python script.py <get_city|get_department|add_city|delete_city|delete_department|delete> <parameters>")
