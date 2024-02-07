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


import json
import time
from modules.database import Database

def result(job_id, runner_result):
    #result_dict = json.loads(runner_result)

    runner_result['time'] = int(time.time())
    print(runner_result)
    print("The job id is: " + job_id)

    db_connection = Database("workflow-engine", "runner-result")
    result = db_connection.collection.insert_one(runner_result)
    print("Insert Result: ", result.inserted_id)