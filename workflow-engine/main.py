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
from kubernetes import client, config, utils

def main():
    config.load_kube_config()
    k8s_client = client.ApiClient()
    #Job YAML
    job_yaml = """
apiVersion: batch/v1
kind: Job
metadata:
  name: echo-runner-from-python
  namespace: testing
spec:
  template:
    spec:
      containers:
      - name: echo-runner
        image: ericwsr/runner-echo:1
        env:
        - name: RUNNER_ARGS
          value: "I am running in a k8s job"
      restartPolicy: Never
      imagePullSecrets:
      - name: regcred
  backoffLimit: 4

"""

    job_dict=yaml.safe_load(job_yaml)
    utils.create_from_dict(k8s_client, job_dict)

if __name__ == '__main__':
    main()