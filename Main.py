import visual
import match
import Mein


def main():
    P = match.create_random_points(30)
    R = Mein.heuristica(P)
    return visual.Window(rectangles=R, points=P)


if __name__ == '__main__':
    app = main()
    app.root.mainloop()
    app.paper.scale()
