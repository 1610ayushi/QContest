import unittest
from src.entities import Contest, ContestStatus, Level, User, Question

class ContestTests(unittest.TestCase):

    # TODO: WARNING!!!
    #  DO NOT MODIFY ANY FILES IN THE TESTS/ ASSESSMENTS UNLESS ASKED TO.
    #  Any modifications in this file may result in Assessment failure!

    def test_Contest_WhenQuestionLevelMisMatch_ThrowRuntimeException(self):
        # Arrange
        title = "Crio.Do Launch'22"
        level  = Level.LOW
        createdBy = User("Cri(o Admin")
        questions = [Question("Q1",Level.HIGH,10)]
        # Act and Assert
        self.assertRaises(Exception,Contest,title, level, createdBy, questions)

    def test_endContest_WhenContestIsEnded_EndContest(self):
        # Arrange
        title = "Crio.Do Launch'22"
        level  = Level.LOW
        createdBy = User("Cri(o Admin")
        questions = [Question("Q1",level,10)]
        contest = Contest(title, level, createdBy, questions)
        # Act
        contest.end_contest()
        # Assert
        self.assertEqual(ContestStatus.ENDED,contest.get_status())

if __name__ == '__main__':
    unittest.main()