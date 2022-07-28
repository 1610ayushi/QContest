from src.entities.Level import Level


class Question:
    def __init__(self, title: str, level: Level, score:int, id=None ) -> None:
        self._title = title
        self._level = level
        self._score = score
        self._id = id

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_title(self):
        return self._title

    def get_level(self):
        return self._level

    def get_score(self):
        return self._score

    def __repr__(self) -> str:
        return f'Question [id="{self._id}"]'
