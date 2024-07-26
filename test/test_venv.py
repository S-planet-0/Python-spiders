import sys

print("修复 Python recursionError: maximum recursion depth exceeded in comparison(递归限制)\n也可以调整至:2000")
sys.setrecursionlimit(1000)
print(sys.getrecursionlimit())

# 代码运行环境设置成功！
print("OK!")

