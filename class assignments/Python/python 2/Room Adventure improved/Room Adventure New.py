################################################################################################################
#Name:Joshua Brack
#Date: 4/12/2019
#Description: Room adventure with some gui improvements. Click the items and grabbables to look/grab
#############################################################################################################


#Note to professor
#click the items in the gui to interact.




from Tkinter import *

# the blueprint for a room
class Room(object):
        # the constructor
        def __init__(self, name, image):
                # rooms have a name, an image exitst  exits (e.g., south), exit locations (e.g., to the south is room n),
                # items (e.g., table), item descriptions (for each item), and grabbables (things that can
                # be taken into inventory)
                self.name = name
                self.image = image
                self.exits = {}
                self.items = {}
                self.grabbables = []

        # getters and setters for the instance variables
        @property
        def name(self):
                return self._name

        @name.setter
        def name(self, value):
                self._name = value
                
        @property
        def image(self):
                return self._image
        
        @image.setter
        def image(self, value):
                self._image = value

        @property
        def exits(self):
                return self._exits

        @exits.setter
        def exits(self, value):
                self._exits = value

        @property
        def items(self):
                return self._items

        @items.setter
        def items(self, value):
                self._items = value

        @property
        def itemDescriptions(self):
                return self._itemDescriptions

        @itemDescriptions.setter
        def itemDescriptions(self, value):
                self._itemDescriptions = value

        @property
        def grabbables(self):
                return self._grabbables

        @grabbables.setter
        def grabbables(self, value):
                self._grabbables = value

        # adds an exit to the room
        # the exit is a string (e.g., north)
        # the room is an instance of a room
        def addExit(self, exit, room):
                # append the exit and room to the appropriate lists
                self._exits[exit] = room

        # adds an item to the room
        # the item is a string (e.g., table)
        # the desc is a string that describes the item (e.g., it is made of wood)
        def addItem(self, item, desc):
                # append the item and description to the appropriate lists
                self._items[item] = desc

        # adds a grabbable item to the room
        # the item is a string (e.g., key)
        def addGrabbable(self, item):
                # append the item to the list
                self._grabbables.append(item)

        # removes a grabbable item from the room
        # the item is a string (e.g., key)
        def delGrabbable(self, item):
                # remove the item from the list
                self._grabbables.remove(item)

        # returns a string description of the room
        def __str__(self):
                # first, the room name
                s = "You are in {}.\n".format(self.name)

                # next, the items in the room
                s += "You see: "
                for item in self.items:
                        s += item + " "
                s += "\n"

                # next, the exits from the room
                s += "Exits: "
                for exit in self.exits:
                        s += exit + " "

                return s
###########################################################
class Game(Frame):
        def __init__(self, parent):
                Frame.__init__(self, parent)

        def createRooms(self):
                # r1 through r4 are the four rooms in the mansion
                # currentRoom is the room the player is currently in (which can be one of r1 through r4)
                # since it needs to be changed in the main part of the program, it must be global
                global currentRoom

                # create the rooms and give them meaningful names
                r1 = Room("Room 1", "room1.gif")
                r2 = Room("Room 2", "room2.gif")
                r3 = Room("Room 3", "room3.gif")
                r4 = Room("Room 4", "room4.gif")

                # add exits to room 1
                r1.addExit("east", r2)  # -> to the east of room 1 is room 2
                r1.addExit("south", r3)
                # add grabbables to room 1
                r1.addGrabbable("key")
                # add items to room 1
                r1.addItem("chair", "It is made of wicker and no one is sitting on it.")
                r1.addItem("table", "It is made of oak.  A golden key rests on it.")

                # add exits to room 2
                r2.addExit("west", r1)
                r2.addExit("south", r4)
                # add items to room 2
                r2.addItem("rug", "It is nice and Indian.  It also needs to be vacuumed.")
                r2.addItem("fireplace", "It is full of ashes.")

                # add exits to room 3
                r3.addExit("north", r1)
                r3.addExit("east", r4)
                # add grabbables to room 3
                r3.addGrabbable("book")
                # add items to room 3
                r3.addItem("bookshelves", "They are empty.  Go figure.")
                r3.addItem("statue", "There is nothing special about it.")
                r3.addItem("desk", "The statue is resting on it.  So is a book.")

                # add exits to room 4
                r4.addExit("north", r2)
                r4.addExit("west", r3)
                r4.addExit("south", None)       # DEATH!
                # add grabbables to room 4
                r4.addGrabbable("6-pack")
                # add items to room 4
                r4.addItem("brew_rig", "Gourd is brewing some sort of oatmeal stout on the brew rig.  A 6-pack is resting beside it.")

                # set room 1 as the current room at the beginning of the game
                Game.currentRoom = r1

                #This is wher the player's grabbables are stored
                Game.inventory = []
                
        def setUpGui(self):
                self.pack(fill = BOTH, expand = 1)
                
                Game.player_input = Entry(self, bg = "white")
                Game.player_input.bind("<Return>", self.process)
                Game.player_input.pack(side = BOTTOM, fill = X)
                Game.player_input.focus()

                img = None
                Game.image = Label(self, width = WIDTH/2, image = img)
                Game.image.image = img
                Game.image.pack(side = LEFT, fill = Y)
                Game.image.pack_propagate(False)

                text_frame = Frame(self, width = WIDTH/2)
                Game.text = Text(text_frame, bg = "lightgrey", state = DISABLED)
                Game.text.pack(fill = Y, expand = 1)
                text_frame.pack(side = RIGHT, fill = Y)
                text_frame.pack_propagate(False)
                
                

        def setRoomImage(self):
                if (Game.currentRoom == None):
                        Game.img = PhotoImage(file = "skull.gif")
                else:
                        Game.img = PhotoImage(file = Game.currentRoom.image)

                Game.image.config(image = Game.img)
                Game.image.image = Game.img

        
        def setStatus(self, status):
                Game.text.config(state = NORMAL)
                Game.text.delete("1.0", END)

                if (Game.currentRoom == None):
                        Game.text.insert(END, "You are dead. Quit now")
                else:
                        Game.text.insert(END, str(Game.currentRoom) +\
                                "\nYou are carrying: "+str(Game.inventory) +\
                                "\n\n" +status)
                Game.text.config(state = DISABLED)
                

        def play(self):
                self.createRooms()
                self.setUpGui()
                self.setRoomImage()
                self.setStatus("")
                

        def process(self, event):
                action = Game.player_input.get()
                action = action.lower()

                
                response = "I don't understand. Try verb noun. Valid verbs"+\
                " are go look take"
                if (action == "bye" or action == "quit" or action == "exit"):
                        exit(0)
                if (Game.currentRoom == None):
                        Game.player_input.delete(0, END)
                        return
                words = action.split()
                if (len(words) == 2):
                        verb = words[0]
                        noun = words[1]
                        if (verb == "go"):
                                response = "Invalid exit"

                                if(noun in Game.currentRoom.exits):
                                        Game.currentRoom = Game.currentRoom.exits[noun]
                                        response = "Room changed"
                        elif (verb == "look"):
                                response = "I don't see that item"

                                if(noun in Game.currentRoom.items):
                                        response = Game.currentRoom.items[noun]

                        elif (verb == "take"):
                                response = "I don't see that item"

                                if(noun in Game.currentRoom.grabbables):
                                        Game.inventory.append(noun)
                                        Game.currentRoom.delGrabbable(noun)
                                        response = "Item grabbed"

                # Decide to place buttons or remove buttons
                if(not("key" in Game.currentRoom.grabbables)):
                        try:
                                key.place_forget()
                        except:
                                pass
                else:
                        key.place(x=20+R1XADJUST,y=20+R1YADJUST)
                        
                if(not("book" in Game.currentRoom.grabbables)):
                        try:
                                book.place_forget()
                        except:
                                pass
                else:
                        book.place(x=149,y=132)
                        
                if(not("6-pack" in Game.currentRoom.grabbables)):
                        try:
                                beer.place_forget()
                        except:
                                pass
                else:
                        beer.place(x=127 ,y=125)
                        
                if(not("table" in Game.currentRoom.items)):
                        try:
                                table.place_forget()
                        except:
                                pass
                else:
                        table.place(x=20+R1XADJUST, y=70+R1YADJUST)

                if(not("chair" in Game.currentRoom.items)):
                        try:
                                chair.place_forget()
                        except:
                                pass
                else:
                        chair.place(x=198+R1XADJUST, y=70+R1YADJUST)

                if(not("rug" in Game.currentRoom.items)):
                        try:
                                rug.place_forget()
                        except:
                                pass
                else:
                        rug.place(x =209, y = 0)
                if(not("fireplace" in Game.currentRoom.items)):
                        try:
                                fireplace.place_forget()
                        except:
                                pass
                else:
                        fireplace.place(x =0, y = 0)
                        
                if(not("bookshelves" in Game.currentRoom.items)):
                        try:
                                bookshelves.place_forget()
                        except:
                                pass
                else:
                        bookshelves.place(x = 0, y = 0)
                        
                if(not("desk" in Game.currentRoom.items)):
                        try:
                                desk.place_forget()
                        except:
                                pass
                else:
                        desk.place(x = 130, y = 200)

                if(not("statue" in Game.currentRoom.items)):
                        try:
                                statue.place_forget()
                        except:
                                pass
                else:
                        statue.place(x = 149, y = 0)
                        
                if(not("brew_rig" in Game.currentRoom.items)):
                        try:
                                brewrig.place_forget()
                        except:
                                pass
                else:
                        brewrig.place(x = 0, y = 0)
                ####end section of placing and removing buttons        
                self.setStatus(response)
                self.setRoomImage()
                Game.player_input.delete(0, END)

        #function for grabbables button
        def take(self,name):
                Game.inventory.append(name)
                Game.currentRoom.delGrabbable(name)
                self.setStatus("{} grabbed.".format(name))
                if(name == "key"):
                        key.destroy()
                elif(name == "book"):
                        book.destroy()
                elif(name== "6-pack"):
                        beer.destroy()

        #function for items button
        def look(self, name):
                self.setStatus(Game.currentRoom.items[name])

###################MAIN#####################################
WIDTH = 800
HEIGHT = 600
#help us adjust position of room1 stuff
R1XADJUST = 0
R1YADJUST = 0
window = Tk()
window.title("Room Adventure...Reloaded")



g = Game(window)
g.play()

#define all buttons
#room 1
photo=PhotoImage(file="key.gif")
key = Button(window,image=photo, command=lambda :g.take("key"), height=50, width=100)
key.image=photo
key.place(x=20+R1XADJUST, y=20+R1YADJUST)

photo = PhotoImage(file="table.gif")
table = Button(window, image= photo,command=lambda :g.look("table"),height = 168, width = 198)
table.image=photo
table.place(x=20+R1XADJUST, y=70+R1YADJUST)


photo = PhotoImage(file="chair.gif")
chair = Button(window, image= photo, command=lambda:g.look("chair"),height = 168, width = 100)
chair.image = photo
chair.place(x=198+R1XADJUST, y=70+R1YADJUST)

#room 2
photo = PhotoImage(file="rug.gif")
rug = Button(window, image=photo, command=lambda:g.look("rug"), height =118 , width = 190)
rug.image = photo

photo = PhotoImage(file="fireplace.gif")
fireplace = Button(window, image=photo, command=lambda:g.look("fireplace"), height = 151, width = 209)
fireplace.image = photo

#room 3
photo = PhotoImage(file="bookshelves.gif")
bookshelves = Button(window, image=photo, command=lambda:g.look("bookshelves"), height = 200, width = 149)
bookshelves.image = photo

photo = PhotoImage(file="desk.gif")
desk = Button(window, image=photo, command=lambda:g.look("desk"), height = 100, width = 123)
desk.image = photo

photo = PhotoImage(file="statue.gif")
statue = Button(window, image=photo, command=lambda:g.look("statue"), height = 200, width = 82)
statue.image = photo

photo=PhotoImage(file="book.gif")
book = Button(window,image=photo, command=lambda :g.take("book"), height=68, width=75)
book.image=photo             

#room 4
photo=PhotoImage(file="6-pack.gif")
beer = Button(window,image=photo, command=lambda :g.take("6-pack"), height=75, width=58)
beer.image=photo

photo = PhotoImage(file="brew_rig.gif")
brewrig = Button(window, image=photo, command=lambda:g.look("brew_rig"), height = 200, width = 127)
brewrig.image = photo

window.mainloop()
