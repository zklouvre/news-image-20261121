# Story data for The Daily Globe — Saturday 21 November 2026.
# Every story below happened, or was first reported, on 21 November 2026
# in at least one time zone. Sources were checked live on 21 Nov 2026
# (Al Jazeera live feed, Reuters, BBC, NDTV, White House briefing,
# IGP/GFZ seismology, UN, EU, US court reporting).
# Tags: CONFIRMED = verified by a primary source or wire;
#       REPORTED = reported by a named outlet, not yet independently verified;
#       CLAIM    = one party's claim, unverified.
# Fields (17): War, Diplomacy, Disaster, Politics, Climate, Law, Tech,
# Sport, Markets, Crime, Society, Aid, Health, Refugees, Environment,
# Media, Science. Regions (7): North America, South America, Europe,
# Africa, Middle East, Asia, Oceania.

LEADS = [
    {
        "n": 1, "field": "War", "region": "Middle East",
        "kicker": "THE GULF WAR",
        "headline": "Gulf war widens: coalition downs Houthi missiles; Iran's tankers mass at Kharg",
        "body": ("The Saudi-led coalition says it downed Houthi missiles "
                 "overnight; Iran's Guard claims a US MQ-9 drone downed over "
                 "the Strait of Hormuz. Satellite data show 14+ Iranian "
                 "tankers massing at Kharg Island to test a US blockade."),
        "chip": "CONFIRMED", "source": "Al Jazeera live, 21 Nov 00:00 UTC",
        "pin": (26.5, 56.5), "art": "gulf",
    },
    {
        "n": 2, "field": "Diplomacy", "region": "North America",
        "kicker": "TRUMP, BACK FROM ASIA",
        "headline": "Xi agrees to three-way nuclear talks; Quad to meet on business",
        "body": ("At a White House briefing after his Asia tour, Trump said Xi "
                 "agreed in Shenzhen to three-way nuclear-risk talks with the US "
                 "and Russia, and that humans must stay in charge of military "
                 "AI. Rubio confirmed a Quad business forum for early 2027."),
        "chip": "CONFIRMED", "source": "White House briefing, reported 21 Nov",
        "pin": (38.9, -77.0), "art": "summit",
    },
    {
        "n": 3, "field": "Disaster", "region": "South America",
        "kicker": "EARTHQUAKE",
        "headline": "M6.8 quake shakes Peru, felt in Lima",
        "body": ("A magnitude 6.8 earthquake struck the Junin region at 00:09 "
                 "UTC, about 118 km deep; tremors were felt 320 km away in "
                 "Lima, where residents rushed into the streets. Peru's "
                 "geophysics institute put the magnitude at 6.7."),
        "chip": "CONFIRMED", "source": "Reuters / GFZ / IGP, 21 Nov",
        "pin": (-11.0, -76.0), "art": "quake",
    },
]

SMALL = [
    {"n": 4, "field": "Politics", "region": "Europe",
     "headline": "Gen Z protests sweep 25 European countries",
     "chip": "REPORTED", "source": "Al Jazeera, 02:49 UTC", "pin": (50.8, 4.35)},
    {"n": 5, "field": "Climate", "region": "Europe",
     "headline": "COP31 in Antalya: deal stalls; draft drops fossil fuels",
     "chip": "CONFIRMED", "source": "Al Jazeera, 01:44 UTC", "pin": (36.9, 30.7)},
    {"n": 6, "field": "Law", "region": "Europe",
     "headline": "Denmark expels diplomat over 'plot to kill rapper'",
     "chip": "REPORTED", "source": "Al Jazeera, 01:12 UTC", "pin": (55.7, 12.6)},
    {"n": 7, "field": "Tech", "region": "North America",
     "headline": "Trump calls for Nvidia to reinstate 'brilliant' Jensen Huang",
     "chip": "CONFIRMED", "source": "Al Jazeera, 01:49 UTC", "pin": (37.4, -121.9)},
    {"n": 8, "field": "Sport", "region": "Oceania",
     "headline": "KL Rahul completes the SENA set; India 371/2 vs NZ 368",
     "chip": "CONFIRMED", "source": "NDTV, 03:37 UTC", "pin": (-41.3, 174.8)},
    {"n": 9, "field": "Markets", "region": "Asia",
     "headline": "Record \u20b91.22 lakh crore flows into Indian shares",
     "chip": "CONFIRMED", "source": "Depository data, 21 Nov", "pin": (28.6, 77.2)},
    {"n": 10, "field": "War", "region": "Middle East",
     "headline": "Israeli drone attacks kill seven Palestinians in central Gaza",
     "chip": "REPORTED", "source": "Al Jazeera, 21 Nov", "pin": (31.5, 34.45)},
    {"n": 11, "field": "War", "region": "North America",
     "headline": "Two Salvadoran soldiers killed in Haiti while handling explosives",
     "chip": "REPORTED", "source": "Al Jazeera, 21 Nov", "pin": (18.5, -72.3)},
    {"n": 12, "field": "Science", "region": "North America",
     "headline": "US declassifies more UFO footage filmed in the Middle East",
     "chip": "REPORTED", "source": "BBC, 21 Nov", "pin": (33.3, 44.4)},
    {"n": 13, "field": "Law", "region": "Europe",
     "headline": "French police sentenced over beating of Michel Zecler",
     "chip": "CONFIRMED", "source": "BBC, 21 Nov", "pin": (48.85, 2.35)},
    {"n": 14, "field": "Crime", "region": "North America",
     "headline": "Nikhil Gupta jailed 19+ years in US over plot to kill Sikh leader",
     "chip": "CONFIRMED", "source": "US court, 21 Nov", "pin": (40.7, -74.0)},
    {"n": 15, "field": "Sport", "region": "Oceania",
     "headline": "Ashes day one: Starc 7/58 as England fall for 172; Australia 123/9",
     "chip": "REPORTED", "source": "Glance, 21 Nov", "pin": (-31.95, 115.85)},
]

NUMBERED = [
    (16, "Iraq PM targets militia stronghold", "REPORTED", "Al Jazeera", "Politics", "Middle East"),
    (17, "US lawmakers push tougher AI chip rules", "REPORTED", "Al Jazeera", "Tech", "North America"),
    (18, "Rahul Gandhi backs strong India-Israel ties", "REPORTED", "Al Jazeera", "Diplomacy", "Asia"),
    (19, "Boat capsizes in Nigeria, 4 mourners dead", "REPORTED", "Al Jazeera", "Disaster", "Africa"),
    (20, "Gaza's displaced children mark Children's Day", "REPORTED", "Al Jazeera", "Society", "Middle East"),
    (21, "Estonia to close crossings with Russia", "REPORTED", "EU feed", "Politics", "Europe"),
    (22, "Czechia mulls faster air-defence build-up", "REPORTED", "EU feed", "Politics", "Europe"),
    (23, "HIMARS strike kills 20 Russian commanders", "CLAIM", "Kyiv claim", "War", "Europe"),
    (24, "Ukraine says it hit 3 Russian missile launchers", "CLAIM", "Kyiv claim", "War", "Europe"),
    (25, "Putin rules out energy, Black Sea ceasefire", "CONFIRMED", "Kremlin", "War", "Europe"),
    (26, "Germany's defence chief open to Kremlin talks", "REPORTED", "Berlin", "Diplomacy", "Europe"),
    (27, "Russia attacks after Putin vows 'harsh' offensive", "REPORTED", "Moscow", "War", "Europe"),
    (28, "Russia unveils first memorial at a kindergarten", "REPORTED", "Moscow", "Society", "Europe"),
    (29, "California subpoenas Nvidia on China chips", "CLAIM", "Investors", "Tech", "North America"),
    (30, "Taiwan: China-linked accounts target elections", "REPORTED", "Taipei", "Tech", "Asia"),
    (31, "US limits military ties with Canada", "REPORTED", "Washington", "Diplomacy", "North America"),
    (32, "Amnesty: Spanish police 'excessive' at strike", "REPORTED", "Madrid", "Law", "Europe"),
    (33, "Italian streets fill in protest against Meloni", "REPORTED", "Rome", "Politics", "Europe"),
    (34, "Lula boosts Indigenous land protection", "CONFIRMED", "Brasilia", "Environment", "South America"),
    (35, "Ukraine to give large food aid to nine nations", "REPORTED", "Kyiv", "Aid", "Europe"),
    (36, "UN: Hodeidah attacks threaten aid lifeline", "CONFIRMED", "UN", "Aid", "Middle East"),
    (37, "Saudi warnings in Jazan and Najran", "REPORTED", "Riyadh", "Disaster", "Middle East"),
    (38, "EU pays out record ~\u20ac8bn to Ukraine", "CONFIRMED", "Brussels", "Aid", "Europe"),
    (39, "Ebola in Congo: 100 schools affected", "REPORTED", "DRC health", "Health", "Africa"),
    (40, "Rohingya in Cox's Bazar welcome ICJ verdict", "REPORTED", "Cox's Bazar", "Refugees", "Asia"),
    (41, "China seeks 'all-encompassing' Rohingya deal", "REPORTED", "Beijing", "Diplomacy", "Asia"),
    (42, "US Army delays Iowa blasting over safety fears", "REPORTED", "Iowa", "Society", "North America"),
    (43, "Media told to hand in phones on Air Force One", "REPORTED", "Beijing", "Media", "Asia"),
    (44, "Philippines to buy 20 Boeing 787 Dreamliners", "CONFIRMED", "Manila", "Markets", "Asia"),
    (45, "Thailand scraps tariffs, buys $2.6bn farm goods", "REPORTED", "Bangkok", "Markets", "Asia"),
    (46, "Nepal PM's first trip: Delhi on Sunday", "REPORTED", "Kathmandu", "Diplomacy", "Asia"),
    (47, "EU, Canada deepen minerals and defence ties", "REPORTED", "Brussels", "Diplomacy", "Europe"),
    (48, "Araqchi wants dialogue; Trump rejects proposals", "REPORTED", "Tehran", "Diplomacy", "Middle East"),
    (49, "US denies new strikes on Iran's Qeshm Island", "REPORTED", "CENTCOM", "War", "Middle East"),
    (50, "WPL auction: 277 players for 73 spots", "CONFIRMED", "New Delhi", "Sport", "Asia"),
    (51, "Gill out of 2nd Test; Pant leads, Rabada out too", "CONFIRMED", "Guwahati", "Sport", "Asia"),
]

# UTC timeline of the day's first hours (as of 04:30 UTC; the day is in progress).
TIMELINE = [
    ("00:00", "Coalition downs Houthi missiles"),
    ("00:09", "M6.8 quake, Junin, Peru"),
    ("01:12", "Denmark expels diplomat"),
    ("01:44", "COP31 deal stalls"),
    ("02:49", "Gen Z protests sweep Europe"),
    ("03:37", "Rahul completes SENA set"),
]

# Older stories deliberately LEFT OUT of the 51 — a careless page would include them.
DATE_CHECK = [
    ("ICJ rules Myanmar committed genocide", "19 Nov, The Hague"),
    ("Russia hits three Kyiv bridges; missiles crash in Poland", "20 Nov"),
    ("S&P 500 enters correction; Nvidia slides on SEC probe", "20 Nov"),
    ("UK and EU seal post-Brexit trade deal", "20 Nov"),
    ("Mamdani sets 2032 to close Rikers Island", "20 Nov"),
    ("Mongolia's parliament accepts president's resignation", "19 Nov"),
    ("Shenzhen trilateral declaration", "18-19 Nov"),
    ("Saudi strikes on Hodeidah port", "20 Nov"),
]

# Rough continent outlines (lon, lat) for the drawn world map.
CONTINENTS = [
    # North America
    [(-168, 66), (-140, 70), (-120, 72), (-95, 80), (-75, 73), (-55, 60), (-60, 47),
     (-70, 42), (-75, 35), (-80, 26), (-85, 20), (-92, 15), (-97, 16), (-105, 20),
     (-110, 24), (-117, 33), (-125, 40), (-125, 49), (-135, 58), (-155, 58), (-168, 66)],
    # South America
    [(-78, 7), (-72, 11), (-60, 8), (-52, 5), (-42, -3), (-35, -8), (-40, -20),
     (-48, -28), (-58, -35), (-65, -41), (-70, -52), (-73, -50), (-73, -37),
     (-70, -20), (-80, -5), (-81, 2), (-78, 7)],
    # Africa
    [(-17, 15), (-16, 21), (-10, 31), (0, 36), (10, 37), (20, 32), (32, 31),
     (35, 28), (43, 12), (51, 11), (48, 2), (41, -2), (40, -10), (36, -18),
     (33, -26), (26, -34), (19, -35), (15, -27), (12, -18), (9, -1), (-8, 5), (-17, 15)],
    # Europe
    [(-10, 36), (-9, 43), (-2, 48), (-5, 50), (2, 51), (5, 53), (8, 57), (10, 59),
     (18, 56), (21, 55), (24, 58), (28, 60), (30, 62), (30, 70), (40, 68),
     (44, 66), (40, 60), (35, 55), (30, 50), (28, 45), (23, 40), (19, 42),
     (12, 44), (8, 38), (3, 38), (-2, 37), (-10, 36)],
    # Asia (incl. Middle East, India, SE Asia, China, Siberia)
    [(30, 36), (36, 36), (44, 39), (48, 30), (52, 26), (57, 25), (61, 25),
     (66, 25), (72, 20), (77, 8), (80, 7), (85, 19), (89, 22), (92, 16),
     (98, 8), (100, 6), (104, 2), (107, 11), (109, 14), (106, 20), (110, 22),
     (114, 22), (118, 25), (121, 28), (122, 32), (120, 35), (122, 38),
     (127, 40), (130, 42), (135, 44), (138, 46), (142, 50), (142, 59),
     (158, 60), (162, 62), (170, 66), (178, 65), (170, 70), (160, 70),
     (140, 72), (120, 73), (100, 77), (80, 73), (68, 70), (60, 69),
     (55, 68), (50, 68), (45, 68), (40, 68), (35, 66), (32, 66), (30, 62),
     (28, 58), (25, 55), (22, 50), (20, 46), (25, 42), (30, 36)],
    # Australia
    [(113, -22), (114, -30), (115, -35), (118, -35), (124, -33), (129, -32),
     (132, -32), (136, -35), (140, -38), (145, -38), (150, -37), (153, -27),
     (153, -24), (150, -22), (146, -19), (142, -11), (137, -12), (132, -12),
     (126, -14), (122, -17), (118, -20), (113, -22)],
]
