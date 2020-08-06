class Pid():
    def __init__(self, kp:int, kd:int, ki:int, sp:int):
        self.kp = kp
        self.kd = kd
        self.ki = ki
        self.sp = sp
        self.last_error = 0

    def accumulate(self, value:int) -> int:
        error = sp - value
        p = self.kp * error
        d1 = self.kd * 10
        d2 = error - self.last_error
        d = d1 * d2
        i1 = ki / 10
        i2 = error + self.last_error
        self.pid = p + i + d

if __name__ == '__main__':
    pid = Pid(kp=25, kd=8, ki=10, sp=15)
    pid.accumulate(17)
    print(pid.pid)