__author__ = 'Administrator'
import wikipedia as wiki

from test_python_grammer import util


def get_wikipedia_content_based_on_ck_12_keyword_one_file_per_keyword():
    '''
    Get wikipedia page content based on the keywords crawled from the ck-12 website.
    '''
    path_keyword = 'data/ck12_list_keyword.txt'
    dir_output = 'data/wikipedia_content_based_on_ck_12_keyword_one_file_per_keyword/'
    #path_keyword = 'data/training_set_question.tsv'
    #dir_output = 'data/wikipedia_content_based_on_train_question_one_file_per_keyword/'
    #path_keyword = 'data/validation_set_question.tsv'
    #dir_output = 'data/wikipedia_content_based_on_validation_question_one_file_per_keyword/'
    path_meta = path_keyword[:-4] + '_wiki_meta.tsv'
    file_meta = open(path_meta, 'w')
    lst_keyword = open(path_keyword).readlines()
    n_total = len(lst_keyword)
    for index, line in enumerate(lst_keyword):
        keyword = line.strip('\n').lower()
        print index, n_total, index * 1.0 / n_total, keyword
        content = None
        title = None
        try:
            content = wiki.page(keyword).content.encode('ascii', 'ignore')
            url = wiki.page(keyword).url.encode('ascii', 'ignore')
            title = wiki.page(keyword).title.encode('ascii', 'ignore')
        except wiki.exceptions.DisambiguationError as e:
            print 'DisambiguationError', keyword
        except:
            print 'Error', keyword
        if not content or not title:
            continue
        file_meta.write("%s\t%s\t%s\n" % (keyword, title, url))
        #file = open('data/wikipedia_content_based_on_ck_12_keyword_one_file_per_keyword/' + '_'.join(keyword.split()) + '.txt', 'w')
        path_output = dir_output + '/' + '_'.join(title.replace('/', '__').split()) + '.txt'
        file = open(path_output, 'w')
        for line in content.split('\n'):
            line = ' '.join(map(util.norm_word, line.split()))
            if line:
                file.write(line + '\n')
        file.close()

def get_wikipedia_meta_based_on_ck_12_keyword_one_file_per_keyword():
    '''
    Get wikipedia title, url information for the wikipedia page of the keywords
    '''
    path_keyword = 'data/ck12_list_keyword.txt'
    file = open(path_keyword[:-4] + '_meta.tsv', 'w')
    lst_keyword = open(path_keyword).readlines()
    n_total = len(lst_keyword)
    for index, line in enumerate(lst_keyword):
        keyword = line.strip('\n').lower()
        print index, n_total, index * 1.0 / n_total, keyword
        try:
            url = wiki.page(keyword).url.encode('ascii', 'ignore')
            title = wiki.page(keyword).title.encode('ascii', 'ignore')
            #content = wiki.page(keyword).content.encode('ascii', 'ignore')
        except wiki.exceptions.DisambiguationError as e:
            print 'DisambiguationError', keyword
        except:
            print 'Error', keyword
        res = "%s\t%s\t%s\n" % (keyword, title, url)
        file.write(res)
    file.close()

#get_wikipedia_meta_based_on_ck_12_keyword_one_file_per_keyword()
get_wikipedia_content_based_on_ck_12_keyword_one_file_per_keyword()
#get_wikipedia_content_based_on_ck_12_keyword(