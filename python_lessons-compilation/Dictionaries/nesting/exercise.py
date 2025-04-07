ammie={'name' :'ammie','age':25, 'complexion':'chocolate'}
jen={'name' :'jenny','age':20, 'complexion':'fair'}
mandy={'name' :'amanda','age':30, 'complexion':'dark'}

people =[ammie,jen,mandy]

for person in people:
    # print(person)
    for k,v in person.items():
        print(f"\n{k} {v}")

fav_places ={
    'jen':['mcdonald','chinos'],
    'sandra':['wallmart','amazon'],
    'dony':['cinema','gamehub','strip club']
}
for name,places in fav_places.items():
    print(f"{name.title()} liks to visit:")
    for place in places:
        print(f"\t{place}  ")

cities ={
    'newyork':{
        'country':'US',
        'population':125,
        'fun_fact':'Newyork city please go easy on me '
    },
    'chicago':{
        'country':'Us',
        'population': 6547,
        'fun_fact':'gun violence'
    },
    'manchester':{
        'country':'UK',
        'population': 4597,
        'fun_fact':'too cold'
    }
}

cities['dallas'] ={
    'country':'US',
    'population':2356,
    'fun_fact':'I love dallas'
}
for city,info in cities.items():
    print(f"The city name:{city.title()}")
    country =f"{info['country']}"
    population=f"{info['population']}"
    fact=f"{info['fun_fact']}"
    print(f"\tcounty its in: {country} population: {population} fact: {fact}")

