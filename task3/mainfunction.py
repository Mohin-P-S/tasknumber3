def main():
    # Adjust file path according to your actual file location
    file_path = r"D:\User\Downloads\spam.csv"
    
    # Step 1: Load the dataset
    data = load_data(file_path)
    if data is None:
        return
    
    # Step 2: Preprocess the data
    X = data['v2']
    y = data['v1'].map({'ham': 0, 'spam': 1})
    X, y = preprocess_data(X, y)
    if X is None or y is None:
        return
    
    # Step 3: Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Step 4: Train the model
    model = train_model(X_train, y_train)
    if model is None:
        return
    
    # Step 5: Evaluate the model
    accuracy, report = evaluate_model(model, X_test, y_test)
    if accuracy is not None and report is not None:
        print(f"Accuracy: {accuracy}")
        print(f"Classification Report:\n{report}")

if __name__ == "__main__":
    main()