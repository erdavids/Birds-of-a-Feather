w, h = 1400, 1400

# Number of birds
grid_x = 5
grid_y = 5

# The birds will draw inside this rectangle
grid_x_pixels = .8 * w
grid_y_pixels = .8 * h

# Distance between the birds
sep_x = grid_x_pixels / (grid_x - 1)
sep_y = grid_y_pixels / (grid_y - 1)

# Background Color
bc = (255, 255, 255)

# Global bird variables

colors = [(189, 208, 196), (154,183,211), (245,210,211), (247,225,211), (223,204,241)]
feet_length = 40
body_height = 100
line_thickness = 7

body_fill_chance = .3
head_fill_chance = .3
tail_chance = .3
arc_chance = .4

min_shape_lines = 1
max_shape_lines = 5

def get_random_element(l):
    return l[int(random(len(l)))]

# Adds shading to some of the randomly drawn triangles
def draw_lines(point_list):

    p1 = point_list.pop(point_list.index(get_random_element(point_list)))
    p2 = point_list.pop(point_list.index(get_random_element(point_list)))
    p3 = point_list.pop(point_list.index(get_random_element(point_list)))
    
    # Create lines
    lines = int(random(min_shape_lines, max_shape_lines))
    print(lines)
    
    if (p3[0] - p1[0] == 0):
        first_x_adj = 1
    else:
        first_x_adj = (p3[0] - p1[0])/abs(p3[0] - p1[0])
        
    if (p3[1] - p1[1] == 0):
        first_y_adj = 1
    else:
        first_y_adj = (p3[1] - p1[1])/abs(p3[1] - p1[1])
        
    first_x_sep = sqrt(pow(p1[0] - p3[0], 2))/lines * first_x_adj
    first_y_sep = sqrt(pow(p1[1] - p3[1], 2))/lines * first_y_adj
    
    if (p3[0] - p2[0] == 0):
        second_x_adj = 1
    else:
        second_x_adj = (p3[0] - p2[0])/abs(p3[0] - p2[0])
        
    if (p3[1] - p2[1] == 0):
        second_y_adj = 1
    else:
        second_y_adj = (p3[1] - p2[1])/abs(p3[1] - p2[1])
        
    second_x_sep = sqrt(pow(p2[0] - p3[0], 2))/lines * second_x_adj
    second_y_sep = sqrt(pow(p2[1] - p3[1], 2))/lines * second_y_adj

    for i in range(lines):
        line(p1[0] + first_x_sep * i, p1[1] + first_y_sep * i, p2[0] + second_x_sep * i, p2[1] + second_y_sep * i)


def draw_bird_base(x, y, pc, dc):
    
    ###########
    # Draw Legs
    ###########
    stroke(0)
    strokeCap(ROUND)
    line(x - feet_length, y, x + feet_length, y)
    line(x - feet_length/3.0, y, x - feet_length/3.0 - feet_length/2.0, y - feet_length)
    line(x + feet_length/3.0, y, x + feet_length/3.0 - feet_length/2.0, y - feet_length)
    
    ###########
    # Draw Body
    ###########
    stroke(*dc)
    body_bottom = y - feet_length/2.0
    
    body_one = (int(x - feet_length * 2.0), int(body_bottom))
    body_two = (int(x + feet_length*1.5), int(body_bottom))
    body_three = (int(x + feet_length*2.1), int(body_bottom - body_height))
    body_four = (int(x), int(body_bottom - body_height * 1.3))
    
    left_midpoint = ((body_four[0] + body_one[0]) / 2, (body_four[1] + body_one[1]) / 2)
    top_midpoint = ((body_four[0] + body_three[0]) / 2, (body_four[1] + body_three[1]) / 2)
    right_midpoint = ((body_two[0] + body_three[0]) / 2, (body_two[1] + body_three[1]) / 2)
    bottom_midpoint = ((body_one[0] + body_two[0]) / 2, (body_one[1] + body_two[1]) / 2)
    
    true_midpoint = ((left_midpoint[0] + right_midpoint[0]) / 2, (left_midpoint[1] + right_midpoint[1]) / 2)
    
    
    body_points = [ body_one, body_three, body_four, left_midpoint, top_midpoint, bottom_midpoint]
    
    fill(*bc)
    beginShape()
    vertex(*body_one)
    vertex(*body_two)
    vertex(*body_three)
    vertex(*body_four)
    endShape(CLOSE)
    
    for i in range(int(random(1, 4))):
        point_one = get_random_element(body_points)
        point_two = get_random_element(body_points)
        point_three = get_random_element(body_points)
        point_four = get_random_element(body_points)
        
        
        fill(pc[0], pc[1], pc[2])
        beginShape()
        vertex(*point_one)
        vertex(*point_two)
        vertex(*point_three)
        endShape(CLOSE)
        noFill()
        
        if (random(1) < .5):
            draw_lines([point_one, point_two, point_three])
    
    head_x = x + feet_length
    head_y = body_bottom - body_height * 1.1
    head_size = 90
    
    ###########
    # Draw Tail
    ###########
    if (random(1) < tail_chance):
        stroke(*dc)
        fill(*pc)
        var_width = random(15, 30)
        var_x = random(-25, -15)
        var_y = random(-50, -30)
        if (random(1) < .3):
            var_y *= -1
        
        beginShape()
        vertex(body_one[0], body_one[1])
        vertex(body_one[0] + var_width, body_one[1])
        vertex(body_one[0] + + var_width + var_x, body_one[1] + var_y)
        vertex(body_one[0] + var_x, body_one[1] + var_y)
        endShape(CLOSE)
    
    
    ###########
    # Draw Beak
    ###########
    y_variance = random(10, 40)
    length_variance = random(50, 100)
    

    # pc = get_random_element(colors)
    # inc = .2 * 255
    # stroke(pc[0] - inc, pc[1] - inc, pc[2] - inc)
    
    if (random(1) < body_fill_chance):
        fill(*pc)
    else:
        fill(*bc)
    
    triangle(head_x, head_y - y_variance, head_x, head_y + y_variance, head_x + length_variance, head_y)
    
    ###########
    # Draw Head
    ###########
    fill(*bc)
    circle(head_x, head_y, head_size)
    
    if (random(1) < arc_chance):
        fill(*pc)
        noStroke()
        arc(head_x, head_y, head_size, head_size, random(.7, 1)*PI, 1.8*PI, PIE);
    
    stroke(*dc)
        
    if (random(1) < head_fill_chance):
        fill(*pc)
    else:
        noFill()
    circle(head_x, head_y, head_size)
    

    
    ###########
    # Draw Eyes
    ###########
    eye_x = head_x + head_size/6.0
    eye_y = head_y - head_size/8.0
    eye_size = 25
    fill(*bc)
    circle(eye_x, eye_y, eye_size)
    
    stroke(0)
    fill(0)
    noStroke()
    circle(eye_x, eye_y, 10)
    
def setup():
    size(w, h)
    
    background(*bc)
    pixelDensity(2)
    stroke(0)
    strokeWeight(line_thickness)
    strokeJoin(ROUND)
    
    current_x = w/2.0 - grid_x_pixels/2.0
    current_y = h/2.0 - grid_y_pixels/2.0 + body_height
    
    for i in range(grid_x):
        for j in range(grid_y):
            
            pc = get_random_element(colors)
            inc = .2 * 255
            dc = (pc[0] - inc, pc[1] - inc, pc[2] - inc)
            draw_bird_base(current_x, current_y, pc, dc)
            current_y += sep_y
        current_y = h/2.0 - grid_y_pixels/2.0 + body_height
        current_x += sep_x
            
    seed = str(int(random(10000)))
    save("Examples/" + str(grid_x) + "-" + str(grid_y) + "-s-" + seed + ".png")
