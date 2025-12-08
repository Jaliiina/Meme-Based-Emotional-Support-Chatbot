from retriever import Retriever
from reranker import Reranker
from reader import Reader
import pdb

from req_wenxin import get_completion
from req_doubao import get_doubao
import json
import random
import os
import gradio as gr
import pickle
URL1="w8smrcmj_l0408comfort_spd"
reader = Reader(r'/root/data/working/liujianhui/nlp_hw/geng')
corpus = reader.load()
retriever = Retriever(corpus=corpus, emb_model_name_or_path='/share/models/bge-large-zh-v1.5')
reranker = Reranker()
SYSTEM="""
你是一个风格化的聊天助手，现在我想把一些有意思的流行梗加入到原来的回答中，使得原来的回答更加风趣、幽默、滑稽、抽象、犀利、骚气，越骚气越好，请你帮我完成新回答的修改撰写，我会给你提供原问答对话和可以融入其中的流行梗。注意融入梗的时候，可以对原来的梗做一些灵活的修改，不必一模一样地把梗加进去，而且使用梗的时候也不用特意用引号标注，这样显得很刻意不够自然。注意一定要自然地运用梗，一点要多利用梗，哪怕稍微偏离一点安慰，也要多融合几个梗进去，就当是在讲笑话，最后圆回来把主题放到安慰上。
原问题：{q}
原回答：{a}
可以加入其中的梗和说明：{g}
请你直接返回修改后的回答，不需要返回其他任何多余的内容、说明或者符号：
"""
def get_rag(text,top_num):
    # 检索文档
    rerank_lists, combined_docs = retriever.retrieval(text, k=top_num)
    # 重排序文档
    reranked_docs = reranker.rerank(rerank_lists, combined_docs, k=top_num)
    # pdb.set_trace()
    return reranked_docs

def get_msg(id):
    base_path=r'/root/data/working/liujianhui/nlp_hw/chat_saving/'+str(id)+'.pkl'
    if os.path.exists(base_path):
        with open(base_path,'rb') as f:
            return pickle.load(f)
    else:
        return []
def save_msg(message,id):
    base_path=r'/root/data/working/liujianhui/nlp_hw/chat_saving/'+str(id)+'.pkl'
    with open(base_path,'wb') as f:
        pickle.dump(message,f)



def chat(query,id):
    #获取用户历史消息
    message=get_msg(id)
    #截取最近5轮对话
    if len(message)>=10:
        message=message[:10]

    #更新消息对话
    message.append({'role':'user','content':query})
    #存储
    save_msg(message,id)
    #获取无梗回答
    response=get_completion(eval(json.dumps(message,ensure_ascii=False)),URL1)
    # pdb.set_trace()
    #检索梗
    q_rag=get_rag(query,2)[:2]
    a_rag=get_rag(response,4)[:4]
    q_rag.extend(a_rag)
    total=''.join(q_rag)

    #提示词引导
    prompt=SYSTEM.format(q=query,a=response,g=total)

    #获取带梗回答
    answer=get_doubao(prompt)
    # pdb.set_trace()

    #更新消息记录
    message.append({'role':'assistant','content':answer})
    save_msg(message,id)
    return answer


def chat_with_model(input_text, user_id):
    return chat(input_text, user_id)
def new_user_id():
    return str(random.randint(1000000000, 9999999999))
# 创建Gradio界面
with gr.Blocks() as demo:
    gr.Markdown("## Chat with ME")
    
    user_id_input = gr.State()  # 初始化时不设置值
    
    with gr.Row():
        with gr.Column():
            chatbox = gr.Chatbot()
            user_input = gr.Textbox(placeholder="Type your question here...", label="Your Question")
            submit_button = gr.Button("Send")

    # 在页面加载时生成新的用户ID
    demo.load(fn=new_user_id, outputs=[user_id_input])

    # 处理用户输入和模型响应
    def respond(message, user_id, chat_history):
        user_message = f"用户: {message}"  # 用户消息前缀
        response = chat_with_model(message, user_id)
        jay_chou_message = f"助手: {response}"  # 周杰伦消息前缀
        
        chat_history.append((user_message, jay_chou_message))  # 更新聊天记录
        return chat_history, ""  # 清空输入框

    submit_button.click(respond, [user_input, user_id_input, chatbox], [chatbox, user_input])

# 启动Gradio应用，设置host和port
demo.launch(server_name="0.0.0.0", server_port=8805)
