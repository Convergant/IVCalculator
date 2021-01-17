from EXPGroup import EXPGroup

file = open("pokemon.csv", "r")
temp = file.read()
file.close()

temp = temp.split("\n")
names = []

for i, row in enumerate(temp):
    temp[i] = row.split(",")

    names.append(temp[i][0])
    temp[i].pop(0)

    for j in range(len(temp[i])):
        temp[i][j] = int(temp[i][j])

base_stats_data = dict(zip(names, temp))

exp_groups_data = {
    "Abomasnow": EXPGroup.SLOW,
    "Abra": EXPGroup.MEDIUM_SLOW,
    "Absol": EXPGroup.MEDIUM_SLOW,
    "Accelgor": EXPGroup.MEDIUM_FAST,
    "Aegislash": EXPGroup.MEDIUM_FAST,
    "Aerodactyl": EXPGroup.SLOW,
    "Aggron": EXPGroup.SLOW,
    "Aipom": EXPGroup.FAST,
    "Alakazam": EXPGroup.MEDIUM_SLOW,
    "Alcremie": EXPGroup.MEDIUM_FAST,
    "Alomomola": EXPGroup.FAST,
    "Altaria": EXPGroup.ERRATIC,
    "Amaura": EXPGroup.MEDIUM_FAST,
    "Ambipom": EXPGroup.FAST,
    "Amoonguss": EXPGroup.MEDIUM_FAST,
    "Ampharos": EXPGroup.MEDIUM_SLOW,
    "Anorith": EXPGroup.ERRATIC,
    "Appletun": EXPGroup.ERRATIC,
    "Applin": EXPGroup.ERRATIC,
    "Araquanid": EXPGroup.MEDIUM_FAST,
    "Arbok": EXPGroup.MEDIUM_FAST,
    "Arcanine": EXPGroup.SLOW,
    "Arceus": EXPGroup.SLOW,
    "Archen": EXPGroup.MEDIUM_FAST,
    "Archeops": EXPGroup.MEDIUM_FAST,
    "Arctovish": EXPGroup.SLOW,
    "Arctozolt": EXPGroup.SLOW,
    "Ariados": EXPGroup.FAST,
    "Armaldo": EXPGroup.ERRATIC,
    "Aromatisse": EXPGroup.MEDIUM_FAST,
    "Aron": EXPGroup.SLOW,
    "Arrokuda": EXPGroup.SLOW,
    "Articuno": EXPGroup.SLOW,
    "Audino": EXPGroup.FAST,
    "Aurorus": EXPGroup.MEDIUM_FAST,
    "Avalugg": EXPGroup.MEDIUM_FAST,
    "Axew": EXPGroup.SLOW,
    "Azelf": EXPGroup.SLOW,
    "Azumarill": EXPGroup.FAST,
    "Azurill": EXPGroup.FAST,
    "Bagon": EXPGroup.SLOW,
    "Baltoy": EXPGroup.MEDIUM_FAST,
    "Banette": EXPGroup.FAST,
    "Barbaracle": EXPGroup.MEDIUM_FAST,
    "Barboach": EXPGroup.MEDIUM_FAST,
    "Barraskewda": EXPGroup.SLOW,
    "Basculin": EXPGroup.MEDIUM_FAST,
    "Bastiodon": EXPGroup.ERRATIC,
    "Bayleef": EXPGroup.MEDIUM_SLOW,
    "Beartic": EXPGroup.MEDIUM_FAST,
    "Beautifly": EXPGroup.MEDIUM_FAST,
    "Beedrill": EXPGroup.MEDIUM_FAST,
    "Beheeyem": EXPGroup.MEDIUM_FAST,
    "Beldum": EXPGroup.SLOW,
    "Bellossom": EXPGroup.MEDIUM_SLOW,
    "Bellsprout": EXPGroup.MEDIUM_SLOW,
    "Bergmite": EXPGroup.MEDIUM_FAST,
    "Bewear": EXPGroup.MEDIUM_FAST,
    "Bibarel": EXPGroup.MEDIUM_FAST,
    "Bidoof": EXPGroup.MEDIUM_FAST,
    "Binacle": EXPGroup.MEDIUM_FAST,
    "Bisharp": EXPGroup.MEDIUM_FAST,
    "Blacephalon": EXPGroup.SLOW,
    "Blastoise": EXPGroup.MEDIUM_SLOW,
    "Blaziken": EXPGroup.MEDIUM_SLOW,
    "Blipbug": EXPGroup.MEDIUM_FAST,
    "Blissey": EXPGroup.FAST,
    "Blitzle": EXPGroup.MEDIUM_FAST,
    "Boldore": EXPGroup.MEDIUM_SLOW,
    "Boltund": EXPGroup.FAST,
    "Bonsly": EXPGroup.MEDIUM_FAST,
    "Bouffalant": EXPGroup.MEDIUM_FAST,
    "Bounsweet": EXPGroup.MEDIUM_SLOW,
    "Braixen": EXPGroup.MEDIUM_SLOW,
    "Braviary": EXPGroup.SLOW,
    "Breloom": EXPGroup.FLUCTUATING,
    "Brionne": EXPGroup.MEDIUM_SLOW,
    "Bronzong": EXPGroup.MEDIUM_FAST,
    "Bronzor": EXPGroup.MEDIUM_FAST,
    "Bruxish": EXPGroup.MEDIUM_FAST,
    "Budew": EXPGroup.MEDIUM_SLOW,
    "Buizel": EXPGroup.MEDIUM_FAST,
    "Bulbasaur": EXPGroup.MEDIUM_SLOW,
    "Buneary": EXPGroup.MEDIUM_FAST,
    "Bunnelby": EXPGroup.MEDIUM_FAST,
    "Burmy": EXPGroup.MEDIUM_FAST,
    "Butterfree": EXPGroup.MEDIUM_FAST,
    "Buzzwole": EXPGroup.SLOW,
    "Cacnea": EXPGroup.MEDIUM_SLOW,
    "Cacturne": EXPGroup.MEDIUM_SLOW,
    "Camerupt": EXPGroup.MEDIUM_FAST,
    "Carbink": EXPGroup.SLOW,
    "Carkol": EXPGroup.MEDIUM_SLOW,
    "Carnivine": EXPGroup.SLOW,
    "Carracosta": EXPGroup.MEDIUM_FAST,
    "Carvanha": EXPGroup.SLOW,
    "Cascoon": EXPGroup.MEDIUM_FAST,
    "Castform": EXPGroup.MEDIUM_FAST,
    "Caterpie": EXPGroup.MEDIUM_FAST,
    "Celebi": EXPGroup.MEDIUM_SLOW,
    "Celesteela": EXPGroup.SLOW,
    "Centiskorch": EXPGroup.MEDIUM_FAST,
    "Chandelure": EXPGroup.MEDIUM_SLOW,
    "Chansey": EXPGroup.FAST,
    "Charizard": EXPGroup.MEDIUM_SLOW,
    "Charjabug": EXPGroup.MEDIUM_FAST,
    "Charmander": EXPGroup.MEDIUM_SLOW,
    "Charmeleon": EXPGroup.MEDIUM_SLOW,
    "Chatot": EXPGroup.MEDIUM_SLOW,
    "Cherrim": EXPGroup.MEDIUM_FAST,
    "Cherubi": EXPGroup.MEDIUM_FAST,
    "Chesnaught": EXPGroup.MEDIUM_SLOW,
    "Chespin": EXPGroup.MEDIUM_SLOW,
    "Chewtle": EXPGroup.MEDIUM_FAST,
    "Chikorita": EXPGroup.MEDIUM_SLOW,
    "Chimchar": EXPGroup.MEDIUM_SLOW,
    "Chimecho": EXPGroup.FAST,
    "Chinchou": EXPGroup.SLOW,
    "Chingling": EXPGroup.FAST,
    "Cinccino": EXPGroup.FAST,
    "Cinderace": EXPGroup.MEDIUM_SLOW,
    "Clamperl": EXPGroup.ERRATIC,
    "Clauncher": EXPGroup.SLOW,
    "Clawitzer": EXPGroup.SLOW,
    "Claydol": EXPGroup.MEDIUM_FAST,
    "Clefable": EXPGroup.FAST,
    "Clefairy": EXPGroup.FAST,
    "Cleffa": EXPGroup.FAST,
    "Clobbopus": EXPGroup.MEDIUM_SLOW,
    "Cloyster": EXPGroup.SLOW,
    "Coalossal": EXPGroup.MEDIUM_SLOW,
    "Cobalion": EXPGroup.SLOW,
    "Cofagrigus": EXPGroup.MEDIUM_FAST,
    "Combee": EXPGroup.MEDIUM_SLOW,
    "Combusken": EXPGroup.MEDIUM_SLOW,
    "Comfey": EXPGroup.FAST,
    "Conkeldurr": EXPGroup.MEDIUM_SLOW,
    "Copperajah": EXPGroup.MEDIUM_FAST,
    "Corphish": EXPGroup.FLUCTUATING,
    "Corsola": EXPGroup.FAST,
    "Corviknight": EXPGroup.MEDIUM_SLOW,
    "Corvisquire": EXPGroup.MEDIUM_SLOW,
    "Cosmoem": EXPGroup.SLOW,
    "Cosmog": EXPGroup.SLOW,
    "Cottonee": EXPGroup.MEDIUM_FAST,
    "Crabominable": EXPGroup.MEDIUM_FAST,
    "Crabrawler": EXPGroup.MEDIUM_FAST,
    "Cradily": EXPGroup.ERRATIC,
    "Cramorant": EXPGroup.MEDIUM_FAST,
    "Cranidos": EXPGroup.ERRATIC,
    "Crawdaunt": EXPGroup.FLUCTUATING,
    "Cresselia": EXPGroup.SLOW,
    "Croagunk": EXPGroup.MEDIUM_FAST,
    "Crobat": EXPGroup.MEDIUM_FAST,
    "Croconaw": EXPGroup.MEDIUM_SLOW,
    "Crustle": EXPGroup.MEDIUM_FAST,
    "Cryogonal": EXPGroup.MEDIUM_FAST,
    "Cubchoo": EXPGroup.MEDIUM_FAST,
    "Cubone": EXPGroup.MEDIUM_FAST,
    "Cufant": EXPGroup.MEDIUM_FAST,
    "Cursola": EXPGroup.FAST,
    "Cutiefly": EXPGroup.MEDIUM_FAST,
    "Cyndaquil": EXPGroup.MEDIUM_SLOW,
    "Darkrai": EXPGroup.SLOW,
    "Darmanitan": EXPGroup.MEDIUM_SLOW,
    "Dartrix": EXPGroup.MEDIUM_SLOW,
    "Darumaka": EXPGroup.MEDIUM_SLOW,
    "Decidueye": EXPGroup.MEDIUM_SLOW,
    "Dedenne": EXPGroup.MEDIUM_FAST,
    "Deerling": EXPGroup.MEDIUM_FAST,
    "Deino": EXPGroup.SLOW,
    "Delcatty": EXPGroup.FAST,
    "Delibird": EXPGroup.FAST,
    "Delphox": EXPGroup.MEDIUM_SLOW,
    "Deoxys": EXPGroup.SLOW,
    "Dewgong": EXPGroup.MEDIUM_FAST,
    "Dewott": EXPGroup.MEDIUM_SLOW,
    "Dewpider": EXPGroup.MEDIUM_FAST,
    "Dhelmise": EXPGroup.MEDIUM_FAST,
    "Dialga": EXPGroup.SLOW,
    "Diancie": EXPGroup.SLOW,
    "Diggersby": EXPGroup.MEDIUM_FAST,
    "Diglett": EXPGroup.MEDIUM_FAST,
    "Ditto": EXPGroup.MEDIUM_FAST,
    "Dodrio": EXPGroup.MEDIUM_FAST,
    "Doduo": EXPGroup.MEDIUM_FAST,
    "Donphan": EXPGroup.MEDIUM_FAST,
    "Dottler": EXPGroup.MEDIUM_FAST,
    "Doublade": EXPGroup.MEDIUM_FAST,
    "Dracovish": EXPGroup.SLOW,
    "Dracozolt": EXPGroup.SLOW,
    "Dragalge": EXPGroup.MEDIUM_FAST,
    "Dragapult": EXPGroup.SLOW,
    "Dragonair": EXPGroup.SLOW,
    "Dragonite": EXPGroup.SLOW,
    "Drakloak": EXPGroup.SLOW,
    "Drampa": EXPGroup.MEDIUM_FAST,
    "Drapion": EXPGroup.SLOW,
    "Dratini": EXPGroup.SLOW,
    "Drednaw": EXPGroup.MEDIUM_FAST,
    "Dreepy": EXPGroup.SLOW,
    "Drifblim": EXPGroup.FLUCTUATING,
    "Drifloon": EXPGroup.FLUCTUATING,
    "Drilbur": EXPGroup.MEDIUM_FAST,
    "Drizzile": EXPGroup.MEDIUM_SLOW,
    "Drowzee": EXPGroup.MEDIUM_FAST,
    "Druddigon": EXPGroup.MEDIUM_FAST,
    "Dubwool": EXPGroup.MEDIUM_FAST,
    "Ducklett": EXPGroup.MEDIUM_FAST,
    "Dugtrio": EXPGroup.MEDIUM_FAST,
    "Dunsparce": EXPGroup.MEDIUM_FAST,
    "Duosion": EXPGroup.MEDIUM_SLOW,
    "Duraludon": EXPGroup.MEDIUM_FAST,
    "Durant": EXPGroup.MEDIUM_FAST,
    "Dusclops": EXPGroup.FAST,
    "Dusknoir": EXPGroup.FAST,
    "Duskull": EXPGroup.FAST,
    "Dustox": EXPGroup.MEDIUM_FAST,
    "Dwebble": EXPGroup.MEDIUM_FAST,
    "Eelektrik": EXPGroup.SLOW,
    "Eelektross": EXPGroup.SLOW,
    "Eevee": EXPGroup.MEDIUM_FAST,
    "Eiscue": EXPGroup.SLOW,
    "Ekans": EXPGroup.MEDIUM_FAST,
    "Eldegoss": EXPGroup.MEDIUM_FAST,
    "Electabuzz": EXPGroup.MEDIUM_FAST,
    "Electivire": EXPGroup.MEDIUM_FAST,
    "Electrike": EXPGroup.SLOW,
    "Electrode": EXPGroup.MEDIUM_FAST,
    "Elekid": EXPGroup.MEDIUM_FAST,
    "Elgyem": EXPGroup.MEDIUM_FAST,
    "Emboar": EXPGroup.MEDIUM_SLOW,
    "Emolga": EXPGroup.MEDIUM_FAST,
    "Empoleon": EXPGroup.MEDIUM_SLOW,
    "Entei": EXPGroup.SLOW,
    "Escavalier": EXPGroup.MEDIUM_FAST,
    "Espeon": EXPGroup.MEDIUM_FAST,
    "Espurr": EXPGroup.MEDIUM_FAST,
    "Eternatus": EXPGroup.SLOW,
    "Excadrill": EXPGroup.MEDIUM_FAST,
    "Exeggcute": EXPGroup.SLOW,
    "Exeggutor": EXPGroup.SLOW,
    "Exploud": EXPGroup.MEDIUM_SLOW,
    "Falinks": EXPGroup.MEDIUM_FAST,
    "Farfetch'd": EXPGroup.MEDIUM_FAST,
    "Fearow": EXPGroup.MEDIUM_FAST,
    "Feebas": EXPGroup.ERRATIC,
    "Fennekin": EXPGroup.MEDIUM_SLOW,
    "Feraligatr": EXPGroup.MEDIUM_SLOW,
    "Ferroseed": EXPGroup.MEDIUM_FAST,
    "Ferrothorn": EXPGroup.MEDIUM_FAST,
    "Finneon": EXPGroup.ERRATIC,
    "Flaaffy": EXPGroup.MEDIUM_SLOW,
    "Flabébé": EXPGroup.MEDIUM_FAST,
    "Flapple": EXPGroup.ERRATIC,
    "Flareon": EXPGroup.MEDIUM_FAST,
    "Fletchinder": EXPGroup.MEDIUM_SLOW,
    "Fletchling": EXPGroup.MEDIUM_SLOW,
    "Floatzel": EXPGroup.MEDIUM_FAST,
    "Floette": EXPGroup.MEDIUM_FAST,
    "Florges": EXPGroup.MEDIUM_FAST,
    "Flygon": EXPGroup.MEDIUM_SLOW,
    "Fomantis": EXPGroup.MEDIUM_FAST,
    "Foongus": EXPGroup.MEDIUM_FAST,
    "Forretress": EXPGroup.MEDIUM_FAST,
    "Fraxure": EXPGroup.SLOW,
    "Frillish": EXPGroup.MEDIUM_FAST,
    "Froakie": EXPGroup.MEDIUM_SLOW,
    "Frogadier": EXPGroup.MEDIUM_SLOW,
    "Froslass": EXPGroup.MEDIUM_FAST,
    "Frosmoth": EXPGroup.MEDIUM_FAST,
    "Furfrou": EXPGroup.MEDIUM_FAST,
    "Furret": EXPGroup.MEDIUM_FAST,
    "Gabite": EXPGroup.SLOW,
    "Gallade": EXPGroup.SLOW,
    "Galvantula": EXPGroup.MEDIUM_FAST,
    "Garbodor": EXPGroup.MEDIUM_FAST,
    "Garchomp": EXPGroup.SLOW,
    "Gardevoir": EXPGroup.SLOW,
    "Gastly": EXPGroup.MEDIUM_SLOW,
    "Gastrodon": EXPGroup.MEDIUM_FAST,
    "Genesect": EXPGroup.SLOW,
    "Gengar": EXPGroup.MEDIUM_SLOW,
    "Geodude": EXPGroup.MEDIUM_SLOW,
    "Gible": EXPGroup.SLOW,
    "Gigalith": EXPGroup.MEDIUM_SLOW,
    "Girafarig": EXPGroup.MEDIUM_FAST,
    "Giratina": EXPGroup.SLOW,
    "Glaceon": EXPGroup.MEDIUM_FAST,
    "Glalie": EXPGroup.MEDIUM_FAST,
    "Glameow": EXPGroup.FAST,
    "Gligar": EXPGroup.MEDIUM_SLOW,
    "Gliscor": EXPGroup.MEDIUM_SLOW,
    "Gloom": EXPGroup.MEDIUM_SLOW,
    "Gogoat": EXPGroup.MEDIUM_FAST,
    "Golbat": EXPGroup.MEDIUM_FAST,
    "Goldeen": EXPGroup.MEDIUM_FAST,
    "Golduck": EXPGroup.MEDIUM_FAST,
    "Golem": EXPGroup.MEDIUM_SLOW,
    "Golett": EXPGroup.MEDIUM_FAST,
    "Golisopod": EXPGroup.MEDIUM_FAST,
    "Golurk": EXPGroup.MEDIUM_FAST,
    "Goodra": EXPGroup.SLOW,
    "Goomy": EXPGroup.SLOW,
    "Gorebyss": EXPGroup.ERRATIC,
    "Gossifleur": EXPGroup.MEDIUM_FAST,
    "Gothita": EXPGroup.MEDIUM_SLOW,
    "Gothitelle": EXPGroup.MEDIUM_SLOW,
    "Gothorita": EXPGroup.MEDIUM_SLOW,
    "Gourgeist": EXPGroup.MEDIUM_FAST,
    "Granbull": EXPGroup.FAST,
    "Grapploct": EXPGroup.MEDIUM_SLOW,
    "Graveler": EXPGroup.MEDIUM_SLOW,
    "Greedent": EXPGroup.MEDIUM_FAST,
    "Greninja": EXPGroup.MEDIUM_SLOW,
    "Grimer": EXPGroup.MEDIUM_FAST,
    "Grimmsnarl": EXPGroup.MEDIUM_FAST,
    "Grookey": EXPGroup.MEDIUM_SLOW,
    "Grotle": EXPGroup.MEDIUM_SLOW,
    "Groudon": EXPGroup.SLOW,
    "Grovyle": EXPGroup.MEDIUM_SLOW,
    "Growlithe": EXPGroup.SLOW,
    "Grubbin": EXPGroup.MEDIUM_FAST,
    "Grumpig": EXPGroup.FAST,
    "Gulpin": EXPGroup.FLUCTUATING,
    "Gumshoos": EXPGroup.MEDIUM_FAST,
    "Gurdurr": EXPGroup.MEDIUM_SLOW,
    "Guzzlord": EXPGroup.SLOW,
    "Gyarados": EXPGroup.SLOW,
    "Hakamo-o": EXPGroup.SLOW,
    "Happiny": EXPGroup.FAST,
    "Hariyama": EXPGroup.FLUCTUATING,
    "Hatenna": EXPGroup.SLOW,
    "Hatterene": EXPGroup.SLOW,
    "Hattrem": EXPGroup.SLOW,
    "Haunter": EXPGroup.MEDIUM_SLOW,
    "Hawlucha": EXPGroup.MEDIUM_FAST,
    "Haxorus": EXPGroup.SLOW,
    "Heatmor": EXPGroup.MEDIUM_FAST,
    "Heatran": EXPGroup.SLOW,
    "Heliolisk": EXPGroup.MEDIUM_FAST,
    "Helioptile": EXPGroup.MEDIUM_FAST,
    "Heracross": EXPGroup.SLOW,
    "Herdier": EXPGroup.MEDIUM_SLOW,
    "Hippopotas": EXPGroup.SLOW,
    "Hippowdon": EXPGroup.SLOW,
    "Hitmonchan": EXPGroup.MEDIUM_FAST,
    "Hitmonlee": EXPGroup.MEDIUM_FAST,
    "Hitmontop": EXPGroup.MEDIUM_FAST,
    "Honchkrow": EXPGroup.MEDIUM_SLOW,
    "Honedge": EXPGroup.MEDIUM_FAST,
    "Ho-Oh": EXPGroup.SLOW,
    "Hoopa": EXPGroup.SLOW,
    "Hoothoot": EXPGroup.MEDIUM_FAST,
    "Hoppip": EXPGroup.MEDIUM_SLOW,
    "Horsea": EXPGroup.MEDIUM_FAST,
    "Houndoom": EXPGroup.SLOW,
    "Houndour": EXPGroup.SLOW,
    "Huntail": EXPGroup.ERRATIC,
    "Hydreigon": EXPGroup.SLOW,
    "Hypno": EXPGroup.MEDIUM_FAST,
    "Igglybuff": EXPGroup.FAST,
    "Illumise": EXPGroup.FLUCTUATING,
    "Impidimp": EXPGroup.MEDIUM_FAST,
    "Incineroar": EXPGroup.MEDIUM_SLOW,
    "Indeedee": EXPGroup.FAST,
    "Infernape": EXPGroup.MEDIUM_SLOW,
    "Inkay": EXPGroup.MEDIUM_FAST,
    "Inteleon": EXPGroup.MEDIUM_SLOW,
    "Ivysaur": EXPGroup.MEDIUM_SLOW,
    "Jangmo-o": EXPGroup.SLOW,
    "Jellicent": EXPGroup.MEDIUM_FAST,
    "Jigglypuff": EXPGroup.FAST,
    "Jirachi": EXPGroup.SLOW,
    "Jolteon": EXPGroup.MEDIUM_FAST,
    "Joltik": EXPGroup.MEDIUM_FAST,
    "Jumpluff": EXPGroup.MEDIUM_SLOW,
    "Jynx": EXPGroup.MEDIUM_FAST,
    "Kabuto": EXPGroup.MEDIUM_FAST,
    "Kabutops": EXPGroup.MEDIUM_FAST,
    "Kadabra": EXPGroup.MEDIUM_SLOW,
    "Kakuna": EXPGroup.MEDIUM_FAST,
    "Kangaskhan": EXPGroup.MEDIUM_FAST,
    "Karrablast": EXPGroup.MEDIUM_FAST,
    "Kartana": EXPGroup.SLOW,
    "Kecleon": EXPGroup.MEDIUM_SLOW,
    "Keldeo": EXPGroup.SLOW,
    "Kingdra": EXPGroup.MEDIUM_FAST,
    "Kingler": EXPGroup.MEDIUM_FAST,
    "Kirlia": EXPGroup.SLOW,
    "Klang": EXPGroup.MEDIUM_SLOW,
    "Klefki": EXPGroup.FAST,
    "Klink": EXPGroup.MEDIUM_SLOW,
    "Klinklang": EXPGroup.MEDIUM_SLOW,
    "Koffing": EXPGroup.MEDIUM_FAST,
    "Komala": EXPGroup.SLOW,
    "Kommo-o": EXPGroup.SLOW,
    "Krabby": EXPGroup.MEDIUM_FAST,
    "Kricketot": EXPGroup.MEDIUM_SLOW,
    "Kricketune": EXPGroup.MEDIUM_SLOW,
    "Krokorok": EXPGroup.MEDIUM_SLOW,
    "Krookodile": EXPGroup.MEDIUM_SLOW,
    "Kyogre": EXPGroup.SLOW,
    "Kyurem": EXPGroup.SLOW,
    "Lairon": EXPGroup.SLOW,
    "Lampent": EXPGroup.MEDIUM_SLOW,
    "Landorus": EXPGroup.SLOW,
    "Lanturn": EXPGroup.SLOW,
    "Lapras": EXPGroup.SLOW,
    "Larvesta": EXPGroup.SLOW,
    "Larvitar": EXPGroup.SLOW,
    "Latias": EXPGroup.SLOW,
    "Latios": EXPGroup.SLOW,
    "Leafeon": EXPGroup.MEDIUM_FAST,
    "Leavanny": EXPGroup.MEDIUM_SLOW,
    "Ledian": EXPGroup.FAST,
    "Ledyba": EXPGroup.FAST,
    "Lickilicky": EXPGroup.MEDIUM_FAST,
    "Lickitung": EXPGroup.MEDIUM_FAST,
    "Liepard": EXPGroup.MEDIUM_FAST,
    "Lileep": EXPGroup.ERRATIC,
    "Lilligant": EXPGroup.MEDIUM_FAST,
    "Lillipup": EXPGroup.MEDIUM_SLOW,
    "Linoone": EXPGroup.MEDIUM_FAST,
    "Litleo": EXPGroup.MEDIUM_SLOW,
    "Litten": EXPGroup.MEDIUM_SLOW,
    "Litwick": EXPGroup.MEDIUM_SLOW,
    "Lombre": EXPGroup.MEDIUM_SLOW,
    "Lopunny": EXPGroup.MEDIUM_FAST,
    "Lotad": EXPGroup.MEDIUM_SLOW,
    "Loudred": EXPGroup.MEDIUM_SLOW,
    "Lucario": EXPGroup.MEDIUM_SLOW,
    "Ludicolo": EXPGroup.MEDIUM_SLOW,
    "Lugia": EXPGroup.SLOW,
    "Lumineon": EXPGroup.ERRATIC,
    "Lunala": EXPGroup.SLOW,
    "Lunatone": EXPGroup.FAST,
    "Lurantis": EXPGroup.MEDIUM_FAST,
    "Luvdisc": EXPGroup.FAST,
    "Luxio": EXPGroup.MEDIUM_SLOW,
    "Luxray": EXPGroup.MEDIUM_SLOW,
    "Lycanroc": EXPGroup.MEDIUM_FAST,
    "Machamp": EXPGroup.MEDIUM_SLOW,
    "Machoke": EXPGroup.MEDIUM_SLOW,
    "Machop": EXPGroup.MEDIUM_SLOW,
    "Magby": EXPGroup.MEDIUM_FAST,
    "Magcargo": EXPGroup.MEDIUM_FAST,
    "Magearna": EXPGroup.SLOW,
    "Magikarp": EXPGroup.SLOW,
    "Magmar": EXPGroup.MEDIUM_FAST,
    "Magmortar": EXPGroup.MEDIUM_FAST,
    "Magnemite": EXPGroup.MEDIUM_FAST,
    "Magneton": EXPGroup.MEDIUM_FAST,
    "Magnezone": EXPGroup.MEDIUM_FAST,
    "Makuhita": EXPGroup.FLUCTUATING,
    "Malamar": EXPGroup.MEDIUM_FAST,
    "Mamoswine": EXPGroup.SLOW,
    "Manaphy": EXPGroup.SLOW,
    "Mandibuzz": EXPGroup.SLOW,
    "Manectric": EXPGroup.SLOW,
    "Mankey": EXPGroup.MEDIUM_FAST,
    "Mantine": EXPGroup.SLOW,
    "Mantyke": EXPGroup.SLOW,
    "Maractus": EXPGroup.MEDIUM_FAST,
    "Mareanie": EXPGroup.MEDIUM_FAST,
    "Mareep": EXPGroup.MEDIUM_SLOW,
    "Marill": EXPGroup.FAST,
    "Marowak": EXPGroup.MEDIUM_FAST,
    "Marshadow": EXPGroup.SLOW,
    "Marshtomp": EXPGroup.MEDIUM_SLOW,
    "Masquerain": EXPGroup.MEDIUM_FAST,
    "Mawile": EXPGroup.FAST,
    "Medicham": EXPGroup.MEDIUM_FAST,
    "Meditite": EXPGroup.MEDIUM_FAST,
    "Meganium": EXPGroup.MEDIUM_SLOW,
    "Melmetal": EXPGroup.SLOW,
    "Meloetta": EXPGroup.SLOW,
    "Meltan": EXPGroup.SLOW,
    "Meowstic": EXPGroup.MEDIUM_FAST,
    "Meowth": EXPGroup.MEDIUM_FAST,
    "Mesprit": EXPGroup.SLOW,
    "Metagross": EXPGroup.SLOW,
    "Metang": EXPGroup.SLOW,
    "Metapod": EXPGroup.MEDIUM_FAST,
    "Mew": EXPGroup.MEDIUM_SLOW,
    "Mewtwo": EXPGroup.SLOW,
    "Mienfoo": EXPGroup.MEDIUM_SLOW,
    "Mienshao": EXPGroup.MEDIUM_SLOW,
    "Mightyena": EXPGroup.MEDIUM_FAST,
    "Milcery": EXPGroup.MEDIUM_FAST,
    "Milotic": EXPGroup.ERRATIC,
    "Miltank": EXPGroup.SLOW,
    "Mime Jr.": EXPGroup.MEDIUM_FAST,
    "Mimikyu": EXPGroup.MEDIUM_FAST,
    "Minccino": EXPGroup.FAST,
    "Minior": EXPGroup.MEDIUM_SLOW,
    "Minun": EXPGroup.MEDIUM_FAST,
    "Misdreavus": EXPGroup.FAST,
    "Mismagius": EXPGroup.FAST,
    "Moltres": EXPGroup.SLOW,
    "Monferno": EXPGroup.MEDIUM_SLOW,
    "Morelull": EXPGroup.MEDIUM_FAST,
    "Morgrem": EXPGroup.MEDIUM_FAST,
    "Morpeko": EXPGroup.MEDIUM_FAST,
    "Mothim": EXPGroup.MEDIUM_FAST,
    "Mr. Mime": EXPGroup.MEDIUM_FAST,
    "Mr. Rime": EXPGroup.MEDIUM_FAST,
    "Mudbray": EXPGroup.MEDIUM_FAST,
    "Mudkip": EXPGroup.MEDIUM_SLOW,
    "Mudsdale": EXPGroup.MEDIUM_FAST,
    "Muk": EXPGroup.MEDIUM_FAST,
    "Munchlax": EXPGroup.SLOW,
    "Munna": EXPGroup.FAST,
    "Murkrow": EXPGroup.MEDIUM_SLOW,
    "Musharna": EXPGroup.FAST,
    "Naganadel": EXPGroup.SLOW,
    "Natu": EXPGroup.MEDIUM_FAST,
    "Necrozma": EXPGroup.SLOW,
    "Nickit": EXPGroup.FAST,
    "Nidoking": EXPGroup.MEDIUM_SLOW,
    "Nidoqueen": EXPGroup.MEDIUM_SLOW,
    "Nidoran": EXPGroup.MEDIUM_SLOW,
    "Nidorina": EXPGroup.MEDIUM_SLOW,
    "Nidorino": EXPGroup.MEDIUM_SLOW,
    "Nihilego": EXPGroup.SLOW,
    "Nincada": EXPGroup.ERRATIC,
    "Ninetales": EXPGroup.MEDIUM_FAST,
    "Ninjask": EXPGroup.ERRATIC,
    "Noctowl": EXPGroup.MEDIUM_FAST,
    "Noibat": EXPGroup.MEDIUM_FAST,
    "Noivern": EXPGroup.MEDIUM_FAST,
    "Nosepass": EXPGroup.MEDIUM_FAST,
    "Numel": EXPGroup.MEDIUM_FAST,
    "Nuzleaf": EXPGroup.MEDIUM_SLOW,
    "Obstagoon": EXPGroup.MEDIUM_FAST,
    "Octillery": EXPGroup.MEDIUM_FAST,
    "Oddish": EXPGroup.MEDIUM_SLOW,
    "Omanyte": EXPGroup.MEDIUM_FAST,
    "Omastar": EXPGroup.MEDIUM_FAST,
    "Onix": EXPGroup.MEDIUM_FAST,
    "Oranguru": EXPGroup.SLOW,
    "Orbeetle": EXPGroup.MEDIUM_FAST,
    "Oricorio": EXPGroup.MEDIUM_FAST,
    "Oshawott": EXPGroup.MEDIUM_SLOW,
    "Pachirisu": EXPGroup.MEDIUM_FAST,
    "Palkia": EXPGroup.SLOW,
    "Palossand": EXPGroup.MEDIUM_FAST,
    "Palpitoad": EXPGroup.MEDIUM_SLOW,
    "Pancham": EXPGroup.MEDIUM_FAST,
    "Pangoro": EXPGroup.MEDIUM_FAST,
    "Panpour": EXPGroup.MEDIUM_FAST,
    "Pansage": EXPGroup.MEDIUM_FAST,
    "Pansear": EXPGroup.MEDIUM_FAST,
    "Paras": EXPGroup.MEDIUM_FAST,
    "Parasect": EXPGroup.MEDIUM_FAST,
    "Passimian": EXPGroup.SLOW,
    "Patrat": EXPGroup.MEDIUM_FAST,
    "Pawniard": EXPGroup.MEDIUM_FAST,
    "Pelipper": EXPGroup.MEDIUM_FAST,
    "Perrserker": EXPGroup.MEDIUM_FAST,
    "Persian": EXPGroup.MEDIUM_FAST,
    "Petilil": EXPGroup.MEDIUM_FAST,
    "Phanpy": EXPGroup.MEDIUM_FAST,
    "Phantump": EXPGroup.MEDIUM_FAST,
    "Pheromosa": EXPGroup.SLOW,
    "Phione": EXPGroup.SLOW,
    "Pichu": EXPGroup.MEDIUM_FAST,
    "Pidgeot": EXPGroup.MEDIUM_SLOW,
    "Pidgeotto": EXPGroup.MEDIUM_SLOW,
    "Pidgey": EXPGroup.MEDIUM_SLOW,
    "Pidove": EXPGroup.MEDIUM_SLOW,
    "Pignite": EXPGroup.MEDIUM_SLOW,
    "Pikachu": EXPGroup.MEDIUM_FAST,
    "Pikipek": EXPGroup.MEDIUM_FAST,
    "Piloswine": EXPGroup.SLOW,
    "Pincurchin": EXPGroup.MEDIUM_FAST,
    "Pineco": EXPGroup.MEDIUM_FAST,
    "Pinsir": EXPGroup.SLOW,
    "Piplup": EXPGroup.MEDIUM_SLOW,
    "Plusle": EXPGroup.MEDIUM_FAST,
    "Poipole": EXPGroup.SLOW,
    "Politoed": EXPGroup.MEDIUM_SLOW,
    "Poliwag": EXPGroup.MEDIUM_SLOW,
    "Poliwhirl": EXPGroup.MEDIUM_SLOW,
    "Poliwrath": EXPGroup.MEDIUM_SLOW,
    "Polteageist": EXPGroup.MEDIUM_FAST,
    "Ponyta": EXPGroup.MEDIUM_FAST,
    "Poochyena": EXPGroup.MEDIUM_FAST,
    "Popplio": EXPGroup.MEDIUM_SLOW,
    "Porygon": EXPGroup.MEDIUM_FAST,
    "Porygon2": EXPGroup.MEDIUM_FAST,
    "Porygon-Z": EXPGroup.MEDIUM_FAST,
    "Primarina": EXPGroup.MEDIUM_SLOW,
    "Primeape": EXPGroup.MEDIUM_FAST,
    "Prinplup": EXPGroup.MEDIUM_SLOW,
    "Probopass": EXPGroup.MEDIUM_FAST,
    "Psyduck": EXPGroup.MEDIUM_FAST,
    "Pumpkaboo": EXPGroup.MEDIUM_FAST,
    "Pupitar": EXPGroup.SLOW,
    "Purrloin": EXPGroup.MEDIUM_FAST,
    "Purugly": EXPGroup.FAST,
    "Pyroar": EXPGroup.MEDIUM_SLOW,
    "Pyukumuku": EXPGroup.FAST,
    "Quagsire": EXPGroup.MEDIUM_FAST,
    "Quilava": EXPGroup.MEDIUM_SLOW,
    "Quilladin": EXPGroup.MEDIUM_SLOW,
    "Qwilfish": EXPGroup.MEDIUM_FAST,
    "Raboot": EXPGroup.MEDIUM_SLOW,
    "Raichu": EXPGroup.MEDIUM_FAST,
    "Raikou": EXPGroup.SLOW,
    "Ralts": EXPGroup.SLOW,
    "Rampardos": EXPGroup.ERRATIC,
    "Rapidash": EXPGroup.MEDIUM_FAST,
    "Raticate": EXPGroup.MEDIUM_FAST,
    "Rattata": EXPGroup.MEDIUM_FAST,
    "Rayquaza": EXPGroup.SLOW,
    "Regice": EXPGroup.SLOW,
    "Regigigas": EXPGroup.SLOW,
    "Regirock": EXPGroup.SLOW,
    "Registeel": EXPGroup.SLOW,
    "Relicanth": EXPGroup.SLOW,
    "Remoraid": EXPGroup.MEDIUM_FAST,
    "Reshiram": EXPGroup.SLOW,
    "Reuniclus": EXPGroup.MEDIUM_SLOW,
    "Rhydon": EXPGroup.SLOW,
    "Rhyhorn": EXPGroup.SLOW,
    "Rhyperior": EXPGroup.SLOW,
    "Ribombee": EXPGroup.MEDIUM_FAST,
    "Rillaboom": EXPGroup.MEDIUM_SLOW,
    "Riolu": EXPGroup.MEDIUM_SLOW,
    "Rockruff": EXPGroup.MEDIUM_FAST,
    "Roggenrola": EXPGroup.MEDIUM_SLOW,
    "Rolycoly": EXPGroup.MEDIUM_SLOW,
    "Rookidee": EXPGroup.MEDIUM_SLOW,
    "Roselia": EXPGroup.MEDIUM_SLOW,
    "Roserade": EXPGroup.MEDIUM_SLOW,
    "Rotom": EXPGroup.MEDIUM_FAST,
    "Rowlet": EXPGroup.MEDIUM_SLOW,
    "Rufflet": EXPGroup.SLOW,
    "Runerigus": EXPGroup.MEDIUM_FAST,
    "Sableye": EXPGroup.MEDIUM_SLOW,
    "Salamence": EXPGroup.SLOW,
    "Salandit": EXPGroup.MEDIUM_FAST,
    "Salazzle": EXPGroup.MEDIUM_FAST,
    "Samurott": EXPGroup.MEDIUM_SLOW,
    "Sandaconda": EXPGroup.MEDIUM_FAST,
    "Sandile": EXPGroup.MEDIUM_SLOW,
    "Sandshrew": EXPGroup.MEDIUM_FAST,
    "Sandslash": EXPGroup.MEDIUM_FAST,
    "Sandygast": EXPGroup.MEDIUM_FAST,
    "Sawk": EXPGroup.MEDIUM_FAST,
    "Sawsbuck": EXPGroup.MEDIUM_FAST,
    "Scatterbug": EXPGroup.MEDIUM_FAST,
    "Sceptile": EXPGroup.MEDIUM_SLOW,
    "Scizor": EXPGroup.MEDIUM_FAST,
    "Scolipede": EXPGroup.MEDIUM_SLOW,
    "Scorbunny": EXPGroup.MEDIUM_SLOW,
    "Scrafty": EXPGroup.MEDIUM_FAST,
    "Scraggy": EXPGroup.MEDIUM_FAST,
    "Scyther": EXPGroup.MEDIUM_FAST,
    "Seadra": EXPGroup.MEDIUM_FAST,
    "Seaking": EXPGroup.MEDIUM_FAST,
    "Sealeo": EXPGroup.MEDIUM_SLOW,
    "Seedot": EXPGroup.MEDIUM_SLOW,
    "Seel": EXPGroup.MEDIUM_FAST,
    "Seismitoad": EXPGroup.MEDIUM_SLOW,
    "Sentret": EXPGroup.MEDIUM_FAST,
    "Serperior": EXPGroup.MEDIUM_SLOW,
    "Servine": EXPGroup.MEDIUM_SLOW,
    "Seviper": EXPGroup.FLUCTUATING,
    "Sewaddle": EXPGroup.MEDIUM_SLOW,
    "Sharpedo": EXPGroup.SLOW,
    "Shaymin": EXPGroup.MEDIUM_SLOW,
    "Shedinja": EXPGroup.ERRATIC,
    "Shelgon": EXPGroup.SLOW,
    "Shellder": EXPGroup.SLOW,
    "Shellos": EXPGroup.MEDIUM_FAST,
    "Shelmet": EXPGroup.MEDIUM_FAST,
    "Shieldon": EXPGroup.ERRATIC,
    "Shiftry": EXPGroup.MEDIUM_SLOW,
    "Shiinotic": EXPGroup.MEDIUM_FAST,
    "Shinx": EXPGroup.MEDIUM_SLOW,
    "Shroomish": EXPGroup.FLUCTUATING,
    "Shuckle": EXPGroup.MEDIUM_SLOW,
    "Shuppet": EXPGroup.FAST,
    "Sigilyph": EXPGroup.MEDIUM_FAST,
    "Silcoon": EXPGroup.MEDIUM_FAST,
    "Silicobra": EXPGroup.MEDIUM_FAST,
    "Silvally": EXPGroup.SLOW,
    "Simipour": EXPGroup.MEDIUM_FAST,
    "Simisage": EXPGroup.MEDIUM_FAST,
    "Simisear": EXPGroup.MEDIUM_FAST,
    "Sinistea": EXPGroup.MEDIUM_FAST,
    "Sirfetch'd": EXPGroup.MEDIUM_FAST,
    "Sizzlipede": EXPGroup.MEDIUM_FAST,
    "Skarmory": EXPGroup.SLOW,
    "Skiddo": EXPGroup.MEDIUM_FAST,
    "Skiploom": EXPGroup.MEDIUM_SLOW,
    "Skitty": EXPGroup.FAST,
    "Skorupi": EXPGroup.SLOW,
    "Skrelp": EXPGroup.MEDIUM_FAST,
    "Skuntank": EXPGroup.MEDIUM_FAST,
    "Skwovet": EXPGroup.MEDIUM_FAST,
    "Slaking": EXPGroup.SLOW,
    "Slakoth": EXPGroup.SLOW,
    "Sliggoo": EXPGroup.SLOW,
    "Slowbro": EXPGroup.MEDIUM_FAST,
    "Slowking": EXPGroup.MEDIUM_FAST,
    "Slowpoke": EXPGroup.MEDIUM_FAST,
    "Slugma": EXPGroup.MEDIUM_FAST,
    "Slurpuff": EXPGroup.MEDIUM_FAST,
    "Smeargle": EXPGroup.FAST,
    "Smoochum": EXPGroup.MEDIUM_FAST,
    "Sneasel": EXPGroup.MEDIUM_SLOW,
    "Snivy": EXPGroup.MEDIUM_SLOW,
    "Snom": EXPGroup.MEDIUM_FAST,
    "Snorlax": EXPGroup.SLOW,
    "Snorunt": EXPGroup.MEDIUM_FAST,
    "Snover": EXPGroup.SLOW,
    "Snubbull": EXPGroup.FAST,
    "Sobble": EXPGroup.MEDIUM_SLOW,
    "Solgaleo": EXPGroup.SLOW,
    "Solosis": EXPGroup.MEDIUM_SLOW,
    "Solrock": EXPGroup.FAST,
    "Spearow": EXPGroup.MEDIUM_FAST,
    "Spewpa": EXPGroup.MEDIUM_FAST,
    "Spheal": EXPGroup.MEDIUM_SLOW,
    "Spinarak": EXPGroup.FAST,
    "Spinda": EXPGroup.FAST,
    "Spiritomb": EXPGroup.MEDIUM_FAST,
    "Spoink": EXPGroup.FAST,
    "Spritzee": EXPGroup.MEDIUM_FAST,
    "Squirtle": EXPGroup.MEDIUM_SLOW,
    "Stakataka": EXPGroup.SLOW,
    "Stantler": EXPGroup.SLOW,
    "Staraptor": EXPGroup.MEDIUM_SLOW,
    "Staravia": EXPGroup.MEDIUM_SLOW,
    "Starly": EXPGroup.MEDIUM_SLOW,
    "Starmie": EXPGroup.SLOW,
    "Staryu": EXPGroup.SLOW,
    "Steelix": EXPGroup.MEDIUM_FAST,
    "Steenee": EXPGroup.MEDIUM_SLOW,
    "Stonjourner": EXPGroup.SLOW,
    "Stoutland": EXPGroup.MEDIUM_SLOW,
    "Stufful": EXPGroup.MEDIUM_FAST,
    "Stunfisk": EXPGroup.MEDIUM_FAST,
    "Stunky": EXPGroup.MEDIUM_FAST,
    "Sudowoodo": EXPGroup.MEDIUM_FAST,
    "Suicune": EXPGroup.SLOW,
    "Sunflora": EXPGroup.MEDIUM_SLOW,
    "Sunkern": EXPGroup.MEDIUM_SLOW,
    "Surskit": EXPGroup.MEDIUM_FAST,
    "Swablu": EXPGroup.ERRATIC,
    "Swadloon": EXPGroup.MEDIUM_SLOW,
    "Swalot": EXPGroup.FLUCTUATING,
    "Swampert": EXPGroup.MEDIUM_SLOW,
    "Swanna": EXPGroup.MEDIUM_FAST,
    "Swellow": EXPGroup.MEDIUM_SLOW,
    "Swinub": EXPGroup.SLOW,
    "Swirlix": EXPGroup.MEDIUM_FAST,
    "Swoobat": EXPGroup.MEDIUM_FAST,
    "Sylveon": EXPGroup.MEDIUM_FAST,
    "Taillow": EXPGroup.MEDIUM_SLOW,
    "Talonflame": EXPGroup.MEDIUM_SLOW,
    "Tangela": EXPGroup.MEDIUM_FAST,
    "Tangrowth": EXPGroup.MEDIUM_FAST,
    "Tapu Bulu": EXPGroup.SLOW,
    "Tapu Fini": EXPGroup.SLOW,
    "Tapu Koko": EXPGroup.SLOW,
    "Tapu Lele": EXPGroup.SLOW,
    "Tauros": EXPGroup.SLOW,
    "Teddiursa": EXPGroup.MEDIUM_FAST,
    "Tentacool": EXPGroup.SLOW,
    "Tentacruel": EXPGroup.SLOW,
    "Tepig": EXPGroup.MEDIUM_SLOW,
    "Terrakion": EXPGroup.SLOW,
    "Thievul": EXPGroup.FAST,
    "Throh": EXPGroup.MEDIUM_FAST,
    "Thundurus": EXPGroup.SLOW,
    "Thwackey": EXPGroup.MEDIUM_SLOW,
    "Timburr": EXPGroup.MEDIUM_SLOW,
    "Tirtouga": EXPGroup.MEDIUM_FAST,
    "Togedemaru": EXPGroup.MEDIUM_FAST,
    "Togekiss": EXPGroup.FAST,
    "Togepi": EXPGroup.FAST,
    "Togetic": EXPGroup.FAST,
    "Torchic": EXPGroup.MEDIUM_SLOW,
    "Torkoal": EXPGroup.MEDIUM_FAST,
    "Tornadus": EXPGroup.SLOW,
    "Torracat": EXPGroup.MEDIUM_SLOW,
    "Torterra": EXPGroup.MEDIUM_SLOW,
    "Totodile": EXPGroup.MEDIUM_SLOW,
    "Toucannon": EXPGroup.MEDIUM_FAST,
    "Toxapex": EXPGroup.MEDIUM_FAST,
    "Toxel": EXPGroup.MEDIUM_SLOW,
    "Toxicroak": EXPGroup.MEDIUM_FAST,
    "Toxtricity": EXPGroup.MEDIUM_SLOW,
    "Tranquill": EXPGroup.MEDIUM_SLOW,
    "Trapinch": EXPGroup.MEDIUM_SLOW,
    "Treecko": EXPGroup.MEDIUM_SLOW,
    "Trevenant": EXPGroup.MEDIUM_FAST,
    "Tropius": EXPGroup.SLOW,
    "Trubbish": EXPGroup.MEDIUM_FAST,
    "Trumbeak": EXPGroup.MEDIUM_FAST,
    "Tsareena": EXPGroup.MEDIUM_SLOW,
    "Turtonator": EXPGroup.MEDIUM_FAST,
    "Turtwig": EXPGroup.MEDIUM_SLOW,
    "Tympole": EXPGroup.MEDIUM_SLOW,
    "Tynamo": EXPGroup.SLOW,
    "Type: Null": EXPGroup.SLOW,
    "Typhlosion": EXPGroup.MEDIUM_SLOW,
    "Tyranitar": EXPGroup.SLOW,
    "Tyrantrum": EXPGroup.MEDIUM_FAST,
    "Tyrogue": EXPGroup.MEDIUM_FAST,
    "Tyrunt": EXPGroup.MEDIUM_FAST,
    "Umbreon": EXPGroup.MEDIUM_FAST,
    "Unfezant": EXPGroup.MEDIUM_SLOW,
    "Unown": EXPGroup.MEDIUM_FAST,
    "Ursaring": EXPGroup.MEDIUM_FAST,
    "Uxie": EXPGroup.SLOW,
    "Vanillish": EXPGroup.SLOW,
    "Vanillite": EXPGroup.SLOW,
    "Vanilluxe": EXPGroup.SLOW,
    "Vaporeon": EXPGroup.MEDIUM_FAST,
    "Venipede": EXPGroup.MEDIUM_SLOW,
    "Venomoth": EXPGroup.MEDIUM_FAST,
    "Venonat": EXPGroup.MEDIUM_FAST,
    "Venusaur": EXPGroup.MEDIUM_SLOW,
    "Vespiquen": EXPGroup.MEDIUM_SLOW,
    "Vibrava": EXPGroup.MEDIUM_SLOW,
    "Victini": EXPGroup.SLOW,
    "Victreebel": EXPGroup.MEDIUM_SLOW,
    "Vigoroth": EXPGroup.SLOW,
    "Vikavolt": EXPGroup.MEDIUM_FAST,
    "Vileplume": EXPGroup.MEDIUM_SLOW,
    "Virizion": EXPGroup.SLOW,
    "Vivillon": EXPGroup.MEDIUM_FAST,
    "Volbeat": EXPGroup.ERRATIC,
    "Volcanion": EXPGroup.SLOW,
    "Volcarona": EXPGroup.SLOW,
    "Voltorb": EXPGroup.MEDIUM_FAST,
    "Vullaby": EXPGroup.SLOW,
    "Vulpix": EXPGroup.MEDIUM_FAST,
    "Wailmer": EXPGroup.FLUCTUATING,
    "Wailord": EXPGroup.FLUCTUATING,
    "Walrein": EXPGroup.MEDIUM_SLOW,
    "Wartortle": EXPGroup.MEDIUM_SLOW,
    "Watchog": EXPGroup.MEDIUM_FAST,
    "Weavile": EXPGroup.MEDIUM_SLOW,
    "Weedle": EXPGroup.MEDIUM_FAST,
    "Weepinbell": EXPGroup.MEDIUM_SLOW,
    "Weezing": EXPGroup.MEDIUM_FAST,
    "Whimsicott": EXPGroup.MEDIUM_FAST,
    "Whirlipede": EXPGroup.MEDIUM_SLOW,
    "Whiscash": EXPGroup.MEDIUM_FAST,
    "Whismur": EXPGroup.MEDIUM_SLOW,
    "Wigglytuff": EXPGroup.FAST,
    "Wimpod": EXPGroup.MEDIUM_FAST,
    "Wingull": EXPGroup.MEDIUM_FAST,
    "Wishiwashi": EXPGroup.FAST,
    "Wobbuffet": EXPGroup.MEDIUM_FAST,
    "Woobat": EXPGroup.MEDIUM_FAST,
    "Wooloo": EXPGroup.MEDIUM_FAST,
    "Wooper": EXPGroup.MEDIUM_FAST,
    "Wormadam": EXPGroup.MEDIUM_FAST,
    "Wurmple": EXPGroup.MEDIUM_FAST,
    "Wynaut": EXPGroup.MEDIUM_FAST,
    "Xatu": EXPGroup.MEDIUM_FAST,
    "Xerneas": EXPGroup.SLOW,
    "Xurkitree": EXPGroup.SLOW,
    "Yamask": EXPGroup.MEDIUM_FAST,
    "Yamper": EXPGroup.FAST,
    "Yanma": EXPGroup.MEDIUM_FAST,
    "Yanmega": EXPGroup.MEDIUM_FAST,
    "Yungoos": EXPGroup.MEDIUM_FAST,
    "Yveltal": EXPGroup.SLOW,
    "Zacian": EXPGroup.SLOW,
    "Zamazenta": EXPGroup.SLOW,
    "Zangoose": EXPGroup.ERRATIC,
    "Zapdos": EXPGroup.SLOW,
    "Zebstrika": EXPGroup.MEDIUM_FAST,
    "Zekrom": EXPGroup.SLOW,
    "Zeraora": EXPGroup.SLOW,
    "Zigzagoon": EXPGroup.MEDIUM_FAST,
    "Zoroark": EXPGroup.MEDIUM_SLOW,
    "Zorua": EXPGroup.MEDIUM_SLOW,
    "Zubat": EXPGroup.MEDIUM_FAST,
    "Zweilous": EXPGroup.SLOW,
    "Zygarde": EXPGroup.SLOW,
}

judge_map = {
    "": [0, 31],
    "No Good": [0, 0],
    "Decent": [1, 15],
    "Pretty Good": [16, 25],
    "Very Good": [26, 29],
    "Fantastic": [30, 30],
    "Best": [31, 31]
}