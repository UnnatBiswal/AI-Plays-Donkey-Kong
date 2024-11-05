import os
import random
import pygame

os.environ['SDL_VIDEO_CENTERED'] = '1' 
pygame.init()
info = pygame.display.Info()
window_width, window_height = 1020, 730

timer = pygame.time.Clock()
fps = 60

pygame.display.set_caption('Ai Plays Donkey Kong')

font = pygame.font.Font('freesansbold.ttf', 50)
font2 = pygame.font.Font('freesansbold.ttf', 30)

screen = pygame.display.set_mode([window_width, window_height])
section_width = window_width // 32
section_height = window_height // 32
slope = section_height // 8
barrel_spawn_time = 360
barrel_count = barrel_spawn_time / 2
barrel_time = 360
barrel_img = pygame.transform.scale(pygame.image.load("assets/barrels/barrel.png"),
                                    (section_width * 1.2, section_height * 1.8))
flames_img = pygame.transform.scale(pygame.image.load("assets/fire.png"),
                                    (section_width * 2, section_height))
barrel_side = pygame.transform.scale(pygame.image.load("assets/barrels/barrel2.png"),
                                     (section_width * 1.5, section_height * 2))
dk1 = pygame.transform.scale(pygame.image.load("assets/donkey's dong/dk1.png"),
                             (section_width * 5, section_height * 5))
dk2 = pygame.transform.scale(pygame.image.load("assets/donkey's dong/dk2.png"),
                             (section_width * 5, section_height * 5))
dk3 = pygame.transform.scale(pygame.image.load("assets/donkey's dong/dk3.png"),
                             (section_width * 5, section_height * 5))
peach1 = pygame.transform.scale(pygame.image.load('assets/peach/peach1.png'),
                                (2 * section_width, 2 * section_height))
peach2 = pygame.transform.scale(pygame.image.load('assets/peach/peach2.png'),
                                (2 * section_width, 2 * section_height))
fireball = pygame.transform.scale(pygame.image.load('assets/fireball.png'),
                                  (1.5 * section_width, 2 * section_height))
fireball2 = pygame.transform.scale(pygame.image.load('assets/fireball2.png'),
                                   (1.5 * section_width, 2 * section_height))
standing = pygame.transform.scale(pygame.image.load('assets/mario/standing.png'),
                                  (1.5 * section_width, 2 * section_height))
jumping = pygame.transform.scale(pygame.image.load('assets/mario/jumping.png'),
                                 (1.5 * section_width, 2 * section_height))
running = pygame.transform.scale(pygame.image.load('assets/mario/running.png'),
                                 (1.5 * section_width, 2 * section_height))
climbing1 = pygame.transform.scale(pygame.image.load('assets/mario/climbing1.png'),
                                   (1.5 * section_width, 2 * section_height))
climbing2 = pygame.transform.scale(pygame.image.load('assets/mario/climbing2.png'),
                                   (1.5 * section_width, 2 * section_height))

fireball_trigger = False
counter = 0
score = 0
high_score = 0
bonus = 6000
first_fireball_trigger = False
victory = False
reset_game = False
keys = {
    "left": False,
    "right": False,
    "climb_up": False,
    "climb_down": False
}
start_y = window_height - 2 * section_height
row2_y = start_y - 4 * section_height
row3_y = row2_y - 7 * slope - 3 * section_height
row4_y = row3_y - 4 * section_height
row5_y = row4_y - 7 * slope - 3 * section_height
row6_y = row5_y - 4 * section_height
row6_top = row6_y - 4 * slope
row5_top = row5_y - 8 * slope
row4_top = row4_y - 8 * slope
row3_top = row3_y - 8 * slope
row2_top = row2_y - 8 * slope
row1_top = start_y - 5 * slope
# Draw lines for the "top" of each row
levels = [{'bridges': [(1, start_y, 15), (16, start_y - slope, 3),
                       (19, start_y - 2 * slope, 3), (22, start_y - 3 * slope, 3),
                       (25, start_y - 4 * slope, 3), (28, start_y - 5 * slope, 3),
                       (25, row2_y, 3), (22, row2_y - slope, 3),
                       (19, row2_y - 2 * slope, 3), (16, row2_y - 3 * slope, 3),
                       (13, row2_y - 4 * slope, 3), (10, row2_y - 5 * slope, 3),
                       (7, row2_y - 6 * slope, 3), (4, row2_y - 7 * slope, 3),
                       (2, row2_y - 8 * slope, 2), (4, row3_y, 3),
                       (7, row3_y - slope, 3), (10, row3_y - 2 * slope, 3),
                       (13, row3_y - 3 * slope, 3), (16, row3_y - 4 * slope, 3),
                       (19, row3_y - 5 * slope, 3), (22, row3_y - 6 * slope, 3),
                       (25, row3_y - 7 * slope, 3), (28, row3_y - 8 * slope, 2),
                       (25, row4_y, 3), (22, row4_y - slope, 3),
                       (19, row4_y - 2 * slope, 3), (16, row4_y - 3 * slope, 3),
                       (13, row4_y - 4 * slope, 3), (10, row4_y - 5 * slope, 3),
                       (7, row4_y - 6 * slope, 3), (4, row4_y - 7 * slope, 3),
                       (2, row4_y - 8 * slope, 2), (4, row5_y, 3),
                       (7, row5_y - slope, 3), (10, row5_y - 2 * slope, 3),
                       (13, row5_y - 3 * slope, 3), (16, row5_y - 4 * slope, 3),
                       (19, row5_y - 5 * slope, 3), (22, row5_y - 6 * slope, 3),
                       (25, row5_y - 7 * slope, 3), (28, row5_y - 8 * slope, 2),
                       (25, row6_y, 3), (22, row6_y - slope, 3),
                       (19, row6_y - 2 * slope, 3), (16, row6_y - 3 * slope, 3),
                       (2, row6_y - 4 * slope, 14), (13, row6_y - 4 * section_height, 6),
                       (10, row6_y - 3 * section_height, 3)],
           'ladders': [(12, row2_y + 6 * slope, 2), (12, row2_y + 29 * slope, 2),
                       (24, row2_y + 13 * slope, 4), (6, row3_y + 13 * slope, 3),
                       (14, row3_y + 10 * slope, 4), (10, row4_y + 6 * slope, 1),
                       (10, row4_y + 27 * slope, 2), (16, row4_y + 10 * slope, 4),
                       (25, row4_y + 14 * slope, 3), (6, row5_y + 14 * slope, 3),
                       (11, row5_y + 12 * slope, 3), (23, row5_y + 4 * slope, 1),
                       (23, row5_y + 24 * slope, 2), (25, row6_y + 14 * slope, 3),
                       (13, row6_y + 6 * slope, 2), (13, row6_y + 27 * slope, 2),
                       (18, row6_y - 30 * slope, 4), (12, row6_y - 20 * slope, 2),
                       (10, row6_y - 20 * slope, 2), (12, -5, 14), (10, -5, 14)],
           'goal': (13, row6_y - 4 * section_height, 3)}]


class Player(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)
        self.y_velocity = 0
        self.x_speed = 2.7
        self.x_velocity = 0
        self.on_ground = False
        self.pos = 0
        self.dir = 1
        self.count = 0
        self.climbing = False
        self.image = standing
        self.rect = self.image.get_rect()
        self.rect.width -= 18
        self.hitbox = self.rect
        self.rect.center = (x_pos, y_pos)
        self.over_barrel = False
        self.bottom = pygame.rect.Rect(self.rect.left, self.rect.bottom - 20, self.rect.width, 20)

    def update(self):
        self.on_ground = False
        for i in range(len(plats)):
            if self.bottom.colliderect(plats[i]):
                self.on_ground = True
                if not self.climbing:
                    self.rect.centery = plats[i].top - self.rect.height / 2 + 1
        if not self.on_ground and not self.climbing:
            self.y_velocity += 0.37
        self.rect.move_ip(self.x_velocity * self.x_speed, self.y_velocity)
        self.bottom = pygame.rect.Rect(self.rect.left, self.rect.bottom - 23, self.rect.width, 20)
        #pygame.draw.rect(screen, 'blue', self.bottom)
        if self.x_velocity != 0 or (self.climbing and self.y_velocity != 0):
            self.count = (self.count + 1) % 5 
            if self.count == 0:
                self.pos = (self.pos + 1) % 2 
        else:
            self.pos = 0
        # Check if player goes out of window bounds
        if self.rect.top > window_height or self.rect.right < 0 or self.rect.left > window_width:
            reset()  # Call the reset function if the player goes out of bounds

    def draw(self):
        # Determine player state and set appropriate image
        if self.climbing:
            # Switch between climbing images based on position
            self.image = climbing1 if self.pos == 0 else climbing2
        elif self.on_ground:
            # Choose standing or running based on position and movement
            self.image = standing if self.pos == 0 else running
        else:
            # Set to jumping image if player is in the air
            self.image = jumping

        # Flip the image if the player is facing left
        self.image = pygame.transform.flip(self.image, True, False) if self.dir == -1 else self.image

        # Draw the image with a slight offset for better alignment
        screen.blit(self.image, (self.rect.x - 8, self.rect.y - 3))
        #pygame.draw.rect(screen, 'blue', self.rect)


class Barrel(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((36, 29))
        self.rect = self.image.get_rect()
        self.rect.center = (x_pos, y_pos)
        self.y_velocity = 0
        self.x_velocity = 1
        self.pos = 0
        self.count = 0
        self.oil_collision = False
        self.falling = False
        self.bottom = self.rect

    def update(self, fire_trig):
        if self.y_velocity < 8 and not self.falling:
            barrel.y_velocity += 2
        for i in range(len(plats)):
            if self.bottom.colliderect(plats[i]):
                self.y_velocity = 0
                self.falling = False
        if self.rect.colliderect(oil_drum):
            if not self.oil_collision:
                self.oil_collision = True
                if random.randint(0, 2) == 2:
                    fire_trig = True
        if not self.falling:
            if row5_top >= self.rect.bottom or row3_top >= self.rect.bottom >= row4_top or row1_top >= self.rect.bottom >= row2_top:
                self.x_velocity = 4
            else:
                self.x_velocity = -4
        else:
            self.x_velocity = 0
        self.rect.move_ip(self.x_velocity, self.y_velocity)
        if self.rect.top > window_height:
            self.kill()
        if self.count < 15:
            self.count += 1
        else:
            self.count = 0
            if self.x_velocity != 0:
                self.pos = (self.pos + (1 if self.x_velocity > 0 else -1)) % 4
        self.bottom = pygame.rect.Rect((self.rect[0] , self.rect.bottom), (self.rect[2], 4))
        #pygame.draw.rect(screen, 'purple', self.bottom) #for debugging
        return fire_trig
    
    def draw(self):
        screen.blit(pygame.transform.rotate(barrel_img, 90 * self.pos), self.rect.topleft)
        #pygame.draw.rect(screen , 'white', self.rect) #for debugging


class Flame(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = fireball
        self.rect = self.image.get_rect()
        self.rect.center = (x_pos, y_pos)
        self.current_frame = 1
        self.count = 0
        self.x_count = 0
        self.x_velocity = 2
        self.x_max = 4
        self.y_velocity = 0
        self.row = 1
        self.check_lad = False
        self.climbing = False

    def update(self):
        if self.y_velocity < 3 and not self.climbing:
            flame.y_velocity += 0.25
        for i in range(len(plats)):
            if self.rect.colliderect(plats[i]):
                flame.climbing = False
                flame.y_velocity = -4
        #frame controlled animation system
        if self.count < 15:
            self.count += 1
        else:
            self.count = 0
            self.current_frame *= -1
            if self.x_count < self.x_max:
                self.x_count += 1
            else:  
                self.x_count = 0
                if self.x_velocity > 0:
                    if self.row in [1, 3, 5]:
                        self.x_max = random.randint(3, 6)
                    else:
                        self.x_max = random.randint(6, 10)
                else:
                    if self.row in [1, 3, 5]:
                        self.x_max = random.randint(6, 10)
                    else:
                        self.x_max = random.randint(3, 6)
                self.x_velocity *= -1
        if self.current_frame == 1:
            if self.x_velocity > 0:
                self.image = fireball
            else:
                self.image = pygame.transform.flip(fireball, True, False)
        else:
            if self.x_velocity > 0:
                self.image = fireball2
            else:
                self.image = pygame.transform.flip(fireball2, True, False)
        self.rect.move_ip(self.x_velocity, self.y_velocity)
        #pygame.draw.rect(screen, 'green', self.rect) #debugging
        if self.rect.top > window_height or self.rect.top < 0:
            self.kill()

    def check_climb(self):
        already_collided = False
        for lad in lads:
            if self.rect.colliderect(lad) and not self.climbing and not self.check_lad:
                self.check_lad = True
                already_collided = True
                if random.randint(0, 60) == 60:
                    self.climbing = True
                    self.y_velocity = - 2
        if not already_collided:
            self.check_lad = False
        if self.rect.bottom < row6_y:
            self.row = 6
        elif self.rect.bottom < row5_y:
            self.row = 5
        elif self.rect.bottom < row4_y:
            self.row = 4
        elif self.rect.bottom < row3_y:
            self.row = 3
        elif self.rect.bottom < row2_y:
            self.row = 2
        else:
            self.row = 1


class Bridge:
    def __init__(self, x_pos, y_pos, length):
        self.x_pos = x_pos * section_width
        self.y_pos = y_pos
        self.length = length
        self.top = self.draw()

    def draw(self):
        line_width = 4
        platform_color = (254,44, 84)
        for i in range(self.length):
            bot_coord = self.y_pos + section_height
            left_coord = self.x_pos + (section_width * i)
            mid_coord = left_coord + (section_width * 0.5)
            right_coord = left_coord + section_width
            top_coord = self.y_pos
            # draw 4 lines, top, bot, left diag, right diag
            pygame.draw.line(screen, platform_color, (left_coord, top_coord),
                             (right_coord, top_coord), line_width)
            pygame.draw.line(screen, platform_color, (left_coord, bot_coord),
                             (right_coord, bot_coord), line_width)
            pygame.draw.line(screen, platform_color, (left_coord, bot_coord),
                             (mid_coord, top_coord), line_width)
            pygame.draw.line(screen, platform_color, (mid_coord, top_coord),
                             (right_coord, bot_coord), line_width)
        # get the top platform 'surface'
        Platform_top = pygame.rect.Rect((self.x_pos, self.y_pos), (self.length * section_width, 4))
        #pygame.draw.rect(screen, 'green', Platform_top) #for debugging
        return Platform_top


class Ladder:
    def __init__(self, x_pos, y_pos, length):
        self.x_pos = x_pos * section_width
        self.y_pos = y_pos
        self.length = length
        self.body = self.draw()

    def draw(self):
        line_width = 4
        lad_color = (52,204,255)
        lad_height = 0.65
        for i in range(self.length):
            top_coord = self.y_pos + lad_height * section_height * i
            bot_coord = top_coord + lad_height * section_height
            mid_coord = (lad_height / 2) * section_height + top_coord
            left_coord = self.x_pos
            right_coord = left_coord + section_width
            pygame.draw.line(screen, lad_color, (left_coord, top_coord), (left_coord, bot_coord), line_width)
            pygame.draw.line(screen, lad_color, (right_coord, top_coord), (right_coord, bot_coord), line_width)
            pygame.draw.line(screen, lad_color, (left_coord, mid_coord), (right_coord, mid_coord), line_width)
        body = pygame.rect.Rect((self.x_pos, self.y_pos - section_height),
                                (section_width, (lad_height * self.length * section_height + section_height)))
        return body


# function to draw platforms and ladders
def draw_screen():
    platforms = []
    climbers = []
    ladder_objs = []
    bridge_objs = []

    ladders = levels[0]['ladders']
    bridges = levels[0]['bridges']

    for ladder in ladders:
        ladder_objs.append(Ladder(*ladder))
        if ladder[2] >= 3:
            climbers.append(ladder_objs[-1].body)
    for bridge in bridges:
        bridge_objs.append(Bridge(*bridge))
        platforms.append(bridge_objs[-1].top)

    return platforms, climbers


def draw_extras():
    screen.blit(font.render(f'I•{score}', True, 'white'), (3*section_width, 2*section_height))
    screen.blit(font.render(f'TOP• {high_score}', True, 'white'), (14 * section_width, 2 * section_height))
    screen.blit(font.render(f'[          ]', True, 'white'), (20 * section_width, 4 * section_height))
    screen.blit(font2.render(f'   BONUS      ', True, 'white'), (20 * section_width + 5, 4 * section_height))
    screen.blit(font2.render(f'    {bonus}        ', True, 'white'),
                (20 * section_width + 5, 5 * section_height))
    # drawing peach
    if barrel_count < barrel_spawn_time / 2:
        screen.blit(peach1, (13 * section_width, row6_y - 6 * section_height))
    else:
        screen.blit(peach2, (13 * section_width, row6_y - 6 * section_height))
    # drawing oil drum
    oil = draw_oil()
    # drawing stationary barrels
    draw_barrels()
    # drawing donkey kong
    draw_kong()
    return oil


def draw_oil():
    x_coord, y_coord = 4 * section_width, window_height - 4.5 * section_height
    oil = pygame.draw.rect(screen, 'blue', [x_coord, y_coord, 2 * section_width, 2.5 * section_height])
    pygame.draw.rect(screen, 'blue', [x_coord - 0.1 * section_width, y_coord, 2.2 * section_width, .2 * section_height])
    pygame.draw.rect(screen, 'blue',
                     [x_coord - 0.1 * section_width, y_coord + 2.3 * section_height, 2.2 * section_width,
                      .2 * section_height])
    pygame.draw.rect(screen, 'light blue',
                     [x_coord + 0.1 * section_width, y_coord + .2 * section_height, .2 * section_width,
                      2 * section_height])
    pygame.draw.rect(screen, 'light blue',
                     [x_coord, y_coord + 0.5 * section_height, 2 * section_width, .2 * section_height])

    pygame.draw.rect(screen, 'light blue',
                     [x_coord, y_coord + 1.7 * section_height, 2 * section_width, .2 * section_height])
    screen.blit(font2.render('OIL', True, 'light blue'), (x_coord + .4 * section_width, y_coord + 0.7 * section_height))
    for i in range(4):
        pygame.draw.circle(screen, 'red',
                           (x_coord + 0.5 * section_width + i * 0.4 * section_width, y_coord + 2.1 * section_height), 3)
    # draw the flames on top
    if counter < 15 or 30 < counter < 45:
        screen.blit(flames_img, (x_coord, y_coord - section_height))
    else:
        screen.blit(pygame.transform.flip(flames_img, True, False), (x_coord, y_coord - section_height))
    return oil


def draw_barrels():
    screen.blit(pygame.transform.rotate(barrel_side, 90), (section_width * 1.6, 7.3 * section_height))
    screen.blit(pygame.transform.rotate(barrel_side, 90), (section_width * 2.5, 7.3 * section_height))
    screen.blit(pygame.transform.rotate(barrel_side, 90), (section_width * 2.5, 9.4 * section_height))
    screen.blit(pygame.transform.rotate(barrel_side, 90), (section_width * 1.6, 9.4 * section_height))


def draw_kong():
    phase_time = barrel_time // 4
    if barrel_spawn_time - barrel_count > 3 * phase_time:
        dk_img = dk2
    elif barrel_spawn_time - barrel_count > 2 * phase_time:
        dk_img = dk1
    elif barrel_spawn_time - barrel_count > phase_time:
        dk_img = dk3
    else:
        dk_img = pygame.transform.flip(dk1, True, False)
        screen.blit(barrel_img, (250, 220))
    screen.blit(dk_img, (3.5 * section_width, row6_y - 5.5 * section_height))


def check_climb():
    can_climb = False
    climb_down = False
    under = pygame.rect.Rect((player.rect[0], player.rect[1] + 2 * section_height), (player.rect[2], player.rect[3]))
    for lad in lads:
        if player.hitbox.colliderect(lad) and not can_climb:
            can_climb = True
        if under.colliderect(lad):
            climb_down = True
    if (not can_climb and (not climb_down or player.y_velocity < 0)) or \
            (player.on_ground and can_climb and player.y_velocity > 0 and not climb_down):
        player.climbing = False
    return can_climb, climb_down


def barrel_collide(reset):
    global score
    under = pygame.rect.Rect((player.rect[0], player.rect[1] + 2 * section_height), (player.rect[2], player.rect[3]))
    #pygame.draw.rect(screen, 'blue', under) #debuggin
    for brl in barrels:
        if brl.rect.colliderect(player.hitbox):
            reset = True
        elif not player.on_ground and not player.over_barrel and under.colliderect(brl):
            player.over_barrel = True
            score += 500
    if player.on_ground:
        player.over_barrel = False
    return reset


def reset():
    global player, barrels, flames, first_fireball_trigger, victory, bonus
    global barrel_spawn_time, barrel_count
    pygame.time.delay(1000)
    for bar in barrels:
        bar.kill()
    for flam in flames:
        flam.kill()
    bonus = 6000
    player.kill()
    player = Player(250, window_height - 70)
    first_fireball_trigger = False
    barrel_spawn_time = 360
    barrel_count = barrel_spawn_time / 2
    victory = False


def check_victory():
    goal = levels[0]['goal']
    goal_rect = pygame.rect.Rect((goal[0]*section_width, goal[1]), (section_width*goal[2], 1))
    #pygame.draw.rect(screen , 'blue', goal_rect) #for debugging
    return player.bottom.colliderect(goal_rect)


barrels = pygame.sprite.Group()
flames = pygame.sprite.Group()
player = Player(250, window_height - 70)

run = True
while run:
    screen.fill('black')
    timer.tick(fps)
    if counter < 60:
        counter += 1
    else:
        counter = 0
        if bonus > 0:
            bonus -= 100

    # draw platforms and ladders on the screen in dedicated function
    plats, lads = draw_screen()
    oil_drum = draw_extras()
    climb, down = check_climb()
    victory = check_victory()
    if barrel_count < barrel_spawn_time:
        barrel_count += 1
    else:
        barrel_count = random.randint(0, 120)
        barrel_time = barrel_spawn_time - barrel_count
        barrel = Barrel(270, 210)
        barrels.add(barrel)
        if not first_fireball_trigger:
            flame = Flame(5 * section_width, window_height - 4 * section_height)
            flames.add(flame)
            first_fireball_trigger = True
    for barrel in barrels:
        barrel.draw()
        fireball_trigger = barrel.update(fireball_trigger)
        if fireball_trigger:
            flame = Flame(5 * section_width, window_height - 4 * section_height)
            flames.add(flame)
            fireball_trigger = False

    for flame in flames:
        flame.check_climb()
        if flame.rect.colliderect(player.hitbox):
            reset_game = True
    flames.draw(screen)
    flames.update()
    player.update()
    player.draw()

    reset_game = barrel_collide(reset_game)
    if reset_game:
        reset()
        reset_game = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
        # Right movement
            if event.key == pygame.K_d and not player.climbing:
                keys["right"] = True
                player.x_velocity = 1
                player.dir = 1
            
            # Left movement
            if event.key == pygame.K_a and not player.climbing:
                keys["left"] = True
                player.x_velocity = -1
                player.dir = -1

            # Jump
            if event.key == pygame.K_SPACE and player.on_ground:
                player.on_ground = False
                player.y_velocity = -6

            # Climb up
            if event.key == pygame.K_w:
                keys["climb_up"] = True
                if climb:
                    player.y_velocity = -1
                    player.x_velocity = 0
                    player.climbing = True

            # Climb down
            if event.key == pygame.K_s:
                keys["climb_down"] = True
                if down:
                    player.y_velocity = 1
                    player.x_velocity = 0
                    player.climbing = True

        if event.type == pygame.KEYUP:
            # Stop right movement
            if event.key == pygame.K_d:
                keys["right"] = False
                if not keys["left"]:  # Stop only if not pressing left
                    player.x_velocity = 0
                else:
                    player.x_velocity = -1
                    player.dir = -1

            # Stop left movement
            if event.key == pygame.K_a:
                keys["left"] = False
                if not keys["right"]:  # Stop only if not pressing right
                    player.x_velocity = 0
                else:
                    player.x_velocity = 1
                    player.dir = 1

            # Stop climb up
            if event.key == pygame.K_w:
                keys["climb_up"] = False
                if climb:
                    player.y_velocity = 0
                if player.climbing and player.on_ground:
                    player.climbing = False

            # Stop climb down
            if event.key == pygame.K_s:
                keys["climb_down"] = False
                if down:
                    player.y_velocity = 0
                if player.climbing and player.on_ground:
                    player.climbing = False
        if victory:
            screen.fill('black')
            reset_game = True
            score += bonus
            if score > high_score:
                high_score = score
            victory_text = font.render(f'VICTORY! Score: {score}', True, 'white')
            screen.blit(victory_text, (window_width / 2 - victory_text.get_width() / 2, window_height / 2))
            score = 0
            player.climbing = False

    pygame.display.flip()
pygame.quit()