# Sorting Algorithm Visualizer by Bklyn1
# 12/02/2023
# Made in python using the pygame module
# Only works with in-place sorting algorithms
# Visualization of heap sort is a tad bit broken

import random
import time
import pygame as pg

from sorting_vis import *

pg.init()


def generate_new_list(n=50, min_val=0, max_val=100):
    return [random.randint(min_val, max_val) for _ in range(n)]


def main():
    def reset():
        return generate_new_list(lst_size), False, False, 0, 0
    
    # Init
    run = True
    clock = pg.time.Clock()

    lst_size = 50
    lst, sorting, sorted, perf_info.runtime, perf_info.operations = reset()

    draw_info = DrawInfo(width=1024, height=768, lst=lst)
    algo_info = bubble_sort_info

    ascending = True
    muted = False

    fps = 60
    while run:
        clock.tick(fps)

        # VISUALIZE ALGORITHM
        if sorting:
            try:
                next(algo_info.generator) 
            except StopIteration:
                sorting = False
                sorted = True
                perf_info.calc_runtime()
        else:
            draw_text(draw_info, algo_info, perf_info, (fps, lst_size), ascending, muted)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            if event.type != pg.KEYDOWN:
                continue

            # RESET
            if event.key == pg.K_r:
                lst, sorting, sorted, perf_info.runtime, perf_info.operations = reset()
                draw_info.set_list(lst)

            # START SORT
            elif event.key == pg.K_SPACE and not sorting and not sorted:
                sorting = True
                perf_info.start_time = time.time()
                algo_info.generator = algo_info.sort(draw_info, ascending)
            # ASCENDING
            elif event.key == pg.K_a and not sorting:
                ascending = True
            # DESCENDING
            elif event.key == pg.K_d and not sorting:
                ascending = False   
            # MUTE / UNMUTE 
            elif event.key == pg.K_m and not sorting:
                muted = not muted
                set_muted(muted)
            
            # CHANGE ALGORTIHM
            elif event.key == pg.K_1 and not sorting:
                algo_info = bubble_sort_info
            elif event.key == pg.K_2 and not sorting:
                algo_info = selection_sort_info
            elif event.key == pg.K_3 and not sorting:
                algo_info = insertion_sort_info
            elif event.key == pg.K_4 and not sorting:
                algo_info = shell_sort_info
            elif event.key == pg.K_5 and not sorting:
                algo_info = heap_sort_info

            # CHANGE SPEED & SIZE
            elif event.key == pg.K_UP and not sorting:
                fps += 10
            elif event.key == pg.K_DOWN and not sorting and fps > 10:
                fps -= 10
            elif event.key == pg.K_RIGHT and not sorting:
                lst_size += 10
            elif event.key == pg.K_LEFT and not sorting and lst_size > 10:
                lst_size -= 10

    pg.quit()


if __name__ == "__main__":
    main()