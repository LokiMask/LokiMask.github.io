# Vertical Q&A

该模块主要完成基于垂直知识库的问题求解，利用IR检索相似问题，并通过融合浅层语义语法知识以及深度语义特征进行重排序筛选出最终结果

## Installation

程序所依赖的环境如下：

- python 3
- numpy
- gensim
- sklearn
- jdk 1.7+

## Running

首先需要更改配置文件信息

service.properties

1. service_host=[当前服务器地址]
2. sen2vec_port=[sent2vec模块的端口号]
3. Ner_port=[ner模块端口号]
4. qa_port=[用于启动本模块供外部使用的端口号]

sen2vecdata/service.conf

1. service_host=[当前服务器地址]
2. sen2vec_port=[sent2vec模块的端口号]

该模块主体部分用java编写，句子建模部分使用的python，因而运行分为两步进行

1. `python3 ./sen2vecdata/sen2vecsocketservice.py`

2. `cd ./VerticalQa/src/` 

   `bash launch.sh`