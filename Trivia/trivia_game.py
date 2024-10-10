from random import shuffle
from time import sleep, time

qna = [

    {
        "Question": "What is the National animal of Scotland?",
        "Answers": ["A. Red Deer", "B. Scottish Wildcat", "C. Unicorn", "D. Puffins"],
        "Correct": "C"
    },

    {
        "Question": "Which country is known as the Land of the Rising Sun?",
        "Answers": ["A. China", "B. Japan", "C. South Korea", "D. Thailand"],
        "Correct": "B"
    },

    {
        "Question": "What is the capital city of Brazil?",
        "Answers": ["A. Buenos Aires", "B. Rio de Janeiro", "C. Brasília", "D. São Paulo"],
        "Correct": "C"
    },

    {
        "Question": "Which element has the chemical symbol 'O'?",
        "Answers": ["A. Silver", "B. Gold", "C. Uranium", "D. Oxygen"],
        "Correct": "A"
    },

    {
        "Question": "Who wrote 'Romeo and Juliet'?",
        "Answers": ["A. Charles Dickens", "B. William Shakespeare", "C. Jane Austen", "D. Mark Twain"],
        "Correct": "B"
    },

    {
        "Question": "In which year did the Titanic sink?",
        "Answers": ["A. 1912", "B. 1920", "C. 1905", "D. 1931"],
        "Correct": "A"
    },

    {
        "Question": "What is the currency of Japan?",
        "Answers": ["A. Yen", "B. Won", "C. Ringgit", "D. Baht"],
        "Correct": "A"
    },

    {
        "Question": "Which famous scientist developed the theory of relativity?",
        "Answers": ["A. Isaac Newton", "B. Galileo Galilei", "C. Albert Einstein", "D. Marie Curie"],
        "Correct": "C"
    },

    {
        "Question": "What is the largest ocean on Earth?",
        "Answers": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Southern Ocean", "D. Pacific Ocean"],
        "Correct": "D"
    },
    {
        "Question": "Who painted the Starry Night?",
        "Answers": ["A. Leonardo da Vinci", "B. Pablo Picasso", "C. Claude Monet ", "D. Vincent van Gogh"],
        "Correct": "D"
    },

    {
        "Question": "Which gas makes up the majority of Earth's atmosphere?",
        "Answers": ["A. Nitrogen", "B. Carbon Dioxide", "C.Oxygen ", "D. Hydrogen"],
        "Correct": "A"
    },

    {
        "Question": "What is the largest mammal in the world?",
        "Answers": ["A. Elephant", "B. Giraffe", "C. Blue Whale", "D. Lion"],
        "Correct": "C"
    },
    {
        "Question": "Which planet is known as the 'Red Planet'?",
        "Answers": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
        "Correct": "B"
    },

    {
        "Question": "Who wrote 'To Kill a Mockingbird'?",
        "Answers": ["A. J.K. Rowling", "B. Harper Lee", "C. George Orwell", "D. Jane Austen"],
        "Correct": "B"
    },

    {
        "Question": "What is the world's largest desert?",
        "Answers": ["A. Sahara Desert", "B. Gobi Desert", "C. Antarctica", "D. Arabian Desert"],
        "Correct": "C"
    },

    {
        "Question": "Which country is known as the 'Land of the Midnight Sun'?",
        "Answers": ["A. Sweden", "B. Norway", "C. Finland", "D. Iceland"],
        "Correct": "B"
    },

    {
        "Question" : "What is the end of a shoelace called?",
        "Answers" : ["A. Terminator", "B. Aglet", "C. Residual ", "D. Bunt"],
        "Correct" : "B" 
    },

    {
        "Question" : "Which planet in our solar system is the hottest?",
        "Answers" : ["A. Mercury", "B. Earth", "C. Jupiter", "D. Venus"],
        "Correct" : "D" 
    },

    {
        "Question" : "What is the largest organ humans possess.",
        "Answers" : ["A. Skin", "B. Heart", "C. Liver", "D. Gut"],
        "Correct" : "A" 
    },

    {
        "Question": "What is the smallest prime number?",
        "Answers": ["A. 0", "B. 1", "C. 2", "D. 3"],
        "Correct": "C"
    }
]

if __name__ == "__main__":
    
    shuffle(qna)
    score = 0
    start = time()

    print("\nTo exit at anytime type exit or quit in the answer field.\n")

    for question in qna:
        print(question["Question"])
        for answer in question["Answers"]:
            print(answer)

        while True:
            u_answer = str(input("Choose A, B, C or D: ").upper())
            
            if u_answer == "":
                print("Please provide an answer. Try again.")
            
            elif u_answer == "EXIT" or u_answer == "QUIT":
                print("Quitters never win. :(\n")
                print(f"Your final score was: {score}/{len(qna)}")
                print(f"Your final time was: {time()-start:.2f} seconds")
                print("\nThe terminal will terminate shortly.")
                sleep(5)
                exit()
            
            elif u_answer == question["Correct"]:
                print("Correct, +1 Point!", '\n')
                score += 1
                break
            
            else:
                print("Wrong!", '\n')
                break

    if 0<=score<5:
        print("You need to work on your trivia...")


    if 5<=score<15:
        print("You lose... atleast you put up a good fight.")

    if 15<=score<20:
        print("YOU WON! But you didn't get a perfect score ( >o<)")

    if score == 20:
        print("PERFECT SCORE!!! WELL DONE!")

    print(f"Your final score was: {score}/{len(qna)}")
    print(f"Your final time was: {time()-start:.2f} seconds")
    print("\nThe terminal will terminate shortly.")
    sleep(5)

