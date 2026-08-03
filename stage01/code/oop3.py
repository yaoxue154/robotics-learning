class Robot:
    def __init__(self,name):
        self.name=name
    def introduce(self):
        print(f"我是{self.name}机器人")
xizhi=Robot("西智")
xizhi.introduce()