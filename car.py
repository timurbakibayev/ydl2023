import math


class Car:
    def __init__(self, name: str, x: int = 0, speed: int = 10, y: int = 0) -> None:
        self.name: str = name
        self.rotation: int = 0  # 0 - 360, degrees
        self.speed: int = speed
        self.x: int = x
        self.y: int = y

    def forward(self) -> None:
        # convert to radians
        angle = self.rotation * 3.1415926 / 180
        self.x += int(self.speed * round(math.cos(angle)))
        self.y += int(self.speed * round(math.sin(angle)))

    def rotate(self, angle: int) -> None:
        self.rotation += angle
