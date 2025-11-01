from typing import Union


def calculate_sum(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Calcule la somme de deux nombres.

    Correction mypy: Ajout d'annotations de type pour les arguments et le retour.
    Correction flake8: Suppression des espaces excessifs autour de l'opérateur.
    """
    result = a + b
    return result


def main() -> None:
    """
    Point d'entrée principal du programme.

    Correction flake8: Utilisation de guillemets doubles pour le style.
    """
    print("Démarrage du programme")

    # Correction du typage potentiel: L'appel à la fonction doit utiliser des types
    # compatibles (int ou float) pour un calcul mathématique standard.
    # L'exemple initial (5, "10") forcerait la concaténation de chaînes si le typage
    # n'était pas respecté.
    sum_result = calculate_sum(5, 10)
    print(f"La somme est: {sum_result}")


if __name__ == "__main__":
    main()
