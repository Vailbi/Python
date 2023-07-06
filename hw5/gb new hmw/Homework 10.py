import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
human = ['1' if i == 'human' else '0' for i in lst]
robot = ['1' if i == 'robot' else '0' for i in lst]
data['human'] = human
data['robot'] = robot
print(data)