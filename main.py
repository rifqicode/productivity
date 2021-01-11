# author Muhammad Rifqi <muhammadrifqi.tb@gmail.com>

import logging
import sys
import active_window
import json


def run():
    window_list = {}

    while 1:
        current_window = active_window.get_active_window()
        if current_window == '' or current_window == 'Task Switching':
            continue
            
        window_name = active_window.get_window_name(current_window).strip()
        if window_name in window_list:
            window_list[window_name]['time'] += 1
        else:
            window_list[window_name] = {
                'time' : 0
            }
        
        print(window_list)
        
run()