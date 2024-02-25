import ast
import subprocess


# 插桩抽象语法树中语句节点类
class Instrument(ast.NodeTransformer):

    def __init__(self):
        self.assign_list = []      # 语句列表


    # return节点插桩
    def visit_Return(self, node):
        mark_code = "executed_list.append({})".format(node.lineno)
        mark_node = ast.parse(mark_code)
        self.assign_list.append(node.lineno)
        return mark_node, node


    # 语句节点插桩
    def visit_Assign(self, node):
        mark_code = "executed_list.append({})".format(node.lineno)
        mark_node = ast.parse(mark_code)
        self.assign_list.append(node.lineno)
        return mark_node, node


    # 语句覆盖率
    def assign_coverage(self, new_code):
        print('Assign_Coverage')

        # 添加语句覆盖率计算代码
        code_1 = "executed_list = []\n"
        code_2 = "assign_num = {}\n".format(len(self.assign_list))
        code_3 = '''
executed_num = len(executed_list)
print('Executed_Assign', executed_list)
print(f'assign_coverage :{(executed_num / assign_num) * 100:.2f} %')
        '''
        # 生成，执行插桩后代码
        new_code = code_1 + code_2 + new_code + code_3

        file_name = "new_test.py"

        with open(file_name, "w") as file:
            file.write(new_code)
        print('code_executed_result:')
        subprocess.run(['python', file_name], check=True)


