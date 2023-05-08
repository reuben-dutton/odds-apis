import json


with open("data.json", 'r') as j:
    odds = json.load(j)

for game in odds:

    gameOdds = dict()

    for bookmaker in game['bookmakers']:
        bookmakername = bookmaker['title']
        for outcome in bookmaker['markets'][0]['outcomes']:
            name, outcomeOdds = outcome['name'], outcome['price']
            gameOdds[name] = gameOdds.get(name, []) + [{'bookmaker': bookmakername, 'odds': outcomeOdds}]

    bestOddsGiven = dict()

    for outcome, outcomeOdds in gameOdds.items():
        bestOdds = max([givenOdds['odds'] for givenOdds in outcomeOdds])
        bestBookmakers = [givenOdds for givenOdds in outcomeOdds if givenOdds['odds'] == bestOdds]
        bestOddsGiven[outcome] = bestBookmakers
    
    total = 0
    for outcome, bestBookmakers in bestOddsGiven.items():
        bestOdds = bestBookmakers[0]['odds']
        total += 1 / bestOdds
    
    if total > 0 and total < 1:
        print(game['sport_title'])
        print(total, bestOddsGiven)
