import os


# 文件分析
def analyze_file(file_path):
    with open(file_path, 'r') as file:
        source_code = file.read()
    return source_code



# 项目分析
def analyze_project(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                analyze_file(file_path)

