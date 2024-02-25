import ast
import subprocess


# 遍历抽象语法树中分支节点类
class Branch(ast.NodeTransformer):

    def __init__(self):
        self.branch_num = 0        # 分支总数
        self.branch_dict = []      # 分支字典

    '''
    分支节点遍历, AST中,elif 作为 If 中的 orelse 部分之内的一个额外 If 节点出现
    具体文档: https://docs.python.org/zh-cn/3/library/ast.html#control-flow
    '''
    def visit_If(self, node):
        self.branch_dict.append({
            "branch_num" : self.branch_num,
            "start_line" : node.body[0].lineno,
            "end_line" : node.body[-1].lineno,
            "all_line" : len(node.body),
            "flag" : False
            })
        if hasattr(node, 'orelse'):
            if type(node.orelse[0]) == ast.If:
                self.visit_If(node.orelse[0])
            else:
                self.branch_dict.append({
                "branch_num" : self.branch_num,
                "start_line" : node.orelse[0].lineno,
                "end_line" : node.orelse[-1].lineno,
                "all_line" : len(node.orelse),
                "flag" : False
                })
                self.branch_num += 1
        return node



    # 语句覆盖率
    def branch_coverage(self, new_code):
        print('Branch_Coverage')
        code_1 = "branch_dict = {}\n".format(self.branch_dict)
        code_2 = "branch_num = {}\n".format(self.branch_num)
        code_3 = "executed_list = []\n"
        code_4 = '''
for index in branch_dict:
    for value in executed_list:
        if value >= index['start_line'] and value <= index['end_line']:
            index['flag'] = True
for index in branch_dict:
    print(index)
for value in range(branch_num):
    branch_all_line = 0
    executed_line = 0
    for index in branch_dict:
        if index['branch_num'] == value:
            branch_all_line += index['all_line']
        if index['flag'] == True:
            executed_line = index['all_line']
    print(f'branch:{value} coverage:{(executed_line / branch_all_line)* 100:.2f} %')
        '''

        # 生成，执行插桩后代码
        new_code = code_1 + code_2 + code_3 + new_code + code_4

        file_name = "new_test.py"

        with open(file_name, "w") as file:
            file.write(new_code)
        print('code_executed_result:')
        subprocess.run(['python', file_name], check=True)


