'''class Enemy:
    life = 3

    def attack(self): #self is automatic included
        print( 'ouch!')
        self.life -=1 #self. access variable in the class

    def checklife(self):
        if self.life <= 0:
            print('I am dead')
        else:
            print(str(self.life), 'life left')

# enemy1 is the object
# enemy2 is another object
enemy1 = Enemy() #enemy1 and enemy2 are independent of each other
enemy2 = Enemy() #Both enemy1 and enemy2 can get to use the same function without creating a new function

enemy1.attack()
enemy1.checklife()
enemy2.attack()
enemy2.checklife()

#Finding range can only be done in str, tuple and list

a = 'Hello'
print(a[0]) #H

b = (1,2,3)
print(b[0]) #1

c = [1,2,3]
print(c[0]) #1

#Printing every single character in a str, tuple and list
for i in 'String':
    print(i) # S\nt\nr\ni\nn\ng

for i in (1,2,3):
    print(i) #1\n2\n3

for i in [1,2,3]:
    print(i) #1\n2\n3

#Range is only used on int
for i in range(10):  # 0 to 10 (exclusive) automatic start at 0
    print(i) # 0 to 9  '''





