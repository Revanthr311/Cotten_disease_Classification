from cnnClassifier.constants import *
from cnnClassifier.utils.commen import read_yaml,create_directories
from cnnClassifier.entity.config_entity import DataIngestionconfig

class ConfigurationManager:
    def __init__(
            self,
            config_filepath=CONFIG_FILE_PATH,
            paras_filepath=PARAMS_FILE_PATH):
        self.config=read_yaml(config_filepath)
        self.params=read_yaml(paras_filepath)

        create_directories([self.config.artifacts_roots])

    def get_data_ingestion_config(self)-> DataIngestionconfig:
        config=self.config.data_ingestion
        
        create_directories([config.root_dir])

        data_ingestion_config=DataIngestionconfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config