# Combining Distant and Partial Supervision for Relation Extraction

1.背景：属性抽取的性能受制于训练语料不足，而distant supervision的方法又引入了大量噪声。

2.方法：通过高质量的标注先初始化一个全监督分类器，然后通过active learning的方法选择远程监督中标注的数据和初始分类器有歧义（用置信度度量）的并且具有代表性的放到amazon mechanical turk中进行标注，其中代表性采用了Jensen-Shanno divergence(js散度)的度量方式

3.语料：已发布（以获取）

4.性能：baseline是12年的多实例多标签的方法，比之提升了3.9个点

5.需要补充阅读MIMI-RE（Surdeanu et）论文（已整理）