import unittest
from src.constants import UserOrder

from src.entities import User
from src.services import UserService
from src.repositories import UserRepository


class UserServiceTests(unittest.TestCase):

    # TODO: WARNING!!!
    #  DO NOT MODIFY ANY FILES IN THE TESTS/ ASSESSMENTS UNLESS ASKED TO.
    #  Any modifications in this file may result in Assessment failure!

    def test_createUser_WhenUserNameGiven_CreateUser(self):
        # Arrange
        userService = UserService(UserRepository())
        expectedId = 1
        expectedName = "User 1"
        # Act
        actual = userService.createUser(expectedName)
        # Assert
        self.assertEqual(expectedId,actual.get_id())
        self.assertEqual(expectedName,actual.get_name())


    def test_getUsers_WhenUserOrderIsScoreASC_ReturnScoreASCWiseUserList(self):
        # Arrange
        userRepository = UserRepository()
        user1 = userRepository.save(User("User 1"))
        user1.modify_score(80)
        user2 = userRepository.save(User("User 2"))
        user2.modify_score(50)
        userService = UserService(userRepository)
        expected = [user2,user1]
        # Act
        actual = userService.getUsers(UserOrder.SCORE_ASC)
        # Assert
        self.assertListEqual(expected,actual)


    def test_getUsers_WhenUserOrderIsScoreDESC_ReturnScoreDESCWiseUserList(self):
        # Arrange
        userRepository = UserRepository()
        user1 = userRepository.save(User("User 1"))
        user1.modify_score(80)
        user2 = userRepository.save(User("User 2"))
        user2.modify_score(90)
        userService = UserService(userRepository)
        expected = [user2,user1]
        # Act
        actual = userService.getUsers(UserOrder.SCORE_DESC)
        # Assert
        self.assertListEqual(expected,actual)


if __name__ == '__main__':
    unittest.main()