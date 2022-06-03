class Shiritori:
	def __init__(self):
		self.words = []
		self.game_over = False
	
	def play(self,new):
		if self.words==[] or (new[0]==self.words[-1][-1] and new not in self.words):
			self.words.append(new)
			return self.words
		self.game_over = True
		return "game over"
	
	def restart(self):
		self.__init__()
		return "game restarted"


my_shiritori = Shiritori()
print(my_shiritori.game_over)
print(my_shiritori.play("hostess"))
print(my_shiritori.play("stash"))
print(my_shiritori.play("hostess"))


