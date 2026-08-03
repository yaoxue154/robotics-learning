class Motor:
    def __init__(self,motor_id):
        self.motor_id=motor_id
        self.speed=0
    def set_speed(self,speed):
        self.speed=speed
    def status(self):
        print(f"电机{self.motor_id}的转速是{self.speed}rpm")

m1=Motor(1)
m2=Motor(2)
m1.set_speed(3000)
m1.status()
m2.status()