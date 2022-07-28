from typing import List
from src.constants import UserOrder
from src.entities import User
from src.repositories import UserRepository

class UserService:
    def __init__(self, userRepository: UserRepository) -> None:
        self._userRepository = userRepository
    
    # TODO: CRIO_TASK_MODULE_SERVICES
    # Complete the implementation of createUser method
    # Implementation must take care of the following cases:-
    # 1) Create and store user in the repository.

    def createUser(self, name: str) -> User:
        pass

    # TODO: CRIO_TASK_MODULE_SERVICES
    # Complete the implementation of getAllUser method
    # Implementation must take care of the following cases:-
    # 1) Get all the users in ascending Order w.r.t score.
    # 2) Get all the users in descending Order w.r.t score.

    def getUsers(self, order: UserOrder) -> List[User]:
        pass
