import unittest
from src.entities import User

class UserTests(unittest.TestCase):

    # TODO: WARNING!!!
    #  DO NOT MODIFY ANY FILES IN THE TESTS/ ASSESSMENTS UNLESS ASKED TO.
    #  Any modifications in this file may result in Assessment failure!

    def test_modifyScore_WhenScoreNegative_ThrowRunTimeException(self):
        # Arrange
        user = User("Crio User 1")
        # Act and Assert
        self.assertRaises(Exception,user.modify_score,-1)

    def test_modifyScore_WhenScoreIsModified_ModifyScore(self):
        # Arrange
        user = User("Crio User 1")
        # Act
        user.modify_score(50)
        # Assert
        self.assertEqual(50,user.get_total_score())
    
    
if __name__ == '__main__':
    unittest.main()