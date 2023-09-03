from metaflow import (
    FlowSpec,
    step,
)
import logging
import sys
logger = logging.getLogger(__name__)
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s -   %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger.setLevel(logging.INFO)


class TrainingFlow(FlowSpec):
    @step
    def start(self):
        logger.info('Starting the training pipeline')
        self.next(self.end)

    @step
    def end(self):
        logger.info('Successfully finished running the training pipeline')

if __name__ == '__main__':
    TrainingFlow()