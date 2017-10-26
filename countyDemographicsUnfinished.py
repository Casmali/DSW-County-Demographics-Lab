import json

def main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    print(alphabetically_first_county(counties))
    print(county_most_under_18(counties))
    print(percent_most_under_18(counties))
    print(most_under_18(counties))
    print(state_with_most_counties(counties))
    print(your_interesting_demographic_function(counties))

def alphabetically_first_county(counties):
    ret = counties[0]["County"]
    for x in counties:
        if x["County"] < ret:
            ret = x["County"]
    return ret

    """Return the county with the name that comes first alphabetically."""


def county_most_under_18(counties):
    ret = counties[0]
    for x in counties:
        if x["Age"]["Percent Under 18 Years"] > ret["Age"]["Percent Under 18 Years"]:
            ret = x
    return ret["County"] +","+ ret["State"]
    """Return the name and state of a county ("<county name>, <state>") with the highest percent of under 18 year olds."""

    
def percent_most_under_18(counties):
    ret = counties[0]["Age"]["Percent Under 18 Years"]
    for x in counties:
        if x["Age"]["Percent Under 18 Years"] > ret:
            ret = x["Age"]["Percent Under 18 Years"]
    return ret
    """Return the highest percent of under 18 year olds."""

    
def most_under_18(counties):
    res = counties[0]
    for x in counties:
        if x["Age"]["Percent Under 18 Years"] > res["Age"]["Percent Under 18 Years"]:
            res = x
    w = res["County"] +","+ res["State"]
    return [w,res["Age"]["Percent Under 18 Years"]]
    """Return a list with the name and state of a county ("<county name>, <state>") and the percent of under 18 year olds for a county with the highest percent of under 18 year olds."""

    
def state_with_most_counties(counties):
    dict = {"AL":0}
    for x in counties:
        if x["State"] in dict:
            dict[x["State"]] += 1
        else:
            dict[x["State"]] = 1
    retNum = 0
    retName = ""
    for x in dict:
        if dict[x] > retNum:
            retNum = dict[x]
            retName = x
    return retName
    """Return a state that has the most counties."""
    #Make a dictionary that has a key for each state and the values keep track of the number of counties in each state
    
    #Find the state in the dictionary with the most counties
    
    #Return the state with the most counties
    
    
def your_interesting_demographic_function(counties):
    ret = counties[0]
    for x in counties:
        if x["Education"]["Bachelor's Degree or Higher"] > ret["Education"]["Bachelor's Degree or Higher"]:
            ret = x
    return [ret["County"],ret["State"]]
    """Compute and return an interesting fact using the demographic data about the counties in the US."""

if __name__ == '__main__':
    main()
