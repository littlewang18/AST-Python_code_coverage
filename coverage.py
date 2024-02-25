import ast
import astor

import export
import fileimport
import Typecoverage.Branch as Branch
import Typecoverage.Visitor as Visitor
import Typecoverage.Instrument as Instrument


# 主函数
def run(file_path, index_type, export_flag):

    # 测试代码导入， AST抽象语法树生成
    code = fileimport.analyze_file(file_path)
    tree = ast.parse(code)

    # 语法树图片输出
    if export_flag['export_png']:
        export.export_png(tree, export_flag['export_path'])

    # 函数覆盖率
    if 'func' in index_type:
        visitor = Visitor.Visitor()             # 遍历抽象语法树类
        visitor.visit(tree)                     # 遍历抽象语法树
        visitor.func_coverage()                 # 函数覆盖率
    # 语句和分支覆盖率
    if 'assign' in index_type or 'branch' in index_type:
        branch = Branch.Branch()                # 遍历抽象语法树中分支节点类
        branch.visit(tree)
        mark = Instrument.Instrument()          # 插桩抽象语法树中语句节点类
        marked_tree = mark.visit(tree)
        new_code = astor.to_source(marked_tree) # 生成插桩后代码
        if 'assign' in index_type:
            mark.assign_coverage(new_code)      # 语句覆盖率
        if 'branch' in index_type:
            branch.branch_coverage(new_code)    # 分支覆盖率

