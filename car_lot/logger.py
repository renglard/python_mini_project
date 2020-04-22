from datetime import datetime
import os
import definitions


class Logger:
    path = definitions.LOG_DEFAULT_PATH
    log_format = definitions.LOG_DEFAULT_TIME_FORMAT

    def add_to_log(self, msg):
        date = datetime.now()
        date_string = date.strftime(definitions.LOG_DEFAULT_TIME_FORMAT)
        try:
            file = open(self.path + os.sep + "log.txt", "w")
            file.write(date_string + " " + msg + "\n")

        except OSError:
            try:
                os.mkdir(self.path)
            except Exception as err:
                print(f"Error logging {msg}, the error is {err.args[0]}")

    def set_path(self, path):
        definitions.LOG_DEFAULT_PATH = path

    def set_time_stamp_format(self, log_format):
        definitions.LOG_DEFAULT_TIME_FORMAT = log_format

    def get_path(self):
        return self.path

    def get_time_stamp(self):
        return self.log_format


log = Logger()
log.add_to_log("works")