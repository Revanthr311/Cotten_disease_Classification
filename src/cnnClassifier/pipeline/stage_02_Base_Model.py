from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.Base_Model import PrepareBaseModel
from cnnClassifier import logger

STAGE_NAME="Base Model"

class PrepareBaseModelTrainingPpeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()


if __name__=='__main__':
    try:
        logger.info(f">>>>>> stage{STAGE_NAME} started<<<<<<")
        obj=PrepareBaseModelTrainingPpeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx=========x")
    except Exception as e:
        logger.exception(e)
        raise e