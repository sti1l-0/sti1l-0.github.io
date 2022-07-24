## python生成索引文件
用os读一下当前目录下的md文件，然后通过格式化字符串生成md格式的链接，最后拼接到index.md文件的末尾即可

## Github action更新索引文件
每次项目有提交的时候触发github action，准备python环境并运行脚本文件生成index.md。

然后借助[ad-m/github-push-action](https://github.com/ad-m/github-push-action)项目将更新的index推到仓库里。按照README里给的示例简单调整一下代码就可以用。