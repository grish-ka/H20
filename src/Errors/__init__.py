class FileError(Exception):
    def __init__(self, message="There was a error in the file"):
        self.message = message
        super().__init__(self.message)

class UnknownError(Exception):
    def __init__(self, message="There was an unexpected error"):
        self.message = message
        super().__init__(self.message)