from src.entities import Contest, Question, User


class Contestant:
    def __init__(self, user: User, contest: Contest) -> None:
        self._user = user
        self._contest = contest
        self._current_contest_points = 0
        self._attempted_questions = []

    def get_contest(self) -> Contest:
        return self._contest

    def get_user(self) -> User:
        return self._user
    
    def get_current_contest_points(self) -> int:
        return self._current_contest_points

    def add_question(self, question: Question) -> None:
        # Add the Questions attempted by the Contestant in the List.
        self._attempted_questions.append(question)
        # Add the score obtained for the question attempted.
        self._current_contest_points+= question.get_score()

    def __repr__(self) -> str:
        return f'Contestant [user="{self._user.get_name()}, contest={self._contest.get_id()}, current_contest_points={self._current_contest_points}, attempted_questions={self._attempted_questions}"]'