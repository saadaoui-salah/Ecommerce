import os

keys = ['SECRET_KEY', 'ENV']

def get_env(secret_name):
    secret_name += '='
    variables = open('.env', 'r').read().split('\n')
    for var in variables:
        if secret_name in var:
            return var.replace(secret_name,'').replace("'",'')


for key in keys:
    print(f"setting {key} ...")
    os.environ[key] = str(get_env(key))
