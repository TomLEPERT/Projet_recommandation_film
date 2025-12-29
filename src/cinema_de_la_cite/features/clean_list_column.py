import pandas as pd
import re

def clean_list_column(value):
    # Si c'est une liste ou une Series, on la transforme en liste de chaînes
    if isinstance(value, (list, pd.Series)):
        return [str(v).strip() for v in value if pd.notna(v) and str(v).strip()]

    # Si c'est un float NaN ou None
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return []

    # Convertir en chaîne pour extraire les éléments
    value = str(value)

    # Supprimer crochets
    value = value.replace('[', '').replace(']', '')
    # Normaliser les guillemets
    value = value.replace('""', '"').replace("'", '"')
    # Extraire tout ce qui est entre guillemets
    items = re.findall(r'"([^"]+)"', value)
    # Nettoyage final
    return [item.strip() for item in items if item.strip()]
