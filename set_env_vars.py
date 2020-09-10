#!/usr/bin/env python
import argparse


def get_stage_vars(function_name, environment_variables,
                   aws_region='eu-west-1', profile_name=None):
    import boto3
    if profile_name:
        session = boto3.Session(profile_name=profile_name)
    else:
        session = boto3.Session()

    lambda_client = session.client('lambda', region_name=aws_region)
    print(environment_variables)
    #
    response = lambda_client.update_function_configuration(
        FunctionName=function_name,
        Environment={
            'Variables': environment_variables
        }
    )

    return response


args = argparse.ArgumentParser(add_help=False)
args.add_argument('project_name')
args.add_argument('branch')
args.add_argument('aws_region', default="ap-south-1")
args.add_argument('env_file')
args.add_argument('profile_name', default=None)


def main():
    flags = args.parse_args()
    old_project_name = flags.project_name
    branch = flags.branch
    aws_region = flags.aws_region
    profile_name = flags.profile_name
    env_file = flags.env_file
    function_name = old_project_name + "-" + branch

    env_variables = {}
    with open(env_file, 'r') as file_reader:
        for line in file_reader.readlines():
            if len(line.split("export ")) <= 1:
                continue
            parsed_line = line.split("export ")[1]
            if not parsed_line.strip():
                continue
            if len(parsed_line.split("=")) != 2:
                continue
            key = parsed_line.split("=")[0]
            value = parsed_line.split("=")[1]
            env_variables[key] = value.strip()[1:-1]

    get_stage_vars(
        function_name,
        environment_variables=env_variables,
        aws_region=aws_region,
        profile_name=profile_name
    )


if __name__ == "__main__":
    """
    * Download & place get_stage_vars.py your project directory

    ```sh

    $python get_stage_vars.py project_name branch aws_region
        usage: get_stage_vars.py project_name branch aws_region

    $python get_stage_vars.py ib_service alpha eu-west-1
    ```

    * above script will be usefull to execute the management commands in zappa based deployments
    """
    main()
