#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import sys

print(u"120万人名数据库分析")

family_names = {}
given_names = {}

jin_words = {}
mu_words = {}
shui_words = {}
huo_words = {}
tu_words = {}

line_count = 45

from cnradical import Radical, RunOption

radical = Radical(RunOption.Radical)

def increase_word(table, char):
    if char in table:
        table[char] += 1
    else:
        table[char] = 0
def freq_sort(d):
    result = []
    max = 0
    for w in sorted(d, key=d.get, reverse=True):
        freq = d[w]
        if max == 0:
            max = freq
        result.append((w, float(freq) / max))
    return result
def print_sorted_table(table):
    sorted_table = freq_sort(table)
    count = 0
    for item in sorted_table:
        word, freq = item
        sys.stdout.write(word)
        count += 1
        if count >= line_count:
            count = 0
            sys.stdout.write("\n")
with open("Chinese_Names_Corpus_120W.txt") as fp:
    content = fp.read()
    # content = content.decode('utf-8')
    print("数据库示例")
    print(content[111128:111156].replace('\r\n', ','))
    print(len(content))
    prev_is_line_break = True
    for char in content:
        if ord(char) > 256:
            if prev_is_line_break:
                increase_word(family_names, char)
            else:
                radical_out = radical.trans_ch(char)
                if radical_out == '金' or radical_out == '钅':
                    increase_word(jin_words, char)
                elif radical_out == '木':
                    increase_word(mu_words, char)
                elif radical_out == '水' or radical_out == '氵':
                    increase_word(shui_words, char)
                elif radical_out == '火':
                    increase_word(huo_words, char)
                elif radical_out == '土':
                    increase_word(tu_words, char)
                else:
                    increase_word(given_names, char)
            prev_is_line_break = False
        elif char == '\n' or char == '\r':
            prev_is_line_break = True
    print(u'family name用字总数')
    print(len(family_names))
    print(u'given name用字总数')
    print(len(given_names))
    print()
    print(u"------ 姓氏排序 ------")
    print_sorted_table(family_names)
    sys.stdout.write("\n\n")
    print(u"------ 金 ------")
    print_sorted_table(jin_words)
    sys.stdout.write("\n")
    print(u"------ 木 ------")
    print_sorted_table(mu_words)
    sys.stdout.write("\n")
    print(u"------ 水 ------")
    print_sorted_table(shui_words)
    sys.stdout.write("\n")
    print(u"------ 火 ------")
    print_sorted_table(huo_words)
    sys.stdout.write("\n")
    print(u"------ 土 ------")
    print_sorted_table(tu_words)
    sys.stdout.write("\n\n")
    print(u"------ 过滤金木水火土和姓氏后的 常用起名汉字频率排序表(从120万中国姓名数据库统计) ------")
    sorted_given_names = freq_sort(given_names)
    freq_range = 1.0
    count = 0
    for item in sorted_given_names:
        word, freq = item
        if count == 0:
            count = line_count
            freq_range = freq
            sys.stdout.write(u"\n\n使用频率%.4f " %freq_range)
        sys.stdout.write(word)
        count -= 1
    sys.stdout.write("\n")


