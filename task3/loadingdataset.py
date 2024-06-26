def load_data(file_path):
    """Load data from CSV file."""
    try:
        data = pd.read_csv(file_path, encoding='latin-1')
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error loading data: {e}")
        return None