Robot Framework 介绍
Robot Framework 是一款基于 Python 的功能自动化测试框架。它具备良好的可扩展性，支持关键字驱动，可以同时测试多种类型的客户端或者接口，可以进行分布式测试执行。主要用于轮次很多的验收测试和验收测试驱动开发（ATDD）。在我们进行全球化测试的时候可以用此框架来编写一些脚本任务，如定时下载 daily build , 配合 Selenium 完成自动化截图等，来方便我们的测试。

一、安装：
1、安装及运行所依赖的第三方库均可通过 Python 的包管理器 pip 进行安装。
 pip3 install robotframework
 
2、安装 wxPython：（不安装则无法运行 RIDE 编辑器）
 pip3 install wxpython

3、安装 RIDE 编辑器：
pip3 install robotframework-ride

4、安装常用的第三方库：
pip3 install robotframework-seleniumlibrary  # 用于进行 Web 自动化测试
pip3 install robotframework-appiumlibrary  # 用于进行 app 自动化测试
pip3 install robotframework-requests  # 用于进行接口自动化测试
pip3 install robotframework-autoitlibrary  # 用于进行 Windows GUI 自动化测试（专用于 Windows 系统，安装时需要管理员权限）


二、Robot Framework IDE (RIDE) 编辑器的基本使用
具体可以参考：https://www.jianshu.com/p/9dcb4242b8f2

今天主要学习了requests库的关键字
F5可以查询关键字
注意项：首先需要在suite那里添加：RequestsLibrary

创建一个POST接口case

Create Session   首先使用关键字create session创建一个会话，连接到服务器的host。脚本格式：关键字   别名   域名

通过关键字create dictionary创建一个变量${header}，用于存放请求的头文件
通过关键字create dictionary创建一变量${param}，用于存放多个入参
通过关键字post request（如果是get方式，则使用关键字get request）发起请求，并将请求的结果返回给变量${response}
