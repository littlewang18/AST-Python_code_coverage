from coverage import run


'''测试函数路径'''
file_path = 'D:\All\projects\Python\Coverage\Python-code-coverage\TestFunc\\test.py'


'''代码覆盖率指标种类'''
index_type = ['func','assign','branch']
# 'func'   函数覆盖率
# 'assign' 语句覆盖率
# 'branch' 分支覆盖率


'''数据保存'''
export_flag = {
    'export_png': True,
    'export_path' : 'D:\All\projects\Python\Coverage\Python-code-coverage\\ast_tree'
}

# 主函数
run(file_path, index_type, export_flag)