import csv

def read_nba_standings(file_name):
    eastern_05 = []
    
    with open(file_name, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  
        #定義資料
        for row in reader:
            if len(row)==" ":
                break
            else:
                conference = row[0]
                team = row[1]
                win_loss_pct = float(row[3])
                home_record = row[7]
                home_record=home_record.split("-")
                home_win=int(home_record[0])/(int(home_record[0])+int(home_record[1]))
                away_record = row[8]
                away_record=away_record.split("-")
                away_win=int(away_record[0])/(int(away_record[0])+int(away_record[1]))
                points_for = float(row[5])
                points_against = float(row[6])
            
            if conference == 'Eastern' and home_win<away_win:
                eastern_05.append(team)
    return eastern_05

def calculate_pf_pa(file_name):
    eastern_05 = []
    
    with open(file_name, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        i=[]
        j=[]
        #定義資料
        for row in reader:
            conference = row[0]
            team = row[1]
            win_loss_pct = float(row[3])
            home_record = row[7]
            home_record=home_record.split("-")
            home_win=int(home_record[0])/(int(home_record[0])+int(home_record[1]))
            away_record = row[8]
            away_record=away_record.split("-")
            away_win=int(away_record[0])/(int(away_record[0])+int(away_record[1]))
            points_for = float(row[5])
            points_against = float(row[6])
            pf_pa=points_for-points_against
            
            if conference=="Eastern":
                i+=pf_pa
            if conference=="Western":
                j+pf_pa
    if sum(i)>sum(j):
        return "Eastern"
    else:
        return "Western"                
            
            

    
#勝率
def calculate_win_rate(record):
    record=record.split('-')
    wins, losses = int(record[0]),int(record[1])
    total_games = wins + losses
    return wins / total_games



file_name = 'pe8_data.csv'
eastern_05= read_nba_standings(file_name)
mpf_pa=calculate_pf_pa(file_name)#pf-pa更高的conference
print("(1) Eastern Conference had the win-loss percentage of Home lower than the win-loss percentage of Away")
for team in eastern_05:
    print(team)

print("\n(2)The conference had a higher average difference about PF minus PA:")
print(mpf_pa)


