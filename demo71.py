class Team:
    name = 'Normal Team'
    member = 100

team1 = Team()
print team1.name
team1.name = 'R&D Team'
team2 = Team()
print team1.name, team2.name, Team.name
del team1.name
print team1.name, team2.name, Team.name
print team1.member , team2.member
team1.member = 9
team2.member = 999
print team1.name, team1.member,team2.member

