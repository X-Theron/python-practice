#if __name__ == "__main__": 的作用说明：
    1. 当这个 .py 文件被“直接运行”时，Python 会把 __name__ 设置为 "__main__"，
    所以条件成立，下面的 main() 会被执行。 
    2. 当这个文件被其他程序用 import 导入时，__name__ 是模块名（不是 "__main__"），
    而是该文件名，条件不成立，下面的 main() 不会自动执行。
    3. 这样写的好处：文件既能作为脚本直接运行，也能作为模块被其他代码复用，
    导入时不会自动执行测试/主程序代码。
    简单记： 
       直接运行 -> 执行 main() 
       被 import -> 不自动执行 main()
#把重复出现的"写死数字"提成常量
    好处：规则只改一处，全游戏跟着变，不会遗漏。
#命名规则
    1. 常量（ConSTANT）→ 全大写 + 下划线
    运行时永远不变的值。
    例：MAX_NUM、MAX_TRIES、PI = 3.14159。
    大写提醒人"这是写死的设定，别动它"。
    2. 变量（variable）→ 全部小写 + 下划线
    运行时会被赋新值的。
    例：num、times、guess_number、win_times。
    多个词用下划线连接，不驼峰（winTimes ❌，win_times ✅）。
    3. 函数（function）→ 小写 + 下划线（和变量同一套规则）
    例：game()、def is_even(n)。
    和变量同风格，作用不同但不冲突。
    4. 类（class）→ 首字母大写驼峰（CapWords）
    例：class Random、class GuessingGame。
    这是唯一用驼峰命名的类型。（你现在还没写类，先了解即可）
    5. 模块/文件名 → 全小写
    例：random、p02_guess_number.py。
    6. 私有（约定用单下划线开头）→ 团队/模块内部"别动"信号
    例：_internal。属于高级约定，暂可不记。