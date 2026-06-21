class Human:
    def __init__(self,name,torso,left_leg,right_leg):
        self.name = name
        self.torso = torso
        self.left_leg = left_leg
        self.right_leg = right_leg
        

class Head:
    def __init__(self):
        pass

class Torso:
    def __init__(self,head,right_arm,left_arm):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm

class Hand:
    def __init__(self):
        pass

class Arm:
    def __init__(self,hand):
        self.hand = hand

class Feet:
    def __init__(self):
        pass

class Leg:
    def __init__(self,feet):
        self.feet = feet

head = Head()

right_hand = Hand()
left_hand = Hand()

right_arm = Arm(right_hand)
left_arm = Arm(left_hand)

left_feet = Feet()
right_feet = Feet()

left_leg = Leg(left_feet)
right_leg = Leg(right_feet)

torso = Torso(head,right_arm,left_arm)

Manfred = Human("Manfred", torso, left_leg, right_leg)