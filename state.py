from __future__ import annotations
import random
from abc import ABC, abstractmethod


class Game:
    def __init__(self):
        self.state = WelcomeScreenState(self)

    def change_state(self, state):
        self.state = state


class State(ABC):
    def __init__(self, game):
        self.game = game
        print(f"Currently in {self} state")

    @abstractmethod
    def on_welcome_screen(self):
        pass

    @abstractmethod
    def on_playing(self):
        pass

    @abstractmethod
    def on_break(self):
        pass

    @abstractmethod
    def on_end_game(self):
        pass


class WelcomeScreenState(State):
    def on_welcome_screen(self):
        print("Currently on welcome screen")

    def on_playing(self):
        self.game.change_state(PlayingState(self.game))

    def on_break(self):
        print("From welcome to break not allowed")

    def on_end_game(self):
        print("From welcome to end game not allowed")


class PlayingState(State):
    def on_welcome_screen(self):
        print("From playing to welcome not allowed")

    def on_playing(self):
        print("Currently playing")

    def on_break(self):
        self.game.change_state(BreakState(self.game))

    def on_end_game(self):
        self.game.change_state(EndGameState(self.game))


class BreakState(State):
    def on_welcome_screen(self):
        print("From break to welcome not allowed")

    def on_playing(self):
        self.game.change_state(PlayingState(self.game))

    def on_break(self):
        print("Currently on break")

    def on_end_game(self):
        print("From break to end game not allowed")


class EndGameState(State):
    def on_welcome_screen(self):
        self.game.change_state(WelcomeScreenState(self.game))

    def on_playing(self):
        print("From end game to playing not allowed")

    def on_break(self):
        print("From end game to break now allowed")

    def on_end_game(self):
        print("Currently on end game")


if __name__ == '__main__':
    game = Game()

    for i in range(20):
        state = random.randrange(4)
        if state == 0:
            print("Move to welcome")
            game.state.on_welcome_screen()
        elif state == 1:
            print("Move to playing")
            game.state.on_playing()
        elif state == 2:
            print("Move to break")
            game.state.on_break()
        else:
            print("Move to end game")
            game.state.on_end_game()
