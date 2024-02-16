
class Tortugas:

    def __init__ (self):
        tortugas=[]
        for i in turtles:
            name = i["name"]
            name = Turtle()
            name.color(i["name"])
            name.shape("turtle")
            name.shapesize(2)
            name.penup()
            name.goto(i["pos"])
            tortugas.append(name)
        return tortugas

    def move(self, lista):
        for i in range(0,6):
            lista[i].forward(r(1,10))
