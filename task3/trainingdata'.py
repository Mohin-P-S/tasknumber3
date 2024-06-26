def train_model(X_train, y_train):
    """Train a Naive Bayes classifier."""
    try:
        model = MultinomialNB()
        model.fit(X_train, y_train)
        return model
    except Exception as e:
        print(f"Error in training model: {e}")
        return None