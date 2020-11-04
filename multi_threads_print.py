class MultiThreadsPrint:
    """
    说明：
        MultiThreadsPrint 模块是为了解决
        多线程同时调用print函数时出现输出冲突，覆盖等异常情况的而开发的简易替代品

    如何使用：
        导入 MultiThreadsPrint 模块，或将代码复制到你的脚本中
        将这句话粘贴在你程序的主线程的主函数中，或者是你将要调用 mt_print 函数的代码之前
        'mt_print = MultiThreadsPrint().mt_print'
        然后你就可以在自己的多线程应用中用 mt_print() 替换 print() 了，赶紧试一试吧

    示例：
        （主线程中）
        if __name__ == '__main__':
            mt_print = MultiThreadsPrint().mt_print
            num = int(input("请输入数字"))
            ......
            ......
            ......
    """

    def __init__(self):

        from threading import Thread as Td
        from threading import Lock as Lk
        from threading import active_count as ac

        self.output_td = Td(target=self.output)
        self.lock = Lk()
        self.ac = ac

        self.start_ac = ac()+1
        self.list = []
        self.running = False

    def start(self):
        with self.lock:
            if not self.running:
                self.output_td.start()
                self.running = True
            return

    def mt_print(self, *args, end="\n"):
        with self.lock:
            self.list.append((args, end))

        self.start()

    def output(self):
        while self.ac() > self.start_ac:
            if len(self.list):
                content = self.list.pop(0)
                print(*content[0], end=content[1])
