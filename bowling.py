from bowling_error import BowlingError
from frame import Frame


class BowlingGame:

    def __init__(self):
        self._frames = []
    
    def add_frame(self, frame: Frame) -> None:
        if len(self._frames) == 10: raise BowlingError
        self._frames.append(frame)

    def get_frame_at(self, i: int) -> Frame:
        if i>=len(self._frames):
            raise BowlingError
        return self._frames[i]

    def calculate_score(self) -> int:
        total_score = 0
        is_spare = False
        for frame in self._frames:
            if is_spare:
                total_score += frame.get_first_throw()
                is_spare = False
            if frame.is_spare():
                is_spare = True
            total_score += frame.score()
        return total_score

    def set_first_bonus_throw(self, bonus_throw: int) -> None:
        pass

    def set_second_bonus_throw(self, bonus_throw: int) -> None:
        pass
