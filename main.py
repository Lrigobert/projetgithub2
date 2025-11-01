# Fichier main.py - Contient des erreurs de style et de typage

def calculate_sum(a, b):
    # Erreur de style: trop d'espaces autour de l'opérateur
    result = a + b
    
    # Erreur de typage: 'a' et 'b' ne sont pas typés.
    # Si 'a' est un int et 'b' est un str, cela va échouer à l'exécution.
    return result

def main():
    # Erreur de style: utilisation de guillemets simples
    print('Démarrage du programme')
    
    # Erreur de typage potentielle
    somme = calculate_sum(5, "10")
    print(f"La somme est: {somme}")

if __name__ == "__main__":
    main()
