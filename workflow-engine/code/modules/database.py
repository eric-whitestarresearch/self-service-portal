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
import urllib.parse

class Database:
    conf_home = "/opt/self-service-portal/conf"

    def __init__(self, database, collection) -> None:
        with open(self.conf_home+"/db.yaml",'r') as file:
            db_config = yaml.safe_load(file)

        username = urllib.parse.quote_plus(db_config['username'])
        password = urllib.parse.quote_plus(db_config['password'])
        self.mongo_client = MongoClient('mongodb://%s:%s@%s:%s' % (username, password, db_config['host'], db_config['port']))
        self.database = self.mongo_client[database]
        self.collection = self.database[collection]