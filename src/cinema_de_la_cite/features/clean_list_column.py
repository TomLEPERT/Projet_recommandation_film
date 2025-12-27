import pandas as pd
import re

def clean_list_column(value):
        if pd.isna(value):
            return []

        value = str(value)
        # Supprimer crochets
        value = value.replace('[', '').replace(']', '')
        # Normaliser les guillemets
        value = value.replace('""', '"').replace("'", '"')
        # Extraire tout ce qui est entre guillemets
        items = re.findall(r'"([^"]+)"', value)
        # Nettoyage final
        return [item.strip() for item in items if item.strip()]