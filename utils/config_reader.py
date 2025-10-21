import yaml
import os

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), "..", "config.yaml")
    with open(config_path, "r") as file:
        config_data= yaml.safe_load(file)
    
    # Override sensitive values with environment variables if available
    config_data["username"] = os.getenv("APP_USERNAME", config_data["username"])
    config_data["password"] = os.getenv("APP_PASSWORD", config_data["password"])
    config_data["azure_devops"]["pat_token"] = os.getenv("AZURE_DEVOPS_PAT", config_data["azure_devops"]["pat_token"])
    return config_data

config = load_config()
