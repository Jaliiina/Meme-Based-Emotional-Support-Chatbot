import pdb
import re

def match_name(text):
    #匹配输入字符在 {梗名称:"  和   ",解释   之间的字符
    pattern=r"{梗名称:\"(.*?)\",解释"
    match=re.search(pattern,text)
    return match.group(1)
def match_content(text):
    #匹配输入字符在 {梗名称:"  和   ",解释   之间的字符
    pattern=r"\",解释:\"(.*?)\"}"
    match=re.search(pattern,text)
    return match.group(1)
with open("/root/data/working/liujianhui/nlp_hw/geng.txt",'r',encoding='utf-8') as f:
    for line in f.readlines():
        name=match_name(line)
        content=match_content(line)
        # print(name+"\n"+content)
        with open()