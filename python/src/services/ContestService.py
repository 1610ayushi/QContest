import random
from typing import List
from src.entities import ContestStatus, Contestant, Level, Contest, Question
from src.repositories import ContestRepository, ContestantRepository, QuestionRepository, UserRepository

class ContestService:
    def __init__(
        self,
        contestantRepository: ContestantRepository, 
        contestRepository: ContestRepository,
        questionRepository: QuestionRepository,
        userRepository: UserRepository
        ) -> None:
        self._contestantRepository = contestantRepository
        self._contestRepository = contestRepository
        self._questionRepository = questionRepository
        self._userRepository = userRepository
       
    def createContest(self, title: str, level: Level, created_by: str, num_questions: int) -> Contest:
        # Check if creator exists.
        creator = self._userRepository.findByName(created_by)
        if creator is None:
            raise Exception(f"User with name: {created_by} not found!")
        # Get total count of questions in repository.
        totalQuestionsCount = self._questionRepository.count()
        # Throw RunTime Exception if requested number of questions are not present in the repository.
        if totalQuestionsCount <= num_questions:
            raise Exception(f"Requested Number of questions: {num_questions} cannot be fulfilled!")
        # Get questions with specified level from the repository.
        questionList = self._questionRepository.findAllQuestionLevelWise(level)
        # Pick up random requested number of questions from the question list fetch from the repository.
        randomList = self._pickRandomQuestions(questionList,num_questions);
        # Create a new Contest Object.
        c = Contest(title,level,creator,randomList)
        # Save the contest in the repository.
        saved_contest = self._contestRepository.save(c)
        # Register the Contest Creator to this contest. ( This operation will fail if it is not implemented yet.)
        self.createContestant(saved_contest.get_id(),created_by)
        return saved_contest

    # https:#stackabuse.com/how-to-randomly-select-elements-from-a-list-in-python/
    def _pickRandomQuestions(self, questionList: List[Question], num_questions: int) -> List[Question]:
        return random.sample(questionList,num_questions)
        
    # TODO: CRIO_TASK_MODULE_SERVICES
    # Complete the implementation of getAllContestLevelWise method
    # Implementation must take care of the following cases:-
    # 1) Get all the questions.
    # 2) Get all the questions for a given level.

    def getContests(self, level: Level) -> List[Contest]:
        pass

    # TODO: CRIO_TASK_MODULE_SERVICES
    # Complete the implementation of createContestant method.
    # This method registers the user to the valid contest.
    # Implementation must take care of the following cases:-
    # 1) Validate if the contest and user exists otherwise throw RunTimeException with an appropriate message.
    # 2) Validate if the contest is has not yet started / ended otherwise throw RunTimeException with an appropriate message.
    # 3) Create and store Contestant in the contestantRepository.

    def createContestant(self,contest_id : int, user_name: str ) -> Contestant:
        pass

    def deleteContestant(self,contest_id : int, user_name: str ) -> str:
        # Validate if the user is registered in the contest already.
        contestant = self._contestantRepository.find(contest_id,user_name)
        if contestant is None:
            raise Exception(f"Contestant with {contest_id} and {user_name} not found!")
        status = contestant.get_contest().get_status()
        # Check if contest is valid as per the required conditions.
        if status is ContestStatus.IN_PROGRESS:
            raise Exception(f"Contest has already started!")
        if status is ContestStatus.ENDED:
            raise Exception(f"Contest has already ended!")
        # Delete the contestant from the repository.  
        self._contestantRepository.delete(contestant)
        return f"Contestant with name {user_name} for contest {contest_id} deleted!"

    def runContest(self,contest_id: int, createdBy: str) -> List[Contestant]:
        # Check if contest is valid as per the required conditions.
        contest = self._contestRepository.findById(contest_id)
        if contest is None:
            raise Exception(f"Contest: {contest_id} not found!")
        status = contest.get_status()
        if status is ContestStatus.IN_PROGRESS:
            raise Exception(f"Contest has already started!")
        if status is ContestStatus.ENDED:
            raise Exception(f"Contest has already ended!")
        if contest.get_creator().get_name() != createdBy:
            raise Exception(f"User {createdBy} is not a valid creator for contest {contest_id} !")
        
        contestLevel = contest.get_level()
        # Get all the contestants who registered for the given contest.
        contestantList = self._contestantRepository.findAllByContestId(contest_id)
        contestQuestionList = contest.get_questions()
        contestQuestionListSize = len(contest.get_questions())
        # For each contestant,
        for contestant in contestantList:
            # Select random questions from the contest which will be considered as solved by the contestant.
            solvedQuestionsList = self._pickRandomQuestions(contestQuestionList,random.randrange(contestQuestionListSize))
            # Store the solved questions in the contestant.
            for question in solvedQuestionsList:
                contestant.add_question(question)
            user = contestant.get_user()
            # Generate new totalScore for the user as per the recently solved questions.
            new_score = contestant.get_current_contest_points() + user.get_total_score() - contestLevel.value
            # Update the totalscore of the user.
            user.modify_score(new_score)
        # End the contest once scores are updated for all the users.
        contest.end_contest()
        #  Return the list of contestants in descending order( user with highest score is first ) as per their score in the current contest. 
        contestantList.sort(key=lambda c: c.get_current_contest_points(),reverse=True)
        return contestantList    

    # TODO: CRIO_TASK_MODULE_SERVICES
    # Complete the implementation of contestHistory method.
    # Implementation must take care of the following cases:-
    # 1) Return the list of contestants in descending order( user with highest score is first ) as per their score in a given contest.
    # 2) Throw RunTimeException with an appropriate message if the contest was never ran.

    def contestHistory(self,contest_id) -> List[Contestant]:
        pass

