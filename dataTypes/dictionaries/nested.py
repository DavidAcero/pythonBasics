tournaments = {
    "AO Open":{
        "surface": "Hard",
        "place" : "Melbourne"
    },
    "Roland Garros" :{
        "surface": "Clay", 
        "place" : "Paris"
    },
    "Wimbledon": {
        "surface": "Grass", 
        "place": "London"
    },
    "US Open": {
        "surface": "Hard", 
        "place": "New York"
    }
}

# Another way 
ao = {
        "surface": "Hard",
        "place" : "Melbourne"
    }
rg = {
        "surface": "Clay", 
        "place" : "Paris"
    }
wb = {
        "surface": "Grass", 
        "place": "London"
    }
uo = {
        "surface": "Hard", 
        "place": "New York"
    }

otherTournaments = {
    "AO Open" : ao, 
    "Roland Garros" : rg, 
    "Wimbledon": wb,
    "US Open" : uo
}
print(tournaments)
print(otherTournaments)
print("=" * 20)
print(tournaments["AO Open"])
print(tournaments["Wimbledon"]["surface"])