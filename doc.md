#设计文档

##项目需求
创建一个在线markdown编译环境，提供基于网页的markdown编写预览服务。

##主要功能

* 提供线上的markdown书写环境，并且提供预览功能。
* 提供简单的markdown格式辅助书写功能。
* 提供线上编译的markdown文件生成下载服务。

##功能流程

1. 在网页指定的文本编译区域书写markdown文件。
2. 借助markdown辅助工具完成markdown文件的编写。
3. 根据文本域中内容转换为markdown浏览模式，并提供给用户预览。
4. 提供用户`title.md`文件下载

##技术支持

* 开发语言：[python](http://www.python.org)
* 网页架构：[python flask](http://flask.pocoo.org/)
* css美工：[bootstrap](http://twitter.github.io/bootstrap/)
