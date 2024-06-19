import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from xgboost import XGBClassifier
from catboost import CatBoostClassifier
from lightgbm import LGBMClassifier
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

class TransactionRiskModel:
    def __init__(self, data: pd.DataFrame):
        self.data = data
        self.X = data.drop(['label'], axis=1)
        self.y = data['label']
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)

    def create_pipeline(self) -> Pipeline:
        numeric_features = self.X.select_dtypes(include=['int64', 'float64']).columns
        categorical_features = self.X.select_dtypes(include=['object']).columns

        numeric_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler())
        ])

        categorical_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
            ('onehot', pd.get_dummies)
        ])

        preprocessor = ColumnTransformer(
            transformers=[
                ('num', numeric_transformer, numeric_features),
                ('cat', categorical_transformer, categorical_features)
            ]
        )

        pipeline = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('classifier', self.create_classifier())
        ])

        return pipeline

    def create_classifier(self) -> object:
        # Choose one of the following classifiers or implement your own
        # classifier = RandomForestClassifier(n_estimators=100, random_state=42)
        # classifier = XGBClassifier(objective='binary:logistic', max_depth=6, learning_rate=0.1, n_estimators=100, n_jobs=-1)
        # classifier = CatBoostClassifier(iterations=100, learning_rate=0.1, depth=6, verbose=False)
        # classifier = LGBMClassifier(objective='binary', max_depth=6, learning_rate=0.1, n_estimators=100, n_jobs=-1)
        classifier = self.create_neural_network()
        return classifier

    def create_neural_network(self) -> Sequential:
        model = Sequential()
        model.add(Dense(64, activation='relu', input_shape=(self.X.shape[1],)))
        model.add(Dropout(0.2))
        model.add(Dense(32, activation='relu'))
        model.add(Dropout(0.2))
        model.add(Dense(1, activation='sigmoid'))
        model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        return model

    def train_model(self, pipeline: Pipeline) -> None:
        pipeline.fit(self.X_train, self.y_train)

    def evaluate_model(self, pipeline: Pipeline) -> None:
        y_pred = pipeline.predict(self.X_test)
        print('Accuracy:', accuracy_score(self.y_test, y_pred))
        print('Classification Report:')
        print(classification_report(self.y_test, y_pred))
        print('Confusion Matrix:')
        print(confusion_matrix(self.y_test, y_pred))

    def predict(self, pipeline: Pipeline, transaction: pd.DataFrame) -> float:
        return pipeline.predict_proba(transaction)[:, 1]
