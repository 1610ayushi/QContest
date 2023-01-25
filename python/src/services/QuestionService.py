from typing import List
from src.entities import Level, Question
from src.repositories import QuestionRepository

class QuestionService:
    def __init__(self, questionRepository: QuestionRepository) -> None:
        self._questionRepository = questionRepository

    def createQuestion(self, title: str, level: Level, difficultyScore: int) -> Question:
        q = Question(title,level,difficultyScore)
        return self._questionRepository.save(q)

    def getQuestions(self, level: Level) -> List[Question]:
        if level is None:
            return self._questionRepository.findAll()
        return self._questionRepository.findAllQuestionLevelWise(level)
