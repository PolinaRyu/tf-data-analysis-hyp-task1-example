import pandas as pd
import numpy as np


chat_id = 503882767 

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    
    if (y_success/y_cnt - x_success/x_cnt) < 0.01:
        flag = True
    else:
        flag = False
    
    return flag
