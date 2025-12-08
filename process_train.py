from run import get_rag
import json
import pdb

content=[]


with open('/root/data/working/liujianhui/nlp_hw/train.json','r',encoding='utf-8') as f:
    for line in f.readlines():
        tmp=json.loads(line)
        # content.append(tmp)
        q_rag=get_rag(tmp['prompt'],2)[:2]
        a_rag=get_rag(tmp['response'],2)[:2]
        q_rag.extend(a_rag)
        total=''.join(q_rag)
        # pdb.set_trace()
        tmp['rag']=total
        content.append(tmp)
with open('/root/data/working/liujianhui/nlp_hw/train_with_rag.json','w',encoding='utf-8') as f:
    for tmp in content:
        f.write(json.dumps(tmp,ensure_ascii=False)+'\n')
