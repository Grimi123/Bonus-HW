	def read_nba_standings(file_name):
		east_home_lower_than_away = []
		average_east_difference_PF_PA = 0
		count_east_for_average = 0
		average_west_difference_PF_PA = 0
		count_west_for_average = 0

		east_teams = {}
	    west_teams = {}

		with open(file_name,"r") as file:
			whole = file_name.readlines()

			for line in whole:
				line = line.strip()
				line = line.split(",")
				Conference,Team,W-L,PCT,GB,PF,PA,HOME,AWAY,CONF,DIV,L10,STRK = line[0:13]
				wins_against_other_conference = int(line[-5].split('-')[0])

	            

				if Conference == "Eastern" and float(home.split('-')[0])/(float(home.split('-')[0])+float(home.split('-')[1])) < float(away.split('-')[0])/((float(away.split('-')[0])+float(away.split('-')[1]))):  
					east_home_lower_than_away.append(Team)

				if Conference == "Eastern":
					average_east_difference_PF_PA += int(PF) - int(PA)
					count_east_for_average += 1
				if Conference == "Western":
					average_west_difference_PF_PA += int(PF) - int(PA)
					count_west_for_average += 1

				if conference == 'Eastern':
	                east_teams[team] = wins_against_other_conference
	            elif conference == 'Western':
	                west_teams[team] = wins_against_other_conference


		average_east_difference_PF_PA /= count_east_for_average
		average_west_difference_PF_PA /= count_west_for_average

		return east_home_lower_than_away,average_east_difference_PF_PA,average_west_difference_PF_PA,east_teams, west_teams

	def generate_ranking_list(east_teams, west_teams):
	    ranking_list = sorted(east_teams.keys(), key=lambda x: west_teams.get(x, 0), reverse=True)
	    ranking_list.extend(sorted(west_teams.keys(), key=lambda x: east_teams.get(x, 0), reverse=True))

	    return generate_ranking_list

	file_name = "pe8_data.csv"
	east_home_lower_than_away,average_east_difference_PF_PA,average_west_difference_PF_PA,east_teams, west_teams = read_nba_standings(file_name)
	ranking_list = generate_ranking_list(east_teams, west_teams)

	print("east_home_lower_than_away,average_east_difference_PF_PA,average_west_difference_PF_PA")
	print(east_home_lower_than_away)

	print("(2) Which conference had a higher average difference about “PF minus PA")
	if average_east_difference_PF_PA > average_west_difference_PF_PA:
		print(average_east_difference_PF_PA)
	else:
		print(average_west_difference_PF_PA)






