import logging
import logging.config
logging.config.fileConfig('../data_config/logging.conf')


class Logger:

    def logger(self):
        return logging.getLogger('file')

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
