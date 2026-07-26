import os
import sys
from Respire.Logger import logging

def error_message_detail(error, error_detail=sys):
    if error_detail is not None and hasattr(error_detail, 'exc_info'):
        _, _, exc_tb = error_detail.exc_info()
        if exc_tb is not None:
            file_name = exc_tb.tb_frame.f_code.co_filename
            lineno = exc_tb.tb_lineno
            ermsg = f"Error in Script: {file_name} - Line: {lineno} - Message: {str(error)}"
            logging.info(ermsg)
            return ermsg
    ermsg = f"Error Message: {str(error)}"
    logging.info(ermsg)
    return ermsg

class CustomException(Exception):
    def __init__(self, ermsg, error_detail=sys):
        super().__init__(str(ermsg))
        self.error_message = error_message_detail(
            ermsg, error_detail=error_detail)

    def __str__(self):
        return self.error_message