from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_Base_Model import PrepareBaseModelTrainingPpeline

STAGE_NAME="Data Ingestion stage"

try:
    logger.info(f">>>>>> stage{STAGE_NAME} started<<<<<<")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME="Base Model"

try:
    logger.info(f">>>>>> stage{STAGE_NAME} started<<<<<<")
    obj=PrepareBaseModelTrainingPpeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e