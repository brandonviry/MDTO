"""
Nom du fichier : file.py
Auteur           : VIRY Brandon
Date             : 2024-08-28
Version          : 1.0
Description  : Ce fichier fournit un ensemble de fonctions utilitaires pour manipuler des fichiers texte, notamment la lecture, l'écriture et la recherche de contenu.

"""


def read_file(file_name ,encoding='utf-8'):
    """
    Lit le contenu d'un fichier.

    Args:
        file_name (str): Le chemin d'accès au fichier à lire.
        encoding (str) : L'encodage du fichier.


    Returns:
        str: Le contenu du fichier.
    """

    with open(file_name, "r" ,encoding=encoding) as file:
        content = file.read()
    return content
def write_file(file_name, content ,encoding='utf-8'):
    """
    Écrit le contenu dans un fichier.

    Args:
        file_name (str): Le chemin d'accès du fichier à écrire.
        content (str): Le contenu à écrire dans le fichier.
        encoding (str) : L'encodage du fichier.
    """

    with open(file_name, "w",encoding=encoding) as file:
        file.write(content)
def search_in_file(file_name, search_string,encoding='utf-8'):
    """
    Recherche une chaîne de caractères dans un fichier.

    Args:
        file_name (str): Le chemin d'accès du fichier dans lequel rechercher la chaîne de caractères.
        search_string (str): La chaîne de caractères à rechercher dans le fichier.
        encoding (str) : L'encodage du fichier.


    Returns:
        bool: True si la chaîne de caractères est trouvée dans le fichier, False sinon.
    """

    with open(file_name, "r",encoding=encoding) as file:
        content = file.read()
        if search_string in content:
            return True
        else:
            return False