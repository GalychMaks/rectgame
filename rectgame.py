import pygame, random
from pygame.locals import *

# Initialise screen
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('non Basic Pygame program')

# Fill background
background = pygame.Surface((800, 400)).convert()
background.fill((250, 250, 250))

class Manager():
	def __init__(self):
		self.players = [player1, player2]
		self.i = 0
		self.moving_now = self.players[self.i]

	def next(self):
		self.i += 1
		if self.i == len(self.players):
			self.i = 0
		self.moving_now = self.players[self.i]

	def who_win(self):
		if player1.score > player2.score:
			return player1
		if player2.score > player1.score:
			return player2
		else:
			return 0

	def is_end(self):
		for x in range(0, 400, 20):
			for y in range(0, 400, 20):
				if game_field.posible(mng.moving_now, x, y, game_field.rect_list_tmp[-1].wigth, game_field.rect_list_tmp[-1].height):
					return False
		return True

	def win_protocol(self,):
		f = True
		clock = pygame.time.Clock()
		while f:
			screen_1 = pygame.display.set_mode((600, 300))
			clock.tick(15)
			font = pygame.font.Font(None, 40)
			final_text1 = "My congratulations:"
			final_text2 = f"Won - {self.who_win().name}"
			final_text3 = f"With the score {self.who_win().score}"
			text1 = font.render(final_text1, 1, (100, 10, 100))
			text2 = font.render(final_text2, 1, (100, 10, 100))
			text3 = font.render(final_text3, 1, (100, 10, 100))
			screen_1.blit(text1, (0,0))
			screen_1.blit(text2, (0,100))
			screen_1.blit(text3, (0,200))
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return
			pygame.display.flip()

class Player():
	def __init__(self, name, turpule):
		self.name = name
		self.point_list = [turpule]
		self.my_rect = []
		self.score = 0

	def generate_list(self, rect):
		for x in range(0, rect.wigth, 20):
			self.point_list.append((x+rect.x, rect.y+rect.height))
			self.point_list.append((x+rect.x, rect.y))
		for y in range(0, rect.height, 20):
			self.point_list.append((rect.x+rect.wigth, y+rect.y))
			self.point_list.append((rect.x, y+rect.y))

	def make_move(self):
		rect = Rect()
		game_field.rect_list_tmp.append(rect)

	def make_choise(self):
		for rect in game_field.rect_list_tmp:
			self.my_rect.append(rect)
			self.score += rect.wigth//20*rect.height//20
			game_field.rect_list.append(game_field.rect_list_tmp.pop(0))

class Table():
	def __init__(self):
		self.x = 0
		self.y = 0
		self.table_surface = pygame.Surface((400, 400)).convert()
		self.font = pygame.font.Font(None, 30)
		self.font_small = pygame.font.Font(None, 15)
		self.wight = self.font.render(f"Ширина: {self.x}", 1, (100, 10, 100))
		self.height = self.font.render(f"Висота: {self.y}", 1, (100, 10, 100))
		self.wightpos = self.wight.get_rect()
		self.heightpos = self.height.get_rect()
		self.heightpos.y = self.heightpos.y + self.wightpos.height
		self.table_surface.blit(self.wight, self.wightpos)
		self.table_surface.blit(self.height, self.heightpos)
		self.hint_text1 = "use x to create a rectangele"
		self.hint_text2 = "use arrows to move your rectangele"
		self.hint_text3 = "use c to roll your rectangele"
		self.hint_text4 = "use z to fix your rectangele"
		self.hint1 = self.font_small.render(self.hint_text1, 1, (100, 10, 100))
		self.hint2 = self.font_small.render(self.hint_text2, 1, (100, 10, 100))
		self.hint3 = self.font_small.render(self.hint_text3, 1, (100, 10, 100))
		self.hint4 = self.font_small.render(self.hint_text4, 1, (100, 10, 100))


	def update(self):
		self.x = game_field.rect_list_tmp[-1].wigth//20 if len(game_field.rect_list_tmp)>0 else 0
		self.y = game_field.rect_list_tmp[-1].height//20 if len(game_field.rect_list_tmp)>0 else 0
		self.table_surface = pygame.Surface((400, 400)).convert()
		self.wight = self.font.render(f"wigth: {self.x}", 1, (100, 10, 100))
		self.height = self.font.render(f"height: {self.y}", 1, (100, 10, 100))
		self.moving_now = self.font.render(f"Moving now: {mng.moving_now.name}", 1, (100, 10, 100))
		self.score = self.font.render(f"{player1.name}: {player1.score}   {player2.name}: {player2.score}", 1, (100, 10, 100))
		self.table_surface.blit(self.score, (0, 100))
		self.table_surface.blit(self.moving_now, (0, 200))
		self.table_surface.blit(self.wight, self.wightpos)
		self.table_surface.blit(self.height, self.heightpos)
		self.table_surface.blit(self.hint1, (0, 300))
		self.table_surface.blit(self.hint2, (0, 310))
		self.table_surface.blit(self.hint3, (0, 320))
		self.table_surface.blit(self.hint4, (0, 330))

class Field():
	def __init__(self):
		self.field_surface = pygame.Surface((400,400)).convert()
		self.field_surface.fill((34,53,144))
		self.rect_list = []
		self.rect_list_tmp = []
		self.move_time = True

	def blit_everything(self):
		for rect in player2.my_rect:
			font = pygame.font.Font(None, 20)
			sqr = str((rect.wigth//20)*(rect.height//20))
			squere = font.render(sqr, 1, (100, 10, 100))#text
			surface = pygame.Surface((rect.wigth, rect.height)).convert()
			surface.fill((255, 255, 255))
			squerepos = squere.get_rect()
			surface.blit(squere, squerepos)
			self.field_surface.blit(surface, (rect.x,rect.y))
		for rect in player1.my_rect:
			font = pygame.font.Font(None, 20)
			sqr = str((rect.wigth//20)*(rect.height//20))
			squere = font.render(sqr, 1, (100, 10, 100))#text
			surface = pygame.Surface((rect.wigth, rect.height)).convert()
			surface.fill((0, 0, 0))
			squerepos = squere.get_rect()
			surface.blit(squere, squerepos)
			self.field_surface.blit(surface, (rect.x,rect.y))

	def make_move(self):
		pass

	def update(self):
		self.field_surface = pygame.Surface((400,400)).convert()
		self.field_surface.fill((34,53,144))

	def posible(self, player, x, y, wigth, height):
		if x + wigth > 400 or y + height > 400:
			return False
		for rect in self.rect_list:
			if pygame.Rect(rect.x,rect.y,rect.wigth,rect.height).colliderect(pygame.Rect(x, y, wigth, height)):
				return False
		for coord in player.point_list:
			if coord == (x, y):
				return True
			for g in range(0, wigth, 20):
				if coord == (x + g, y):
					return True
				if coord == (x + g, y+height):
					return True
			for g in range(20, height, 20):
				if coord == (x+wigth, y+g):
					return True
				if coord == (x, y+g):
					return True
		return False

class Rect():
	def __init__(self):
		self.x = 0
		self.y = 0
		self.wigth = random.randint(1, 6)*20
		self.height = random.randint(1, 6)*20

	def roll_90(self):
		self.wigth, self.height = self.height, self.wigth

	def show_yourself(self, player):
		if game_field.posible(player, game_field.rect_list_tmp[-1].x, game_field.rect_list_tmp[-1].y, game_field.rect_list_tmp[-1].wigth, game_field.rect_list_tmp[-1].height):
			pygame.draw.rect(game_field.field_surface, (1, 99, 1), (self.x, self.y, self.wigth, self.height))
		else:
			pygame.draw.rect(game_field.field_surface, (200, 0, 1), (self.x, self.y, self.wigth, self.height))

	def move_left(self):
		self.x -= 20
		if self.x < 0:
			self.x = 400 - self.wigth

	def move_right(self):
		self.x += 20
		if self.x + self.wigth > 400:
			self.x = 0

	def move_up(self):
		self.y -= 20
		if self.y < 0:
			self.y = 400 - self.height

	def move_down(self):
		self.y += 20
		if self.y + self.height > 400:
			self.y = 0

# Game objects
player1 = Player('up-left', (0,0))
player2 = Player('down-right',(400-20,400))
game_table = Table()
game_field = Field()
clock = pygame.time.Clock()
mng = Manager()

def main():
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == KEYDOWN:
            	if event.key == K_x:
            		if game_field.move_time:
            			game_field.move_time = False
            			mng.moving_now.make_move()
            			if mng.is_end():
            				clock.tick(300)
            				mng.win_protocol()
            	if event.key == K_z:
            		if not game_field.move_time:
            			if game_field.posible(mng.moving_now, game_field.rect_list_tmp[-1].x, game_field.rect_list_tmp[-1].y, game_field.rect_list_tmp[-1].wigth, game_field.rect_list_tmp[-1].height):
            				game_field.move_time = True
            				mng.moving_now.make_choise()
            				mng.moving_now.generate_list(game_field.rect_list[-1])
            				mng.next()
            	if len(game_field.rect_list_tmp) > 0:
            		if event.key == K_LEFT:
            			game_field.rect_list_tmp[-1].move_left()
            		if event.key == K_RIGHT:
            			game_field.rect_list_tmp[-1].move_right()
            		if event.key == K_UP:
            			game_field.rect_list_tmp[-1].move_up()
            		if event.key == K_DOWN:
            			game_field.rect_list_tmp[-1].move_down()
            		if event.key == K_c:
            			game_field.rect_list_tmp[-1].roll_90()

        
        game_table.update()
        game_field.update()
        game_field.blit_everything()
        for rect in game_field.rect_list_tmp:
        	rect.show_yourself(mng.moving_now)
        background.blit(game_field.field_surface, (0,0))
        background.blit(game_table.table_surface, (400, 0))
        screen.blit(background, (0, 0))
        pygame.display.flip()
        clock.tick(15)

if __name__ == '__main__': main()
