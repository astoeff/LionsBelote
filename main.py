from player import Player
from team import Team
from round import Round
from game import Game
from safe_to_txt import *
import json
from round import Round
import copy
def main():
	team1_name = input('Team 1 name: ')
	team2_name = input('Team 2 name: ')

	team1_players=input(team1_name + ' players: ').split(',')
	team2_players=input(team2_name + ' players: ').split(',')
	
	if len(team1_players)!=2 or len(team2_players)!=2:
		raise ValueError

	p1 = Player(name = team1_players[0].replace(' ',''))
	p3 = Player(name = team1_players[1].replace(' ',''))

	p2 = Player(name = team2_players[0].replace(' ',''))
	p4 = Player(name = team2_players[1].replace(' ',''))

	team1 = Team(team1_name,p1,p3)
	team2 = Team(team2_name,p2,p4)
#test
	all_games ={} 
	game = Game(team1,team2)
	with open('results.txt','w') as file:
		pass
	game_number = 1
	game1 = {}
	game2 = {}
	game3 = {}
	while game.team1_wins !=2 and game.team2_wins!=2:
		round_number = 1
		create_file_with_headers(team1,team2)
		is_game_won = False
		while not is_game_won:
				r = game.play_round(round_number)
				if round_number == 1:
					safe_to_txt(team1,team2,first_round = True)
				else:
					safe_to_txt(team1,team2)
				if sum(team1.points)>150 or sum(team2.points)>150 and sum(team1.points) != sum(team2.points):
					is_game_won = True
				r.empty_announcements()
				round_number +=1

		safe_to_txt(team1,team2,last_round = True)
		if sum(team1.points) > sum(team2.points):
			game.team1_wins +=1
			game.last_winner = 'team1'
		elif sum(team1.points)<sum(team2.points):
			game.team2_wins +=1
			game.last_winner = 'team2'
		if game_number ==1:
			game1['game 1'] = copy.deepcopy(game.game_dict)
			all_games.update(game1)
		if game_number == 2:
			game2['game 2'] = copy.deepcopy(game.game_dict)
			all_games.update(game2)
		if game_number == 3:
			game3['game 3'] = copy.deepcopy(game.game_dict)
			all_games.update(game3)
		team1.points = []
		team2.points = []
		game_number += 1
		display_game_points(game.team1_wins,game.team2_wins)

	with open('data.json', 'w') as file:
		json.dump(all_games,file,indent = 4)

	if game.team2_wins > game.team1_wins:
		print(team2_name + ' is the winner!!!')
	else:
		print(team1_name + ' is the winner!!!')

if __name__ == '__main__':
	main()