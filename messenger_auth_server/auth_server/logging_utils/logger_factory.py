class LoggerFactory:
    _loggers = {}

    @classmethod
    def add_logger(cls, name, logger):
        if name not in cls._loggers:
            cls._loggers[name] = logger

    @classmethod
    def get_logger(cls, name):
        if name in cls._loggers:
            return cls._loggers[name]

        return None
