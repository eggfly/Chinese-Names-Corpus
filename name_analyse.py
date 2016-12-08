#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import sys

print(u"120万人名数据库分析")

words = {}

def freq_sort(d):
    result = []
    max = 0
    for w in sorted(d, key=d.get, reverse=True):
        freq = d[w]
        if max == 0:
            max = freq
        result.append((w, float(freq) / max))
    return result

with open("Chinese_Names_Corpus_120W.txt") as fp:
    content = fp.read()
    content = content.decode('utf-8')
    print("数据库示例")
    print(content[111128:111256].replace('\r\n', ','))
    print len(content)
    for char in content:
        if ord(char) < 256:
            continue
        if char in words:
            words[char] += 1
        else:
            words[char] = 0
    print(u'用字总数')
    print(len(words))
    print(u'所有用字')
    print(u"".join([char for char in words]))
    print()
    print(u"------ 起名常用汉字频率排序表(从120万中国姓名数据库统计) ------")
    sorted_words = freq_sort(words)
    freq_range = 1.0
    every_count = 50
    count = 0
    for item in sorted_words:
        word, freq = item
        if count == 0:
            count = every_count
            freq_range = freq
            print u"\n使用频率%.4f " %freq_range,
        sys.stdout.write(word)
        count -= 1
    sys.stdout.write("\n")


