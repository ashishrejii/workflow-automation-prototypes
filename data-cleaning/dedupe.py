import pandas as pd

def remove_duplicates(input_path, output_path, key_column):
    """
    Removes duplicate rows based on a key column.
    Useful for cleaning ticket logs, customer tables, and analytics exports.
    """

    df = pd.read_csv(input_path)

    before = len(df)
    df = df.drop_duplicates(subset=[key_column], keep="first")
    after = len(df)

    df.to_csv(output_path, index=False)

    return {
        "records_before": before,
        "records_after": after,
        "duplicates_removed": before - after
    }


if __name__ == "__main__":
    print(remove_duplicates("sample.csv", "deduped_sample.csv", "ticket_id"))
