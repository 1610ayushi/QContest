class User:
    def __init__(self, name: str, id=None ) -> None:
        self._name = name
        self._total_score = 150
        self._id = id

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_total_score(self):
        return self._total_score

    # TODO: CRIO_TASK_MODULE_ENTITIES
    # Complete the implementation of modifyScore method
    # Implementation must take care of the following cases:-
    # 1) Set an appropriate totalScore.
    # 2) Throw a Runtime Exception with an appropriate message for invalid score.

    def modify_score(self, score: int) -> None:
        pass

    def __repr__(self) -> str:
        return f'User [id="{self._id}"]'