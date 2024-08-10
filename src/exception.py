import sys
import os
# Function to generate a detailed error message
def generate_error_message(error, error_detail:sys):
    _, _, exc_tb = sys.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occurred at [{filename}] in line number [{exc_tb.tb_lineno}] and was of type [{str(error)}]"
    return error_message

# Custom exception class
class CustomException(Exception):
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)  # Call the superclass (Exception) initializer
        self.error_message = generate_error_message(error_message, error_detail)  # Generate and store detailed error message
    def __str__(self):
        return self.error_message