# kaggle_AIIen_AI2
kaggle,The Allen AI Science Challenge,Is your model smarter than an 8th grader, QA about American 8th grade science multiple-choice questions

##1.获取数据
1. 在http://www.ck12.org/上爬取与美国八年级科学相关的关键词。

2. 爬取这些关键词对应的维基百科正文。

##2.搭建本地搜索引擎
1. 使用Lucene3.5建立倒排索引并搜索

2. 搜索结果为topN相关维基百科正文

##3.计算答案与topN维基百科正文相似度
1. 使用TF-IDF
2. 使用textrank算法提取关键词，之后使用word2vec计算相似度。

##备注:本人本科毕设论文已上传至github。 