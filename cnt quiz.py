import pandas as pd

def fetch_questions():
    
    df = pd.read_excel("questions.xlsx")

    questions = df.sample(n=10)

    return questions.values.tolist()

def ask_question(question, options, answer):
    print("\n" + question)
    for i, option in enumerate(options):
        print(f"{i+1}) {option}")

    user_answer = input("Resposta (Digite o número da opção correta): ")
    if user_answer.isdigit() and int(user_answer) == answer:
        print("Resposta correta!")
        return 1
    else:
        print("Resposta incorreta!")
        return 0

questions = fetch_questions()

score = 0 

for question, option1, option2, option3, option4, answer in questions:
    options = [option1, option2, option3, option4]
    score += ask_question(question, options, answer)

print ("\===== Pontuação Final =====")
print (f"Total de perguntas: {len(questions)}")
print (f"Perguntas corretas:{score}")
print (f"Perguntas incorretas: {len(questions) - score}")