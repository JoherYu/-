from random import choice

class RandomWalk():
    """生成随即漫步数据"""
    
    def __init__(self, num_points=5000):
        """初始化"""
        self.num_points = num_points  # 漫步步数
        self.x_values = [0]
        self.y_values = [0]
        
    def fill_walk(self):
        """计算所有漫步点并加入数组中"""
        while len(self.x_values) < self.num_points:
            
            # 前进方向及前进距离
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance
            
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance
            
            # 原地踏步不加入数组
            if x_step == 0 and y_step == 0:
                continue
                
            # 计算下一点并加入数组
            next_x = self.x_values[-1] + x_step
            self.x_values.append(next_x)
            
            next_y = self.y_values[-1] + y_step
            self.y_values.append(next_y)