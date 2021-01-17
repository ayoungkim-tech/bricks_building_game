###################### User Manual #########################
#This is a game that build whatever you want with bricks
#You can choose the brick size within 30-100
#To build, click and drag the bricks within window size
#To trash away bricks, click and drag out of window size
############################################################

# import tkinter and random
import tkinter
import random
import tkinter.messagebox

class BuildingBricks:
    def __init__(self):
        #create main window
        self.main_window=tkinter.Tk()

        #create 4 frame for main_window wigets
        self.top_frame=tkinter.Frame()
        self.mid_frame=tkinter.Frame()
        self.bottom_frame=tkinter.Frame()
        self.result_frame=tkinter.Frame()

        #create top_frame widgets
        self.width_label=tkinter.Label(self.top_frame,
                                       text='Enter width 30-100: ')
        self.width_entry=tkinter.Entry(self.top_frame, width=10)

        #Pack top_frame widgets
        self.width_label.pack(side='left')
        self.width_entry.pack(side='left')

        #create mid_frame widgets
        self.height_label=tkinter.Label(self.mid_frame,
                                       text='Enter height 30-100: ')
        self.height_entry=tkinter.Entry(self.mid_frame, width=10)

        #Pack mid_frame widgets
        self.height_label.pack(side='left')
        self.height_entry.pack(side='left')

        #create bottom_frame widgets
        self.play_button=tkinter.Button(self.bottom_frame, text='Play',
                                        command=self.play_page)

        #Pack button
        self.play_button.pack()

        #create result frame widget
        #create StringVar object to show result
        self.value=tkinter.StringVar()
        self.block_label=tkinter.Label(self.result_frame, textvariable=self.value)

        #Pack frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        #self.result_frame.pack()

        #Create main loop
        tkinter.mainloop()



    def play_page(self):
        tk_rgb = "#%02x%02x%02x" % (250, 100, 100) # 255
        ####brick size by user
        brick_width = int(self.width_entry.get())
        brick_height = int(self.height_entry.get())

        if 100>=brick_width>=30 and 100>=brick_height>=30:

            #create result canvas
            canvas = tkinter.Canvas(width= 900, height=700)
            canvas.pack(side='left', fill='both')

            #make brick wall where rabbit hops around
            def onebrick(x,y,color):
                global brick_width, brick_height
                brick_width = int(self.width_entry.get())
                brick_height = int(self.height_entry.get())
                brick = canvas.create_rectangle(x,y,x+brick_width,y+brick_height,fill=color,width=3)

            #Find the closest brick near clicked location
            def find_item(event) :
                global x, y, item
                x = event.x
                y = event.y
                item = canvas.find_closest(x,y)

            #Moving choosed item
            def move_item(event) :
                global x, y
                nx = event.x
                ny = event.y
                distx = nx - x
                disty = ny - y
                canvas.move(item, distx, disty)
                x = nx
                y = ny

            #Bricks in random red colors
            x1 = -brick_width
            y1 = 0
            for y in range(30):
                for x in range(35):
                    x1 += brick_width
                    rr = 130 + random.randint(1,30)
                    rg = 30 + random.randint(1,20)
                    rb = 0 + random.randint(1,20)
                    tk_rgb = "#%02x%02x%02x" % (rr,rg,rb)
                    onebrick(x1,y1,tk_rgb)
                x1 -= 40 * brick_width + brick_width/2
                y1 += brick_height

            #first click and drag to move
            canvas.bind("<Button-1>", find_item)
            canvas.bind("<B1-Motion>", move_item)

            ###Show the play page
            self.value=canvas
            self.quit_button = tkinter.Button(self.result_frame, text='Quit'
                                          , command=self.main_window.destroy)
            #pack button
            self.quit_button.pack(side='right')

            #pack result_frame
            self.result_frame.pack()


        #Handle error situation
        else:
            tkinter.messagebox.showinfo('Error message',
                                        'Width or Height value is out of range.\n Try again')


# create instance of class BuildingBricks
buildingBricks = BuildingBricks()