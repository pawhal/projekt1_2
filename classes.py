class Exercise:
    exerciseCount = 0

    def __init__(self, number, query):
        self.number = 1
        self.query = "text"
        Exercise.exerciseCount += 1

    def show(self):
        print (self.number,self.query)
