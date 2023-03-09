from . import file_helper
from .test_agent import TestAgent
from .drone import Drone
from .simulator import Simulator
from .drone_test import AssertionConfig, DroneTest, DroneTestResult
import logging

logger = logging.getLogger(__name__)


class LocalAgent(TestAgent):
    def __init__(self, config: DroneTest) -> None:
        super().__init__(config)
        self.simulator = None
        if self.config.simulation is not None:
            self.simulator = Simulator(self.config.simulation)

        self.drone = None
        if self.config.drone is not None:
            self.drone = Drone(self.config.drone)
            if self.config.test is not None:
                self.drone.schedule_test(self.config.test)

    def run(self, config: DroneTest):
        try:
            self.drone.run_scheduled()
            log = self.simulator.get_log()
            if self.config.agent is not None and self.config.agent.path is not None:
                logger.info("Didn't come here")
                file_helper.upload(log, self.config.agent.path)
            logger.info("******")
            logger.info(log)
            self.results.append(DroneTestResult(log, AssertionConfig.TRAJECTORY))
            return self.results
        except Exception as e:
            self.simulator.kill()
            raise (e)

    def manual(self):
        self.drone.manual()
        self.log = Simulator.get_log()
