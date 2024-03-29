import logging
import os
import sys
import datetime
from datetime import tzinfo, timezone


class LoggerConfig:
    def __init__(self):
        self.pasta_logs = os.path.join('assets/', "logs/")
        self.validar_e_criar_pastas()

        self.logger_erros = self.configure_logger('logger_erros', self.pasta_logs+'/erros.log', logging.ERROR)
        self.logger_infos = self.configure_logger('logger_infos', self.pasta_logs+'/infos.log', logging.INFO)


    def validar_e_criar_pastas(self):
        pastas = [self.pasta_logs]

        for pasta in pastas:
            if not os.path.exists(pasta):
                os.makedirs(pasta)


    def configure_logger(self, logger_name, log_file, log_level):
        logger = logging.getLogger(logger_name)
        logger.setLevel(log_level)

        class CustomFormatter(logging.Formatter):
            def formatTime(self, record, datefmt=None):
                dt = datetime.datetime.fromtimestamp(record.created, tz=timezone.utc).astimezone(timezone(datetime.timedelta(hours=-3)))
                return dt.strftime('%m/%d/%Y %H:%M')

        formatter = CustomFormatter('%(asctime)s - %(levelname)s - %(message)s')

        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        return logger
