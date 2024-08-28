"""
Nom du script     : main.py
Auteur            : VIRY Brandon
Date              : 2024-08-28
version           : 1.0
Description       : Fichier principal 
"""


from file import read_file
from file import write_file
from extract import extract_motif_gras , extract_motif_italique ,remplacer_lignes_vides
from formatUnicode import format_to_bold , format_to_italic
import sys

def main(file_name):
    """_summary_

    Fonction qui applique la mise en forme du post LinkedIn et le sauvegarde dans un fichier text

    Args:
        file_name (str): nom du fichier
    returns:
        (void): Fichier text mise en forme 

    """
    
    # Lire le fichier en encodage utf-8
    content = read_file(file_name, encoding='utf-8')
    

    # Format gras
    textExtactGras =  extract_motif_gras(content)
    for text in textExtactGras:
        content = content.replace("**" +text+"**",format_to_bold(text))

    # Format italique
    textExtactItalique =  extract_motif_italique(content)
    for text in textExtactItalique:
        content = content.replace("*" + text + "*", format_to_italic(text))
    
    # Format ligne 
    content = remplacer_lignes_vides(content)

    # Format list
    content = content.replace("* ", "🔹➤ ")
    content = content.replace("- ", "🔹➤ ")
    
    # Eire le contenue du fichier en  en codage utf-8
    write_file(file_name+".txt", content, encoding='utf-8')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: py main.py <file_name>")
        sys.exit(1)
    else:
        file_name = sys.argv[1]
        main(file_name)
    
