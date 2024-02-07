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

import os
import requests
from time import sleep

pod_id = os.environ['POD_ID']
job_id = os.environ['JOB_ID']
wait_seconds = os.environ["WAIT_SECONDS"]
url = os.environ["POSTBACK_HOST"] + "/" + job_id

data = {
    "job_id": job_id,
    "pod_id": pod_id,
    "execution_status": "success",
    "execution_output": "",
}

sleep(int(wait_seconds))
response = requests.post(url, json=data)

print("Status Code: ", response.status_code)
print("Data: ", data)