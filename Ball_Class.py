class Ball:
    
    def __init__(self,canvas,x,y,diameter,xVelocity,yVelocity,color): #construct
        self.canvas = canvas
        self.image = canvas.create_oval(x,y,x +diameter,y + diameter,fill=color) #create a oval
        self.xVelocity = xVelocity #create x and y motion
        self.yVelocity = yVelocity
        
    def move(self):
        coordinates = self.canvas.coords(self.image)
        if(coordinates[2]>=(self.canvas.winfo_width()) or coordinates[0]<0): #[2] = index 2
            self.xVelocity = -self.xVelocity
        if(coordinates[3]>=(self.canvas.winfo_height()) or coordinates[1]<0):
            self.yVelocity = -self.yVelocity
        
        self.canvas.move(self.image,self.xVelocity,self.yVelocity) #move the object
        
        
        
        