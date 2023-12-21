from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_Base_Model import PrepareBaseModelTrainingPpeline
from cnnClassifier.pipeline.stage_03_Model_training import ModelTrainingPipeline




# ----------------------------------------IMPORTING___DATA---------------------------------------------#
STAGE_NAME="Data Ingestion stage"

try:
    logger.info(f">>>>>> stage{STAGE_NAME} started<<<<<<")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e




#----------------------------------------IMPORTING___PRE-TRAINED__MODEL----------------------------------#
STAGE_NAME="Base Model"

try:
    logger.info(f">>>>>> stage{STAGE_NAME} started<<<<<<")
    obj=PrepareBaseModelTrainingPpeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e




#------------------------------------------MODEL___TRAINING-----------------------------------------------#
STAGE_NAME="Training"

try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e