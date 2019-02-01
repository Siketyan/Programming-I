import wiringpi
import time

class Player:
    FREQUENCIES = {
        "R": 0,
        "A3": 220,
        "A#3": 233,
        "B3": 247,
        "C4": 262,
        "D4": 294,
        "E4": 330,
        "F4": 349,
        "G4": 392,
        "A4": 440,
        "B4": 494,
        "C5": 523,
        "D5": 587,
        "E5": 659,
        "F5": 698,
        "G5": 784,
        "A5": 880
    }

    BPM = 120

    LENGTHS = {
        2: 60 / BPM * 2,
        2.5: 60 / BPM * 3,
        4: 60 / BPM,
        4.5: 60 / BPM + 60 / BPM / 2,
        8: 60 / BPM / 2,
        8.5: 60 / BPM / 2 + 60 / BPM / 4,
        16: 60 / BPM / 4,
        32: 60 / BPM / 8
    }

    SOUNDER = 27
    SW1 = 5

    def __init__(self):
        wiringpi.wiringPiSetupGpio()
        wiringpi.softToneCreate(self.SOUNDER)
        wiringpi.pinMode(self.SW1, 0)

    def load(self, path):
        self.notes = []
        score = open(path, "r")
        for line in score.readlines():
            if (line == "") continue
            data = line.split()
            self.notes.append([
                data[0],
                float(data[1])
            ])

    def play(self):
        for note in self.notes:
            wiringpi.softToneWrite(self.SOUNDER, self.FREQUENCIES[note[0]])
            time.sleep(self.LENGTHS[note[1]])
            if wiringpi.digitalRead(self.SW1) == 0:
                return

    def wait(self):
        while wiringpi.digitalRead(self.SW1) == 1:
            pass

    def main(self):
        self.load("toyota.txt")
        self.wait()
        self.play()

if __name__ == "__main__":
    Player().main()

