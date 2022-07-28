from typing import List, Optional

from src.entities import User

class UserRepository:
    def __init__(self) -> None:
        self._userMap = {}
        self._autoIncrement = 1

    # TODO: CRIO_TASK_MODULE_SERVICES
    # Complete the implementation of save method
    # Implementation must take care of the following cases:-
    # 1) Save a new user with unique ID to Dictionary. ( Make use of AutoIncrement for unique ID)
    # 2) Increment autoIncrement variable once new user is saved.

    def save(self,user: User) -> User:
        pass

    # TODO: CRIO_TASK_MODULE_SERVICES
    # Complete the implementation of findAll method
    # Implementation must take care of the following cases:-
    # 1) Return all the users stored in HashMap.

    def findAll(self) -> List[User]:
        pass

    def findById(self, id: int) -> Optional[User]:
        return self._userMap.get(id)

    def findByName(self,name: str) -> Optional[User]:
    # Find an user which matches with the required name.
        return next(filter(lambda u: u.get_name() == name,self._userMap.values()),None)