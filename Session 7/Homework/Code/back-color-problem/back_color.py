from random import randint, choice
from is_inside import is_inside

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]

def get_shapes():
    return shapes


def generate_quiz():
    return [
                choice(['RED', 'blue' , 'yellow' , 'green']),
                choice(['#4CAF50', '#3F51B5' , '#FFD600' , '#4CAF50']),
                randint(0, 1) # 0 : meaning, 1: color,
            ]

def mouse_press(x, y, text, color, quiz_type):
    check = [x, y]
    for i in range(4):
        if is_inside(check, shapes[i]["rect"]) == True:
            mean_color = [shapes[i]["text"], shapes[i]["color"]]
    if quiz_type == 0:
        if mean_color[0] == text:
            return True
        else:
            return False
    elif quiz_type == 1:
        if mean_color[1] == color:
            return True
        else:
            return False
    return True
