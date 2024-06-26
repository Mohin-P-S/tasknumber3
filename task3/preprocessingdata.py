
def preprocess_data(X, y):
    """Preprocess text data and convert labels to numerical."""
    try:
        vectorizer = CountVectorizer()
        X = vectorizer.fit_transform(X)
        return X, y
    except Exception as e:
        print(f"Error in preprocessing data: {e}")
        return None, None