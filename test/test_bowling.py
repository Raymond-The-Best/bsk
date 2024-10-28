import unittest

from bowling import BowlingGame
from bowling_error import BowlingError
from frame import Frame


class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame()

    def test_game_created(self):
        f = Frame(1,5)
        self.game.add_frame(f)
        self.assertEquals(self.game.get_frame_at(0), f)


    def test_get_missing_frame_raises_BowlingError(self):
        self.assertRaises(BowlingError, self.game.get_frame_at, 0)

    def test_game_created_10_frames(self):
        self.game.add_frame(Frame(1,5))
        self.game.add_frame(Frame(3,6))
        self.game.add_frame(Frame(7,2))
        self.game.add_frame(Frame(3,6))
        self.game.add_frame(Frame(4, 4))
        self.game.add_frame(Frame(5,3))
        self.game.add_frame(Frame(3,3))
        self.game.add_frame(Frame(4,5))
        self.game.add_frame(Frame(8,1))
        f = Frame(2,6)
        self.game.add_frame(f)
        self.assertEquals(self.game.get_frame_at(9), f)

    def test_game_created_11_frames(self):
     self.game.add_frame(Frame(1, 5))
     self.game.add_frame(Frame(3, 6))
     self.game.add_frame(Frame(7, 2))
     self.game.add_frame(Frame(3, 6))
     self.game.add_frame(Frame(4, 4))
     self.game.add_frame(Frame(5, 3))
     self.game.add_frame(Frame(3, 3))
     self.game.add_frame(Frame(4, 5))
     self.game.add_frame(Frame(8, 1))
     self.game.add_frame(Frame(2, 6))

     self.assertRaises(BowlingError, self.game.add_frame, Frame(1, 1))