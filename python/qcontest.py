from sys import argv
import traceback
from typing import List
from src.constants import UserOrder
from src.entities import Level
from src.repositories import ContestRepository, ContestantRepository, QuestionRepository, UserRepository
from src.services import ContestService, QuestionService, UserService

def main():
    if len(argv) != 2:
        raise Exception("File path not entered")
    run(argv)

def run(commandLineArgs : List[str]) -> None:
    # Initialize repositories
    questionRepository = QuestionRepository()
    userRepository = UserRepository()
    contestRepository = ContestRepository()
    contestantRepository = ContestantRepository()

    # Initialize services
    questionService = QuestionService(questionRepository)
    userService = UserService(userRepository)
    contestService = ContestService(contestantRepository,contestRepository,questionRepository,userRepository)

    inputFile = commandLineArgs[1].split("=")[1]
    try:
        f = open(inputFile, 'r')
        while True:
            line = f.readline()
            if not line:
                break
            tokens = line.strip().split(" ")

            # Execute Services
            if tokens[0] == "CREATE_USER":
                name = tokens[1]
                u = userService.createUser(name)
                print(u)

            elif tokens[0] == "CREATE_QUESTION":
                title = tokens[1]
                level = Level[tokens[2]]
                score = int(tokens[3])
                q = questionService.createQuestion(title,level,score)
                print(q)

            elif tokens[0] == "LIST_QUESTION":
                if(len(tokens) == 1):
                    qList = questionService.getQuestions(None)
                    print(qList)
                elif(len(tokens) == 2):
                    level = Level[tokens[1]]
                    qList = questionService.getQuestions(level)
                    print(qList)

            elif tokens[0] == "CREATE_CONTEST":
                title = tokens[1]
                level = Level[tokens[2]]
                created_by = tokens[3]
                num_questions = int(tokens[4])
                c = contestService.createContest(title,level,created_by,num_questions)
                print(c)

            elif tokens[0] == "LIST_CONTEST":
                if(len(tokens) == 1):
                    cList = contestService.getContests(None)
                    print(cList)
                elif(len(tokens) == 2):
                    level = Level[tokens[1]]
                    cList = contestService.getContests(level)
                    print(cList)

            elif tokens[0] == "ATTEND_CONTEST":
                contest_id = int(tokens[1])
                user_name = tokens[2]
                c = contestService.createContestant(contest_id,user_name)
                print(c)

            elif tokens[0] == "WITHDRAW_CONTEST":
                contest_id = int(tokens[1])
                user_name = tokens[2]
                c = contestService.deleteContestant(contest_id,user_name)
                print(c)

            elif tokens[0] == "RUN_CONTEST":
                contest_id = int(tokens[1])
                creator_user_name = tokens[2]
                cResultList = contestService.runContest(contest_id,creator_user_name)
                print(cResultList)
                
            elif tokens[0] == "CONTEST_HISTORY":
                contest_id = int(tokens[1])
                cHistoryList = contestService.contestHistory(contest_id)
                print(cHistoryList)

            elif tokens[0] == "LEADERBOARD":
                score_order = UserOrder(f"SCORE_{tokens[1]}")
                uList = userService.getUsers(score_order)
                print(uList)
                
            else:
                raise Exception("Invalid Command")
            
    except Exception as e:
        print(e.__class__, '-', e)
        traceback.print_exc()
    
if __name__ == "__main__":
    main()