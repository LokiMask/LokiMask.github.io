#__init__.py详解

*init文件讲解*
##简介
init.py是将一个文件夹转化为一个python模块的必备文件，我们在导入一个包的时候，实际上是导入了它的init.py文件。

##功能
- 在init.py中批量导入模块
	e.g.
	 init.py

			#package
			import re
			import urllib
	
	a.py
	
			import package
			print(package.re,package.urllib)
	*注意这里访问init.py中引用的文件需要加入包名*

- init中的重要变量__all__
	e.g.
	init.py
	
		#package
		__all__=['re','urllib']
		
	a.py
	
		from package import *
*这时就会把注册在__init__.py文件中__all__列表中的模块和包导入到当前文件中来*



		