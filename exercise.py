print(
"""
Sports Table Programme
1. Add Teams
2. Add Result
3. Search Team
4. Print Table
5. Exit
"""
)
def header():
    print("Team             Played      Won     Loss    Draw    Points")
    
def line_break():
    print("-----------------------------------------------------------")

def generate_spacing(x, total_spacing=17):
    taken_spacing = len(x)
    avail_spacing = total_spacing - taken_spacing
    avail_spacing_str = " " * avail_spacing
    return avail_spacing_str
    #return an int value

dict = {}

while True:
    #dict.update({"filler": [0, 0, 0, 0, 0]})
    
    action = input("Please enter your choice >")
    #1. Add Teams
    if (action == "1"):
        name_team = input("Enter name of team >")
        dict.update({name_team: [0, 0, 0, 0, 0]})
    elif (action == "2"):
        match_score = input("Please enter the result >")
        
        #get team info
        word = match_score.split()
        first_team = word[0]
        second_team = word[2]
        
        #check case exception
        if first_team not in list(dict) or second_team not in list(dict):
            print("Invalid result entry")
            continue
            
            
        #print("first_team :", first_team)
        #print("second_team :", second_team)
        
        #push played count data
        first_team_played = dict[first_team][0] + 1
        second_team_played = dict[second_team][0] + 1
        #print("first_team_played :", first_team_played)
        #print("second_team_played :", second_team_played)
        
        #push win data
        first_team_score = word[1][0]
        second_team_score = word[1][2]
        #print("first_team_score :", first_team_score)
        #print("second_team_score :", second_team_score)
        
        if (first_team_score > second_team_score):
            #winning team data
            first_team_wins = dict[first_team][1] + 1
            second_team_wins = dict[second_team][1]
            
            #losing team data
            first_team_lost = dict[first_team][2] 
            second_team_lost = dict[second_team][2] + 1
            
            #draw team data
            first_team_draw = dict[first_team][3]
            second_team_draw = dict[second_team][3]
            
            #point system data
            first_team_points = dict[first_team][4] + 3
            second_team_points = dict[second_team][4]
            
        elif (first_team_score < second_team_score):
            #winning team data
            first_team_wins = dict[first_team][1]
            second_team_wins = dict[second_team][1] + 1
            
            #losing team data
            first_team_lost = dict[first_team][2] + 1
            second_team_lost = dict[second_team][2]
            
            #draw team data
            first_team_draw = dict[first_team][3]
            second_team_draw = dict[second_team][3]
            
            #point system data
            first_team_points = dict[first_team][4] + 3
            second_team_points = dict[second_team][4] + 3
            
        else:
            #winning team data
            first_team_wins = dict[first_team][1]
            second_team_wins = dict[second_team][1]
            
            #losing team data
            first_team_lost = dict[first_team][2]
            second_team_lost = dict[second_team][2]
            
            #draw team data
            first_team_draw = dict[first_team][3] + 1
            second_team_draw = dict[second_team][3] + 1
            
            #point system data
            first_team_points = dict[first_team][4]
            second_team_points = dict[second_team][4]
    
        #push final formatted data into dict
        dict.update({first_team: [first_team_played, first_team_wins, first_team_lost, first_team_draw, first_team_points]})
        dict.update({second_team: [second_team_played, second_team_wins, second_team_lost, second_team_draw, second_team_points]})
    
    elif (action == "3"):
        keys = []
        
        for key in dict:
            keys.append(key)
        for i in range(len(dict)):
            print(i+1,". ",keys[i],end="\n", sep="")
        count = int(input("Please enter team to search >"))
        
        search_team = keys[count-1]
        
        header()
        line_break()
        
        #call predefined functions to format answer
        x = search_team
        avail_spacing_str = generate_spacing(x)
        
        #spacings- 11, 7, 7, 7
        
        print(search_team,avail_spacing_str, dict[search_team][0],"           ", dict[search_team][1], "       ", dict[search_team][2], "       ", dict[search_team][3], "       ", dict[search_team][4],end="\n",sep="")
        line_break()
        
    elif (action == "4"):
        header()
        line_break()
        
        keys = []
        
        for i in range(len(dict)):
            for key in dict:
                keys.append(key)
                
            key_current = keys[i]
            
            #call predefined functions to format answer
            x = key_current
            avail_spacing_str = generate_spacing(x)
        
            print(key_current ,avail_spacing_str, dict[key_current][0],"           ", dict[key_current][1], "       ", dict[key_current][2], "       ", dict[key_current][3], "       ", dict[key_current][4],end="\n",sep="")
            #print("\n")

        line_break()
    
    elif (action == "5"):
        quit()
    
    else:
        print("Invalid result entry")
