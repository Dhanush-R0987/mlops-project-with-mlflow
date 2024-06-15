from MLproject.constants import *
from MLproject.utils.common import read_yaml, create_directories
from MLproject.entity.config_entity import (DataIngestionConfig)

"""
Manages configuration settings for the project by reading from YAML files and creating necessary directories.
"""

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root]) # Creates the root directory for artifacts if it does not exist.

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir]) # creates a data_ingestion folder inside it contain zip folder and unzip file

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config