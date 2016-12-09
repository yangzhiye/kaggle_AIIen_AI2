__author__ = 'Administrator'
import os
from textblob import TextBlob


tar_data = 'data/keywords_per_doucment'
dir_data = 'C:\workspace\MyPythonWorkspace\kaggle_Allen_AI_get_data\data\wikipedia_content_based_on_ck_12_keyword_one_file_per_keyword'
def txt2keywords_each_document(dir_data):
    for path in os.listdir(dir_data):
        try:
            path_name = path
            path = dir_data + '/' + path
            f = open(path)
            string1 = f.read()
            f.close()
            textblob_object = TextBlob(string1)
            wordlist = textblob_object.noun_phrases
            string2 = ''.join(wordlist)
            word_list = string2.split()
            f1 = open('data/keywords_per_doucment/'+path_name,'w')
            for i in word_list:
                   f1.write(i)
                   f1.write(',')
            f1.close()
        except Exception,ex:
             print Exception,":",ex

txt2keywords_each_document(dir_data)
#print text.noun_phrases
