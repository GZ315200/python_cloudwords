import codecs
import jieba.analyse

wf = codecs.open('clean_title.txt', 'w+','utf-8')
for line in open('/Users/mazean/PycharmProjects/unistacks/csvFile2.csv'):
    item = line.strip('\n\r').split('\t')
    # tags = jieba.cut(item,cut_all=False)
    tags = jieba.analyse.extract_tags(line,topK=20)
    tagsw = ",".join(tags)
    wf.write(tagsw)

wf.close()