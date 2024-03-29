'''import sys
from src.mlproject.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
    file_name,exc_tb.tb_lineno,str(error))

    return error_message


class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_details)

    def __str__(self):
        return self.error_message'''


import sys
import traceback

def error_message_detail(error_message, error_details):
    exc_type, exc_obj = error_details[:2]
    exc_tb = exc_obj.__traceback__
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occurred in python script name [{file_name}] line number [{exc_tb.tb_lineno}] error message[{error_message}]"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_details=None):
        super().__init__(error_message)
        self.error_details = error_details

    def __str__(self):
        return f"{super().__str__()}\nError details: {self.error_details}"





