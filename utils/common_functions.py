import os
import pandas as pd
from src.logger import get_logger
from src.custom_exception import CustomException
from config.paths_config import *
import yaml

logger = get_logger(__name__)

def read_yaml(file_path):
      try:
            if not os.path.exists(file_path):
                  raise FileNotFoundError("File is not in the given path")
            with open(file_path, "r") as yaml_file:
                  config = yaml.safe_load(yaml_file)
                  logger.info("YAML file read successfully")
                  return config
      except Exception as e:
            logger.error("Error occurred while reading YAML file")
            raise CustomException("Failed to read YAML file", e)
      
def load_data(path):
      try:
            logger.info("Loading data")
            df= pd.read_csv(path)
            return df
      except Exception as e:
            logger.error("Error loading data")
            raise CustomException("Failed to load data", e)
      
      
            