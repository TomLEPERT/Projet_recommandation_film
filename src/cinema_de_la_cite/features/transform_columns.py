import ast

def transform_columns_to_list(df, columns):
    """
    Transforme des colonnes contenant des listes sous forme de string
    en vraies listes Python.
    """

    for col in columns:
        df[col] = df[col].apply(
            lambda x: ast.literal_eval(x) if isinstance(x, str) else x
        )

    return df