from rest_framework.views import exception_handler
import logging

def api_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
    	resp_data = {}
    	resp_data['status_code'] = response.status_code
    	resp_data['message'] = response.data['detail']
    	del response.data['detail']
        response.data['error'] = resp_data
    return response

class LogHandler(object):
	LOG_LEVEL = logging.DEBUG
	LOG_FILE = '/home/salman/NBA-Players-Database-Website/nba.log'
	def __init__(self, name):
		self.logger = logging.getLogger(name)
		self.logger.setLevel(self.LOG_LEVEL)
		file_handle = logging.handlers.RotatingFileHandler(self.LOG_FILE, maxBytes = 50000, backupCount = 100)
		file_handle.setLevel(self.LOG_LEVEL)
		formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(filename)s: %(message)s')
		file_handle.setFormatter(formatter)
		self.logger.addHandler(file_handle)
	def log(self, severity, msg): 
		self.logger.log(severity, msg)