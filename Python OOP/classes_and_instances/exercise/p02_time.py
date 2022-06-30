class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):
        hours = self.hours
        minutes = self.minutes
        seconds = self.seconds
        seconds += 1
        if seconds > Time.max_seconds:
            seconds %= 60
            minutes += 1
        if minutes > Time.max_minutes:
            minutes %= 60
            hours += 1
        if hours > Time.max_hours:
            hours %= 24
        self.set_time(hours, minutes, seconds)
        return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())

time2 = Time(10, 59, 59)
print(time2.next_second())

time3 = Time(23, 59, 59)
print(time3.next_second())

