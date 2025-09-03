import sys   # talk to Python interpreter (exit, args, path)
import os    # talk to OS (environment variables, paths)
import pymongo  # connect and interact with MongoDB
import certifi  # SSL certificates for secure connection

from us_visa.exception import USvisaException   # custom exception handler for project
from us_visa.logger import logging              # project logger
from us_visa.constant import DATABASE_NAME, MONGODB_URL_KEY  # constants (dbname, env key)

ca = certifi.where()   # gets the location of trusted SSL certificates

class MongoDBClient:
    """
    Class Name : export_data_info_feature_store
    Description : This method exports the dataframe from mongodb feature store as dataframe
    Output : connection to mongodb database
    On Failure : raises an exception
    """

    client = None


    def __init__(self, database_name=DATABASE_NAME) -> None:
        
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY) # get DB URL from env variable
                if mongo_db_url is None:
                    raise Exception(f"Environment key: {MONGODB_URL_KEY} is not set.")
            
                # Connect securely to MongoDB using SSL cert
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            
            # Reuse the client
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("MongoDB connection succesfull")
        
        except Exception as e:
            raise USvisaException(e, sys) # raise project-specific exception



