import sys
from src.logger import logging

def error_msg_detail(error, err_detail: sys):
    _, _, exc_tb = err_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    err_message = "You have an Error in python script [{0}] line number [{1}] error msg [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return err_message

class CustomException(Exception):
    def __init__(self, error, err_detail: sys):
        super().__init__(error)
        self.error_msg = error_msg_detail(error, err_detail=err_detail)

    def __str__(self):
        return self.error_msg
