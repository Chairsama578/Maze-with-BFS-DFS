import sys
import os

# Đảm bảo đường dẫn hiện tại trỏ đúng đến thư mục chứa các module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import các module từ UI và Model
from UI.Maze import maze, COLOR, pel, textLabel
from Model.BFS import BFS
from Model.DFS import DFS

# Khởi tạo mê cung 5x5
m = maze(5, 5)

# Tạo mê cung với phần trăm vòng lặp là 100%
m.createMaze(loopPercent=100)

# Thực hiện tìm kiếm theo DFS
search, path = DFS(m)

# Tạo các điểm để đánh dấu trong mê cung
a = pel(m, color=COLOR.blue)
b = pel(m)

# Vẽ đường tìm kiếm và đường ngắn nhất
m.tracePath({a: search}, delay=100)
m.tracePath({b: path}, delay=100)

# Hiển thị độ dài của đường ngắn nhất
l = textLabel(m, 'Length of Shortest Path', len(path) + 1)

# Nếu bạn có phương thức chạy mê cung trong loop
m.run()
