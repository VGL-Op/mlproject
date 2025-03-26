# Data Ingestion : Data ingestion is the process of collecting and importing data from various sources (databases, APIs, files, etc.) 
# into a storage system (data lake, warehouse, or processing pipeline). It can be done in batch mode (at scheduled intervals) or 
# streaming mode (real-time data flow).

import os
import sys
from src.exception import CustomException
from src.logger import logging 
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# dataclasses helps in minimizing boilerplate code 
@dataclass
class DataIngestionConfig :
    train_data_path : str = os.path.join('artifacts','train.csv')  
    test_data_path : str = os.path.join('artifacts','test.csv')   
    raw_data_path : str = os.path.join('artifacts','raw.csv')     # raw data path

class DataIngestion : 
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info('Data Ingestion methods Starts')
        try : 
            # This line is imp as it specifies from where we will be reading data..
            # It can be from csv files, mongodb database , API calls etc.
            
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname((self.ingestion_config.train_data_path)),exist_ok = True)

            df.to_csv(self.ingestion_config.raw_data_path,index = False, header = True) 

            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
                
            )
        except Exception as e : 
            raise CustomException(e,sys)

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()