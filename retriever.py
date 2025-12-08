from langchain.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.schema import Document
from rank_bm25 import BM25Okapi
from typing import List
import numpy as np
class Retriever:
    def __init__(self, emb_model_name_or_path, corpus):
        # 使用HuggingFace嵌入模型
        self.embeddings = HuggingFaceEmbeddings(model_name=emb_model_name_or_path)
        
        # 创建FAISS向量存储
        docs = [Document(page_content=" ".join(doc.page_content) if isinstance(doc.page_content, list) else str(doc.page_content)) for doc in corpus]
        self.vectorstore = FAISS.from_documents(docs, self.embeddings)

        # 初始化 BM25 检索器
        self.corpus = [doc.page_content for doc in docs]
        tokenized_corpus = [doc.split(" ") for doc in self.corpus]
        self.bm25 = BM25Okapi(tokenized_corpus)

    def faiss_retrieval(self, query, k=10):
        results = self.vectorstore.similarity_search(query, k=k)
        return [doc.page_content for doc in results]

    def bm25_retrieval(self, query, k=10):
        tokenized_query = query.split(" ")
        bm25_scores = self.bm25.get_scores(tokenized_query)
        top_k_indices = np.argsort(bm25_scores)[-k:][::-1]
        return [self.corpus[idx] for idx in top_k_indices]

    def retrieval(self, query, k=10):
        # 结合两种方法的结果
        faiss_docs = self.faiss_retrieval(query, k)
        bm25_docs = self.bm25_retrieval(query, k)
        # import pdb;pdb.set_trace()
        # 返回重排序所需的数据
        rerank_lists = [faiss_docs, bm25_docs]
        combined_docs = list(dict.fromkeys(faiss_docs + bm25_docs))

        return rerank_lists, combined_docs
