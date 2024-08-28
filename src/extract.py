"""
Nom du fichier   : extract.py
Auteur           : VIRY Brandon
Date             : 2024-08-28
Version          : 1.0
Description      :Ce fichier fournit un essemble de fonction qui extrait des motifs d'un texte en utilisant des expressions régulières.

"""
import re

def extraire_motifs_entiers(motif, phrase):
    """
    Fonction qui extrait des motifs d'un texte en utilisant des expressions régulières.

    Args:
        motif (str): expression régulière utilisée pour trouver les motifs
        phrase (str): texte pour lequel on veut extraire les motifs

    Returns:
        str[]: liste de tous les motifs trouvés dans le texte
    """
    # Utiliser findall pour trouver toutes les correspondances
    matches = re.findall(motif, phrase)
    if matches:
   
        return [elt for elt in matches if elt != '']
    else:
        return ""

def extract_motif_gras(phrase): 
    """
    Fonction qui extrait liste de tous les motifs de type gras dans un texte.

    Args:
        phrase (str): texte pour lequel on veut extraire les motifs

    Returns:
        str[]: liste de tous les motifs trouvés dans le texte
    """
    # Motif pour trouver le texte entre deux paires d'astérisques
    return extraire_motifs_entiers(r'\*\*(.*?)\*\*', phrase)

def extract_motif_italique(phrase):
    # Motif pour trouver le texte entre une paire d'astérisques (sans chevauchement)
    return extraire_motifs_entiers(r'\*(.*?)\*', phrase)

def remplacer_lignes_vides(content):
    """
    fonction qui remplace les lignes vides par '---'
    
    Args:
        content (str): contenu du fichier
    Returns:
        str: contenu du fichier avec les lignes vides remplacées par '---'
    """
    # Remplacer les lignes vides par '---'
    return re.sub(r'(?m)^\s*$', '---', content)

