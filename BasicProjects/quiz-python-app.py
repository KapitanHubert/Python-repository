import requests
import html

class Question:
    def __init__(self,category, questionStr,correctAnswerFlag):
        self.category = category
        self.questionSTR = questionStr
        self.correctAnswer = correctAnswerFlag

class Quiz:
    def __init__(self,numQuestions):
        self.apiURL = "https://opentdb.com/api.php?difficulty=easy&type=boolean&amount="
        self.numQuestions = numQuestions
        self.Questionlist = []
        self.loadQuestions(numQuestions)
#{'response_code': 0, 'results': [{'type': 'boolean', 'difficulty': 'easy', 'category': 'Entertainment: Video Games', 'question': 'The Kerbol System (from Kerbal Space Program) includes a Saturn analogue.', 'correct_answer': 'False', 'incorrect_answers': ['True']}, {'type': 'boolean', 'difficulty': 'easy', 'category': 'Animals', 'question': 'The Killer Whale is considered a type of dolphin.', 'correct_answer': 'True', 'incorrect_answers': ['False']}, {'type': 'boolean', 'difficulty': 'easy', 'category': 'Animals', 'question': 'A slug&rsquo;s blood is green.', 'correct_answer': 'True', 'incorrect_answers': ['False']}, {'type': 'boolean', 'difficulty': 'easy', 'category': 'Entertainment: Video Games', 'question': 'In the &quot;S.T.A.L.K.E.R.&quot; series, the Freedom faction wishes to destroy the supernatural area known as  &quot;the Zone&quot;.', 'correct_answer': 'False', 'incorrect_answers': ['True']}, {'type': 'boolean', 'difficulty': 'easy', 'category': 'Geography', 'question': 'Nova Scotia is on the east coast of Canada.', 'correct_answer': 'True', 'incorrect_answers': ['False']}, {'type': 'boolean', 'difficulty': 'easy', 'category': 'Animals', 'question': 'The Axolotl is an amphibian that can spend its whole life in a larval state.', 'correct_answer': 'True', 'incorrect_answers': ['False']}, {'type': 'boolean', 'difficulty': 'easy', 'category': 'History', 'question': 'The Spitfire originated from a racing plane.', 'correct_answer': 'True', 'incorrect_answers': ['False']}, {'type': 'boolean', 'difficulty': 'easy', 'category': 'Animals', 'question': 'Rabbits are rodents.', 'correct_answer': 'False', 'incorrect_answers': ['True']}, {'type': 'boolean', 'difficulty': 'easy', 'category': 'General Knowledge', 'question': 'Studies suggest that approximately 40% of the world population is left-handed.', 'correct_answer': 'False', 'incorrect_answers': ['True']}, {'type': 'boolean', 'difficulty': 'easy', 'category': 'Sports', 'question': 'Peyton Manning retired after winning Super Bowl XLIX.', 'correct_answer': 'False', 'incorrect_answers': ['True']}]}
    def loadQuestions(self,numQuestions):
        response = requests.get(self.apiURL + str(numQuestions))

        if response.ok:
            #print(response.json())
            data = response.json()
            results = data["results"]

        for q in results:
            category = q["category"]
            questionType = q["type"]
            difficulty = q["difficulty"]
            questionStr = html.unescape(q["question"])
            #print(questionStr)
            correctAnswerFlag = q["correct_answer"].lower() in [ "true" , "1" , "yes" ]
            #print(q["correct_answer"],correctAnswerFlag)
            
            qObj = Question(category,questionStr,correctAnswerFlag)
            self.Questionlist.append(qObj)

    def startQuiz(self):
        print("\nWelcome in Quiz !")
        numCorrectUserAnswers  = 0
        n = 0
        numQuestions = len(self.Questionlist)
        
        while n < numQuestions:
            q = self.Questionlist[n]
            print("Question Number " + str( n + 1 ) + ": " + q.questionSTR)
            #print(q.correctAnswer)
            answer = input("Give correct answer as (y/n) : ")
            answerBool = False
            if answer == "y":answerBool = True       
            if answerBool == q.correctAnswer:
                print("Dobra Odpowiedź !")
                numCorrectUserAnswers += 1
            else:
                print("Zła odpowiedź !")
            n += 1
        print("Poprawne odpowiedzi :",str(numCorrectUserAnswers)+"/"+str(n))

quiz = Quiz(10)
quiz.startQuiz()