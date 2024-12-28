import threading
import time

class Knight(threading.Thread):
    enemies = 100
    total_days = 10
    lock = threading.Lock()

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        days = 0
        print(f"{self.name}, на нас напали!")

        while days < Knight.total_days:
            days += 1
            time.sleep(1)

            with Knight.lock:
                daily_damage = Knight.enemies / (Knight.total_days - days + 1)
                daily_damage = min(self.power, daily_damage)
                Knight.enemies -= daily_damage
                Knight.enemies = max(Knight.enemies, 0)

                print(f"{self.name} сражается {days} день(дня)..., осталось {Knight.enemies:.0f} воинов.")

        print(f"{self.name} завершил бой спустя {days} дней(дня)!")

knight1 = Knight("Sir Lancelot", 10)
knight2 = Knight("Sir Galahad", 20)

knight1.start()
knight2.start()

knight1.join()
knight2.join()

print("Все битвы закончились!")
