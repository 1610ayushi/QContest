from typing import List, Optional
from src.entities import Level
from src.entities.Question import Question

class QuestionRepository:
    def __init__(self) -> None:
        self._questionMap = {}
        self._autoIncrement = 1

    def save(self,question: Question) -> Question:
        # Create a new Question object with all the parameters with an unique ID.
        q = Question(question.get_title(),question.get_level(),question.get_score(),self._autoIncrement)
        # Store the newly created question object to Dictionary.
        self._questionMap[self._autoIncrement] = q
        # Increment the variable which will be used when next question is saved.
        self._autoIncrement += 1
        return q

    def findAll(self) -> List[Question]:
        # Return all the users stored in Dictionary.
        return list(self._questionMap.values())

    def findById(self, id: int) -> Optional[Question]:
        # Find an user for a given id stored in Dictionary.
        return self._questionMap.get(id)

    def findAllQuestionLevelWise(self,level: Level) -> List[Question]:
        # Find all the contests for a given level stored in Dictionary.
        return list(filter(lambda q: q.get_level() == level,self._questionMap.values()))

    def count(self) ->  int:
        return len(self._questionMap)