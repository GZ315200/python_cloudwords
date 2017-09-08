
# -*- coding:utf-8 -*-
#coding=utf-8
import codecs

import MySQLdb

word_lst = []
word_dict = {}
conn = MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='2241883',
        db ='keyword_list',
        )
cur = conn.cursor()
with open('/Users/mazean/PycharmProjects/unistacks/clean_title.txt') as wf, open("word.txt", 'w') as wf2:

  for word in wf:
    word_lst.append(word.split(','))
    for item in word_lst:
        for item2 in item:
            if item2 not in word_dict:word_dict[item2] = 1
        else:
            word_dict[item2] += 1

  for key in word_dict:
    # cur.execute('insert into word_analysis values (NULL ,%s,%s)', (key, word_dict[key]))
    print key, word_dict[key]
    wf2.write(key + ' ' + str(word_dict[key]) + '\n')



