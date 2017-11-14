# Tree Edit Models for Recognizing Textual Entailments,Paraphrases,and Answers to Questions

1.任务对象&目标：对相同语言的句子对进行识别，发现其中的复述（paraphrase），蕴含（entailment）现象，此外还能用于问题答案对齐

2.方法：通过贪心算法，搜索两棵树之间的编辑序列，找到其最优编辑序列，并针对编辑序列提取特征（如下表），训练LR分类器

| **Feature**                              | **Description**                          |
| ---------------------------------------- | ---------------------------------------- |
| distance                                 | 两个句子间的编辑距离                               |
| renNoun  renVerb  renOther               | 将一个词语的词性改为名词、动词或是其他类型的词性标记               |
| insN,insV  insPunc  insDet  insOtherPos  | 添加一个词性为名词、词性为动词的词语，添加一个标点符号，添加一个其他类型的词语  |
| delN,delV…                               | 删除一个词性标记为上述类型的节点                         |
| ins{N,V,P}Mod  insSub,insObj  insOtherRel | 对包括名词、动词和介词在内的三种词语类型添加修饰语，添加主语，添加宾语和其他类型的修饰成分。 |
| delNMod…                                 | 对名词、动词和介词删除相应的修饰成分，其成分与上面添加操作一致          |
| renNMod                                  | 对名词、动词和介词重命名其修饰成分，其成分与上面的添加操作一致          |
| XEdits                                   | 包括三种基本编辑操作以及扩展的6种编辑操作                    |
| alignNodes  alignNum  alignN,alignV      | 对相似节点的对齐操作以及对齐节点在一次编辑脚本中的数量。此外还特别关注对齐的名词和动词。 |

3.语料： 

- Microsoft Research Paraphrase Corpus(Dolan et al.2004)复述语料
- RTE-1和RTE-2训练，RTE-3测试 蕴含语料
- TREC-8,TREC-12问答语料

4.性能：paraphrase性能acc 73.2比最优的系统低3个点（2009 PoE）主要是忽略了词义特征和实体识别

5.考虑实验中可以组合传统词义特征，补充阅读微软那篇04年复述论文