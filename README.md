# 基于AST的python代码覆盖率测试DEMO

### 基础技术原理

> 抽象语法树 (Abstract Syntax Tree, AST)

python源代码到字节码的生成过程中如下：

源代码解析 --> 语法树 --> 抽象语法树 --> 控制流程图 --> 字节码

因此在抽象语法树中包括了源代码的一系列结点，通过对结点的分析来进行代码覆盖率的计算

具体文档可见：https://docs.python.org/zh-cn/3/library/ast.html

> 插桩 (instrumentation)

在对抽象语法树分析过程中，通过在保证源代码逻辑完整的基础上，进行插入探针代码，再进行运行代码，完成对代码运行中的信息的采集。通过插桩代码得到的数据，进行计算可以获得程序的控制运行。



### 程序框架

```
|
| ———— TestFunc
|        | ---- test.py 测试函数，用于进行代码覆盖率测试的函数
| ---- Typecoverage
|        | ---- Branch.py  分支覆盖率测试，主要用于if-else结点的测试
|        | ---- Instrument.py 插桩函数，对语句进行插桩，以及语句覆盖率测试
|        | ---- Visitor.py  函数覆盖率测试，遍历AST，进行函数覆盖率测试
| ---- coverage.py   覆盖率测试主函数
| ---- export.py     抽象语法树导出函数
| ---- fileimport.py 测试文件导入函数
| ---- main.py       程序入口，进行相关的调控
```



### Get Started

1. 安装graphviz

	程序抽象语法树中的图片导出需要graphviz， 请安装graphviz，并修改export.py中的路径

2. 修改test.py

	将 test.py，修改为自己需要测试的函数

3. 运行main.py

	选择自己需要的测试代码覆盖率指标种类



### 后续开发方向

本程序只是AST python测试方向的一个demo，后续开发中~

- [ ] 测试文件导出
- [ ] 剩余AST结点的测试开发
- [ ] 大型项目测试



### License

MIT License