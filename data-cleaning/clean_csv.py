import pandas as pd

def clean_csv(input_path, output_path="cleaned_output.csv"):
    try:
        df = pd.read_csv(input_path)
    except FileNotFoundError:
        return "Error: Input CSV file not found."

    # Remove duplicates
    df = df.drop_duplicates()

    # Strip whitespace
    df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

    # Standardize column names
    df.columns = (
        df.columns
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )

    # Fill missing text values
    for col in df.select_dtypes(include=["object"]):
        df[col] = df[col].fillna("Unknown")

    # Fill missing numeric values
    for col in df.select_dtypes(include=["number"]):
        df[col] = df[col].fillna(0)

    # Save cleaned file
    df.to_csv(output_path, index=False)
    return f"Cleaned CSV saved to: {output_path}"

if __name__ == "__main__":
    print(clean_csv("sample.csv"))
