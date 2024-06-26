def evaluate_model(model, X_test, y_test):
    """Evaluate the trained model."""
    try:
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred)
        return accuracy, report
    except Exception as e:
        print(f"Error in evaluating model: {e}")
        return None, None