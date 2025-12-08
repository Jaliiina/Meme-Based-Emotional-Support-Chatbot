# import os
# import glob
# import re
# from langchain.schema import Document

# class Reader:
#     def __init__(self, corpus_path, max_len=128, overlap_sentences=2):
#         self.corpus_path = corpus_path
#         self.max_len = max_len
#         self.overlap_sentences = overlap_sentences

#     def load(self):
#         supported_files = {
#             '.txt': self.read_txt,
#             # 后续有别的文件类型可以继续添加
#         }

#         all_texts = []  # 用一个列表来收集所有文档的文本
#         for filepath in glob.glob(os.path.join(self.corpus_path, "*")):
#             _, ext = os.path.splitext(filepath)
#             if ext in supported_files:
#                 print(f"Processing {filepath}")
#                 document_texts = supported_files[ext](filepath)
#                 all_texts.extend(document_texts)  # 将文本添加到列表中
#             else:
#                 print(f"Unsupported file type: {filepath}")

#         return [Document(page_content=text) for text in all_texts]

#     def read_txt(self, filepath):
#         with open(filepath, 'r', encoding='utf-8') as file:
#             content = file.read().replace('\n', ' ')  # 假设换行符可以被空格替代

#         sentences = re.split(r'(?<=[.!?]) +', content)
#         chunks = []
#         chunk = []
#         chunk_len = 0

#         for i, sentence in enumerate(sentences):
#             chunk.append(sentence)
#             chunk_len += len(sentence)

#             if chunk_len >= self.max_len:
#                 if len(chunks) > 0:
#                     chunk = sentences[i - self.overlap_sentences:i] + chunk
#                 chunks.append(' '.join(chunk))
#                 chunk = []
#                 chunk_len = 0

#         if chunk:  # 添加最后一个块
#             if len(chunks) > 0:
#                 chunk = sentences[len(sentences) - self.overlap_sentences:] + chunk
#             chunks.append(' '.join(chunk))

#         return chunks

import os
import glob
from langchain.schema import Document

class Reader:
    def __init__(self, corpus_path, max_len=128, overlap_len=32):
        self.corpus_path = corpus_path
        self.max_len = max_len
        self.overlap_len = overlap_len

    def load(self):
        supported_files = {
            '.txt': self.read_txt,
            # 后续有别的文件类型可以继续添加
        }

        all_texts = []  # 用一个列表来收集所有文档的文本
        for filepath in glob.glob(os.path.join(self.corpus_path, "*")):
            _, ext = os.path.splitext(filepath)
            if ext in supported_files:
                print(f"Processing {filepath}")
                document_texts = supported_files[ext](filepath)
                all_texts.extend(document_texts)  # 将文本添加到列表中
            else:
                print(f"Unsupported file type: {filepath}")

        return [Document(page_content=text) for text in all_texts]

    def read_txt(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
        #     content = file.read().replace('\n', ' ')  # 假设换行符可以被空格替代

        # cleaned_chunks = []
        # i = 0
        # while i < len(content):
        #     cur_s = content[i:i+self.max_len]
        #     if len(cur_s) > 10:  # 可以添加更多条件来过滤掉不想要的片段
        #         cleaned_chunks.append(cur_s)
        #     i += (self.max_len - self.overlap_len)  # 移动索引，保留重叠部分
            cleaned_chunks=file.read().split('\n')

        return cleaned_chunks