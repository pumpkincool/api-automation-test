import logging
import logging.config
logging.config.fileConfig('../configs/logging.ini')


class Logger:

    def logger(self):
        return logging.getLogger('console')

    def debug(self, message):
        self.logger().debug(message)

    def info(self, message):
        self.logger().info(message)

    def warning(self, message):
        self.logger().warning(message)

    def error(self, message):
        self.logger().error(message)

    def critical(self, message):
        self.logger().critical(message)
