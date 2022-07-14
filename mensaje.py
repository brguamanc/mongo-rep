class Mensaje:
    def __init__(self, message, datetime):
        self.message = message
        self.datetime = datetime

    def toDBCollection(self):
        return {
        'message': self.message,
        'datetime': self.datetime
        }
        