import json
import pandas as pd

def flatten_json(input_path, output_path):
    """
    Flattens a nested JSON API response into a clean CSV table.
    Useful for analytics, dashboards, and inspection of API payloads.
    """

    with open(input_path, "r") as f:
        data = json.load(f)

    # Flatten using pandas json_normalize
    flat_df = pd.json_normalize(data)

    flat_df.to_csv(output_path, index=False)
    return f"Flattened JSON saved to {output_path}"


if __name__ == "__main__":
    print(flatten_json("sample_api.json", "flattened_output.csv"))
