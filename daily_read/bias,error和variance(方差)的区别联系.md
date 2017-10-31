# bias,error和variance(方差)的区别联系

![v2-286539c808d9a429e69fd59fe33a16dd_b](/Users/songrui/Downloads/v2-286539c808d9a429e69fd59fe33a16dd_b.png)
$$
error=bias+variance
$$

* error反映的是整个模型的***准确度***
* bias反映的是模型在样本上输出与真实值之间的***误差***，简单讲，就是模型在样本上拟合得好不好。
  * bias上表现好（即low bias）=复杂化模型，增加模型参数—>过拟合  
* variance样本训练出来的模型在测试集的表现，即***稳定性***
  * variance上表现好（即low varience）=简化模型，减少模型参数—>欠拟合

> *引用林轩田老师的课的解释,减少error分如下两步：*
>
> *1.error(train)尽可能小*
>
> *2.error(train)尽可能等于error(test)*

