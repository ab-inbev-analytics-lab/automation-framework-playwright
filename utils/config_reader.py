import yaml
import os

class ConfigError(Exception):
    """Raised when required config values are missing."""
    pass

def load_config():
    # Load config.yaml
    config_path = os.path.join(os.path.dirname(__file__), "..", "config.yaml")
    with open(config_path, "r") as file:
        config_data = yaml.safe_load(file) or {}

    # Helper to get secret from env or config.yaml
    def get_secret(key, env_var, parent=None):
        value = os.getenv(env_var)
        if value:
            return value

        if parent:
            nested = config_data.get(parent, {})
            if key in nested:
                return nested[key]
        else:
            if key in config_data:
                return config_data[key]

        raise ConfigError(f"Missing required secret: {key} (env: {env_var})")

    # Override only the sensitive secrets
    config_data["username"] = get_secret("username", "APP_USERNAME")
    config_data["password"] = get_secret("password", "APP_PASSWORD")
    if "azure_devops" not in config_data:
        config_data["azure_devops"] = {}
    config_data["azure_devops"]["pat_token"] = get_secret("pat_token", "AZURE_DEVOPS_PAT", parent="azure_devops")

    return config_data

# Global config object
config = load_config()
