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

    # TODO: CRIO_TASK_MODULE_ENTITIES
    # Complete the implementation of validateQuestions method
    # Implementation must take care of the following cases:-
    # 1) Verify if the level of all the questions and contest matches.
    # 2) Throw a Runtime Exception with an appropriate message if above condition is not true.

    def validate_questions(self, questions: List[Question]) -> None:
        pass

    # TODO: CRIO_TASK_MODULE_ENTITIES
    # Complete the implementation of endContest method
    # Implementation must take care of the following cases:-
    # 1) Mark the status of contest as ended.

    def end_contest(self) -> None:
        pass

    def __repr__(self) -> str:
        return f'Contest [id="{self._id}"]'