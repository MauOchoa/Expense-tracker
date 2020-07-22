class Robot:
    def __init__(self, name, weight, color):
        self.name = name        #Attibutes
        self.weight = weight
        self.color = color

    def introduceMyself(self): #Method
        intro ="hello my name is " + self.name
        return intro 

r1 = Robot("Mauricio", 60, "brown")

#print(r1.introduceMyself())

r1.name = "pollo"
#print(r1.introduceMyself())

class Person:
    def __init__(self,name,personality,age,robotowned):
        self.robotowned = robotowned.name
        self.name= name
        self.personality = personality
        self.age = age
    def resumen(self):
        attributes = [self.name,self.personality,self.age]
        if (attributes[2] < 18):
            print("cant use a robot")
        else:
            print(self.name + " your robot is " + self.robotowned)
p1 = Person("Mauricio","normal",24,r1)
#p1.resumen()

class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node
        
#LINKED LIST
    
nodeE = Node(6,None)
nodeD = Node(3,nodeE)
nodeC = Node(4,nodeD)
nodeB = Node(5,nodeC)
head = Node(2,nodeB)
suma  = 0
def countNodes(head,suma):
    if(head.next_node != None): 
        head = head.next_node
        suma +=1
        countNodes(head,suma)
    else:
        pass
        #print(suma)
countNodes(head,suma)
lista = ["hello","hawai","victoria"]
#print(sorted(lista,reverse = False))

lista1 = [1,2,3,4,5]
lista0 = [1,2,5,3,4]

for i in range(len(lista0)):
    if lista0[i]==lista1[i]:
        print(lista0[i],lista1[i])
    else:
        print("here")       

s = [1,2,3]
s2 = [1,2,3]

if(s == s2):
    print("equal")
else:
    print("nope")
        



