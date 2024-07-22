class Clock:
    def __init__(self,hour,minutes):
        self.hour=hour
        self.minutes=minutes

    def time(self):

        print(f"Time is {self.hour}:{ self.minutes }")
    def add_minute(self,add_minute):
        total_minutes=self.hour*60+self.minutes+add_minute
        self.hour=(total_minutes//60)%24
        self.minutes=total_minutes%60
        print(f"Time with add {add_minute} minute extra:{self.hour}:{self.minutes}" )

obj=Clock(12,10)
obj.time()
obj.add_minute(60)