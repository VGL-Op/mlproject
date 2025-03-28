import os
import sys
import pandas as pd
import numpy as np
import dill
import pickle

from sklearn.metrics import r2_score
from src.exception import CustomException
from src.logger import logging  


def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)

def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    try:
        report = {} 

        for i in range(len(models)):  # No need to convert to list explicitly
            model_name = list(models.keys())[i]  # Get the model's name
            model = models[model_name]  # Get the model object

            # Uncomment if using hyperparameter tuning
            # para = param[model_name]
            # gs = GridSearchCV(model, para, cv=3)
            # gs.fit(X_train, y_train)
            # model.set_params(**gs.best_params_) 

            model.fit(X_train, y_train)  

            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            report[model_name] = test_model_score  # Fix the assignment

        return report

    except Exception as e:
        raise CustomException(e, sys)


