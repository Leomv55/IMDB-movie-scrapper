class IMDBRequestException(Exception):
    def __init__(self, message, status_code=200) -> None:
        self.message = message
        self.status_code = status_code

    def __str__(self):
        return f"{self.message} - status code: {self.status_code}"
