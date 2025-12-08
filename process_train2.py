SYSTEM="""
你是一个风格化的聊天助手，现在我想把一些有意思的流行梗加入到原来的回答中，使得原来的回答更加风趣、幽默、滑稽、抽象、犀利、骚气，越骚气越好，请你帮我完成新回答的修改撰写，我会给你提供原问答对话和可以融入其中的流行梗。注意融入梗的时候，可以对原来的梗做一些灵活的修改，不必一模一样地把梗加进去，而且使用梗的时候也不用特意用引号标注，这样显得很刻意不够自然。注意一定要自然地运用梗，一点要多利用梗，哪怕稍微偏离一点安慰，也要多融合几个梗进去，就当是在讲笑话，最后圆回来把主题放到安慰上。
原问题：{q}
原回答：{a}
可以加入其中的梗和说明：{g}
请你直接返回修改后的回答，不需要返回其他任何多余的内容、说明或者符号：
"""
import json
prompt_list=[]
with open(r'/root/data/working/liujianhui/nlp_hw/train_with_rag.json','r',encoding='utf-8') as f:
    for line in f.readlines():
        content=json.loads(line)
        prompt=SYSTEM.format(q=content['prompt'],a=content['response'],g=content['rag'])
        prompt_list.append({"prompt":prompt})
        # import pdb;pdb.set_trace()
with open(r'/root/data/working/liujianhui/nlp_hw/train_with_rag_for_poke.json','w',encoding='utf-8') as f:
    for prompt in prompt_list:
        f.write(json.dumps(prompt,ensure_ascii=False)+'\n')