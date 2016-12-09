__author__ = 'Administrator'
import util

def compaerMode1AndCorrectAnswer():
    path_model = 'data/predict/model_00001_v.txt'
    path_train = 'data/training_set.tsv'
    model_answerList = []
    train_answerList = []
    answer_number = 2500
    right_answer = 0
    for line in open(path_model):
        lst = line.strip('\n').split(',')
        answer = lst[1]
        model_answerList.append(answer)

    for index,line in enumerate(open(path_train)):
        if index == 0:
            continue
        lst = line.strip('\n').split('\t')
        correctAnswer = lst[2]
        train_answerList.append(correctAnswer)

    for i in range(0,answer_number):
        if(model_answerList[i] == train_answerList[i]):
            right_answer+=1

    print util.norm(float(right_answer)/answer_number)

compaerMode1AndCorrectAnswer()

