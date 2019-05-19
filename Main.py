import match
import visual

def aparear(n):
    P = match.create_random_points(n)
    R = heuristica(P)
    visual.Window(P,R)
    return 200 * len(R) / n

def heuristica(P):
    # TODO
    Rectangulos = []
    k=0
    Aparear = []
    Visitados=[]
    for i in range(k,len(P)-1):
        if len(Aparear)>0:
            for j in range(0,len(Aparear)):
                if P[i]==Aparear[j]:
                    i=i+1
        for k in range (i+1,i+3):
            if k>=len(P):
                break
            if P[i].color==P[k].color:
                Aparear.append(P[i])
                Aparear.append(P[k])
                Visitados.append(P[i])
                Visitados.append(P[k])
                p=P[i]
                q=P[k]
                Rectangulos.append(match.Rectangle(min(p.x,q.x), max(p.x,q.x), min(p.y,q.y), max(p.y,q.y)))
                i=k
                break
        i=i+1
    print(Aparear)
    return Rectangulos
