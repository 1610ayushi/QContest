from typing import List, Optional

from src.entities import Contestant

class ContestantRepository:
    def __init__(self) -> None:
        self._contestantMap = {}

    def save(self,contestant: Contestant) -> Contestant:
        contestant_id = self._get_contestant_id(contestant)
        self._contestantMap[contestant_id] = contestant
        return contestant

    def find(self,contest_id,user_name) -> Optional[Contestant]:
        # Find the Contestant for a given Contest id and userName from the Dictionary.
        return next(filter(lambda c: c.get_contest().get_id() == contest_id  and c.get_user().get_name() == user_name,self._contestantMap.values()),None)

    def findAllByContestId(self,contest_id) -> List[Contestant]:
        # Find all the Contestants registered for a given contest Id.
        return list(filter(lambda c: c.get_contest().get_id() == contest_id,self._contestantMap.values()))

    def delete(self, contestant: Contestant) -> None:
        contestant_id = self._get_contestant_id(contestant)
        del self._contestantMap[contestant_id]

    def _get_contestant_id(self,contestant):
        # Generate a new ID in this format:- "User[id] Contest[id]"
        # Above representation of ID makes a Contestant unique. 
        return f"User[{contestant.get_user().get_id()}] Contest[{contestant.get_contest().get_id()}]"