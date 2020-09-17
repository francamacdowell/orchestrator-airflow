def get_yaml_config():
    import yaml
    import os

    yaml_config_dict = None

    with open("/home/airflow/dag_config.yaml") as file:
        yaml_config_dict = yaml.load(file, Loader=yaml.Loader)

    return yaml_config_dict
