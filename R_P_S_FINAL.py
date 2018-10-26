import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:  # parent class playes one move

    def __init__(self):
        pass

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class Human_Player(Player):
    def __init__(self):
        pass

    def move(self):
        while True:
            Human_move = input("""Play "rock" or "paper" or "scissors":""")

            if Human_move.lower() not in moves:
                #  add .lower()method in case someone wrote in capital letters
                #  validate the user input
                print("please Enter a valid input")
            else:
                return Human_move.lower()

    def learn(self, my_move, their_move):
        pass


class Random_Player(Player):
    def __init__(self):
        pass

    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        pass


class Reflect_Player(Player):
    # Palyes a random move in round 1 then it saves opponent's previous move
    # and playe that move in the next round
    def __init__(self):
        self.opponent_last_move = ''

    def move(self):
        if self.opponent_last_move == '':
            return random.choice(moves)
        else:
            return self.opponent_last_move

    def learn(self, their_move):
        if their_move in moves:
            self.opponent_last_move = their_move


class Cycle_Player(Player):
    #  plays the value that follows the prevouse one in the list of moves
    #  by remembring the index and reseting it when it reach 2
    def __init__(self):
        self.my_last_move = ''

    def move(self):
        if self.my_last_move == '':
            return random.choice(moves)
        else:
            return self.my_last_move

    def learn(self, my_move):
        if my_move in moves:
            my_move_index = moves.index(my_move)
            if my_move_index == 2:
                self.my_last_move = moves[0]
            else:
                self.my_last_move = moves[my_move_index + 1]


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.Player2_score = 0
        self.Player1_score = 0

    def beats(self, one, two):
        # states the scores and winnign or losing status of the players
        if ((one == 'rock' and two == 'scissors')
            or(one == 'scissors' and two == 'paper')
                or(one == 'paper' and two == 'rock')):

                print("Player1 is the winner")
                self.Player1_score += 1
                print(f"Player1 score is {self.Player1_score}\nPlayer2 "
                      f"score is {self.Player2_score}\n \n")
        elif one == two:
            print(f"it is a tie!\nPlayer1 score is "
                  f"{self.Player1_score} \nPlayer2 score is "
                  f"{self.Player2_score}\n \n")
            self.Player1_score = self.Player1_score
            self.Player2_score = self.Player2_score
        else:
            self.Player2_score += 1
            print(
                f"Player2 is the winner \nPlayer1 score is "
                f"{self.Player1_score} \nPlayer2 score is "
                f"{self.Player2_score}\n \n ")

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        # I had a diffrent idea of how to exploit the learn function.

        print(f"Player 1: {move1}  Player 2: {move2}")

        #  by using isinstance() the program will  check the type of
        #  the object then assign the correct learn method to that object
        if isinstance(self.p1, Reflect_Player):
            # for example : if Player1 is an instance from the
            # Reflect_player class then it will use the corresponding
            # learn function and the appropiate move
            self.p1.learn(move2)
        elif isinstance(self.p1, Cycle_Player):
            # same her is will use the learn method from the class of
            #  the object after it is aninstance from that class
            self.p1.learn(move1)

        # This is the learn functions for Player 2
        if isinstance(self.p2, Reflect_Player):
            self.p2.learn(move1)
        elif isinstance(self.p2, Cycle_Player):
            self.p2.learn(move2)

        self.beats(move1, move2)

    def play_game(self):
        print("welcome!")
        while True:
            number_of_rounds = input("How many rounds would you like to play?")
            if not number_of_rounds.isdigit():
                print("Please enter a number")
                continue
            else:
                break
        print("\n \nGame start!\n \n")
        RN = int(number_of_rounds)
        #  let the rounds start from 1 and end at the number of rounds assinged
        # by the user(+1 becuase it starts at 0)
        for rounds in range(1, RN+1):
            print(f"Round {rounds}:")
            self.play_round()
        print(
            f"Game over! \n \nPlayer1 total score is "
            f"{self.Player1_score} \nPlayer2 total score is "
            f"{self.Player2_score} \n\n")
        # evaluate the winner
        if self.Player1_score > self.Player2_score:
            print("Player1 is the winner")
        elif self.Player1_score < self.Player2_score:
            print("Player2 is the winner")
        else:
            print("it is a tie!")


if __name__ == '__main__':
    player1 = 0
    player2 = 0
    while True:  # let the user choose the palyers modes
                # validate their choice
        print(
            "please choose by entering the corresponding"
            "number:\n 1: Human Player\n 2: The Repeater\n "
            "3: The Rflecter\n 4: The CyclePlayer\n 5: The Random Player")
        Player1 = input('player1 choose: ')
        Player2 = input('player2 choose: ')
        if not Player1.isdigit() or not Player2.isdigit():
            print("Please enter a valid choice")
        else:
            Player1 = int(Player1)
            Player2 = int(Player2)
            if Player1 == 1:
                p1 = Human_Player()
                Player1 = p1
            elif Player1 == 2:
                p1 = Player()
                Player1 = p1
            elif Player1 == 3:
                p1 = Reflect_Player()
                Player1 = p1
            elif Player1 == 4:
                p1 = Cycle_Player()
                Player1 = p1
            elif Player1 == 5:
                p1 = Random_Player()
                Player1 = p1
            elif Player1 not in range(5):
                print("Please enter a valid choice")
                continue

            if Player2 == 1:
                p2 = Human_Player()
                Player2 = p2
            elif Player2 == 2:
                p2 = Player()
                Player2 = p2
            elif Player2 == 3:
                p2 = Reflect_Player()
                Player2 = p2
            elif Player2 == 4:
                p2 = Cycle_Player()
                Player2 = p2
            elif Player2 == 5:
                p2 = Random_Player()
                Player2 = p2
            elif Player1 not in range(5):
                print("Please enter a valid choice")
                continue

            break

    game = Game(Player1, Player2)
    game.play_game()
