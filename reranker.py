from collections import defaultdict

class Reranker:
    def __init__(self, threshold=0, rank_constant=60):
        self.threshold = threshold  # 分数阈值
        self.rank_constant = rank_constant  # RRF 的 Rank 常数

    def rerank(self, rerank_lists, combined_docs, k=5):
        # 使用 RRF 方法对文档进行重排序
        return self.reciprocal_rank_fusion(rerank_lists, combined_docs, k)

    def reciprocal_rank_fusion(self, rerank_lists, combined_docs, k):
        # 创建一个字典来存储累积分数
        scores = defaultdict(float)

        # 遍历每个重排序列表
        for rerank_list in rerank_lists:
            for rank, doc in enumerate(rerank_list, start=1):
                # 计算 RRF 分数并累加
                scores[doc] += 1 / (self.rank_constant + rank)

        # 按累积分数降序排序文档
        sorted_docs = sorted(scores.items(), key=lambda x: x[1], reverse=True)

        # 根据阈值过滤文档并返回前 k 个文档
        filtered_docs = [(doc, score) for doc, score in sorted_docs if score >= self.threshold]

        # 保持原顺序但只返回filtered_docs中的文档
        final_docs = [doc for doc in combined_docs if doc in dict(filtered_docs)]

        return final_docs[:k]
