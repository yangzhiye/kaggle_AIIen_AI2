import wikipedia as wiki

from test_python_grammer import util


def get_wikipedia_content_based_on_ck_12_keyword_one_file_per_keyword():
    path_keyword = 'data/ck12_list_keyword.txt'
    lst_keyword = open(path_keyword).readlines()
    content = None
    n_total = len(lst_keyword)
    for index, line in enumerate(lst_keyword):
        keyword = line.strip('\n').lower()
        print index, n_total, index * 1.0 / n_total, keyword
        try:
            content = wiki.page(keyword).content.encode('ascii', 'ignore')
        except wiki.exceptions.DisambiguationError as e:
            print 'DisambiguationError', keyword
        except:
            print 'Error', keyword
        if not content:
            continue
        file = open('data/'+'_'.join(keyword.split()) + '.txt', 'w')
        for line in content.split('\n'):
            line = ' '.join(map(util.norm_word, line.split()))
            if line:
                file.write(line + '\n')
        file.close()

get_wikipedia_content_based_on_ck_12_keyword_one_file_per_keyword()
