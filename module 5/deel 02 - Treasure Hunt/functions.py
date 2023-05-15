import time
from termcolor import colored
from data import JOURNEY_IN_DAYS
from data import COST_FOOD_HUMAN_COPPER_PER_DAY
from data import COST_FOOD_HORSE_COPPER_PER_DAY

##################### M04.D02.O2 #####################

def copper2silver(amount:int) -> float:
    return amount / 10
    

def silver2gold(amount:int) -> float:
    return amount / 5

def copper2gold(amount:int) -> float:
    return amount / 50

def platinum2gold(amount:int) -> float:
    return amount * 25

def getPersonCashInGold(personCash:dict) -> float:
    gold = silver2gold(personCash.get('silver')) + copper2gold(personCash.get('copper')) + platinum2gold(personCash.get('platinum'))
    gold += personCash.get('gold')
    return gold

##################### M04.D02.O4 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
   

    people = copper2gold(COST_FOOD_HUMAN_COPPER_PER_DAY * people) * JOURNEY_IN_DAYS
    horses = copper2gold(COST_FOOD_HORSE_COPPER_PER_DAY * horses) * JOURNEY_IN_DAYS
    return round(people + horses,2)

    

##################### M04.D02.O5 #####################

#looped door de lijst genaamd friends en voegt de keys en value's toe daarna voegt hij ze toe aan een lege lijst.
def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    lijst = [] 
    
    for item in range (len(list)):
        if list [item][key] == value:
            lijst.append(list[item])
    return lijst


#als de keys in de lijst people(friends) van adventuring op true staan, dan worden die geselecteerd
def getAdventuringPeople(people:list) -> list:
   return getFromListByKeyIs(people, 'adventuring', True) 


#als de keys in de lijst friends van shareWith op true staan, dan worden die geselecteerd
def getShareWithFriends(friends:list) -> int:
   return getFromListByKeyIs(friends, 'shareWith', True)

#er wordt door de lijst friends gelooped en als adventuring en shareWith op true staan worden die aan de lijst toegevoegd.
def getAdventuringFriends(friends:list) -> list:
   lijst = []

   for vrienden in range(len(friends)):
       if friends[vrienden]['adventuring'] and friends[vrienden]['shareWith'] == True:
           lijst.append(vrienden)
           return lijst
       
    

##################### M04.D02.O6 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    pass

def getNumberOfTentsNeeded(people:int) -> int:
    pass

def getTotalRentalCost(horses:int, tents:int) -> float:
    pass

##################### M04.D02.O7 #####################

def getItemsAsText(items:list) -> str:
    pass

def getItemsValueInGold(items:list) -> float:
    pass

##################### M04.D02.O8 #####################

def getCashInGoldFromPeople(people:list) -> float:
    pass

##################### M04.D02.O9 #####################

def getInterestingInvestors(investors:list) -> list:
    pass

def getAdventuringInvestors(investors:list) -> list:
    pass

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    pass

##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    pass

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    pass

##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    pass

##################### M04.D02.O13 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

##################### view functions #####################
def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()