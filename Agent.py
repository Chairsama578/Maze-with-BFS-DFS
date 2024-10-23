from tkinter import *
from enum import Enum
from collections import *
from Color import COLOR
from Maze import *

#create agent
class agent:
    def __init__(self,parentMaze,x=None,y=None,goal=None,color:COLOR=COLOR.pink):
       
        self._parentMaze=parentMaze
        self.color=color
        footprints=True
        if(isinstance(color,str)):
            if(color in COLOR.__members__):
                self.color=COLOR[color]
            else:
                raise ValueError(f'{color} is not a valid COLOR!')
        self._orient=0
        if x is None:x=parentMaze.rows
        if y is None:y=parentMaze.cols
        self.x=x
        self.y=y
        self.footprints=footprints
        self._parentMaze._agents.append(self)
        if goal==None:
            self.goal=self._parentMaze._goal
        else:
            self.goal=goal
        self._body=[]
        self.position=(self.x,self.y)
        
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self,newX):
        self._x=newX
    @property
    def y(self):
        return self._y
    @y.setter
    def y(self,newY):
        self._y=newY
        w=self._parentMaze._cell_width
        x=self.x*w-w+self._parentMaze._LabWidth
        y=self.y*w-w+self._parentMaze._LabWidth
        self._coord=(y, x,y + w, x + w)

        if(hasattr(self,'_head')):
            if self.footprints is False:
                self._parentMaze._canvas.delete(self._head)
            else:
                self._parentMaze._canvas.itemconfig(self._head, fill=self.color.value[1],outline="")
                self._parentMaze._canvas.tag_raise(self._head)
                try:
                    self._parentMaze._canvas.tag_lower(self._head,'ov')
                except:
                    pass
                lll=self._parentMaze._canvas.coords(self._head)
                oldcell=(round(((lll[1]-26)/self._parentMaze._cell_width)+1),round(((lll[0]-26)/self._parentMaze._cell_width)+1))
                self._parentMaze._redrawCell(*oldcell,self._parentMaze.theme)
                self._body.append(self._head)
            self._head=self._parentMaze._canvas.create_rectangle(*self._coord,fill=self.color.value[0],outline='')#stipple='gray75'
            try:
                self._parentMaze._canvas.tag_lower(self._head,'ov')
            except:
                    pass
            self._parentMaze._redrawCell(self.x,self.y,theme=self._parentMaze.theme)
        else:
            self._head=self._parentMaze._canvas.create_rectangle(*self._coord,fill=self.color.value[0],outline='')#stipple='gray75'
            try:
                self._parentMaze._canvas.tag_lower(self._head,'ov')
            except:
                pass
            self._parentMaze._redrawCell(self.x,self.y,theme=self._parentMaze.theme)
    @property
    def position(self):
        return (self.x,self.y)
    @position.setter
    def position(self,newpos):
        self.x=newpos[0]
        self.y=newpos[1]
        self._position=newpos
    def _RCCW(self):
        '''
        To Rotate the agent in Counter Clock Wise direction
        '''
        def pointNew(p,newOrigin):
            return (p[0]-newOrigin[0],p[1]-newOrigin[1])
        w=self._parentMaze._cell_width
        x=self.x*w-w+self._parentMaze._LabWidth
        y=self.y*w-w+self._parentMaze._LabWidth
        cent=(y+w/2,x+w/2)
        p1=pointNew((self._coord[0],self._coord[1]),cent)
        p2=pointNew((self._coord[2],self._coord[3]),cent)
        p1CW=(p1[1],-p1[0])
        p2CW=(p2[1],-p2[0])
        p1=p1CW[0]+cent[0],p1CW[1]+cent[1]
        p2=p2CW[0]+cent[0],p2CW[1]+cent[1]
        self._coord=(*p1,*p2)  
        self._parentMaze._canvas.coords(self._head,*self._coord)
        self._orient=(self._orient-1)%4
 
        
    def _RCW(self):
        '''
        To Rotate the agent in Clock Wise direction
        '''
        def pointNew(p,newOrigin):
            return (p[0]-newOrigin[0],p[1]-newOrigin[1])
        w=self._parentMaze._cell_width
        x=self.x*w-w+self._parentMaze._LabWidth
        y=self.y*w-w+self._parentMaze._LabWidth
        cent=(y+w/2,x+w/2)
        p1=pointNew((self._coord[0],self._coord[1]),cent)
        p2=pointNew((self._coord[2],self._coord[3]),cent)
        p1CW=(-p1[1],p1[0])
        p2CW=(-p2[1],p2[0])
        p1=p1CW[0]+cent[0],p1CW[1]+cent[1]
        p2=p2CW[0]+cent[0],p2CW[1]+cent[1]
        self._coord=(*p1,*p2)  
        self._parentMaze._canvas.coords(self._head,*self._coord)
        self._orient=(self._orient+1)%4