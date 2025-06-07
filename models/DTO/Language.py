from datetime import datetime

class Language:
    def __init__(self, language_id: int, name: str, last_update: datetime):
        self.language_id = language_id
        self.name = name
        self.last_update = last_update
