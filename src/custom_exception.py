import traceback
import sys

class CustomException(Exception):
      def __init__(self, error_message, error_detail: sys):
            super().__init__(error_message)
            self.error_message = self.get_detailed_error_message(error_message, error_detail)

      @staticmethod
      def get_detailed_error_message(error_message, error_detail: sys):
            exc_type, exc_obj, exc_tb = traceback.sys.exc_info()
            if exc_tb is not None:
                  file_name = exc_tb.tb_frame.f_code.co_filename
                  line_number = exc_tb.tb_lineno
            else:
                  file_name = "unknown"
                  line_number = "unknown"
            return f"Error in {file_name} at line {line_number}: {error_message}"

      def __str__(self):
            return self.error_message
