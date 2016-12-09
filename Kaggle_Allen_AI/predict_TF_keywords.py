import os

import util
#-*- coding: UTF-8 -*-
set_stopword = ('a', 'an', 'the', 'are', 'is', 'that', 'this', 'will', 'is', 'are', 'was', 'were', 'of', 'for')
def build_d_word_count_on_each_document(dir_data):
    # {path:{word:count}}
    d = {}
    for path in os.listdir(dir_data):
        dd = {}
        path = dir_data + '\\' + path
        for index, line in enumerate(open(path)):
            lst = map(util.norm_word, line.strip('\n').split(','))
            for word in lst:
                dd.setdefault(word, 0)
                dd[word] += 1
        d[path] = dd
    return d

def build_d_question_choice_validation(path_validation):
    d_q_choice = {}
    d_q_id = {}
    for index, line in enumerate(open(path_validation)):
        if index == 0:
            continue
        lst = line.strip('\n').split('\t')
        #print lst
        d_q_choice[lst[1]] = lst[3:]
        #d_q_choice[lst[1]] = lst[2:]
        d_q_id[lst[1]] = lst[0]
    return d_q_choice, d_q_id

def build_d_question_choice_train(path_train):
    d_q_choice = {}
    d_q_id = {}
    for index, line in enumerate(open(path_train)):
        if index == 0:
            continue
        lst = line.strip('\n').split('\t')
        #print lst
        d_q_choice[lst[1]] = lst[3:]
        d_q_id[lst[1]] = lst[0]
    return d_q_choice, d_q_id

def predict(question, lst_path, lst_choice, d_file_wc, d_q_choice):
    d_question_wc = {}
    for path in lst_path[:4]:
        path = path.replace('/','\\')
        try:
            print('path : %s'%(path))
            d_wc = d_file_wc[path]
        except:
            d_wc = {}
            print('d_wc={}')
        for word in d_wc.keys():
            d_question_wc.setdefault(word, 0)
            d_question_wc[word] += d_wc[word]
    MAX = -1
    answer_p = ''
    for index_c, choice in enumerate(d_q_choice[question]):
        n_count = 0
        TF = 0
        lst_word = map(util.norm_word, list(set(choice.split(' ')).difference(set_stopword)))
        for word in lst_word:
            if d_question_wc.has_key(word):
                n_count += d_question_wc[word]
        TF = float(n_count)/len(lst_word)  #important
        if TF > MAX:
            MAX = TF
            if index_c == 0:
                answer_p = 'A'
            elif index_c == 1:
                answer_p = 'B'
            elif index_c == 2:
                answer_p = 'C'
            elif index_c == 3:
                answer_p = 'D'
    return answer_p


def strQ2B(ustring):
    rstring = ""
    for uchar in ustring:
        inside_code=ord(uchar)
        if (inside_code >= 65281 and inside_code <= 65374):
            inside_code -= 65248

        rstring += unichr(inside_code)
    return rstring

def predict_train():
    path_train = 'data/training_set.tsv'
    path_lucene_search_result = 'data/lucene_search_result_train.txt'
    dir_data = 'data/keywords_per_doucment'
    file = open('data/predict/model_keywords.txt', 'w')

    print "Begin build_d_word_count_on_each_document"
    d_file_wc = build_d_word_count_on_each_document(dir_data)
    print "Begin build_d_question_choice_train"
    d_q_choice, d_q_id = build_d_question_choice_train(path_train)
    for index, line in enumerate(open(path_lucene_search_result)):
        lst = line.strip('\n').strip(',').split('\t')
        question = strQ2B(lst[0])
        lst_path = lst[1].split(',')
        lst_choice = d_q_choice[question]
        answer_p = predict(question, lst_path, lst_choice, d_file_wc, d_q_choice)
        file.write(d_q_id[question] + ',' + answer_p + '\n')
    file.close()

def predict_validation():
    path_validation = 'data/training_set.tsv'
    path_lucene_search_result = 'data/lucene_search_result_training_keywords.txt'
    #dir_data = 'C:\workspace\MyPythonWorkspace\kaggle_Allen_AI_get_data\data\wikipedia_content_based_on_ck_12_keyword_one_file_per_keyword'
    dir_data = 'C:\workspace\MyPythonWorkspace\kaggle_Allen_AI_get_data\data\keywords_per_doucment'
    file = open('data/predict/model_keywords_TF_v.txt', 'w')
    #file.write('id,correctAnswer\n')
    print "Begin build_d_word_count_on_each_document"
    d_file_wc = build_d_word_count_on_each_document(dir_data)
   # print(d_file_wc)
    print "Begin build_d_question_choice_validation"
    d_q_choice, d_q_id = build_d_question_choice_validation(path_validation)
    #print d_q_id
    set_id_validation = set([d_q_id[key] for key in d_q_id.keys()])
    set_id_predicted = set()
    for index, line in enumerate(open(path_lucene_search_result)):
        line = line.replace('\\','/');
        lst = line.strip('\n').strip(',').split('\t')
        question = lst[0]
        if question == 'question':
            continue
        id = d_q_id[question]
        set_id_predicted.add(id)
        lst_path = lst[1].split(',')
        lst_choice = d_q_choice[question]
        #print(lst_path)
        answer_p = predict(question, lst_path, lst_choice, d_file_wc, d_q_choice)
        file.write(d_q_id[question] + ',' + answer_p + '\n')
    print 'Missing', len(set_id_validation.difference(set_id_predicted))
    for id in set_id_validation.difference(set_id_predicted):
        file.write(id + ',' + 'C\n')
    file.close()


predict_validation()


