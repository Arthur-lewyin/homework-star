import pgzrun
import random

HEIGHT = 800
WIDTH = 600

START_SPEED = 10
ITEMS= ["asteroid","a"]

current_level = 1
FINAL_LEVEL = 6

game_over = False
game_complete = False

items = []
animation = []

def draw():
    global items, game_complete, game_over, current_level

    screen.clear()
    screen.blit("bg_images",(0,0))

    if game_over:
        display_message("GAME OVER", "The city died")  
    elif game_complete:
        display_message("WELLDONE", "you saved the city")
    else :
        for item in items:
            item.draw()

def display_message(heading,subheading) :
    screen.draw.text(heading,fontsize = 60, center = (400,300), color="black")
    screen.draw.text(subheading,fontsize = 30, center = (400,340), color="black")

def update():
    global items
    if len(items)==0:
        items = make_items(current_level)

def make_items(number_of_extra_items):
    items_to_create = get_option_to_create(number_of_extra_items)
    new_items = create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items

def get_option_to_create(number_of_extra_items):
    items_to_create = ["star"]
    for i in range(0,number_of_extra_items):
        items_to_create.append(ITEMS)
    return items_to_create

def create_items(items_to_create):
    new_items = []
    for i in items_to_create:
        item = Actor(i)
        new_items.append(item)
    return new_items

def layout_items(items_to_layout):
    number_of_gaps = len(items_to_layout)+1
    gaps_size = WIDTH/number_of_gaps
    random.shuffle(items_to_layout)
    for i, item in enumerate(items_to_layout):
        new_x_pos=(i + 1) * gaps_size
        item.x =new_x_pos
    

def animate_items(items_to_animate):
     global animations
     for i in items_to_animate:
         duration = START_SPEED-current_level
         animation = animate(i,duration=duration,on_finished=handle_game_over, y=HEIGHT)
         animations.append(animation)

def handle_game_over():
    global game_over
    game_over = True

def on_mouse_down(pos):
    global items
    for i in items:
        if i.collidepoint(pos):
            if "star" in i.image:
                handle_game_over()
            else:
                handle_game_complete()

def handle_game_complete():
    global current_level,items,animations,game_complete
    stop_animation(animations)
    if current_level == FINAL_LEVEL:
        game_complete = True
    else:
        current_level = current_level + 1
        items=[]
        animations = []

def stop_animation(animations_to_stop):
    for i in animations_to_stop:
        if i.running:
            i.stop()
    
pgzrun.go()