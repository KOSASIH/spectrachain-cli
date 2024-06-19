import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

class TransactionAnalyzer:
    def __init__(self, transaction_data: pd.DataFrame):
        self.transaction_data = transaction_data

    def train_model(self) -> None:
        X = self.transaction_data.drop(['label'], axis=1)
        y = self.transaction_data['label']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model = RandomForestClassifier(n_estimators=100)
        self.model.fit(X_train, y_train)

    def predict_transaction_risk(self, transaction: dict) -> float:
        # Convert transaction data to pandas dataframe
        transaction_df = pd.DataFrame([transaction])
        # Preprocess data
        #...
        # Make prediction
        prediction = self.model.predict(transaction_df)
        return prediction[0]
