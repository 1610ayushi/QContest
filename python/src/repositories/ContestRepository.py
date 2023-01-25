from typing import List, Optional

from src.entities import Contest, Level

class ContestRepository:
    def __init__(self) -> None:
        self._contestMap = {}
        self._autoIncrement = 1

    def save(self,contest: Contest) -> Contest:
        c = Contest(contest.get_title(),contest.get_level(),contest.get_creator(),contest.get_questions(),self._autoIncrement)
        self._contestMap[self._autoIncrement] = c
        self._autoIncrement += 1
        return c

    def findAll(self) -> List[Contest]:
        return list(self._contestMap.values())

    def findById(self, id: int) -> Optional[Contest]:
        return self._contestMap.get(id)

    # TODO: CRIO_TASK_MODULE_SERVICES
    # Complete the implementation of findAllContestLevelWise method
    # Implementation must take care of the following cases:-
    # 1) Find all the contests for a given level.

    def findAllContestLevelWise(self,level: Level) -> List[Contest]:
        pass
