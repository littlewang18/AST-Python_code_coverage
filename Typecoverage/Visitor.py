import ast


# 遍历抽象语法树中函数节点类
class Visitor(ast.NodeVisitor):

    def __init__(self):
        self.func_dict = {}        # 函数字典

    # 结点递归遍历
    def visit(self, node):
        if type(node) is ast.FunctionDef:
            self.visit_FunctionDef(node)
        if type(node) is ast.Call:                     # 判断AST节点中函数调用
            if hasattr(node.func, 'id'):
                if node.func.id in self.func_dict:
                    self.func_dict[node.func.id]['call_num'] += 1
        self.generic_visit(node)

    # 函数节点遍历
    def visit_FunctionDef(self, node: ast.FunctionDef):
        if node.decorator_list:                        # 装饰器判断
            func_start = node.decorator_list[0].lineno
        else:
            func_start = node.lineno
        self.func_dict[node.name] = {                  # 函数字典导入数据
            'start_line' : func_start,
            'end_line' : node.end_lineno,
            'call_num' : 0 }
        self.generic_visit(node)

    # 函数覆盖率
    def func_coverage(self):
        print('Func_Coverage')
        func_call = 0                   # 函数调用数
        func_num = len(self.func_dict)  # 函数总数
        for index in self.func_dict:
            value = self.func_dict[index]
            print(f'func_name:{index:s}: {value}')
            if value['call_num'] >= 1:
                func_call += 1
        print(f'func_coverage :{(func_call / func_num) * 100:.2f} %')   # 函数覆盖率，函数调用数 / 函数总数

