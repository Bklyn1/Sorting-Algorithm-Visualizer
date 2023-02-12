import pygame as pg

pg.init()

class DrawInfo:
    BLACK = 0,0,0,
    WHITE = 255,255,255
    RED = 255,0,0
    GREEN = 0,255,0
    BLUE = 0,0,255

    GREYS = [
        (128,128,128),
        (160,160,160),
        (192,192,192)
    ]

    BACKGROUND_COLOUR = WHITE
    FONT_DIR = "assets/Roboto-Regular.ttf"
    SMALL_FONT = pg.font.Font(FONT_DIR, 16)
    FONT = pg.font.Font(FONT_DIR, 20)
    LARGE_FONT = pg.font.Font(FONT_DIR, 30)

    SIDE_PAD = 100
    TOP_PAD = 200

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height

        self.window = pg.display.set_mode((width, height))
        pg.display.set_caption("Sorting Algorithm Visualizer")
        
        self.set_list(lst)


    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        self.bar_width = (self.width - self.SIDE_PAD) / len(lst)
        self.bar_height = (self.height - self.TOP_PAD) // (self.max_val - self.min_val)
        self.start_x = self.SIDE_PAD // 2
        

def draw_text(draw_info, algo_info, perf_info, ss_info, ascending, muted):
    win = draw_info.window
    win.fill(draw_info.BACKGROUND_COLOUR)

    title = draw_info.LARGE_FONT.render(f"{algo_info.name} - {'Ascending' if ascending else 'Descending'}", 1, draw_info.BLUE)
    win.blit(title, (draw_info.width / 2 - title.get_width() / 2, 5))

    info = draw_info.FONT.render(f"Ω({algo_info.best_case}) | Θ({algo_info.average_case}) | O({algo_info.worst_case}) | S({algo_info.space_complexity})", 1, draw_info.RED)
    win.blit(info, (draw_info.width / 2 - info.get_width() / 2, 40))

    controls = draw_info.FONT.render(f"R - Reset | SPACE - Start Sort | A - Asc | D - Desc | M - {'Unmute' if muted else 'Mute'} | ^v - FPS | <> - Size", 1, draw_info.BLACK)
    win.blit(controls, (draw_info.width / 2 - controls.get_width() / 2, 80))

    sorting = draw_info.FONT.render("1 - Bubble | 2 - Selection | 3 - Insertion | 4 - Shell | 5 - Heap", 1, draw_info.BLACK)
    win.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 110))

    perf = draw_info.SMALL_FONT.render(f"runtime: {perf_info.runtime}s | operations: {perf_info.operations}", 1, draw_info.BLACK)
    win.blit(perf, (draw_info.start_x, 160))

    ss = draw_info.SMALL_FONT.render(f"fps: {ss_info[0]} | size: {ss_info[1]}", 1, draw_info.BLACK)
    win.blit(ss, (draw_info.width - draw_info.start_x - ss.get_width(), 160))

    draw_list(draw_info)
    pg.display.update()


def draw_list(draw_info, colour_positions={}, clear_bg=False):
    lst = draw_info.lst

    if clear_bg:
        clear_rect = (draw_info.start_x, draw_info.TOP_PAD, 
                      draw_info.width - draw_info.SIDE_PAD, draw_info.height - draw_info.TOP_PAD)
        pg.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOUR, clear_rect)

    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.bar_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.bar_height

        colour = draw_info.GREYS[i % 3]

        if i in colour_positions:
            colour = colour_positions[i]

        pg.draw.rect(draw_info.window, colour, (x, y, draw_info.bar_width, draw_info.height))

    if clear_bg:
        pg.display.update()