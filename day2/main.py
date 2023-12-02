import re

f = open('day2/input.txt', "r")

lines = f.readlines()


    
class Game: 
    def __init__(self, line, red, green, blue):
        self.line = line
        self.id = self.gameId()
        self.roundsLines = []
        self.rounds = []
        self.getGames()
        
        self.red = red
        self.green = green
        self.blue = blue
        
        self.fewestRed = 0
        self.fewestGreen = 0
        self.fewestBlue = 0
        
        self.getFewestBallsNeeded()
        self.power = self.fewestRed * self.fewestGreen * self.fewestBlue
        
        self.isPossible = self.gameIsPossible()
        
        
    def gameId(self):
        match = re.search(r"(?<=Game )(.*)(?=:)", self.line).group(0)
        self.id = match
        return match
    
    def  getGames(self):
        roundsLines = re.search(r"(?<=:)(.*?)(?=$)", self.line).group(0)
        roundsLines = roundsLines.split("; ")
        for roundLine in roundsLines:
            self.roundsLines.append(roundLine)
            
        for roundLine in self.roundsLines:
            self.rounds.append(Round(roundLine))
            
    def gameIsPossible(self):
        for round in self.rounds:
            if round.red > self.red or round.blue > self.blue or round.green > self.green:
                return False

        return True
    
    def printGameInfo(self):
        print("id", self.id)
        print("rounds", len(self.roundsLines))
        for round in self.rounds:
            print(round.red)
            print(round.blue)
            print(round.green)
            print("-----")
        print(self.isPossible)

        print("==================")
    
    def getFewestBallsNeeded(self):
        for round in self.rounds:
            if round.red > self.fewestRed:
                self.fewestRed = round.red
            if round.blue > self.fewestBlue:
                self.fewestBlue = round.blue 
            if round.green > self.fewestGreen:
                self.fewestGreen = round.green
                
class Round:
    def __init__(self, roundLine):
        self.roundLine = roundLine
        self.red = 0
        self.blue = 0
        self.green = 0
        self.getRed()
        self.getBlue()
        self.getGreen()
        
        
    def getRed(self):
        try:
            self.red = int(re.search(r"([0-9]*?)(?= red)", self.roundLine).group(0))
        except:
            self.red = 0
            
        return self.red

    def getBlue(self):
        try:
            self.blue = int(re.search(r"([0-9]*?)(?= blue)", self.roundLine).group(0))
        except:
            self.blue = 0
        return self.blue
    
    def getGreen(self):
        try:
            self.green = int(re.search(r"([0-9]*?)(?= green)", self.roundLine).group(0))
        except:
            self.green = 0
        return self.green
    
    
    
total = 0
for line in lines:
    game = Game(line, 12,13,14)
    if game.isPossible:
        total += int(game.id)
        game.printGameInfo()

print(total) # -> 2505 star 1

power = 0
for line in lines:
    game = Game(line, 12,13,14)
    game.printGameInfo()
    power += game.power
        
print(power)