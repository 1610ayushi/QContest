from typing import List
from src.entities import ContestStatus, Question, Level, User


class Contest:
    def __init__(self, title: str, level: Level, created_by: User, questions: List[Question], id=None ) -> None:
        self._title = title
        self._level = level
        self._created_by = created_by
        self.validate_questions(questions)
        self._questions = questions
        self._status = ContestStatus.NOT_STARTED
        self._id = id

    def get_id(self):
        return self._id

    def get_title(self):
        return self._title

    def get_level(self):
        return self._level

    def get_creator(self):
        return self._created_by

    def get_questions(self):
        return self._questions

    def get_status(self):
        return self._status


    def validate_questions(self, questions: List[Question]) -> None:


    def end_contest(self) -> None:

    def __repr__(self) -> str:
        return f'Contest [id="{self._id}"]'