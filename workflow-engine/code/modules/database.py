#     Self Service Portal - A Portal for users to request services and have them automagically provisioned
#     Copyright (C) 2024  Eric C Moody
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.


import yaml
from pymongo import MongoClient
from bson import ObjectId, json_util
import urllib.parse
import json
import re

class Database:
    """
    This is a class used for accessing the database. When initialize it it open a connection to the database. 
    The config for the database connection comes from /opt/self-service-portal/conf/db.conf

    Attributes:
        mongo_client (MongoClient): The client class for the db connection
        datbase (Database): The database the client is connected to
        collection (Collection): The collection that the client is connect to
    """
    conf_home = "/opt/self-service-portal/conf"

    def __init__(self, database, collection) -> None:
        """
        The constructor for the Database class.

        Parameters:
            self (Database): The object itself
            database (Str): The name of the database to connect to
            collection (Str): The name of the collection to connect to
        """
        with open(self.conf_home+"/db.yaml",'r') as file:
            db_config = yaml.safe_load(file)

        username = urllib.parse.quote_plus(db_config['username'])
        password = urllib.parse.quote_plus(db_config['password'])
        self.mongo_client = MongoClient('mongodb://%s:%s@%s:%s' % (username, password, db_config['host'], db_config['port']))
        self.database = self.mongo_client[database]
        self.collection = self.database[collection]

    def find_by_id(self, object_id):
        """
        A method to find a document by its object id. 
        
        Parameters:
            self (Database): The instantiation of the Database class
            object_id (Str): The id of the document to find. The id must be 24 hexadecimal characters with lowercase letters

        Returns:
            Dict: A dict with the document if the document is found. 
            None: If the document is not found.
        """
        if not re.match('^[0-9a-f]{24}$',object_id):
            raise "Object id must be 24 chacters hexadecimal string with lowercase letters"

        object_instance =  ObjectId(object_id)
        result = self.collection.find_one({"_id": object_instance})

        return json.loads(json_util.dumps(result))

    def find_one_by_query(self, query):
        """
        A function to find one record using a query

        Parameters:
            self (Database): The instantiation of the Database class
            query (Dict): A dictonary with the query
        
        Returns:
            Dict: A dict with the document if document is found
            None: If the document is not found        
        """

        result = self.collection.find_one(query)

        return json.loads(json_util.dumps(result))
    
    def insert_document(self, document):
        """
        A function to insert a new doument

        Parameters:
            self (Database): The instantiation of the Database class
            document (Dict): A dictonary with the document to inset into a collection

        Returns:
            object_id (Str): A 24 character hexadecmal string that represents the id of the new object
        """

        result = self.collection.insert_one(document)

        return str(result.inserted_id)

    


        