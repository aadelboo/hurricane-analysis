# names of hurricanes
names = [
    'Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II',
    'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet',
    'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen',
    'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina',
    'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael'
]

# months of hurricanes
months = [
    'October', 'September', 'September', 'November', 'August', 'September',
    'September', 'September', 'September', 'September', 'September', 'October',
    'September', 'August', 'September', 'September', 'August', 'August',
    'September', 'September', 'August', 'October', 'September', 'September',
    'July', 'August', 'September', 'October', 'August', 'September', 'October',
    'September', 'September', 'October'
]

# years of hurricanes
years = [
    1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961,
    1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004,
    2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018
]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [
    165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160,
    175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175,
    165, 180, 175, 160
]

# areas affected by each hurricane
areas_affected = [
    ['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
    ['Lesser Antilles', 'The Bahamas', 'United States East Coast','Atlantic Canada'
    ], ['The Bahamas', 'Northeastern United States'],
    [
        'Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas',
        'Bermuda'
    ], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'],
    ['Jamaica', 'Yucatn Peninsula'],
    ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'],
    [
        'Southeastern United States', 'Northeastern United States',
        'Southwestern Quebec'
    ], ['Bermuda', 'New England', 'Atlantic Canada'],
    ['Lesser Antilles', 'Central America'],
    ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'],
    ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'],
    ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'],
    ['Mexico'], ['The Caribbean', 'United States East coast'],
    ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'],
    ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'],
    ['The Caribbean', 'United States East Coast'],
    ['The Bahamas', 'Florida', 'United States Gulf Coast'],
    ['Central America', 'Yucatn Peninsula', 'South Florida'],
    ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'],
    ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
    ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'],
    ['Bahamas', 'United States Gulf Coast'],
    ['Cuba', 'United States Gulf Coast'],
    ['Greater Antilles', 'Central America', 'Florida'],
    ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'],
    [
        'Antilles', 'Venezuela', 'Colombia', 'United States East Coast',
        'Atlantic Canada'
    ],
    [
        'Cape Verde', 'The Caribbean', 'British Virgin Islands',
        'U.S. Virgin Islands', 'Cuba', 'Florida'
    ],
    [
        'Lesser Antilles', 'Virgin Islands', 'Puerto Rico',
        'Dominican Republic', 'Turks and Caicos Islands'
    ],
    [
        'Central America',
        'United States Gulf Coast (especially Florida Panhandle)'
    ]
]

# damages (USD($)) of hurricanes
damages = [
    'Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M',
    '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M',
    '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B',
    '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B',
    '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B'
]

# deaths for each hurricane
deaths = [
    90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11,
    2068, 269, 318, 107, 65, 19325, 51, 124, 17, 1836, 125, 87, 45, 133, 603,
    138, 3057, 74
]

# 1
# Update Recorded Damages
conversion = {"M": 1000000, "B": 1000000000}

# create function by updating damages
damage_updated = []
def update_damages(damage):
    for damage in damages:
        if damage[-1] == 'M':
            damage_updated.append(float(damage[0:-1]) * conversion["M"])
        if damage[-1] == "B":
            damage_updated.append(float(damage[0:-1]) * conversion["B"])
        if damage == "Damages not recorded":
            damage_updated.append(damage)
    return damage_updated

damage_updated = update_damages(damages)
#print(damage_updated)



# 2
# Create a functon that constructs a dictionary  from the lists
def construct_hurricane_dict(names, months, years, max_sustained_winds,
                             areas_affected, damage_updated, deaths):
    hurricanes = {}
    for i in range(len(names)):
        hurricanes[names[i]] = {"Name": names[i],
                                "Month": months[i],
                                "Year": years[i],
                                "Max Sustained Wind": max_sustained_winds[i],
                                "Area Affected": areas_affected[i],
                                "Damage Updated": damage_updated[i],
                                "Deaths": deaths[i]
                                }
    return hurricanes

# Call the function and display the result
hurricanes = construct_hurricane_dict(names, months, years, max_sustained_winds,
                             areas_affected, damage_updated, deaths)
#print(hurricanes["Camille"]["Year"])


# 3
# Organizing by Year
hurricane_year = {}
def hurricane_by_year(hurricanes):
    for i in hurricanes:
        current_year = hurricanes[i]["Year"]
        current_cane = hurricanes[i]
        if current_year not in hurricane_year:
            hurricane_year[current_year] = [current_cane]
        else:
            hurricane_year[current_year].append(current_cane)
    return hurricane_year

# create a new dictionary of hurricanes with year and key
hurricane_year = hurricane_by_year(hurricanes)
#print(hurricane_year[1932])


# 4
# Counting Damaged Areas
def count_areas_affected(hurricanes):
    affected_areas_count = {}
    for cane in hurricanes:
        for area in hurricanes[cane]["Area Affected"]:
            if area not in affected_areas_count:
                affected_areas_count[area] = 1
            else:
                affected_areas_count[area] += 1
    return affected_areas_count

# create dictionary of areas to store the number of hurricanes involved in
affected_areas_count = count_areas_affected(hurricanes)
##print(affected_areas_count)


# 5
# Calculating Maximum Hurricane Count
def most_affected_area(affected_areas_count):
    max_area = 'Central America'
    max_area_count = 0
    for area in affected_areas_count:
        if affected_areas_count[area] > max_area_count:
            max_area = area
            max_area_count = affected_areas_count[area]
    return max_area, max_area_count

# find most frequently affected area and the number of hurricanes involved in
max_area, max_area_count = most_affected_area(affected_areas_count)
#print(f"The most area affected is {max_area}, and have been affected {max_area_count} times.")


# 6
# Calculating the Deadliest Hurricane
def most_death(hurricanes):
    max_mortality_cane = "Cane I"
    max_mortality = 0
    for cane in hurricanes:
        if hurricanes[cane]["Deaths"] > max_mortality:
            max_mortality_cane = cane
            max_mortality = hurricanes[cane]["Deaths"]
    return max_mortality, max_mortality_cane

# find highest mortality hurricane and the number of deaths
max_mortality, max_mortality_cane = most_death(hurricanes)
#print(max_mortality, max_mortality_cane)

# 7
# Rating Hurricanes by Mortality

def rate_mortality(hurricanes):
    mortality_scale = {0: 0,
                      1: 100,
                      2: 500,
                      3: 1000,
                      4: 10000}
    hurricanes_by_mortality = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for cane in hurricanes:
        num_death = hurricanes[cane]["Deaths"]
        if num_death == mortality_scale[0]:
            hurricanes_by_mortality[0].append(hurricanes[cane]["Name"])
        elif num_death > mortality_scale[0] and num_death <= mortality_scale[1]:
            hurricanes_by_mortality[1].append(hurricanes[cane]["Name"])
        elif num_death > mortality_scale[1] and num_death <= mortality_scale[2]:
            hurricanes_by_mortality[2].append(hurricanes[cane]["Name"])
        elif num_death > mortality_scale[2] and num_death <= mortality_scale[3]:
            hurricanes_by_mortality[3].append(hurricanes[cane]["Name"])
        elif num_death > mortality_scale[3] and num_death <= mortality_scale[4]:
            hurricanes_by_mortality[4].append(hurricanes[cane]["Name"])
        else:
            hurricanes_by_mortality[5].append(hurricanes[cane]["Name"])
    return hurricanes_by_mortality

# categorize hurricanes in new dictionary with mortality severity as key
hurricane_by_mortality = rate_mortality(hurricanes)
print(hurricane_by_mortality[4])

# 8 Calculating Hurricane Maximum Damage

# find highest damage inducing hurricane and its total cost

# 9
# Rating Hurricanes by Damage
damage_scale = {
    0: 0,
    1: 100000000,
    2: 1000000000,
    3: 10000000000,
    4: 50000000000
}

# categorize hurricanes in new dictionary with damage severity as key
