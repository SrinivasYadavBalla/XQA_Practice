import configparser
import os

class ConfigReader:

    def __init__(self):
        self.config = configparser.ConfigParser()
        print(self.config)
        # config_path = os.path.join(os.path.dirname(__file__), "config.ini")
        config_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "config.ini")
        )
        print(config_path)
        self.config.read(config_path)

    def get_base_url(self):
        return self.config.get("DEFAULT", "base_url")

    def get_browser(self):
        return self.config.get("DEFAULT", "browser")

    def get_wait(self):
        return self.config.getint("DEFAULT", "implicit_wait")


# Create object (used everywhere)
