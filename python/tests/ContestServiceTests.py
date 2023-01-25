import unittest
from src.entities import Contest, Contestant, Level, Question, User

from src.repositories import ContestRepository, ContestantRepository, QuestionRepository, UserRepository
from src.services import ContestService

class ContestServiceTests(unittest.TestCase):

    # TODO: WARNING!!!
    #  DO NOT MODIFY ANY FILES IN THE TESTS/ ASSESSMENTS UNLESS ASKED TO.
    #  Any modifications in this file may result in Assessment failure!

    def setUp(self) -> None:
        self.questionRepository = QuestionRepository()
        self.q1 = self.questionRepository.save(Question("Question 1",Level.LOW,10))
        self.q2 = self.questionRepository.save(Question("Question 2",Level.MEDIUM,20))
        self.q2a = self.questionRepository.save(Question("Question 2a",Level.MEDIUM,30))
        self.q2b = self.questionRepository.save(Question("Question 2b",Level.MEDIUM,40))
        self.q3 = self.questionRepository.save(Question("Question 3",Level.HIGH,30))
        self.userRepository = UserRepository()
        self.u1 = self.userRepository.save(User("User 1"))
        self.u2 = self.userRepository.save(User("User 2"))
        self.u3 = self.userRepository.save(User("User 3"))
        self.contestRepository = ContestRepository()
        self.c1 = self.contestRepository.save(Contest("Contest 1",Level.LOW,self.u1,[self.q1]))
        self.c2 = self.contestRepository.save(Contest("Contest 2",Level.MEDIUM,self.u2,[self.q2,self.q2a,self.q2b]))
        self.c3 = self.contestRepository.save(Contest("Contest 3",Level.HIGH,self.u3,[self.q3]))
        self.contestantRepository = ContestantRepository()
        self.ca1 = self.contestantRepository.save(Contestant(self.u1,self.c2))
        self.ca1.add_question(self.q2)
        self.ca2 = self.contestantRepository.save(Contestant(self.u2,self.c2))
        self.ca2.add_question(self.q2)
        self.ca2.add_question(self.q2a)
        self.ca3 = self.contestantRepository.save(Contestant(self.u3,self.c2))
        self.ca3.add_question(self.q2a)
        self.ca3.add_question(self.q2b)

        self.contestService = ContestService(self.contestantRepository, self.contestRepository, self.questionRepository, self.userRepository)

    def test_getContests_WhenLevelIsNull_ReturnAllContests(self):
        # Arrange
        expected = [self.c1,self.c2,self.c3]
        # Act
        actual = self.contestService.getContests(None)
        # Assert
        self.assertListEqual(expected,actual)

    def test_getContests_WhenLevelGiven_ReturnContestsForGivenLevel(self):
        # Arrange
        expected = [self.c1]
        # Act
        actual = self.contestService.getContests(Level.LOW)
        # Assert
        self.assertListEqual(expected,actual)



    def test_createContestant_WhenContestNotFound_ThrowRuntimeException(self):
        # Arrange
        # Act and Assert
        self.assertRaises(Exception,self.contestService.createContestant,4,"User 1")

    def test_createContestant_WhenUserNameNotFound_ThrowRuntimeException(self):
        # Arrange
        # Act and Assert
        self.assertRaises(Exception,self.contestService.createContestant,3,"User 4")

    def test_createContestant_WhenContestNotValid_ThrowRuntimeException(self):
        # Arrange
        self.c3.end_contest();
        # Act and Assert
        self.assertRaises(Exception,self.contestService.createContestant,3,"User 1")

    def test_createContestant_WhenContestIdAndUserNameGiven_CreateContestant(self):
        # Arrange
        expectedUserName = "User 1"
        expectedContestId = 3
        # Act
        contestant = self.contestService.createContestant(expectedContestId,expectedUserName)
        # Assert
        self.assertEqual(expectedUserName, contestant.get_user().get_name())
        self.assertEqual(expectedContestId, contestant.get_contest().get_id())


    def test_contestHistory_WhenContestNotFound_ThrowRuntimeException(self):
        # Arrange
        # Act and Assert
        self.assertRaises(Exception,self.contestService.contestHistory,4)

    def test_contestHistory_WhenContestNotEnded_ThrowRuntimeException(self):
        # Arrange
        # Act and Assert
        self.assertRaises(Exception,self.contestService.contestHistory,2)

    def test_contestHistory_WhenContestEnded_ReturnContestants(self):
        # Arrange
        expected = [self.ca3,self.ca2,self.ca1]
        self.c2.end_contest()
        # Act
        actual = self.contestService.contestHistory(2)
        # Assert
        self.assertListEqual(expected,actual)

    
if __name__ == '__main__':
    unittest.main()