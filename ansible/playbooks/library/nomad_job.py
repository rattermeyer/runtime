#!/usr/bin/python
import nomad
import yaml
import json
import sys

DOCUMENTATION = '''
---
module: nomad_job
short_description: "handles creation, update or stopping of a nomad job"
author:
  - Richard Attermeyer
requirements:
  - python-nomad
options:
  inline_data:
    description:
      - inline yaml based job description
      required: false
      default: null
example:  '''

from ansible.module_utils.basic import *


def run_module():
  # seed the result dict in the object
  # we primarily care about changed and state
  # change is if this module effectively modified the target
  # state will include any data that you want your module to pass back
  # for consumption, for example, in a subsequent task
  result = dict(
      changed=False,
      original_message='',
      message=''
  )
  
  module = AnsibleModule(
    argument_spec=dict(
      inline_data=dict(required=False, type='str'),
      nomad_host=dict(required=False, type='str'),
      nomad_port=dict(required=False, type='int'),
      nomad_token=dict(required=False, type='str'),
      cert_path=dict(required=False, type='path'),
      secure=dict(required=False,type='bool')
    ),
    supports_check_mode=True
  )

  inline_data = yaml.load(module.params['inline_data'])
  nomad_client = nomad.Nomad(host='127.0.0.1')
  nomad_client.job.register_job("example", inline_data)

  module.exit_json(**result)

def main():
  run_module()

if __name__ == '__main__':
  main()

