"""
Fichier main.py
"""
import string

def ispalindrome(p):
    """
    Vérifie si une chaîne est un palindrome en ignorant les accents, espaces, et caractères spéciaux
    en utilisant translate() et une table de correspondance.
    """
    # Table de correspondance pour remplacer les caractères accentués
    accents = str.maketrans(
        "áàäâãéèëêíìïîóòöôõúùüûýÿñçÁÀÄÂÃÉÈËÊÍÌÏÎÓÒÖÔÕÚÙÜÛÝÑÇ",
        "aaaaaeeeeiiiiooooouuuuyyncAAAAAEEEEIIIIOOOOOUUUUYNC"   
    )

    # Table pour supprimer la ponctuation et les espaces
    suppression = str.maketrans('', '', string.punctuation + string.whitespace + '-')

    # Appliquer les transformations
    p = p.translate(accents)  # Remplacer les accents
    p = p.translate(suppression)  # Supprimer la ponctuation, les espaces et les tirets

    # Mettre en minuscule pour éviter les erreurs dues à la casse
    p = p.lower()

    # Longueur de la chaîne
    l = len(p)
    # Comparaison des caractères
    for i in range(l // 2):
        if p[i] != p[-i-1]:  # Comparaison entre le caractère courant et celui symétrique à la fin
            return False
     # Si toutes les comparaisons sont bonnes, c'est un palindrome
    return True

# Test avec des exemples
def main():
    """
    Teste si la fonction secondaire fonctionne
    """
    test_cases = [
        ("Ésope reste ici et se repose", True),
        ("À révéler mon nom, mon nom relèvera", True),  # Palindrome attendu
        ("Émile-Éric, notre valet, alla te laver ton ciré élimé", True),  # Palindrome attendu
        ("radar", True),
        ("test", False)
    ]

    for s, expected in test_cases:
        result = ispalindrome(s)
        print(f"'{s}': {result} (attendu: {expected})")
        assert result == expected, f"Erreur sur '{s}' : attendu {expected}, obtenu {result}"

if __name__ == "__main__":
    main()
