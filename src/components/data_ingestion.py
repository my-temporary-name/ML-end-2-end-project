# Data ingestion is the process of obtaining and importing data for immediate use or storage in a database.

import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass # This module provides a decorator and functions for automatically adding special methods to classes, which can be used to create classes with instances that can be compared, printed, and converted to string
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig



@dataclass
class DataIngestionConfig: 
    train_data_path: str=os.path.join('artifacts', "train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
    def initiated_data_ingestion(self):
        logging.info("enter the data ingestion method or component")
        try:
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info("Read the dataset as a data frame")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train Test split initiated")
            train_set, test_set=train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Data Ingestion completed")

            return(self.ingestion_config.train_data_path, 
                   self.ingestion_config.test_data_path
                   ) # returning the train and test data to the next component that is data transformation

        except Exception as e:
            raise CustomException(e,sys)

if __name__=="__main__":
    obj=DataIngestion()
    train_data, test_data=obj.initiated_data_ingestion()

    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data,test_data)

