# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[], my_history = [], 
          play_order=[{
              "RR": 0,
              "RP": 0,
              "RS": 0,
              "PR": 0,
              "PP": 0,
              "PS": 0,
              "SR": 0,
              "SP": 0,
              "SS": 0,
          }]):
   
    #We clear each 1000
    if len(opponent_history) % 1001 == 1000:
        opponent_history.clear()
        my_history.clear()

    opponent_history.append(prev_play)

    #First three plays are PRP
    guess = "P"
    if len(opponent_history)== 1:
        guess = "R"
    if len(opponent_history) == 2:
        guess = "P"

    #We discover against which opponent we are playing
    first_three_plays = ''.join(opponent_history[1:4])

    opponent = ''
    if first_three_plays == "RPP":
        opponent = "Quincy"

    if first_three_plays == "PPP":
        opponent = "Abbey"
        

    if first_three_plays == "PPS":
        opponent = "Kris"

    if first_three_plays == "RRR":
        opponent = "Mrgesh"

    #We play against each opponent
    if opponent == "Quincy":
        choices = ["P", "P", "S", "S", "R"]
        guess = choices[(len(opponent_history)) % len(choices)]

    
    if opponent == "Abbey":
        last_two = "".join(my_history[-2:])
        if len(last_two) == 2:
            play_order[0][last_two] += 1

        potential_plays = [
            my_history[-1] + "R",
            my_history[-1] + "P",
            my_history[-1] + "S",
        ]

        sub_order = {
            k: play_order[0][k]
            for k in potential_plays if k in play_order[0]
        }

        prediction_opp = max(sub_order, key=sub_order.get)[-1:]

        ideal_response = {'P': 'R', 'R': 'S', 'S': 'P'}
        guess = ideal_response[prediction_opp]

        
        #Fris
    if opponent== "Kris":
        ideal_response = {'P': 'R', 'R': 'S', 'S': 'P'}
        guess = ideal_response[my_history[-1]]

    if opponent == "Mrgesh":
        my_last_ten = my_history[-10:]
        my_most_frequent = max(set(my_last_ten), key=my_last_ten.count)
        ideal_response = {'P': 'R', 'R': 'S', 'S': 'P'}
        guess = ideal_response[my_most_frequent]
        
    #Update my history
    my_history.append(guess)
    return guess
