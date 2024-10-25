import random
from tkinter import *
from collections import deque
from UI.Pel import pel
from UI.Color import *
from UI.TextLabel import *

class maze: 
    # hàm chính của class maze
    def __init__(self,rows=100,cols=100):
        self.rows=rows
        self.cols=cols
        self.maze_map={}
        self.grid=[]
        self.path={} 
        self._cell_width=50  
        self._win=None 
        self._canvas=None
        self._pels=[]

    @property
    def grid(self):
        return self._grid
    @grid.setter        
    def grid(self,n):
        self._grid=[]
        y=0
        for n in range(self.cols):
            x = 1
            y = 1+y
            for m in range(self.rows):
                self.grid.append((x,y))
                self.maze_map[x,y]={'E':0,'W':0,'N':0,'S':0}
                x = x + 1 
    def _Open_East(self,x, y):
        # Xóa tường bên phải
        self.maze_map[x,y]['E']=1
        if y+1<=self.cols:
            self.maze_map[x,y+1]['W']=1
    def _Open_West(self,x, y):
        # Xóa tường bên trái
        self.maze_map[x,y]['W']=1
        if y-1>0:
            self.maze_map[x,y-1]['E']=1
    def _Open_North(self,x, y):
        # Xóa tường bên tren
        self.maze_map[x,y]['N']=1
        if x-1>0:
            self.maze_map[x-1,y]['S']=1
    def _Open_South(self,x, y):
        # Xóa tường bên duoi
        self.maze_map[x,y]['S']=1
        if x+1<=self.rows:
            self.maze_map[x+1,y]['N']=1
    
    def createMaze(self,loopPercent=0,theme:COLOR=COLOR.dark):
        _stack=[]
        _closed=[]
        self.theme=theme
        # Ngẫu nhiên vị trí của goal
        while (TRUE):
            x = random.randint(1,self.rows)
            y = random.randint(1,self.cols)
            if x!= self.rows or y!= self.cols: break
        
        self._goal=(x,y)
        def blockedNeighbours(cell):
            n=[]
            for d in self.maze_map[cell].keys():
                if self.maze_map[cell][d]==0:
                    if d=='E' and (cell[0],cell[1]+1) in self.grid:
                        n.append((cell[0],cell[1]+1))
                    elif d=='W' and (cell[0],cell[1]-1) in self.grid:
                        n.append((cell[0],cell[1]-1))
                    elif d=='N' and (cell[0]-1,cell[1]) in self.grid:
                        n.append((cell[0]-1,cell[1]))
                    elif d=='S' and (cell[0]+1,cell[1]) in self.grid:
                        n.append((cell[0]+1,cell[1]))
            return n
        def removeWallinBetween(cell1,cell2):
            # xóa tường ở giữa 2 ô
            if cell1[0]==cell2[0]:
                if cell1[1]==cell2[1]+1:
                    self.maze_map[cell1]['W']=1
                    self.maze_map[cell2]['E']=1
                else:
                    self.maze_map[cell1]['E']=1
                    self.maze_map[cell2]['W']=1
            else:
                if cell1[0]==cell2[0]+1:
                    self.maze_map[cell1]['N']=1
                    self.maze_map[cell2]['S']=1
                else:
                    self.maze_map[cell1]['S']=1
                    self.maze_map[cell2]['N']=1
        def isCyclic(cell1,cell2):
            # kiểm tra đường dẫn giữa 2 ô
            ans=False
            if cell1[0]==cell2[0]:
                if cell1[1]>cell2[1]: cell1,cell2=cell2,cell1
                if self.maze_map[cell1]['S']==1 and self.maze_map[cell2]['S']==1:
                    if (cell1[0]+1,cell1[1]) in self.grid and self.maze_map[(cell1[0]+1,cell1[1])]['E']==1:
                        ans= True
                if self.maze_map[cell1]['N']==1 and self.maze_map[cell2]['N']==1:
                    if (cell1[0]-1,cell1[1]) in self.grid and self.maze_map[(cell1[0]-1,cell1[1])]['E']==1:
                        ans= True
            else:
                if cell1[0]>cell2[0]: cell1,cell2=cell2,cell1
                if self.maze_map[cell1]['E']==1 and self.maze_map[cell2]['E']==1:
                    if (cell1[0],cell1[1]+1) in self.grid and self.maze_map[(cell1[0],cell1[1]+1)]['S']==1:
                        ans= True
                if self.maze_map[cell1]['W']==1 and self.maze_map[cell2]['W']==1:
                    if (cell1[0],cell1[1]-1) in self.grid and self.maze_map[(cell1[0],cell1[1]-1)]['S']==1:
                        ans= True
            return ans
       
        _stack.append((x,y))
        _closed.append((x,y))
        bias=0

        while len(_stack) > 0:
            cell = []
            bias+=1
            if(x , y +1) not in _closed and (x , y+1) in self.grid:
                cell.append("E")
            if (x , y-1) not in _closed and (x , y-1) in self.grid:
                cell.append("W")
            if (x+1, y ) not in _closed and (x+1 , y ) in self.grid:
                cell.append("S")
            if (x-1, y ) not in _closed and (x-1 , y) in self.grid:
                cell.append("N") 
            if len(cell) > 0:    
                bias=0
                current_cell = (random.choice(cell))
                if current_cell == "E":
                    self._Open_East(x,y)
                    self.path[x, y+1] = x, y
                    y = y + 1
                    _closed.append((x, y))
                    _stack.append((x, y))

                elif current_cell == "W":
                    self._Open_West(x, y)
                    self.path[x , y-1] = x, y
                    y = y - 1
                    _closed.append((x, y))
                    _stack.append((x, y))

                elif current_cell == "N":
                    self._Open_North(x, y)
                    self.path[(x-1 , y)] = x, y
                    x = x - 1
                    _closed.append((x, y))
                    _stack.append((x, y))

                elif current_cell == "S":
                    self._Open_South(x, y)
                    self.path[(x+1 , y)] = x, y
                    x = x + 1
                    _closed.append((x, y))
                    _stack.append((x, y))

            else:
                x, y = _stack.pop()

        # lặp để tạo nhiều đường dẫn
        if loopPercent!=0:
            
            x,y=self.rows,self.cols
            pathCells=[(x,y)]
            while x!=self.rows or y!=self.cols:
                x,y=self.path[(x,y)]
                pathCells.append((x,y))
            notPathCells=[i for i in self.grid if i not in pathCells]
            random.shuffle(pathCells)
            random.shuffle(notPathCells)
            pathLength=len(pathCells)
            notPathLength=len(notPathCells)
            count1,count2=pathLength/3*loopPercent/100,notPathLength/3*loopPercent/100
            
            # Xóa các khối từ đường dẫn ngắn nhất
            count=0
            i=0
            while count<count1: 
                if len(blockedNeighbours(pathCells[i]))>0:
                    cell=random.choice(blockedNeighbours(pathCells[i]))
                    if not isCyclic(cell,pathCells[i]):
                        removeWallinBetween(cell,pathCells[i])
                        count+=1
                    i+=1
                        
                else:
                    i+=1
                if i==len(pathCells):
                    break
            
            if len(notPathCells)>0:
                count=0
                i=0
                while count<count2: 
                    if len(blockedNeighbours(notPathCells[i]))>0:
                        cell=random.choice(blockedNeighbours(notPathCells[i]))
                        if not isCyclic(cell,notPathCells[i]):
                            removeWallinBetween(cell,notPathCells[i])
                            count+=1
                        i+=1
                            
                    else:
                        i+=1
                    if i==len(notPathCells):
                        break
        self._drawMaze(self.theme)
        pel(self,*self._goal,color=COLOR.red)
      
    def _drawMaze(self,theme):
        # Tao Tkinter 
        
        self._LabWidth= 26
        self._win=Tk()
        self._win.title('Nhom 5')
        scr_width=self._win.winfo_screenheight()
        scr_height=self._win.winfo_screenheight()
        self._win.geometry(f"{scr_width}x{scr_height}+0+0")
        self._canvas = Canvas(width=scr_width, height=scr_height, bg=theme.value[0]) 
        self._canvas.pack(expand=YES, fill=BOTH) 
        # Tính chiều rộng của mê cung
        k=3.25
        if self.rows>=95 and self.cols>=95:
            k=0
        elif self.rows>=80 and self.cols>=80:
            k=1
        elif self.rows>=70 and self.cols>=70:
            k=1.5
        elif self.rows>=50 and self.cols>=50:
            k=2
        elif self.rows>=35 and self.cols>=35:
            k=2.5
        elif self.rows>=22 and self.cols>=22:
            k=3
        self._cell_width=round(min(((scr_height-self.rows-k*self._LabWidth)/(self.rows)),((scr_width-self.cols-k*self._LabWidth)/(self.cols)),90),3)
        
        # Tạo dòng cho mê cung
        if self._win is not None:
            if self.grid is not None:
                for cell in self.grid:
                    x,y=cell
                    w=self._cell_width
                    x=x*w-w+self._LabWidth
                    y=y*w-w+self._LabWidth
                    if self.maze_map[cell]['E']==False:
                        l=self._canvas.create_line(y + w, x, y + w, x + w,width=2,fill=theme.value[1],tag='line')
                    if self.maze_map[cell]['W']==False:
                        l=self._canvas.create_line(y, x, y, x + w,width=2,fill=theme.value[1],tag='line')
                    if self.maze_map[cell]['N']==False:
                        l=self._canvas.create_line(y, x, y + w, x,width=2,fill=theme.value[1],tag='line')
                    if self.maze_map[cell]['S']==False:
                        l=self._canvas.create_line(y, x + w, y + w, x + w,width=2,fill=theme.value[1],tag='line')
    # Tạo cột cho mê cung
    def _redrawCell(self,x,y,theme):
        w=self._cell_width
        cell=(x,y)
        x=x*w-w+self._LabWidth
        y=y*w-w+self._LabWidth
        if self.maze_map[cell]['E']==False:
            self._canvas.create_line(y + w, x, y + w, x + w,width=2,fill=theme.value[1])
        if self.maze_map[cell]['W']==False:
            self._canvas.create_line(y, x, y, x + w,width=2,fill=theme.value[1])
        if self.maze_map[cell]['N']==False:
            self._canvas.create_line(y, x, y + w, x,width=2,fill=theme.value[1])
        if self.maze_map[cell]['S']==False:
            self._canvas.create_line(y, x + w, y + w, x + w,width=2,fill=theme.value[1])

    _tracePathList=[]
    def _tracePathSingle(self,a,p,delay):
       
        if (a.x,a.y)==(a.goal):
            del maze._tracePathList[0][0][a]
            if maze._tracePathList[0][0]=={}:
                del maze._tracePathList[0]
                if len(maze._tracePathList)>0:
                    self.tracePath(maze._tracePathList[0][0])
                 
            return
        # Dành cho đường đi ngắn nhất
        if(type(p)==dict):
            if(len(p)==0):
                del maze._tracePathList[0][0][a]
                return
            a.x,a.y=p[(a.x,a.y)]
        # Danh cho đường đi tìm
        if (type(p)==list):
            if(len(p)==0):
                del maze._tracePathList[0][0][a]
                if maze._tracePathList[0][0]=={}:
                    del maze._tracePathList[0]
                    if len(maze._tracePathList)>0:
                        self.tracePath(maze._tracePathList[0][0]) 
                return
            a.x,a.y=p[0]
            del p[0]

        self._win.after(delay, self._tracePathSingle,a,p,delay)    

    def tracePath(self,d, delay=300):
        self._tracePathList.append((d,delay))
        if maze._tracePathList[0][0]==d: 
            for a,p in d.items():
                if a.goal!=(a.x,a.y) and len(p)!=0:
                    self._tracePathSingle(a,p,delay)
    def run(self):
        self._win.mainloop()