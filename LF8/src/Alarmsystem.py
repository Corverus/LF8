import logging


class Alarmsystem:
    @staticmethod
    def examine(
            parameter_label: str,
            parameter_value: float,
            soft_limit: float,
            hard_limit: float,
            logging_level: str,
            logging: logging
    ):
        if parameter_value < soft_limit and logging_level == 'debug':
            # ToDo
            log_msg = parameter_label + ' = ' + str(parameter_value)
            Alarmsystem.log('debug', log_msg, logging)
            return

        if parameter_value >= soft_limit:
            if parameter_value >= hard_limit:
                log_msg = parameter_label.upper() + ' EXCEEDS HARD LIMIT OF ' + str(parameter_value) + ': ' \
                          + parameter_label + ' = ' + str(parameter_value)
                Alarmsystem.log('warning', log_msg, logging)
                # ToDo Email versenden
                return
            log_msg = parameter_label.upper() + ' EXCEEDS SOFT LIMIT OF ' + str(parameter_value) + ': ' \
                      + parameter_label + ' = ' + str(parameter_value)
            Alarmsystem.log('warning', log_msg, logging)
            return

    @staticmethod
    def log(logging_level: str, log_msg: str, logger: logging):
        if logging_level == 'debug':
            logger.debug(log_msg)
            return
        if logging_level == 'warning':
            logger.warning(log_msg)
            return
