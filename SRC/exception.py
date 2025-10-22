import sys

def error_message_details(error: Exception) -> str:
    """Generate a detailed error message including type, file name, and line number."""
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    return f"Error Type: {exc_type.__name__}, File: {fname}, Line: {line_number}, Message: {str(error)}"

class CustomeException(Exception):
    """Custom exception class that includes detailed error information."""
    def __init__(self, error: Exception):
        self.error = error
        self.message = error_message_details(error)
        super().__init__(self.message)

    def __str__(self):
        return self.message