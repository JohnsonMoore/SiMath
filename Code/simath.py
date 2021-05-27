import math
import os
import random
import time
import decimal
import numpy

# Database


teams = [("Bayern", 99, "Germany"),
         ("Liverpool", 97, "England"),
         ("Man City", 97, "England"),
         ("PSG", 97, "France"),
         ("Real Madrid", 95, "Spain"),
         ("Tottenham", 94, "England"),
         ("Juventus", 94, "Italy"),
         ("Barcelona", 94, "Spain"),
         ("Man United", 93, "England"),
         ("Dortmund", 93, "Germany"),
         ("Chelsea", 92, "England"),
         ("Inter Milan", 92, "Italy"),
         ("Atlético Madrid", 92, "Spain"),
         ("Milan", 91, "Italy"),
         ("Arsenal", 90, "England"),
         ("Everton", 89, "England"),
         ("Ajax", 89, "Netherland"),
         ("Sevilla", 89, "Spain"),
         ("West Ham", 88, "England"),
         ("RB Leipzig", 88, "Germany"),
         ("Roma", 88, "Italy"),
         ("Atalanta", 88, "Italy"),
         ("Porto", 88, "Portugal"),
         ("Villarreal", 88, "Spain"),
         ("Leicester", 87, "England"),
         ("Lyon", 87, "France"),
         ("Bayer Leverkusen", 87, "Germany"),
         ("Wolfsburg", 87, "Germany"),
         ("Olympiacos", 87, "Greece"),
         ("Napoli", 87, "Italy"),
         ("Betis", 87, "Spain"),
         ("Wolves", 86, "England"),
         ("Monaco", 86, "France"),
         ("B. Mönchengladbach", 86, "Germany"),
         ("Schalke", 86, "Germany"),
         ("Lazio", 86, "Italy"),
         ("Benfica", 86, "Portugal"),
         ("Sporting Lisboa", 86, "Portugal"),
         ("CSKA Moscow", 86, "Russia"),
         ("Levante", 86, "Spain"),
         ("Shakhtar Donetsk", 86, "Ukraine"),
         ("Werder", 85, "Germany"),
         ("Udinese", 85, "Italy"),
         ("PSV", 85, "Netherland"),
         ("Rubin", 85, "Russia"),
         ("Valencia", 85, "Spain"),
         ("Athletic", 85, "Spain"),
         ("Beşiktaş", 85, "Turkey"),
         ("Burnley", 84, "England"),
         ("Lille", 84, "France"),
         ("Hoffenheim", 84, "Germany"),
         ("Frankfurt", 84, "Germany"),
         ("PAOK", 84, "Greece"),
         ("Fiorentina", 84, "Italy"),
         ("Sp. Braga", 84, "Portugal"),
         ("Zenit", 84, "Russia"),
         ("Celtic", 84, "Scotland"),
         ("Getafe", 84, "Spain"),
         ("Real Sociedad", 84, "Spain"),
         ("Brugge", 83, "Belgium"),
         ("Crystal Palace", 83, "England"),
         ("Marseille", 83, "France"),
         ("AEK", 83, "Greece"),
         ("Feyenoord", 83, "Netherland"),
         ("Moscow Spartak", 83, "Russia"),
         ("Moscow Lokomotiv", 83, "Russia"),
         ("Rangers", 83, "Scotland"),
         ("RB Salzburg", 82, "Austria"),
         ("Southampton", 82, "England"),
         ("Brighton", 82, "England"),
         ("Stuttgart", 82, "Germany"),
         ("Panathinaikos", 82, "Greece"),
         ("Torino", 82, "Italy"),
         ("Hellas Verona", 82, "Italy"),
         ("Bodø Glimt", 82, "Norway"),
         ("Nacional", 82, "Portugal"),
         ("Krasnodar", 82, "Russia"),
         ("Espanyol", 82, "Spain"),
         ("Basel", 82, "Switzerland"),
         ("Fenerbahçe", 82, "Turkey"),
         ("Anderlecht", 81, "Belgium"),
         ("Dinamo Zagreb", 81, "Croatia"),
         ("Newcastle", 81, "England"),
         ("Montpellier", 81, "France"),
         ("Mainz", 81, "Germany"),
         ("Köln", 81, "Germany"),
         ("Bologna", 81, "Italy"),
         ("AZ", 81, "Netherland"),
         ("Guimarães", 81, "Portugal"),
         ("Rostov", 81, "Russia"),
         ("Celta", 81, "Spain"),
         ("Rayo Vallecano", 81, "Spain"),
         ("Granada", 81, "Spain"),
         ("Young Boys", 81, "Switzerland"),
         ("Galatasaray", 81, "Turkey"),
         ("Dynamo Kyiv", 81, "Ukraine"),
         ("Bournemouth", 80, "England"),
         ("Watford", 80, "England"),
         ("Stoke", 80, "England"),
         ("Santos", 80, "Brazil"),
         ("Toulouse", 80, "France"),
         ("Sampdoria", 80, "Italy"),
         ("Dynamo Moscow", 80, "Russia"),
         ("Valladolid", 80, "Spain"),
         ("Başaksehir", 80, "Turkey"),
         ("FC København", 79, "Denmark"),
         ("Fulham", 79, "England"),
         ("Swansea", 79, "England"),
         ("Aston Villa", 79, "England"),
         ("Boca Juniors", 79, "Argentina"),
         ("Saint-Étienne", 79, "France"),
         ("Rennes", 79, "France"),
         ("Augsburg", 79, "Germany"),
         ("Panionios", 79, "Greece"),
         ("Sassuolo", 79, "Italy"),
         ("Parma", 79, "Italy"),
         ("Genoa", 79, "Italy"),
         ("Steaua Bucharest", 79, "Romania"),
         ("Leganés", 79, "Spain"),
         ("Mallorca", 79, "Spain"),
         ("Osasuna", 79, "Spain"),
         ("Cádiz", 79, "Spain"),
         ("Trabzonspor", 79, "Turkey"),
         ("LASK Linz", 78, "Austria"),
         ("Sparta Prague", 78, "Czech"),
         ("Cardiff", 78, "England"),
         ("Leeds Utd", 78, "England"),
         ("Nantes", 78, "France"),
         ("Reims", 78, "France"),
         ("Corinthians", 78, "Brazil"),
         ("River Plate", 78, "Argentina"),
         ("Hamburg", 78, "Germany"),
         ("SPAL", 78, "Italy"),
         ("Cagliari", 78, "Italy"),
         ("Groningen", 78, "Netherland"),
         ("Red Star", 78, "Serbia"),
         ("Elche", 78, "Spain"),
         ("Zorya", 78, "Ukraine"),
         ("Nice", 77, "France"),
         ("São Paulo", 77, "Brazil"),
         ("Independiente", 77, "Argentina"),
         ("Hertha BSC", 77, "Germany"),
         ("Freiburg", 77, "Germany"),
         ("Paderborn", 77, "Germany"),
         ("Aris", 77, "Greece"),
         ("Ferencváros", 77, "Hungary"),
         ("Lecce", 77, "Italy"),
         ("Chievo", 77, "Italy"),
         ("América", 77, "Mexico"),
         ("Guadalajara", 77, "Mexico"),
         ("Rosenborg", 77, "Norway"),
         ("Cluj", 77, "Romania"),
         ("Monterrey", 77, "Mexico"),
         ("Málaga", 77, "Spain"),
         ("Alanyaspor", 77, "Turkey"),
         ("Genk", 76, "Belgium"),
         ("Viktoria Plzeň", 76, "Czech"),
         ("West Brom", 76, "England"),
         ("Derby", 76, "England"),
         ("Girondins", 76, "France"),
         ("Hannover", 76, "Germany"),
         ("Darmstadt", 76, "Germany"),
         ("Union Berlin", 76, "Germany"),
         ("Utrecht", 76, "Netherland"),
         ("Rio Ave", 76, "Portugal"),
         ("Sporting Gijón", 76, "Spain"),
         ("Girona", 76, "Spain"),
         ("Huesca", 76, "Spain"),
         ("St. Gallen", 76, "Switzerland"),
         ("Gent", 75, "Belgium"),
         ("Standard", 75, "Belgium"),
         ("Ludogorets", 75, "Bulgaria"),
         ("Slovan Liberec", 75, "Czech"),
         ("Slavia Prague", 75, "Czech"),
         ("Brøndby", 75, "Denmark"),
         ("Huddersfield", 75, "England"),
         ("Norwich", 75, "England"),
         ("Sheff Utd", 75, "England"),
         ("Nîmes", 75, "France"),
         ("Holstein Kiel", 75, "Germany"),
         ("Atletico Nacional", 75, "Columbia"),
         ("Grêmio", 75, "Brazil"),
         ("San Lorenzo", 75, "Argentina"),
         ("Rosario Central", 75, "Argentina"),
         ("Racing", 75, "Argentina"),
         ("Guangzhou", 75, "China"),
         ("Atromitos", 75, "Greece"),
         ("Palaio Faliro", 75, "Greece"),
         ("M. Tel-Aviv", 75, "Israel"),
         ("Twente", 75, "Netherland"),
         ("Legia", 75, "Poland"),
         ("U Craiova", 75, "Romania"),
         ("Zaragoza", 75, "Spain"),
         ("Santos Laguna", 75, "Mexico"),
         ("Sivasspor", 75, "Turkey"),
         ("Wolfsberger", 74, "Austria"),
         ("Rijeka", 74, "Croatia"),
         ("APOEL", 74, "Cyprus"),
         ("Midtjylland", 74, "Denmark"),
         ("QPR", 74, "England"),
         ("Strasbourg", 74, "France"),
         ("Nürnberg", 74, "Germany"),
         ("Greuther Fürth", 74, "Germany"),
         ("Bochum", 74, "Germany"),
         ("Peñarol", 74, "Uruguay"),
         ("Olimpia", 74, "Paraguay"),
         ("Internacional", 74, "Brazil"),
         ("Estudiantes", 74, "Argentina"),
         ("Lanus", 74, "Argentina"),
         ("Brescia", 74, "Italy"),
         ("Molde", 74, "Norway"),
         ("Partizan", 74, "Serbia"),
         ("Spartak Trnava", 74, "Slovakia"),
         ("Maribor", 74, "Slovenia"),
         ("Alavés", 74, "Spain"),
         ("Eibar", 74, "Spain"),
         ("Almería", 74, "Spain"),
         ("Las Palmas", 74, "Spain"),
         ("Malmö", 74, "Sweden"),
         ("LA Galaxy", 74, "USA"),
         ("Hajduk", 73, "Croatia"),
         ("Middlesboro", 73, "England"),
         ("Reading", 73, "England"),
         ("Nottm Forest", 73, "England"),
         ("Brentford", 73, "England"),
         ("Karlsruhe", 73, "Germany"),
         ("Asteras", 73, "Greece"),
         ("PAS Giannena", 73, "Greece"),
         ("Nacional", 73, "Uruguay"),
         ("Alianza Lima", 73, "Peru"),
         ("Cerro Porteño", 73, "Paraguay"),
         ("Al-Ahly", 73, "Egypt"),
         ("Barcelona SC", 73, "Ecuador"),
         ("Millonarios", 73, "Columbia"),
         ("Palmeiras", 73, "Brazil"),
         ("Shanghai Port", 73, "China"),
         ("Persepolis", 73, "Iran"),
         ("Kawasaki Frontale", 73, "Japan"),
         ("Frosinone", 73, "Italy"),
         ("NEC", 73, "Netherland"),
         ("Marítimo", 73, "Portugal"),
         ("Slovan Bratislava", 73, "Slovakia"),
         ("Olimpija", 73, "Slovenia"),
         ("Kolos Kovalivka", 73, "Ukraine"),
         ("Salt Lake", 73, "USA"),
         ("Austria Vienna", 72, "Austria"),
         ("Qarabag", 72, "Azerbaijian"),
         ("BATE Borisov", 72, "Belarus"),
         ("OB", 72, "Denmark"),
         ("Dijon", 72, "France"),
         ("Valenciennes", 72, "France"),
         ("Emelec", 72, "Ecuador"),
         ("Indep. Del Valle", 72, "Ecuador"),
         ("Colo Colo", 72, "Chile"),
         ("Fluminense", 72, "Brazil"),
         ("Espérance", 72, "Tunisia"),
         ("Beijing Guoan", 72, "China"),
         ("Al-Hilal", 72, "Saudi Arabia"),
         ("Jeonbuk", 72, "South Korea"),
         ("Ulsan", 72, "South Korea"),
         ("Empoli", 72, "Italy"),
         ("Benevento", 72, "Italy"),
         ("Ascoli", 72, "Italy"),
         ("Lech", 72, "Poland"),
         ("Slovan Liberec", 72, "Slovakia"),
         ("AIK", 72, "Sweden"),
         ("FC Zürich", 72, "Switzerland"),
         ("Angers", 71, "France"),
         ("St. Pauli", 71, "Germany"),
         ("Fortuna Düsseldorf", 71, "Germany"),
         ("Defensor Sporting", 71, "Uruguay"),
         ("Universitario", 71, "Peru"),
         ("Libertad", 71, "Paraguay"),
         ("América Cali", 71, "Columbia"),
         ("U Católica", 71, "Chile"),
         ("Flamengo", 71, "Brazil"),
         ("Newell's", 71, "Argentina"),
         ("Shandong Taishan", 71, "China"),
         ("ES Sétif", 71, "Algeria"),
         ("TP Mazembe", 71, "DR Congo"),
         ("Wydad", 71, "Morocco"),
         ("Sepahan", 71, "Iran"),
         ("Urawa Reds", 71, "Japan"),
         ("Livorno", 71, "Italy"),
         ("Astana", 71, "Kahzakstan"),
         ("Aberdeen", 71, "Scotland"),
         ("Hajduk Kula", 71, "Serbia"),
         ("Celje", 71, "Slovenia"),
         ("Lugano", 71, "Switzerland"),
         ("Kansas City", 71, "USA"),
         ("Rapid Vienna", 70, "Austria"),
         ("Shakhtyor Soligorsk", 70, "Belarus"),
         ("Omonia", 70, "Cyprus"),
         ("Hull", 70, "England"),
         ("Sheff Wed", 70, "England"),
         ("Barnsley", 70, "England"),
         ("Arminia Bielefeld", 70, "Germany"),
         ("Apollon Smyrni", 70, "Greece"),
         ("Cristal", 70, "Peru"),
         ("LDU Quito", 70, "Ecuador"),
         ("Mineiro", 70, "Brazil"),
         ("Bolívar", 70, "Bolivia"),
         ("Mimosa", 70, "Cote D'Ivoire"),
         ("Zamalek", 70, "Egypt"),
         ("Sundowns", 70, "South Africa"),
         ("Al-Sadd", 70, "Qatar"),
         ("Olimpia", 70, "Honduras"),
         ("Fuenlabrada", 70, "Spain"),
         ("Barcelona B", 70, "Spain"),
         ("Grasshopper", 70, "Switzerland"),
         ("Seattle", 70, "USA"),
         ("Admira", 69, "Austria"),
         ("Wigan", 69, "England"),
         ("Heidenheim", 69, "Germany"),
         ("Lamia", 69, "Greece"),
         ("Fehérvár", 69, "Hungary"),
         ("Melbourne V", 69, "Australia"),
         ("Shanghai Shenhua", 69, "China"),
         ("Caracas", 69, "Venezuela"),
         ("Zamora", 69, "Venezuela"),
         ("Torque", 69, "Uruguay"),
         ("Binacional", 69, "Peru"),
         ("Guaraní", 69, "Paraguay"),
         ("El Nacional", 69, "Ecuador"),
         ("Delfín", 69, "Ecuador"),
         ("Dep. Cali", 69, "Columbia"),
         ("U. de Chile", 69, "Chile"),
         ("Cruzeiro", 69, "Brazil"),
         ("Vélez", 69, "Argentina"),
         ("Spezia", 69, "Italy"),
         ("Palermo", 69, "Italy"),
         ("Crotone", 69, "Italy"),
         ("Esteghlal", 69, "Iran"),
         ("Kabylie", 69, "Algeria"),
         ("Nkana", 69, "Zambia"),
         ("Gyeongnam", 69, "South Korea"),
         ("Pakhtakor Tashkent", 69, "Uzbekistan"),
         ("Tromsø", 69, "Norway"),
         ("Jagiellonia", 69, "Poland"),
         ("Hibernian", 69, "Scotland"),
         ("Deportivo", 69, "Spain"),
         ("Lugo", 69, "Spain"),
         ("Real Madrid Castilla", 69, "Spain"),
         ("Djurgården", 69, "Sweden"),
         ("Altay", 69, "Turkey"),
         ("Portland", 69, "USA"),
         ("Montreal", 69, "USA"),
         ("Toronto FC", 69, "Canada"),
         ("Vancouver Whitecaps", 69, "Canada"),
         ("CSKA Sofia", 68, "Bulgaria"),
         ("Lokomotiv Sofia", 68, "Bulgaria"),
         ("Apollon Limassol", 68, "Cyprus"),
         ("AGF", 68, "Denmark"),
         ("Caen", 68, "France"),
         ("Lorient", 68, "France"),
         ("Erzgebirge Aue", 68, "Germany"),
         ("Larissa", 68, "Greece"),
         ("Melbourne City", 68, "Australia"),
         ("Henan Songshan Longmen", 68, "China"),
         ("Sport Boys", 68, "Peru"),
         ("The Strongest", 68, "Bolivia"),
         ("Kashima", 68, "Japan"),
         ("Étoile Sahel", 68, "Tunisia"),
         ("Al-Ittihad", 68, "Saudi Arabia"),
         ("Istiklol", 68, "Tajikistan"),
         ("Górnik Z.", 68, "Poland"),
         ("Alcorcón", 68, "Spain"),
         ("Racing Santander", 68, "Spain"),
         ("Hammarby", 68, "Sweden"),
         ("Dinamo Brest", 67, "Belarus"),
         ("Charlton", 67, "England"),
         ("Birmingham", 67, "England"),
         ("Lens", 67, "France"),
         ("Kerkyra", 67, "Greece"),
         ("H. Be'er Sheva", 67, "Israel"),
         ("Saprissa", 67, "Costa Rica"),
         ("Vaduz", 67, "Lichtenstein"),
         ("Guangzhou City", 67, "China"),
         ("Dep. Táchira", 67, "Venezuela"),
         ("Rentistas", 67, "Uruguay"),
         ("Club Nacional", 67, "Paraguay"),
         ("Cobresal", 67, "Chile"),
         ("Unión Española", 67, "Chile"),
         ("Gamba Osaka", 67, "Japan"),
         ("Pyramids", 67, "Egypt"),
         ("Raja Casablanca", 67, "Morocco"),
         ("Heartland", 67, "Nigeria"),
         ("Orlando Pirates", 67, "South Africa"),
         ("Al-Duhail", 67, "Qatar"),
         ("Pohang", 67, "South Korea"),
         ("Muangthong", 67, "Thailand"),
         ("Al-Wahda", 67, "UAE"),
         ("Tenerife", 67, "Spain"),
         ("Levski", 66, "Bulgaria"),
         ("HNK Gorica", 66, "Croatia"),
         ("Anorthosis", 66, "Cyprus"),
         ("Amiens", 66, "France"),
         ("Cittadella", 66, "Italy"),
         ("Sydney", 66, "Australia"),
         ("Brisbane", 66, "Australia"),
         ("Tractor", 66, "Iran"),
         ("Sanfrecce", 66, "Japan"),
         ("Horoya AC", 66, "Guinea"),
         ("Árabe Unido Colón", 66, "Panama"),
         ("Forge FC", 66, "Canada"),
         ("Forge FC", 66, "Canada"),
         ("Blackburn", 65, "England"),
         ("Ajaccio", 65, "France"),
         ("Dynamo Dresden", 65, "Germany"),
         ("Panachaiki", 65, "Greece"),
         ("Xanthi", 65, "Greece"),
         ("Pisa", 65, "Italy"),
         ("Kairat Almaty", 65, "Kahzakstan"),
         ("Chongqing Liangjiang Athletic", 65, "China"),
         ("U. San Martín", 65, "Peru"),
         ("Once Caldas", 65, "Columbia"),
         ("Jorge Wilstermann", 65, "Bolivia"),
         ("Yokohama FM", 65, "Japan"),
         ("CR Belouizdad", 65, "Algeria"),
         ("Coton Sport", 65, "Cameroon"),
         ("FAR Rabat", 65, "Morocco"),
         ("Kaizer Chiefs", 65, "South Africa"),
         ("Al-Hilal Club", 65, "Sudan"),
         ("Suwon SB", 65, "South Korea"),
         ("Al-Ain", 65, "UAE"),
         ("AEK Larnaca", 64, "Cyprus"),
         ("Osnabrück", 64, "Germany"),
         ("OFI", 64, "Greece"),
         ("Panthrakikos", 64, "Greece"),
         ("Pierikos", 64, "Greece"),
         ("Puskas", 64, "Hungary"),
         ("Herediano", 64, "Costa Rica"),
         ("Venezia", 64, "Italy"),
         ("Motagua", 64, "Honduras"),
         ("Newcastle", 64, "Australia"),
         ("Hebei", 64, "China"),
         ("Oriente Petrolero", 64, "Bolivia"),
         ("AS Vita Club", 64, "DR Congo"),
         ("Club Africain", 64, "Tunisia"),
         ("FC Seoul", 64, "South Korea"),
         ("Bangkok United", 64, "Thailand"),
         ("Neftchi Farg'ona", 64, "Uzbekistan"),
         ("Odd", 64, "Norway"),
         ("Mirandes", 64, "Spain"),
         ("Örebro", 64, "Sweden"),
         ("Guingamp", 63, "France"),
         ("Metz", 63, "France"),
         ("Kastoria", 63, "Greece"),
         ("Panetolikos", 63, "Greece"),
         ("Alajuelense", 63, "Costa Rica"),
         ("Pescara", 63, "Italy"),
         ("Western Sydney Wanderers", 63, "Australia"),
         ("Shenzhen", 63, "China"),
         ("Portuguesa", 63, "Venezuela"),
         ("Danubio", 63, "Uruguay"),
         ("Sol de América", 63, "Paraguay"),
         ("Junior", 63, "Columbia"),
         ("San José", 63, "Bolivia"),
         ("April 25", 63, "North Korea"),
         ("Al-Gharafa", 63, "Qatar"),
         ("Al-Taawon", 63, "Saudi Arabia"),
         ("USM Alger", 63, "Algeria"),
         ("Petro de Luanda", 63, "Angola"),
         ("Canon Yaounde", 63, "Cameroon"),
         ("Africa Sports", 63, "Cote D'Ivoire"),
         ("Al Ittihad", 63, "Libya"),
         ("Enyimba", 63, "Nigeria"),
         ("ZESCO United", 63, "Zambia"),
         ("Alianza FC", 63, "El Salvador"),
         ("Municipal", 63, "Guatemala"),
         ("Sandhausen", 62, "Germany"),
         ("Ilioupoli", 62, "Greece"),
         ("Veria", 62, "Greece"),
         ("Salernitana", 62, "Italy"),
         ("Tauro F.C", 62, "Panama"),
         ("Comunicaciones", 62, "Guatemala"),
         ("Olympiakos Nikosia", 61, "Cyprus"),
         ("Jahn Regensburg", 61, "Germany"),
         ("B. Jerusalem", 61, "Israel"),
         ("Perugia", 61, "Italy"),
         ("Dalian Pro", 61, "China"),
         ("Always Ready", 61, "Bolivia"),
         ("Chiangrai United", 61, "Thailand"),
         ("DC Motema Pembe", 61, "DR Congo"),
         ("Ajax CT", 61, "South Africa"),
         ("Albacete", 61, "Spain"),
         ("Wehen", 60, "Germany"),
         ("Diagoras", 60, "Greece"),
         ("Levadiakos", 60, "Greece"),
         ("Volos NFC", 60, "Greece"),
         ("Audax Italiano", 60, "Chile"),
         ("Simba", 60, "Tanzania"),
         ("Diriangén", 60, "Nicaragua"),
         ("Dinamo Minsk", 59, "Belarus"),
         ("Le Havre", 59, "France"),
         ("Ethnikos Piraeus", 59, "Greece"),
         ("MTK", 59, "Hungary"),
         ("Real España", 59, "Honduras"),
         ("Tianjin Jinmen Tiger", 59, "China"),
         ("Estudiantes", 59, "Venezuela"),
         ("Buriram", 59, "Thailand"),
         ("UMS de Loum", 59, "Cameroon"),
         ("Hearts of Oak", 59, "Ghana"),
         ("Hafia FC", 59, "Guinea"),
         ("Sunshine Stars", 59, "Nigeria"),
         ("FAS", 59, "El Salvador"),
         ("1860 München", 58, "Germany"),
         ("Iraklis", 58, "Greece"),
         ("Wuhan", 58, "China"),
         ("Al-Zawra'a", 58, "Iraq"),
         ("Santa Fe", 58, "Mexico"),
         ("Real Estelí", 58, "Nicaragua"),
         ("Châteauroux", 57, "France"),
         ("M. Haifa", 57, "Israel"),
         ("Deportivo La Guaira", 57, "Nigeria"),
         ("Shooting Stars", 57, "Nigeria"),
         ("Al-Merrikh SC", 57, "Sudan"),
         ("Águila", 57, "El Salvador"),
         ("Kaiserslautern", 56, "Germany"),
         ("Rot-Weiss Essen", 56, "Germany"),
         ("Al-Ahli", 56, "UAE"),
         ("Lokomotiv Tashkent", 56, "Uzbekistan"),
         ("Primeiro de Agosto", 56, "Angola"),
         ("Al Ahli", 56, "Libya"),
         ("Dynamos", 56, "Zimbabwe"),
         ("Portmore United", 56, "Jamaica"),
         ("Qäbälä", 55, "Azerbaijian"),
         ("Le Mans", 55, "France"),
         ("Juve Stabia", 55, "Italy"),
         ("Changchun Yatai", 55, "China"),
         ("Al-Shorta", 55, "Iraq"),
         ("Clermont", 54, "France"),
         ("Olympiakos Volou", 54, "Greece"),
         ("Újpest", 54, "Hungary"),
         ("Virtus Entella", 54, "Italy"),
         ("Cosenza", 54, "Italy"),
         ("AS Kaloum Star", 54, "Guinea"),
         ("Ferroviário de Maputo", 54, "Mozambique"),
         ("Belmopan Bandits", 54, "Belize"),
         ("Platanias", 53, "Greece"),
         ("Cremonese", 53, "Italy"),
         ("Qingdao", 53, "China"),
         ("Eastern", 53, "Hong Kong"),
         ("Al-Quwa", 53, "Iraq"),
         ("TKC Yaoundé", 53, "Cameroon"),
         ("Kotoko", 53, "Ghana"),
         ("Young Africans", 53, "Tanzania"),
         ("Violette AC", 53, "Haiti"),
         ("Al-Wehdat", 52, "Jordan"),
         ("Al-Shabab", 52, "UAE"),
         ("Siena", 51, "Italy"),
         ("Shkendija 79", 51, "Northern Macedonia"),
         ("Cangzhou Mighty Lions", 51, "China"),
         ("Kitchee", 51, "Hong Kong"),
         ("B. Chelsea", 51, "Ghana"),
         ("Djoliba AC", 51, "Mali"),
         ("Waterhouse", 51, "Jamaica"),
         ("Defence Force", 51, "Trinidad and Tobago"),
         ("Orleans", 50, "France"),
         ("Saarbrücken", 50, "Germany"),
         ("HJK", 49, "Finland"),
         ("Shanghai Yellow Chick", 49, "China"),
         ("Wofoo Taipo", 49, "Hong Kong"),
         ("Al-Faisaly", 49, "Jordan"),
         ("FC Platinum", 49, "Zimbabwe"),
         ("Stade Lausanne-Ouchy", 49, "Switzerland"),
         ("Cibao FC", 49, "Dominican Republic"),
         ("Dundalk", 48, "Ireland"),
         ("Vardar Skopje", 48, "Northern Macedonia"),
         ("Bravo", 48, "Slovenia"),
         ("Viettel", 48, "Vietnam"),
         ("Costa do Sol", 48, "Mozambique"),
         ("Sūduva", 47, "Lithuania"),
         ("Valletta", 47, "Malta"),
         ("Sheriff", 47, "Moldova"),
         ("ATK", 47, "India"),
         ("Warriors", 47, "Singapore"),
         ("Club Franciscain", 47, "Martinique"),
         ("Dinamo Tbilisi", 46, "Georgia"),
         ("Valur", 46, "Iceland"),
         ("Shamrock", 46, "Ireland"),
         ("Riga FC", 46, "Latvia"),
         ("Turnovo", 46, "Northern Macedonia"),
         ("South China", 46, "Hong Kong"),
         ("Ceres-Negros", 46, "Philippines"),
         ("Racing Club Aruba", 45, "Aruba"),
         ("Dudelange", 45, "Luxembourg"),
         ("Ha Noi T&T", 45, "Vietnam"),
         ("Stade Malien", 45, "Mali"),
         ("Robinhood", 45, "Suriname"),
         ("Dep. Nacional", 44, "Aruba"),
         ("KR", 44, "Iceland"),
         ("Zalgiris", 44, "Lithuania"),
         ("CRKSV Jong Holland", 44, "Curaçao"),
         ("Saburtalo", 43, "Georgia"),
         ("ÍBV", 43, "Iceland"),
         ("Bohemians", 43, "Ireland"),
         ("FC Daugava", 43, "Latvia"),
         ("Hibernians", 43, "Malta"),
         ("CS Moulien", 43, "Guadeloupe"),
         ("Inter Turku", 42, "Finland"),
         ("KuPS", 42, "Finland"),
         ("Stjarnan", 42, "Iceland"),
         ("Kauro Žalgiris", 42, "Lithuania"),
         ("Birkirkara", 42, "Malta"),
         ("Floriana", 42, "Malta"),
         ("Sutjeska Nikšić", 42, "Montenegro"),
         ("Sileks", 42, "Northern Macedonia"),
         ("Johor Darul Ta'zim", 42, "Malaysia"),
         ("Zrinjski", 41, "Bosnia"),
         ("Torpedo Kutaisi", 41, "Georgia"),
         ("Dakota", 41, "Aruba"),
         ("Víkingur", 41, "Iceland"),
         ("Cork", 41, "Ireland"),
         ("Jūurmala", 41, "Latvia"),
         ("Sliema", 41, "Malta"),
         ("Dacia", 41, "Moldova"),
         ("Skonto", 40, "Latvia"),
         ("Buducnost", 40, "Montenegro"),
         ("The New Saints", 40, "Wales"),
         ("Flamurtari Vlorë", 39, "Albania"),
         ("Flora", 39, "Estonia"),
         ("RoPS", 39, "Finland"),
         ("Estrella", 39, "Aruba"),
         ("Linfield", 39, "Northern Ireland"),
         ("FC Altyn Asyr", 39, "Turkmenistan"),
         ("PHC Zebras", 39, "Bermuda"),
         ("Ararat", 38, "Armenia"),
         ("Sarajevo", 38, "Bosnia"),
         ("Britannia", 38, "Aruba"),
         ("KF Tirana", 37, "Albania"),
         ("Zeljeznicar", 37, "Bosnia"),
         ("Shan United", 37, "Myanmar"),
         ("Levadia", 36, "Estonia"),
         ("Nõmme Kalju", 36, "Estonia"),
         ("Paide", 36, "Estonia"),
         ("Crusaders", 36, "Northern Ireland"),
         ("Ansar", 36, "Lebanon"),
         ("Skënderbeu", 35, "Albania"),
         ("La Fama", 35, "Aruba"),
         ("Pyunik", 34, "Armenia"),
         ("Al-Jaish", 34, "Syria"),
         ("Bubali", 33, "Aruba"),
         ("Racing FC", 33, "Luxembourg"),
         ("KÍ", 31, "Faroe Islands"),
         ("Taipower", 31, "Chinese Taipei"),
         ("Yangon United", 31, "Myanmar"),
         ("HB", 30, "Faroe Islands"),
         ("Tatung", 30, "Chinese Taipei"),
         ("Port Talbot", 30, "Wales"),
         ("Shirak", 29, "Armenia"),
         ("B36", 29, "Faroe Islands"),
         ("Caiquetio", 29, "Aruba"),
         ("Taiwan Steel", 29, "Chinese Taipei"),
         ("Aberystwyth", 29, "Wales"),
         ("Benfica de Macau", 28, "Macau"),
         ("Hang Yuen", 27, "Chinese Taipei"),
         ("Chao Pei Kai", 27, "Macau"),
         ("Auckland City", 23, "New Zealand"),
         ("Lincoln FC", 22, "Gibraltar"),
         ("FC Santa Coloma", 21, "Andorra"),
         ("Tre Fiori", 21, "San Marino"),
         ("Jong Aruba", 19, "Aruba"),
         ("Ba", 19, "Fiji"),
         ("Sant Julià", 18, "Andorra"),
         ("Libertas", 18, "San Marino"),
         ("River Plate", 17, "Aruba"),
         ("Magenta", 17, "New Caledonia"),
         ("Waitakere United", 17, "New Zealand"),
         ("Central-Sport Papeete", 17, "Tahiti"),
         ("Nadi", 16, "Fiji"),
         ("Wollongong Wolves", 16, "New Zealand"),
         ("Koloale", 16, "Solomon Islands"),
         ("Tafea", 16, "Vanuatu"),
         ("Manchester 62", 15, "Gibraltar"),
         ("Hekari United", 15, "Papua New Guinea"),
         ("Kiwi", 15, "Samoa"),
         ("Europa FC", 14, "Gibraltar"),
         ("Lautoka", 14, "Fiji"),
         ("Team Weillington", 14, "New Zealand"),
         ("AS Pirae", 14, "Tahiti"),
         ("Amicale", 14, "Vanuatu"),
         ("JS Baco", 13, "New Caledonia"),
         ("AS Vénus", 13, "Tahiti"),
         ("Tupapa Maraerenga", 12, "Cook Islands"),
         ("Lupe ole Soaga", 12, "Samoa"),
         ("Kossa", 12, "Solomon Islands"),
         ("Tefana", 12, "Tahiti"),
         ("Loto Ha'apai FC", 11, "Tonga"),
         ("Hienghène Sport", 9, "New Caledonia"),
         ("Sobou", 9, "Papua New Guinea")]

stocks_org = [['Apple', 130.21, 0, 0, 0, 0],
              ['Facebook', 319.08, 0, 0, 0, 0],
              ['Baidu', 191.55, 0, 0, 0, 0],
              ['Alibaba', 225.31, 0, 0, 0, 0],
              ['Google', 2351.93, 0, 0, 0, 0],
              ['Tesla', 672.37, 0, 0, 0, 0],
              ['Coca Cola ', 54.51, 0, 0, 0, 0],
              ['Honeywell', 228.79, 0, 0, 0, 0],
              ['Twitter', 53.79, 0, 0, 0, 0],
              ['Bilibili', 101.67, 0, 0, 0, 0]]


def flatten(l, ltypes=(list, tuple)):
    ltype = type(l)
    l = list(l)
    i = 0
    while i < len(l):
        while isinstance(l[i], ltypes):
            if not l[i]:
                l.pop(i)
                i -= 1
                break
            else:
                l[i:i + 1] = l[i]
        i += 1
    return ltype(l)


# The Main System


def intro():
    print('''╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                   _____   _____  ___  ___   ___    _____   _   _                                    ║
║                                  /  ___| |_   _| |  \/  |  / _ \  |_   _| | | | |                                   ║
║                                  \ `--.    | |   | .  . | / /_\ \   | |   | |_| |                                   ║
║                                   `--. \   | |   | |\/| | |  _  |   | |   |  _  |                                   ║
║                                  /\__/ /  _| |_  | |  | | | | | |   | |   | | | |                                   ║
║                                  \____/   \___/  \_|  |_/ \_| |_/   \_/   \_| |_/                                   ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                          Former Vitrual-Vitrual Simulator                                           ║
║                                                                                                                     ║
║                                                 Basic Version 1.0                                                   ║
║                                                                                                                     ║
║                                              Press Enter to Continue...                                             ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝''')
    input()
    os.system('cls')
    startmenu()


def startmenu():
    c = input('''╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                              ╔═══════════════════════╗                                              ║
║                                              ║       Start Menu      ║                                              ║
║                                              ║                       ║                                              ║
║                                              ║  1.    New Game       ║                                              ║
║                                              ║  2.    Load Game      ║                                              ║
║                                              ║  3.    About          ║                                              ║
║                                              ║  4.    Quit Game      ║                                              ║
║                                              ║                       ║                                              ║
║                                              ╚═══════════════════════╝                                              ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
''')
    if c == '1':
        os.system('cls')
        name = yourname()
        os.system('cls')
        birthday = yourbirth()
        os.system('cls')
        money, happiness, fame, health = diffc()
        year = 2021
        month = 1
        day = 1
        dayday = 5
        timep = -1
        stocks = stocks_org
        ability = [0, 0, 0, 0, 0, 0]
        matharc = []
        music = []
        film = []
        litr = []
        paintt = []
        store = [0, 0, 0, 0, 0]
        saveloan = []
        myclub = []
        days = 0
        mainmenu(money, happiness, fame, health, name, year, month, day, dayday, timep, stocks, ability, matharc, music,
                 film, litr, paintt, birthday, store, saveloan, myclub, days)
    elif c == '2':
        money, happiness, fame, health, name, year, month, day, dayday, timep, stocks, ability, matharc, music, film, litr, paintt, birthday, store, saveloan, myclub, days = loaddddd(
            stocks_org)
        if money != -1:
            mainmenu(money, happiness, fame, health, name, year, month, day, dayday, timep, stocks, ability, matharc,
                     music, film, litr, paintt, birthday, store, saveloan, myclub, days)
        else:
            os.system('cls')
            startmenu()
    elif c == '3':
        os.system('cls')
        print('''Special Thanks to Everyone Which Helped Me in The Progress:

恒心Zero
TongaBall
南口西路
阿那托利
Mia san Mia, Der Bayern
卡尔蔡斯耶拿新港西格玛多个主队
Jan29th@洵沫ガチ恋勢
Jodo
搪瓷七厂闸北分厂厂长
Alexis

I appreciate for their Advices and Test-Plays, thoughout all the period of programming.
''')
        input('Press Enter To Continue...')
        startmenu()
    elif c == '4':
        os.system('cls')
        sb = input('Are You Sure?(Y/N) ')
        if sb.upper() == 'Y':
            quit()
        else:
            os.system('cls')
            startmenu()
    else:
        os.system('cls')
        startmenu()


def diffc():
    print('''╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                              ╔═══════════════════════╗                                              ║
║                                              ║                       ║                                              ║
║                                              ║   Difficulty Choice:  ║                                              ║
║                                              ║                       ║                                              ║
║                                              ║    1. Very Easy       ║                                              ║
║                                              ║    2. Easy            ║                                              ║
║                                              ║    3. Normal          ║                                              ║
║                                              ║    4. Hard            ║                                              ║
║                                              ║    5. Bankrupting     ║                                              ║
║                                              ║    6. Beggar          ║                                              ║
║                                              ║                       ║                                              ║
║                                              ╚═══════════════════════╝                                              ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝''')
    d = input('Choose your Difficulty!(1-6) ')
    if d == '1':
        money = 50000
        happiness = 80
        fame = 60
        health = 80
        os.system('cls')
    elif d == '2':
        money = 10000
        happiness = 70
        fame = 0
        health = 70
        os.system('cls')
    elif d == '3':
        money = 5000
        happiness = 60
        fame = 0
        health = 60
        os.system('cls')
    elif d == '4':
        money = 1000
        happiness = 50
        fame = 0
        health = 50
        os.system('cls')
    elif d == '5':
        money = 10
        happiness = 30
        fame = 0
        health = 40
        os.system('cls')
    elif d == '6':
        money = 1
        happiness = 10
        fame = 0
        health = 20
        os.system('cls')
    elif d == 'Million':
        money = 1000000
        os.system('cls')
    elif d == 'Debug':
        money = 1000000000
        os.system('cls')
    else:
        return diffc()
    return money, happiness, fame, health


def yourname():
    os.system('cls')
    name = input('''╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                              ╔═══════════════════════╗                                              ║
║                                              ║   Your Name is ... ?  ║                                              ║
║                                              ║                       ║                                              ║
║                                              ║                       ║                                              ║
║                                              ╚═══════════════════════╝                                              ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
''')
    return name


def yourbirth():
    birthday = [0, 0, 0]
    birthday[0] = int(input('''╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                              ╔═══════════════════════╗                                              ║
║                                              ║   Your Birth Year  ?  ║                                              ║
║                                              ║                       ║                                              ║
║                                              ║                       ║                                              ║
║                                              ╚═══════════════════════╝                                              ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
'''))
    birthday[1] = int(input('''╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                              ╔═══════════════════════╗                                              ║
║                                              ║   Your Birth Month ?  ║                                              ║
║                                              ║                       ║                                              ║
║                                              ║                       ║                                              ║
║                                              ╚═══════════════════════╝                                              ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
'''))
    birthday[2] = int(input('''╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                              ╔═══════════════════════╗                                              ║
║                                              ║   Your Birth Day   ?  ║                                              ║
║                                              ║                       ║                                              ║
║                                              ║                       ║                                              ║
║                                              ╚═══════════════════════╝                                              ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
'''))
    return birthday


def mainmenu(money, happiness, fame, health, name, year, month, day, dayday, timep, stocks, ability, matharc, music,
             film, litr, paintt, birthday, store, saveloan, myclub, days):
    os.system('cls')
    days += 1
    while days > 0:
        age = abs(birthday[0] - year + 1)
        if month >= birthday[1]:
            if day >= birthday[2]:
                age = age + 1
        timep += 1
        if timep == 2:
            timep = 0
            day += 1
            dayday += 1
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            if day == 32:
                month += 1
                day = 1
        if month == 2:
            if year % 4 == 0:
                if day == 30:
                    month += 1
                    day = 1
            else:
                if day == 29:
                    month += 1
                    day = 1
        else:
            if day == 31:
                month += 1
                day = 1
        if month == 13:
            year += 1
            month = 1
        if dayday == 8:
            dayday = 1
        if dayday == 1:
            daydisp = 'Monday'
        elif dayday == 2:
            daydisp = 'Tuesday'
        elif dayday == 3:
            daydisp = 'Wednesday'
        elif dayday == 4:
            daydisp = 'Thursday'
        elif dayday == 5:
            daydisp = 'Friday'
        elif dayday == 6:
            daydisp = 'Saturday'
        elif dayday == 7:
            daydisp = 'Sunday'
        if timep == 0:
            timedisp = 'Morning'
        if timep == 1:
            timedisp = 'Evening'
        if dayday == 1 or dayday == 2 or dayday == 3 or dayday == 4 or dayday == 5:
            for i in range(10):
                stocks[i][2] = round((float(numpy.random.chisquare(3, 1)) * (-1) ** random.randint(0, 1) / 100), 4)
                stocks[i][1] *= 1 + stocks[i][2]
                stocks[i][1] = round(stocks[i][1], 2)
        money, myclub = seematch(money, myclub, dayday, timep)
        saveloan, money = checkbank(year, month, day, saveloan, money)
        if timep == 1:
            year, month, day, dayday, matharc, music, film, litr, paintt, money, fame, happiness = seeseeaward(year,
                                                                                                               month,
                                                                                                               day,
                                                                                                               dayday,
                                                                                                               matharc,
                                                                                                               music,
                                                                                                               film,
                                                                                                               litr,
                                                                                                               paintt,
                                                                                                               money,
                                                                                                               fame,
                                                                                                               happiness)
        days -= 1

    if health < 0:
        os.system('cls')
        print('You Dead!')
        startmenu()
    elif happiness < 0:
        os.system('cls')
        print('You Dead!')
        startmenu()

    if myclub[4] == 0:
        c = input(f'''╔══════════════════════════════════════════════════════════════════════════════════════════════════╦══════════════════╗
║    Year:{year} Month:{month:<2} Day:{day:<2}    {daydisp:<9}                                            {timedisp:<10}  ║                  ║
╠══════════════════════════════════════════════════════════════════════════════════════════════════╣  Name:{name:<10} ║
║    Activities To Do:                                                                             ║  Age:{age:<3}         ║
║    1.   Bet                                    12.  Awards                                       ║                  ║
║    2.   Study                                  13.  Ranking                                      ║                  ║
║    3.   Creation Center                        14.  Horsing                                      ║   这里有个头像   ║
║    4.   Invest                                 15.  Save Game                                    ╠══════════════════╣
║    5.   Work                                   16.  My Club                                      ║                  ║
║    6.   Relax                                  17.  Back To Main Menu                            ║  Money:{money:<10}║
║    7.   Cure                                                                                     ║  Happiness: {happiness:<5}║
║    8.   Store                                                                                    ║  Health: {health:<8}║
║    9.   Scratch                                                                                  ║  Fame: {fame:<10}║
║    10.  Bank                                                                                     ║                  ║
║    11.  Donate                                                                                   ║                  ║
║                                                                                                  ╠══════════════════╣
║                                                                                                  ║  Maths:{ability[0]:<10}║
║                                                                                                  ║  Music:{ability[1]:<10}║
║                                                                                                  ║  Literature:{ability[2]:<5}║
║                                                                                                  ║  Acting:{ability[3]:<9}║
╠══════════════════════════════════════════════════════════════════════════════════════════════════╣  Painting:{ability[4]:<7}║
║   What To Do?                                                                                    ║                  ║
║                                                                                                  ╠══════════════════╣
║                                                                                                  ║                  ║
║                                                                                                  ║    Match Day     ║
║                                                                                                  ║      Today       ║
║                                                                                                  ║                  ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════╩══════════════════╝
''')
    if myclub[4] == 1:
        c = input(f'''╔══════════════════════════════════════════════════════════════════════════════════════════════════╦══════════════════╗
║    Year:{year} Month:{month:<2} Day:{day:<2}    {daydisp:<9}                                            {timedisp:<10}  ║                  ║
╠══════════════════════════════════════════════════════════════════════════════════════════════════╣  Name:{name:<10} ║
║    Activities To Do:                                                                             ║  Age:{age:<3}         ║
║    1.   Bet                                    12.  Awards                                       ║                  ║
║    2.   Study                                  13.  Ranking                                      ║                  ║
║    3.   Creation Center                        14.  Horsing                                      ║   这里有个头像   ║
║    4.   Invest                                 15.  Save Game                                    ╠══════════════════╣
║    5.   Work                                   16.  My Club                                      ║                  ║
║    6.   Relax                                  17.  Back To Main Menu                            ║  Money:{money:<10}║
║    7.   Cure                                                                                     ║  Happiness: {happiness:<5}║
║    8.   Store                                                                                    ║  Health: {health:<8}║
║    9.   Scratch                                                                                  ║  Fame: {fame:<10}║
║    10.  Bank                                                                                     ║                  ║
║    11.  Donate                                                                                   ║                  ║
║                                                                                                  ╠══════════════════╣
║                                                                                                  ║  Maths:{ability[0]:<10}║
║                                                                                                  ║  Music:{ability[1]:<10}║
║                                                                                                  ║  Literature:{ability[2]:<5}║
║                                                                                                  ║  Acting:{ability[3]:<9}║
╠══════════════════════════════════════════════════════════════════════════════════════════════════╣  Painting:{ability[4]:<7}║
║   What To Do?                                                                                    ║                  ║
║                                                                                                  ╠══════════════════╣
║                                                                                                  ║                  ║
║                                                                                                  ║     No  Match    ║
║                                                                                                  ║       Today      ║
║                                                                                                  ║                  ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════╩══════════════════╝
''')
    if c == '1':
        os.system('cls')
        health -= 1
        money, happiness = bet(money, happiness)
        mainmenu(money, happiness, fame, health, name, year, month, day, dayday, timep, stocks, ability, matharc, music,
                 film, litr, paintt, birthday, store, saveloan, myclub, days)
    elif c == '2':
        money, health, happiness, ability = study(money, health, happiness, ability)
        mainmenu(money, happiness, fame, health, name, year, month, day, dayday, timep, stocks, ability, matharc, music,
                 film, litr, paintt, birthday, store, saveloan, myclub, days)
    elif c == '3':
        money, health, fame, ability, matharc, music, film, litr, paintt, days = creation(money,
                                                                                          health,
                                                                                          fame,
                                                                                          ability,
                                                                                          year,
                                                                                          month,
                                                                                          day,
                                                                                          dayday,
                                                                                          matharc,
                                                                                          music,
                                                                                          film,
                                                                                          litr,
                                                                                          paintt)
        mainmenu(money, happiness, fame, health, name, year, month, day, dayday, timep, stocks, ability, matharc, music,
                 film, litr, paintt, birthday, store, saveloan, myclub, days)
    elif c == '9':
        money = scratch(money)
        mainmenu(money, happiness, fame, health, name, year, month, day, dayday, timep, stocks, ability, matharc, music,
                 film, litr, paintt, birthday, store, saveloan, myclub, days)
    elif c == '8':
        money, store = stores(money, store)
        mainmenu(money, happiness, fame, health, name, year, month, day, dayday, timep, stocks, ability, matharc, music,
                 film, litr, paintt, birthday, store, saveloan, myclub, days)
    elif c == '6':
        money, happiness, fame, health, name, year, month, day, dayday, timep = goout(money, happiness, fame,
                                                                                      health, name, year, month, day,
                                                                                      dayday, timep, daydisp,
                                                                                      timedisp, age)
        mainmenu(money, happiness, fame, health, name, year, month, day, dayday, timep, stocks, ability, matharc, music,
                 film, litr, paintt, birthday, store, saveloan, myclub, days)
    elif c == '5':
        money, happiness, fame, health, name, year, month, day, dayday, timep = work(money, happiness, fame, health,
                                                                                     name, year, month, day, dayday,
                                                                                     timep, daydisp, timedisp, age)
        mainmenu(money, happiness, fame, health, name, year, month, day, dayday, timep, stocks, ability, matharc, music,
                 film, litr, paintt, birthday, store, saveloan, myclub, days)
    elif c == '4':
        money, stocks = stockssss(money, stocks)
        mainmenu(money, happiness, fame, health, name, year, month, day, dayday, timep, stocks, ability, matharc, music,
                 film, litr, paintt, birthday, store, saveloan, myclub, days)
    elif c == '7':
        money, happiness, fame, health, name, year, month, day, dayday, timep = hospi(money, happiness, fame,
                                                                                      health, name, year, month, day,
                                                                                      dayday, timep, daydisp,
                                                                                      timedisp, age)
        mainmenu(money, happiness, fame, health, name, year, month, day, dayday, timep, stocks, ability, matharc, music,
                 film, litr, paintt, birthday, store, saveloan, myclub, days)
    elif c == '13':
        richlist(money, name)
        mainmenu(money, happiness, fame, health, name, year, month, day, dayday, timep, stocks, ability, matharc, music,
                 film, litr, paintt, birthday, store, saveloan, myclub, days)
    elif c == '10':
        money, saveloan = bank(money, saveloan, year, month, day)
        mainmenu(money, happiness, fame, health, name, year, month, day, dayday, timep, stocks, ability, matharc, music,
                 film, litr, paintt, birthday, store, saveloan, myclub, days)
    elif c == '12':
        awards(matharc, music, film, litr, paintt)
        mainmenu(money, happiness, fame, health, name, year, month, day, dayday, timep, stocks, ability, matharc, music,
                 film, litr, paintt, birthday, store, saveloan, myclub, days)
    elif c == '15':
        money, happiness, fame, health, name, year, month, day, dayday, timep, stocks, ability, matharc, music, film, litr, paintt, birthday, store, saveloan, myclub, days = saveeeee(
            money, happiness, fame, health, name, year, month, day, dayday, timep, stocks, ability, matharc, music,
            film, litr, paintt, birthday, store, saveloan, myclub, days)
        mainmenu(money, happiness, fame, health, name, year, month, day, dayday, timep, stocks, ability, matharc, music,
                 film, litr, paintt, birthday, store, saveloan, myclub, days)
    elif c == '11':
        money, fame = donateeee(money, fame)
        mainmenu(money, happiness, fame, health, name, year, month, day, dayday, timep, stocks, ability, matharc, music,
                 film, litr, paintt, birthday, store, saveloan, myclub, days)
    elif c == '17':
        os.system('cls')
        startmenu()
    elif c == '14':
        money = horsing(money)
        mainmenu(money, happiness, fame, health, name, year, month, day, dayday, timep, stocks, ability, matharc, music,
                 film, litr, paintt, birthday, store, saveloan, myclub, days)
    elif c == '16':
        money, myclub = myfc(money, myclub)
        mainmenu(money, happiness, fame, health, name, year, month, day, dayday, timep, stocks, ability, matharc, music,
                 film, litr, paintt, birthday, store, saveloan, myclub, days)
    else:
        os.system('cls')
        print('''╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                              ╔═══════════════════════╗                                              ║
║                                              ║                       ║                                              ║
║                                              ║     Worng  Input!!    ║                                              ║
║                                              ║                       ║                                              ║
║                                              ╚═══════════════════════╝                                              ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
║                                                                                                                     ║
╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝''')
        time.sleep(1)
        os.system('cls')
        mainmenu(money, happiness, fame, health, name, year, month, day, dayday, timep, stocks, ability, matharc, music,
                 film, litr, paintt, birthday, store, saveloan, myclub, days)


def scratch(money):
    while True:
        os.system('cls')
        print('Your Money:', money)
        do = input('''What to Do?
        
1. Play
2. Go Back
''')
        if do == '2':
            break
        if do == '1':
            money -= 10
            os.system('cls')
            input('''███████████████
███████████████
███████████████
███████████████''')
            os.system('cls')
            input('''██████████████
██████████████
██████████████
██████████████''')
            os.system('cls')
            input('''█████████████
█████████████
█████████████
█████████████''')
            os.system('cls')
            input('''████████████
████████████
████████████
████████████''')
            os.system('cls')
            input('''███████████
███████████
███████████
███████████''')
            os.system('cls')
            input('''██████████
██████████
██████████
██████████''')
            os.system('cls')
            input('''█████████
█████████
█████████
█████████''')
            os.system('cls')
            input('''████████
████████
████████
████████''')
            os.system('cls')
            input('''███████
███████
███████
███████''')
            os.system('cls')
            input('''█████
█████
█████
█████''')
            os.system('cls')
            input('''████
████
████
████''')
            os.system('cls')
            input('''███
███
███
███''')
            os.system('cls')
            input('''██
██
██
██''')
            os.system('cls')
            input('''█
█
█
█''')
            os.system('cls')
            while True:
                pickt = random.randint(0, 2000000)
                randddd = random.randint(0, 2000000)
                if pickt == randddd:
                    money += 1500000
                    input('You won 1500000 ! Enter To Continue...')
                    break
                pickt = random.randint(0, 2000000)
                randddd = random.sample(range(0, 2000000), 2)
                if pickt in randddd:
                    money += 500000
                    input('You won 500000 ! Enter To Continue...')
                    break
                pickt = random.randint(0, 2000000)
                randddd = random.sample(range(0, 2000000), 4)
                if pickt in randddd:
                    money += 200000
                    input('You won 200000 ! Enter To Continue...')
                    break
                pickt = random.randint(0, 2000000)
                randddd = random.sample(range(0, 2000000), 20)
                if pickt in randddd:
                    money += 80000
                    input('You won 80000 ! Enter To Continue...')
                    break
                pickt = random.randint(0, 2000000)
                randddd = random.sample(range(0, 2000000), 25)
                if pickt in randddd:
                    money += 50000
                    input('You won 50000 ! Enter To Continue...')
                    break
                pickt = random.randint(0, 2000000)
                randddd = random.sample(range(0, 2000000), 100)
                if pickt in randddd:
                    money += 25000
                    input('You won 25000 ! Enter To Continue...')
                    break
                pickt = random.randint(0, 2000000)
                randddd = random.sample(range(0, 2000000), 160)
                if pickt in randddd:
                    money += 10000
                    input('You won 10000 ! Enter To Continue...')
                    break
                pickt = random.randint(0, 2000000)
                randddd = random.sample(range(0, 2000000), 200)
                if pickt in randddd:
                    money += 5000
                    input('You won 5000 ! Enter To Continue...')
                    break
                pickt = random.randint(0, 2000000)
                randddd = random.sample(range(0, 2000000), 1000)
                if pickt in randddd:
                    money += 2500
                    input('You won 2500 ! Enter To Continue...')
                    break
                pickt = random.randint(0, 2000000)
                randddd = random.sample(range(0, 2000000), 1600)
                if pickt in randddd:
                    money += 1000
                    input('You won 2500 ! Enter To Continue...')
                    break
                pickt = random.randint(0, 2000000)
                randddd = random.sample(range(0, 2000000), 4000)
                if pickt in randddd:
                    money += 500
                    input('You won 2500 ! Enter To Continue...')
                    break
                pickt = random.randint(0, 2000000)
                randddd = random.sample(range(0, 2000000), 8000)
                if pickt in randddd:
                    money += 200
                    input('You won 200 ! Enter To Continue...')
                    break
                pickt = random.randint(0, 2000000)
                randddd = random.sample(range(0, 2000000), 40000)
                if pickt in randddd:
                    money += 100
                    input('You won 100 ! Enter To Continue...')
                    break
                pickt = random.randint(0, 2000000)
                randddd = random.sample(range(0, 2000000), 200000)
                if pickt in randddd:
                    money += 50
                    input('You won 50 ! Enter To Continue...')
                    break
                pickt = random.randint(0, 2000000)
                randddd = random.sample(range(0, 2000000), 250000)
                if pickt in randddd:
                    money += 20
                    input('You won 20 ! Enter To Continue...')
                    break
                pickt = random.randint(0, 2000000)
                randddd = random.sample(range(0, 2000000), 400000)
                if pickt in randddd:
                    money += 10
                    input('You won 10 ! Enter To Continue...')
                    break
                pickt = random.randint(0, 2000000)
                randddd = random.sample(range(0, 2000000), 400000)
                if pickt in randddd:
                    money += 5
                    input('You won 5 ! Enter To Continue...')
                    break
                else:
                    input('Thank You! You Won 0! Enter To Continue...')
                    break
    return money


def donateeee(money, fame):
    while True:
        os.system('cls')
        c = input(f'''Your Money:{money}
Your Fame:{fame}

The Organizations:
1. UNICEF
2. Red Cross
3. The Smile of Child
4. Back to Main Menu

Tell me Where To Give Money!
''')
        if c == '1' or c == '2' or c == '3':
            amo = float(input('Tell Me How Much To Give!'))
            if amo < money:
                os.system('cls')
                print(f'You Donated Your Money!')
                print(f'Money -{amo}')
                print(f'Fame  +{round(amo / 10000)}')
                input('Press Enter To Continue...')
                fame += round(amo / 10000)
                money -= amo
            else:
                os.system('cls')
                input('Wrong Input! Press Enter To Continue...')
        elif c == '4':
            break
    return money, fame


def horsing(money):
    horses = ["Simon Says",
              "Horsey McHorseface",
              "Neighmar",
              "Legsxit",
              "Hoof Hearted",
              "Royal Air Horse",
              "Chance Meeting",
              "Jolly Bristols",
              "I'll Be Slack",
              "Urgent Message",
              "Talkie Walkie",
              "Happy Dave",
              "Outside Chance",
              "First Class",
              "Old Saying",
              "Quality Assured",
              "Charlie Blue",
              "Hastalavista",
              "Turkey Snore",
              "Tank Top",
              "Made In Heaven",
              "The Good Stuff",
              "Choice Pick",
              "Partly Political",
              "Last Gasp",
              "Simply The Best",
              "Castanet",
              "Billy Royale",
              "Yeoman's Draft",
              "West Wind",
              "Loophole Runner",
              "Apple Kid",
              "Chelsea Girl",
              "Ghost Rider",
              "Hunch Back Bill",
              "Nonty's Revenge",
              "Parting Glance",
              "Cutie Pie",
              "Lucy Locket",
              "Bunny Hunch",
              "Clucking Bell",
              "Bunch Of Fours",
              "Lollipop Whistle",
              "Clarence Custard",
              "Foul Play",
              "Monty Noodle",
              "Poppy Power",
              "Rosie Po",
              "Lillie The Fish",
              "Supernova",
              "Way Out Front",
              "Alright Kassidy",
              "Tommi Gun",
              "Riverbank Blues",
              "Budding Ollie",
              "Backseat Driver",
              "Super Sonic",
              "Beer Drinker",
              "Early Doors",
              "Techno Prisoners",
              "Banjo Willy",
              "Money For Nothing",
              "Fatal Freddie",
              "Brain Drain",
              "Fill Yer Boots",
              "High Flyer",
              "Road Runner",
              "Owzat",
              "Jingle Wingle",
              "Love Tangle",
              "Bonanza Bob",
              "Double Trouble",
              "Ship Shape",
              "Turn Around",
              "Little Bo Pip",
              "Gordon Blimey",
              "Shelly The Nelly",
              "Ivor's Secret",
              "Happy Monday",
              "Groovy Tuesday",
              "Stone Cold Sober",
              "Glitter Girl",
              "Graceful Glenda",
              "Return To Sender",
              "Soldier On",
              "Sally Sandbags",
              "Rumple Stiltskin",
              "Original Method",
              "Queen Of Hearts",
              "Last To Leave",
              "Arthur Chance",
              "Dreamboat Willie",
              "Mop Head Maurice",
              "Dim Prospect",
              "Tina Marina",
              "High Point",
              "Laughing Stock",
              "Nick Nack Noo",
              "Chestnut Champ",
              "King Rex",
              "Practice Hard",
              "Winter Bloom",
              "Ringtone Mogel",
              "Jink Master",
              "Clever Trevor",
              "Samson Done",
              "Crystal Champers",
              "Sparky Warky",
              "Norms Nibbler",
              "Wooley Jumper",
              "Frank The Yank",
              "Zombie Overlord",
              "Back From Beyond",
              "Bun Cakes",
              "Whatta Mistaker",
              "Choc-a-block",
              "Scrub Master",
              "Dr Dude",
              "Millie Bonkers",
              "Tipple Topple",
              "Chunky Monkey",
              "Chevy Chaser",
              "Over Achiever",
              "Croc Hunter",
              "Hey Diddle",
              "Toolkit Tom",
              "Pork Scratchy",
              "Sting Ray",
              "Get Outta Town",
              "No Way Horsey",
              "Spaghetti Forgetti",
              "Chipmonk Hooray",
              "Snake Pit Jim",
              "Call Again",
              "Wally Hobbit",
              "Alder Ruby",
              "Mud Flap Jack",
              "Mouse House",
              "Plain Jane",
              "Grubby Fingers",
              "Checkout Girl",
              "Shoehorn Sue",
              "Let's Ave It",
              "Apple Stew",
              "Doctor Poop",
              "Fender Bender",
              "Slightly Salted",
              "Crazy Moe",
              "Uncle Joe",
              "Mr Bright Nose",
              "Low Blow",
              "King Simba",
              "Cat's Bloomers",
              "Sophie Doughnut",
              "June Bug",
              "Plum Duckling",
              "Granny Minto",
              "Pickaxe Junky",
              "Proper Bo",
              "Dancing Jester",
              "Peanut Jock",
              "Banana Hammock",
              "Pretty Polly",
              "Mustard Manny",
              "Dog Tired",
              "Muppet Duster",
              "Mutton Jeff",
              "Wicked Wendy",
              "Arctic Arsonist",
              "Ripple Racer",
              "Fickle Battler",
              "Fancy Pants",
              "Ronnie the Rat",
              "Come Home Harvey",
              "Sheep Queen",
              "Upper Crusty",
              "Hamfist Herbert",
              "Groove Buster",
              "The Liquidizer",
              "Jeff Leopard",
              "Heaven Sent",
              "Junk Bond Trader",
              "Slippery Hans",
              "Nuts About You",
              "Cry Baby",
              "Pointy Pete",
              "Big Bouncer",
              "Hungry Horace",
              "Lemon Pie",
              "Cut Above",
              "Plum Pudding",
              "Having A Laugh",
              "Woodchuck Chuck",
              "Legal Eagle",
              "Palmina",
              "Oakbridge Boy",
              "Midrange Killer",
              "French Filly",
              "Day Of Reason",
              "Dream Chaser",
              "Matty Boy",
              "I'm Coasting",
              "Lethal Striker",
              "Insanse Sally",
              "Wild Money"]
    while True:
        os.system('cls')
        print('Your Money:', money)
        random.shuffle(horses)
        match = []
        for i in range(8):
            match.append([i + 1, horses[i], random.randint(1, 10)])
            sum = 0
        for i in range(8):
            sum += match[i][2]
        for i in range(8):
            match[i].append(round(1 / (match[i][2] / sum) * 0.95, 2))
        print('No. Horse                    Level       Odd')
        for i in range(8):
            print(f'{i + 1:<2}  {match[i][1]:<25} {match[i][2] * "*":<10}      {match[i][3]}')
        chooseeee = input('Which Horse To Play? 9 to Skip, 10 to Quit.')
        if chooseeee == '10':
            break
        if chooseeee == '1' or chooseeee == '2' or chooseeee == '3' or chooseeee == '4' or chooseeee == '5' or chooseeee == '6' or chooseeee == '7' or chooseeee == '8':
            play = float(input('Tell me How Much To Play!'))
            money -= play
            for i in range(8):
                match[i][2] *= random.uniform(0.2, 5)
            match.sort(key=lambda x: (x[2]), reverse=True)
            print('You played No.:', chooseeee)
            if chooseeee == str(match[0][0]):
                money += play * match[0][3]
                os.system('cls')
                print('No. Horse                Position')
                for i in range(8):
                    print(f'{match[i][0]} {match[i][1]:<25}  {i + 1}')
                input('You Win! Enter To Continue...')
            else:
                os.system('cls')
                print('No. Horse                Position')
                for i in range(8):
                    print(f'{match[i][0]} {match[i][1]:<25}  {i + 1}')
                input('You Loss! Enter To Continue...')
    return money


def bank(money, saveloan, year, month, day):
    ratess = round(2.5 * random.uniform(0.8, 1.2), 2)
    while True:
        os.system('cls')
        print('My Money:', money)
        print('        Time Deposit   Loan ')
        print(f' Length   Rate    |   Rate')
        print(f'6 Months  {round(ratess, 2):<4}%   |   {round(ratess * 1.2, 2):<4}')
        print(f'1 Year    {round(ratess * 1.2, 2):<4}%   |   {round(ratess * 1.2 * 1.2, 2):<4}')
        print(f'2 Years   {round(ratess * 1.5, 2):<4}%   |   {round(ratess * 2 * 1.5, 2):<4}')
        print(f'5 Years   {round(ratess * 2, 2):<4}%   |   {round(ratess * 2 * 1.2, 2):<4}')
        if saveloan != []:
            print('My Time Deposit/Loan:')
            for i in saveloan:
                print(f'Til: {i[0]}/{i[1]}/{i[2]} Amount:{i[3]}')
        c = input('''What to do?
1. Save Money
2. Loan Money
3. Back to Main Menu
''')
        if c == '3':
            break
        elif c == '1' or c == '2':
            length = input('''For How Long?
1. 6 Months
2. 1 Year
3. 2 Years
4. 5 Years
''')
            os.system('cls')
            mon = float(input('How Much?'))
            if mon <= money:
                if c == '1':
                    if length == '1':
                        if month + 6 > 12:
                            saveloan.append([year + 1, month - 6, day, mon * (1 + 0.01 * ratess)])
                            money -= mon
                            os.system('cls')
                            input('Success! Press Enter To Continue...')
                        else:
                            saveloan.append([year, month + 6, day, mon * (1 + 0.01 * ratess)])
                            money -= mon
                            os.system('cls')
                            input('Success! Press Enter To Continue...')
                    if length == '2':
                        saveloan.append([year + 1, month, day, mon * (1 + 0.01 * ratess * 1.2)])
                        money -= mon
                        os.system('cls')
                        input('Success! Press Enter To Continue...')
                    if length == '3':
                        saveloan.append([year + 2, month, day, mon * (1 + 0.01 * ratess * 1.5)])
                        money -= mon
                        os.system('cls')
                        input('Success! Press Enter To Continue...')
                    if length == '4':
                        saveloan.append([year + 5, month, day, mon * (1 + 0.01 * ratess * 2)])
                        money -= mon
                        os.system('cls')
                        input('Success! Press Enter To Continue...')
                if c == '2':
                    if length == '1':
                        if month + 6 > 12:
                            saveloan.append([year + 1, month - 6, day, -mon * (1 + 0.01 * ratess * 1.2)])
                            money += mon
                            os.system('cls')
                            input('Success! Press Enter To Continue...')
                        else:
                            saveloan.append([year, month + 6, day, -mon * (1 + 0.01 * ratess * 1.2)])
                            money += mon
                            os.system('cls')
                            input('Success! Press Enter To Continue...')
                    if length == '2':
                        saveloan.append([year + 1, month, day, -mon * (1 + 0.01 * ratess * 1.2 * 1.2)])
                        money += mon
                        os.system('cls')
                        input('Success! Press Enter To Continue...')
                    if length == '3':
                        saveloan.append([year + 2, month, day, -mon * (1 + 0.01 * ratess * 1.5 * 1.2)])
                        money += mon
                        os.system('cls')
                        input('Success! Press Enter To Continue...')
                    if length == '4':
                        saveloan.append([year + 5, month, day, -mon * (1 + 0.01 * ratess * 2 * 1.2)])
                        money += mon
                        os.system('cls')
                        input('Success! Press Enter To Continue...')
            else:
                os.system('cls')
                input('Wrong Number! Press Enter To Continue...')
    return money, saveloan


def checkbank(year, month, day, saveloan, money):
    if saveloan == []:
        return saveloan, money
    else:
        saveloan.sort()
        flag = 0
        while flag != 1:
            if saveloan != []:
                if saveloan[0][0] <= year:
                    if saveloan[0][1] <= month:
                        if saveloan[0][2] <= day:
                            money += saveloan[0][3]
                            del (saveloan[0])
                            os.system('cls')
                            input('You Have Got/Give Money from/to the Bank! Enter To Continue...')
                        else:
                            break
                    else:
                        break
                else:
                    break
            else:
                break
        return saveloan, money


def saveeeee(money, happiness, fame, health, name, year, month, day, dayday, timep, stocks, ability, matharc, music,
             film, litr, paintt, birthday, store, saveloan, myclub, days):
    placegood = os.getcwd()
    placegood += '\\save.txt'
    f = open(placegood, 'w')
    f.write(f'''{money}
{happiness}
{fame}
{health}
{name}
{year} 
{month}
{day}
{dayday}
{timep}
{stocks[0][1]}
{stocks[1][1]}
{stocks[2][1]}
{stocks[3][1]}
{stocks[4][1]}
{stocks[5][1]}
{stocks[6][1]}
{stocks[7][1]}
{stocks[8][1]}
{stocks[9][1]}
{stocks[0][3]}
{stocks[1][3]}
{stocks[2][3]}
{stocks[3][3]}
{stocks[4][3]}
{stocks[5][3]}
{stocks[6][3]}
{stocks[7][3]}
{stocks[8][3]}
{stocks[9][3]}
{stocks[0][4]}
{stocks[1][4]}
{stocks[2][4]}
{stocks[3][4]}
{stocks[4][4]}
{stocks[5][4]}
{stocks[6][4]}
{stocks[7][4]}
{stocks[8][4]}
{stocks[9][4]}
{ability[0]}
{ability[1]}
{ability[2]}
{ability[3]}
{ability[4]}
{birthday[0]}
{birthday[1]}
{birthday[2]}
{store[0]}
{store[1]}
{store[2]}
{store[3]}
{store[4]}
{myclub[0]}
{myclub[1]}
{myclub[2]}
{myclub[3]}
{myclub[4]}
''')
    f.close()
    if matharc == []:
        placegood = os.getcwd()
        placegood += '\\math.txt'
        f = open(placegood, 'w')
        f.write(' ')
        f.close()
    else:
        good = flatten(matharc, list)

        placegood = os.getcwd()
        placegood += '\\math.txt'
        f = open(placegood, 'w')
        for i in range(len(good)):
            f.write(f'{good[i]}\n')
        f.close()
    if music == []:
        placegood = os.getcwd()
        placegood += '\\music.txt'
        f = open(placegood, 'w')
        f.write(' ')
        f.close()
    else:
        good = flatten(music, list)
        placegood = os.getcwd()
        placegood += '\\music.txt'
        f = open(placegood, 'w')
        for i in range(len(good)):
            f.write(f'{good[i]}\n')
        f.close()
    if litr == []:
        placegood = os.getcwd()
        placegood += '\\litr.txt'
        f = open(placegood, 'w')
        f.write(' ')
        f.close()
    else:
        good = flatten(litr, list)
        placegood = os.getcwd()
        placegood += '\\litr.txt'
        f = open(placegood, 'w')
        for i in range(len(good)):
            f.write(f'{good[i]}\n')
        f.close()
    if paintt == []:
        placegood = os.getcwd()
        placegood += '\\paint.txt'
        f = open(placegood, 'w')
        f.write(' ')
        f.close()
    else:
        good = flatten(paintt, list)
        placegood = os.getcwd()
        placegood += '\\paint.txt'
        f = open(placegood, 'w')
        for i in range(len(good)):
            f.write(f'{good[i]}\n')
        f.close()
    if film == []:
        placegood = os.getcwd()
        placegood += '\\film.txt'
        f = open(placegood, 'w')
        f.write(' ')
        f.close()
    else:
        good = flatten(film, list)
        placegood = os.getcwd()
        placegood += '\\film.txt'
        f = open(placegood, 'w')
        for i in range(len(good)):
            f.write(f'{good[i]}\n')
        f.close()
    if saveloan == []:
        placegood = os.getcwd()
        placegood += '\\bank.txt'
        f = open(placegood, 'w')
        f.write(' ')
        f.close()
    else:
        good = flatten(saveloan, list)
        placegood = os.getcwd()
        placegood += '\\bank.txt'
        f = open(placegood, 'w')
        for i in range(len(good)):
            f.write(f'{good[i]}\n')
        f.close()
    print('Game Saved!')
    time.sleep(1)
    os.system('cls')
    return money, happiness, fame, health, name, year, month, day, dayday, timep, stocks, ability, matharc, music, film, litr, paintt, birthday, store, saveloan, myclub, days


def loaddddd(stocks_org):
    placegood = os.getcwd()
    placegood += '\\save.txt'
    if os.path.exists(placegood) == True:
        with open(f'{placegood}') as f:
            p = f.readlines()
            money = float(p[0])
            happiness = float(p[1])
            fame = float(p[2])
            health = float(p[3])
            name = str(p[4]).rstrip('\n')
            year = int(p[5])
            month = int(p[6])
            day = int(p[7])
            dayday = int(p[8])
            timep = int(p[9])
            stocks = stocks_org
            store = [0, 0, 0, 0, 0]
            stocks[0][1] = float(p[10])
            stocks[1][1] = float(p[11])
            stocks[2][1] = float(p[12])
            stocks[3][1] = float(p[13])
            stocks[4][1] = float(p[14])
            stocks[5][1] = float(p[15])
            stocks[6][1] = float(p[16])
            stocks[7][1] = float(p[17])
            stocks[8][1] = float(p[18])
            stocks[9][1] = float(p[19])
            stocks[0][3] = float(p[20])
            stocks[1][3] = float(p[21])
            stocks[2][3] = float(p[22])
            stocks[3][3] = float(p[23])
            stocks[4][3] = float(p[24])
            stocks[5][3] = float(p[25])
            stocks[6][3] = float(p[26])
            stocks[7][3] = float(p[27])
            stocks[8][3] = float(p[28])
            stocks[9][3] = float(p[29])
            stocks[0][4] = float(p[30])
            stocks[1][4] = float(p[31])
            stocks[2][4] = float(p[32])
            stocks[3][4] = float(p[33])
            stocks[4][4] = float(p[34])
            stocks[5][4] = float(p[35])
            stocks[6][4] = float(p[36])
            stocks[7][4] = float(p[37])
            stocks[8][4] = float(p[38])
            stocks[9][4] = float(p[39])
            ability = [0, 0, 0, 0, 0]
            ability[0] = float(p[40])
            ability[1] = float(p[41])
            ability[2] = float(p[42])
            ability[3] = float(p[43])
            ability[4] = float(p[44])
            birthday = [0, 0, 0]
            birthday[0] = int(p[45])
            birthday[1] = int(p[46])
            birthday[2] = int(p[47])
            store[0] = int(p[48])
            store[1] = int(p[49])
            store[2] = int(p[50])
            store[3] = int(p[51])
            store[4] = int(p[52])
            myclub = [0, 0, 0, 0, 0]
            myclub[0] = str(p[53]).rstrip('\n')
            myclub[1] = int(p[54])
            myclub[2] = int(p[55])
            myclub[3] = int(p[56])
            myclub[4] = int(p[57])
        f.close()
    placegood = os.getcwd()
    placegood += '\\math.txt'
    if os.path.exists(placegood) == True:
        with open(f'{placegood}') as f:
            p = f.readlines()
            if p == ' ':
                matharc = []
            else:
                matharc = []
                for i in range(round(len(p) / 6)):
                    matharc.append([str(p[6 * i]).rstrip('\n'), int(p[6 * i + 1]), int(p[6 * i + 2]), int(p[6 * i + 3]),
                                    int(p[6 * i + 4]), str(p[6 * i + 5]).rstrip('\n')])
        f.close()
    placegood = os.getcwd()
    placegood += '\\music.txt'
    if os.path.exists(placegood) == True:
        with open(f'{placegood}') as f:
            p = f.readlines()
            if p == ' ':
                music = []
            else:
                music = []
                for i in range(round(len(p) / 6)):
                    music.append([str(p[6 * i]).rstrip('\n'), int(p[6 * i + 1]), int(p[6 * i + 2]), int(p[6 * i + 3]),
                                  int(p[6 * i + 4]), str(p[6 * i + 5]).rstrip('\n')])
        f.close()
    placegood = os.getcwd()
    placegood += '\\film.txt'
    if os.path.exists(placegood) == True:
        with open(f'{placegood}') as f:
            p = f.readlines()
            if p == ' ':
                film = []
            else:
                film = []
                for i in range(round(len(p) / 6)):
                    film.append([str(p[6 * i]).rstrip('\n'), int(p[6 * i + 1]), int(p[6 * i + 2]), int(p[6 * i + 3]),
                                 int(p[6 * i + 4]), str(p[6 * i + 5]).rstrip('\n')])
        f.close()
    placegood = os.getcwd()
    placegood += '\\litr.txt'
    if os.path.exists(placegood) == True:
        with open(f'{placegood}') as f:
            p = f.readlines()
            if p == ' ':
                litr = []
            else:
                litr = []
                for i in range(round(len(p) / 6)):
                    litr.append([str(p[6 * i]).rstrip('\n'), int(p[6 * i + 1]), int(p[6 * i + 2]), int(p[6 * i + 3]),
                                 int(p[6 * i + 4]), str(p[6 * i + 5]).rstrip('\n')])
        f.close()
    placegood = os.getcwd()
    placegood += '\\paint.txt'
    if os.path.exists(placegood) == True:
        with  open(f'{placegood}') as f:
            p = f.readlines()
            if p == ' ':
                paintt = []
            else:
                paintt = []
            for i in range(round(len(p) / 6)):
                paintt.append([str(p[6 * i]).rstrip('\n'), int(p[6 * i + 1]), int(p[6 * i + 2]), int(p[6 * i + 3]),
                               int(p[6 * i + 4]), str(p[6 * i + 5]).rstrip('\n')])
        f.close()
    placegood = os.getcwd()
    placegood += '\\bank.txt'
    if os.path.exists(placegood) == True:
        with open(f'{placegood}') as f:
            p = f.readlines()
            if p == ' ':
                saveloan = []
            else:
                saveloan = []
                for i in range(round(len(p) / 4)):
                    saveloan.append([int(p[4 * i]), int(p[4 * i + 1]), int(p[4 * i + 2]), float(p[4 * i + 3])])
        f.close()
        days = 0
        return money, happiness, fame, health, name, year, month, day, dayday, timep, stocks, ability, matharc, music, film, litr, paintt, birthday, store, saveloan, myclub, days
    else:
        os.system('cls')
        print('There is no Saved Game!')
        time.sleep(1)
        money = -1
        happiness = -1
        fame = -1
        health = -1
        name = -1
        year = -1
        month = -1
        day = -1
        dayday = -1
        timep = -1
        stocks = -1
        ability = -1
        matharc = []
        music = []
        film = []
        litr = []
        paintt = []
        birthday = []
        store = []
        saveloan = []
        myclub = []
        days = 0
    return money, happiness, fame, health, name, year, month, day, dayday, timep, stocks, ability, matharc, music, film, litr, paintt, birthday, store, saveloan, myclub, days


# The System For Outside of Bet


def stockssss(money, stocks):
    os.system('cls')
    while True:
        for i in range(len(stocks)):
            if stocks[i][3] == 0:
                stocks[i][5]
            else:
                stocks[i][5] = round(100 * (stocks[i][1] / stocks[i][4] - 1), 2)
        print(f'My money: {money}')
        print('    Stock       Price    Change    |  My Shares   My Bought Price    My Gain/Loss')
        for i in range(10):
            print(
                f'{i + 1:<2}  {stocks[i][0]:<10}  {stocks[i][1]:<7}  {round(stocks[i][2] * 100, 2):<6}%   |  {stocks[i][3]:<8}      {stocks[i][4]:<10}       {stocks[i][5]}%')
        print(f'''What to Do?
1. Buy
2. Sell
3. Back to main menu
''')
        c = input('')
        if c == '1':
            os.system('cls')
            flag = 0
            while flag != 1:
                s2b = input('Please, Tell me What to Buy! (Tell me the Code) ')
                if s2b == '1' or s2b == '2' or s2b == '3' or s2b == '4' or s2b == '5' or s2b == '6' or s2b == '7' or s2b == '8' or s2b == '9' or s2b == '10':
                    flag = 1
                else:
                    print('Tell me Again!')
            while flag != 2:
                parts = float(input('Please, tell me how much stocks? '))
                if parts * stocks[int(s2b) - 1][1] < money:
                    flag += 1
                    stocks[int(s2b) - 1][3] += parts
                    stocks[int(s2b) - 1][4] = stocks[int(s2b) - 1][1]
                    money -= parts * stocks[int(s2b) - 1][1]
                else:
                    print('Tell me again!')
        elif c == '2':
            os.system('cls')
            sbsbsb = 0
            for i in range(10):
                if stocks[i][3] != 0:
                    sbsbsb = 1
            if sbsbsb == 0:
                print('You Stupid! You have no stocks! ')
            if sbsbsb == 1:
                sell = input('Tell me which one to sell? (Tell me the Code) ')
                if stocks[int(sell) - 1][3] == 0:
                    print('You do not have this stock!')
                else:
                    part = float(input('Tell me how much to sell? '))
                    if part > stocks[int(sell) - 1][3]:
                        print('You do not have so much! ')
                    else:
                        stocks[int(sell) - 1][3] -= part
                        money += part * stocks[int(sell) - 1][1]
                        if stocks[int(sell) - 1][3] == 0:
                            stocks[int(sell) - 1][4] = 0
        elif c == '3':
            return money, stocks


def goout(money, happiness, fame, health, name, year, month, day, dayday, timep, daydisp, timedisp, age):
    os.system('cls')
    dhappiness = random.randint(5, 20)
    dhealth = random.randint(2, 7)
    dmoney = random.randint(5, 150)
    happiness += dhappiness
    health -= dhealth
    money -= dmoney
    c = input(f'''
You Went Out And Became Much More Happier!       
Happiness + {dhappiness:<15}                      
Health    - {dhealth:<12}                         
Money     - {dmoney:<11}                                   
                                                          
   Press Enter to Continue...                
''')
    return money, happiness, fame, health, name, year, month, day, dayday, timep


def hospi(money, happiness, fame, health, name, year, month, day, dayday, timep, daydisp, timedisp, age):
    os.system('cls')
    dhealth = random.randint(10, 30)
    dmoney = random.randint(300, 600)
    health += dhealth
    money -= dmoney
    c = input(f'''
You Went Hospital And Became More Healthier!                
                                                            
Health    + {dhealth:<12}                                            
Money     - {dmoney:<11}                    
                                                                      
Press Enter to Continue...    
''')
    return money, happiness, fame, health, name, year, month, day, dayday, timep


def work(money, happiness, fame, health, name, year, month, day, dayday, timep, daydisp, timedisp, age):
    os.system('cls')
    dhappiness = random.randint(3, 7)
    dhealth = random.randint(2, 5)
    dmoney = random.randint(50, 150)
    happiness -= dhappiness
    health -= dhealth
    money += dmoney
    c = input(f''' 
You Worked Out And You Became much Richer!
Happiness - {dhappiness:<15} 
Health    - {dhealth:<12} 
Money     + {dmoney:<11}   
                              
Press Enter to Continue...   
''')
    return money, happiness, fame, health, name, year, month, day, dayday, timep


def creation(money, health, fame, ability, year, month, day, dayday, matharc, music, film, litr, paintt):
    os.system('cls')
    c = int(input(f'''
═══════════════════════
Money: {money}
Health:{health}

              Ability    
Math:            {ability[0]:<3}        
Music:           {ability[1]:<3}        
Literature:      {ability[2]:<3}        
Acting:          {ability[3]:<3}        
Painting:        {ability[4]:<3}        

What to Create?
═══════════════════════
1.  Mathematical Article
2.  Album of Music
3.  Literature
4.  Film
5.  Painting
6.  See My Creations
7.  Back To Upper Menu
'''))
    if c == 1:
        nameeee = input('Tell me the Name of Your Creation!')
        res = int(numpy.random.poisson(ability[0], 1))
        if res >= 100:
            res = 100
        days = 5 * res + 10 + random.randint(10, 50)
        gain = res * 2.5
        for i in range(days):
            day += 1
            dayday += 1
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                if day == 32:
                    month += 1
                    day = 1
            if month == 2:
                if year % 4 == 0:
                    if day == 30:
                        month += 1
                        day = 1
                else:
                    if day == 29:
                        month += 1
                        day = 1
            else:
                if day == 31:
                    month += 1
                    day = 1
            if month == 13:
                year += 1
                month = 1
            if dayday == 8:
                dayday = 1
        dfame = round(0.5 * res)
        fame += dfame
        money += gain
        matharc.append([nameeee, res, year, month, day, 'No'])
        os.system('cls')
        print(f'''Your Creature:{nameeee}
Has Quality:{res}
Finished at:{day}/{month}/{year}
You Gained {gain} Euro, {dfame} Fame.''')
        input('Press Enter To Quit...')
        days *= 2
        return money, health, fame, ability, matharc, music, film, litr, paintt, days
    elif c == 2:
        nameeee = input('Tell me the Name of Your Creation!')
        res = int(numpy.random.poisson(ability[0], 1))
        if res >= 100:
            res = 100
        days = 5 * res + 10 + random.randint(10, 50)
        gain = res * 2.5
        for i in range(days):
            day += 1
            dayday += 1
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                if day == 32:
                    month += 1
                    day = 1
            if month == 2:
                if year % 4 == 0:
                    if day == 30:
                        month += 1
                        day = 1
                else:
                    if day == 29:
                        month += 1
                        day = 1
            else:
                if day == 31:
                    month += 1
                    day = 1
            if month == 13:
                year += 1
                month = 1
            if dayday == 8:
                dayday = 1
        dayday += days
        dayday = dayday % 7
        dmonth = round(days / 30)
        dday = days % 30
        dfame = round(0.5 * res)
        fame += dfame
        money += gain
        if dday + day >= 31:
            month += 1
            day = day + dday - 31
        else:
            day += dday
        if dmonth + month >= 12:
            year += 1
            month = month + dmonth - 12
        else:
            month += dmonth
        music.append([nameeee, res, year, month, day, 'No'])
        os.system('cls')
        print(f'''Your Creature:{nameeee}
Has Quality:{res}
Finished at:{day}/{month}/{year}
You Gained {gain} Euro, {dfame} Fame.''')
        input('Press Enter To Quit...')
        days *= 2
        return money, health, fame, ability, matharc, music, film, litr, paintt, days
    elif c == 3:
        nameeee = input('Tell me the Name of Your Creation!')
        res = int(numpy.random.poisson(ability[0], 1))
        if res >= 100:
            res = 100
        days = 5 * res + 10 + random.randint(10, 50)
        gain = res * 2.5
        for i in range(days):
            day += 1
            dayday += 1
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                if day == 32:
                    month += 1
                    day = 1
            if month == 2:
                if year % 4 == 0:
                    if day == 30:
                        month += 1
                        day = 1
                else:
                    if day == 29:
                        month += 1
                        day = 1
            else:
                if day == 31:
                    month += 1
                    day = 1
            if month == 13:
                year += 1
                month = 1
            if dayday == 8:
                dayday = 1
        dayday += days
        dayday = dayday % 7
        dmonth = round(days / 30)
        dday = days % 30
        dfame = round(0.5 * res)
        fame += dfame
        money += gain
        if dday + day >= 31:
            month += 1
            day = day + dday - 31
        else:
            day += dday
        if dmonth + month >= 12:
            year += 1
            month = month + dmonth - 12
        else:
            month += dmonth
        film.append([nameeee, res, year, month, day, 'No'])
        os.system('cls')
        print(f'''Your Creature:{nameeee}
Has Quality:{res}
Finished at:{day}/{month}/{year}
You Gained {gain} Euro, {dfame} Fame.''')
        input('Press Enter To Quit...')
        days *= 2
        return money, health, fame, ability, matharc, music, film, litr, paintt, days
    elif c == 4:
        nameeee = input('Tell me the Name of Your Creation!')
        res = int(numpy.random.poisson(ability[0], 1))
        if res >= 100:
            res = 100
        days = 5 * res + 10 + random.randint(10, 50)
        gain = res * 2.5
        for i in range(days):
            day += 1
            dayday += 1
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                if day == 32:
                    month += 1
                    day = 1
            if month == 2:
                if year % 4 == 0:
                    if day == 30:
                        month += 1
                        day = 1
                else:
                    if day == 29:
                        month += 1
                        day = 1
            else:
                if day == 31:
                    month += 1
                    day = 1
            if month == 13:
                year += 1
                month = 1
            if dayday == 8:
                dayday = 1
        dayday += days
        dayday = dayday % 7
        dmonth = round(days / 30)
        dday = days % 30
        dfame = round(0.5 * res)
        fame += dfame
        money += gain
        if dday + day >= 31:
            month += 1
            day = day + dday - 31
        else:
            day += dday
        if dmonth + month >= 12:
            year += 1
            month = month + dmonth - 12
        else:
            month += dmonth
        litr.append([nameeee, res, year, month, day, 'No'])
        os.system('cls')
        print(f'''Your Creature:{nameeee}
Has Quality:{res}
Finished at:{day}/{month}/{year}
You Gained {gain} Euro, {dfame} Fame.''')
        input('Press Enter To Quit...')
        days *= 2
        return money, health, fame, ability, matharc, music, film, litr, paintt, days
    elif c == 5:
        nameeee = input('Tell me the Name of Your Creation!')
        res = int(numpy.random.poisson(ability[0], 1))
        if res >= 100:
            res = 100
        days = 5 * res + 10 + random.randint(10, 50)
        gain = res * 2.5
        for i in range(days):
            day += 1
            dayday += 1
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                if day == 32:
                    month += 1
                    day = 1
            if month == 2:
                if year % 4 == 0:
                    if day == 30:
                        month += 1
                        day = 1
                else:
                    if day == 29:
                        month += 1
                        day = 1
            else:
                if day == 31:
                    month += 1
                    day = 1
            if month == 13:
                year += 1
                month = 1
            if dayday == 8:
                dayday = 1
        dayday += days
        dayday = dayday % 7
        dmonth = round(days / 30)
        dday = days % 30
        dfame = round(0.5 * res)
        fame += dfame
        money += gain
        if dday + day >= 31:
            month += 1
            day = day + dday - 31
        else:
            day += dday
        if dmonth + month >= 12:
            year += 1
            month = month + dmonth - 12
        else:
            month += dmonth
            paintt.append([nameeee, res, year, month, day, 'No'])
            os.system('cls')
            print(f'''Your Creature:{nameeee}
Has Quality:{res}
Finished at:{day}/{month}/{year}
You Gained {gain} Euro, {dfame} Fame.''')
        input('Press Enter To Quit...')
        days *= 2
        return money, health, fame, ability, matharc, music, film, litr, paintt, days
    elif c == 6:
        if len(matharc) == 0:
            print('No Math Article')
        else:
            print('Math:')
            for i in range(len(matharc)):
                print(
                    f'Name:{matharc[i][0]}  Quality:{matharc[i][1]}  Date:{matharc[i][2]}/{matharc[i][3]}/{matharc[i][4]}  Awarded:{matharc[i][5]}')
        if len(music) == 0:
            print('No Musical Album')
        else:
            print('Music:')
            for i in range(len(music)):
                print(
                    f'Name:{music[i][0]}  Quality:{music[i][1]}  Date:{music[i][2]}/{music[i][3]}/{music[i][4]}  Awarded:{music[i][5]}')
        if len(film) == 0:
            print('No Film')
        else:
            print('Film:')
            for i in range(len(film)):
                print(
                    f'Name:{film[i][0]}  Quality:{film[i][1]}  Date:{film[i][2]}/{film[i][3]}/{film[i][4]}   Awarded:{film[i][5]}')
        if len(litr) == 0:
            print('No Books')
        else:
            print('Books:')
            for i in range(len(litr)):
                print(
                    f'Name:{litr[i][0]}  Quality:{litr[i][1]}  Date:{litr[i][2]}/{litr[i][3]}/{litr[i][4]}  Awarded:{litr[i][5]}')
        if len(paintt) == 0:
            print('No Paint')
        else:
            print('Paint:')
            for i in range(len(paintt)):
                print(
                    f'Name:{paintt[i][0]}  Quality:{paintt[i][1]}  Date:{paintt[i][2]}/{paintt[i][3]}/{paintt[i][4]}  Awarded:{paintt[i][5]}')
        input('Enter To Quit')
        days = 0
        return money, health, fame, ability, matharc, music, film, litr, paintt, days
    elif c == 7:
        days = 0
        return money, health, fame, ability, matharc, music, film, litr, paintt, days


def awards(matharc, music, film, litr, paintt):
    os.system('cls')
    print('''
Award Period:

Grammys: January
Oscar: February
JSM: June
Fields: August
Nobel: December
''')
    if matharc == []:
        print('No Math Awards!')
    else:
        flag = 0
        for i in range(len(matharc)):
            if matharc[i][5] != 'No':
                print('Fields:')
                print(f'Article: {matharc[i][0]}')
                flag = 1
        if flag == 0:
            print('No Math Awards!')
    if film == []:
        print('No Oscar Awards!')
    else:
        flag = 0
        for i in range(len(film)):
            if film[i][5] != '0':
                print('Oscar:')
                print(f'Film: {film[i][0]}')
                flag = 1
        if flag == 0:
            print('No Oscar Awards!')
    if music == []:
        print('No Grammys Awards!')
    else:
        flag = 0
        for i in range(len(music)):
            if music[i][5] != '0':
                print('Grammys:')
                print(f'Album: {music[i][0]}')
                flag = 1
        if flag == 0:
            print('No Grammys Awards!')
    if litr == []:
        print('No Nobel Awards!')
    else:
        flag = 0
        for i in range(len(litr)):
            if litr[i][5] != '0':
                print('Nobels:')
                print(f'Book: {litr[i][0]}')
                flag = 1
        if flag == 0:
            print('No Nobel Awards!')
    if paintt == []:
        print('No JSM Awards!')
    else:
        flag = 0
        for i in range(len(paintt)):
            if paintt[i][5] != '0':
                print('JSM:')
                print(f'Painting: {paintt[i][0]}')
                flag = 1
        if flag == 0:
            print('No JSM Awards!')
    input('Enter To Continue...')


def study(money, health, happiness, ability):
    while True:
        os.system('cls')
        c = int(input(f'''
═══════════════════════
Money: {money}
Happiness:{happiness}
Health:{health}

              Ability    Possibility   Price   
Math:            {ability[0]:<3}        {100 - ability[0]:<3}%         {50 * (ability[0] + 1)}            
Music:           {ability[1]:<3}        {100 - ability[1]:<3}%         {50 * (ability[1] + 1)}
Literature:      {ability[2]:<3}        {100 - ability[2]:<3}%         {50 * (ability[2] + 1)}
Acting:          {ability[3]:<3}        {100 - ability[3]:<3}%         {50 * (ability[3] + 1)}
Painting:        {ability[4]:<3}        {100 - ability[4]:<3}%         {50 * (ability[4] + 1)}

Where to go?
═══════════════════════
1.  University
2.  Music School
3.  Literature School
4.  Acting School
5.  Art School
6.  Back To Upper Menu
'''))
        if c == 1 or c == 2 or c == 3 or c == 4 or c == 5:
            os.system('cls')
            ifyesyes = random.random()
            if 100 * ifyesyes >= ability[c - 1]:
                ability[c - 1] += 1
                print('Success! ')
                print('Ability + 1')
            else:
                print('Failed! ')
            dhapp = random.randint(1, 3)
            happiness -= dhapp
            dhealth = random.randint(1, 3)
            health -= dhealth
            money -= 50 * (ability[c - 1] + 1)
            print(f'''Money - {50 * (ability[c - 1] + 1)}
Happiness - {dhapp}
Health - {dhealth}''')
            input('Press Enter To Quit...')
            return money, health, happiness, ability
        if c == 6:
            return money, health, happiness, ability


def seeseeaward(year, month, day, dayday, matharc, music, film, litr, paintt, money, fame, happiness):
    if month == 1:
        if dayday == 7:
            if 23 < day < 30:
                if music != []:
                    temp = []
                    temp2 = []
                    for i in range(len(music)):
                        if music[i][2] == year - 1 or music[i][2] == year - 2:
                            temp.append(music[i])
                    for i in range(len(temp)):
                        if temp[i][2] == year - 1:
                            if temp[i][3] < 9:
                                temp2.append(temp[i])
                            elif temp[i][2] == year - 2:
                                if temp[i][3] >= 9:
                                    temp2.append(temp[i])
                    temp2.sorted(key=lambda x: x[1])
                    best = temp2[0][1]
                    pos = 0.04 * best - 3
                    res = random.random()
                    if res <= pos:
                        print('You Won Grammys! ')
                        print('Fame + 500')
                        print('Happiness + 100')
                        fame += 500
                        happiness += 100
                        music[music.index(temp2[0])][5] = 'Grammys'
                        input('Enter To Continue...')
                        return year, month, day, dayday, matharc, music, film, litr, paintt, money, fame, happiness
                    else:
                        nom = 0.04 * best - (0.3 / (1 / 9))
                        if res <= nom:
                            print('You Nominated Grammys!')
                            print('Fame + 100')
                            print('Happiness + 20')
                            fame += 100
                            happiness += 20
                            music[music.index(temp2[0])][5] = 'Nomination'
                            input('Enter To Continue...')
                            return year, month, day, dayday, matharc, music, film, litr, paintt, money, fame, happiness
                        else:
                            print('Unfortunautlly, You did not even nominated for Grammys!')
                            input('Enter To Continue...')
                            return year, month, day, dayday, matharc, music, film, litr, paintt, money, fame, happiness
                else:
                    print('Unfortunautlly, You did not even nominated for Grammys!')
                    input('Enter To Continue...')
                    return year, month, day, dayday, matharc, music, film, litr, paintt, money, fame, happiness
            else:
                return year, month, day, dayday, matharc, music, film, litr, paintt, money, fame, happiness
        else:
            return year, month, day, dayday, matharc, music, film, litr, paintt, money, fame, happiness
    elif month == 2:
        if dayday == 1:
            if 22 < day < 29:
                if film != []:
                    temp = []
                    for i in range(len(film)):
                        if film[i][2] == year - 1:
                            temp.append(film[i])
                    temp.sorted(key=lambda x: x[1])
                    best = temp[0][1]
                    pos = 0.04 * best - 3
                    res = random.random()
                    if res <= pos:
                        print('You Won Oscar! ')
                        input('Enter To Continue...')
                        print('Fame + 500')
                        print('Happiness + 100')
                        fame += 500
                        happiness += 100
                        film[film.index(temp[0])][5] = 'Oscar'
                        input('Enter To Continue...')
                        return year, month, day, dayday, matharc, music, film, litr, paintt, money, fame, happiness
                    else:
                        nom = 0.04 * best - (0.3 / (1 / 9))
                        if res <= nom:
                            print('You Nominated Oscar!')
                            print('Fame + 100')
                            print('Happiness + 100')
                            fame += 100
                            happiness += 20
                            film[film.index(temp[0])][5] = 'Nomination'
                            input('Enter To Continue...')
                            return year, month, day, dayday, matharc, music, film, litr, paintt, money, fame, happiness
                        else:
                            print('Unfortunautlly, You did not even nominated for Oscar!')
                            input('Enter To Continue...')
                            return year, month, day, dayday, matharc, music, film, litr, paintt, money, fame, happiness
                else:
                    print('Unfortunautlly, You did not even nominated for Oscar!')
                    input('Enter To Continue...')
                    return year, month, day, dayday, matharc, music, film, litr, paintt, money, fame, happiness
            else:
                return year, month, day, dayday, matharc, music, film, litr, paintt, money, fame, happiness
        else:
            return year, month, day, dayday, matharc, music, film, litr, paintt, money, fame, happiness
    elif month == 8:
        if year % 4 == 0:
            if dayday == 1:
                if 7 < day < 14:
                    if matharc != []:
                        temp = matharc
                        temp.sorted(key=lambda x: x[1])
                        i = 0
                        while flag != 1:
                            if temp[i][5] == 'Fields':
                                i += 1
                            else:
                                flag = 0
                        best = temp[i][1]
                        pos = 0.04 * best - 3
                        res = random.random()
                        if res <= pos:
                            print('You Won Fields! ')
                            print('Fame + 500')
                            print('Happiness + 100')
                            fame += 500
                            happiness += 100
                            matharc[matharc.index(temp[i])][5] = 'Fields'
                            input('Enter To Continue...')
                            return year, month, day, dayday, matharc, music, film, litr, paintt, money, fame, happiness
                        else:
                            print('Unfortunautlly, You did not even nominated for Fields!')
                            input('Enter To Continue...')
                    else:
                        print('Unfortunautlly, You did not even nominated for Fields!')
                        input('Enter To Continue...')
                        return year, month, day, dayday, matharc, music, film, litr, paintt, money, fame, happiness
                else:
                    return year, month, day, dayday, matharc, music, film, litr, paintt, money, fame, happiness
            else:
                return year, month, day, dayday, matharc, music, film, litr, paintt, money, fame, happiness
        else:
            return year, month, day, dayday, matharc, music, film, litr, paintt, money, fame, happiness
    elif month == 10:
        if dayday == 1:
            if 7 < day < 14:
                if litr != []:
                    temp = matharc
                    temp.sorted(key=lambda x: x[1])
                    i = 0
                    while flag != 1:
                        if temp[i][5] == 'Nobel':
                            i += 1
                        else:
                            flag = 0
                    best = temp[i][1]
                    pos = 0.04 * best - 3
                    res = random.random()
                    if res <= pos:
                        print('You Won Nobel! ')
                        print('Fame + 500')
                        print('Happiness + 100')
                        fame += 500
                        happiness += 100
                        litr[litr.index(temp[i])][5] = 'Nobel'
                        input('Enter To Continue...')
                    else:
                        print('Unfortunautlly, You did not even nominated for Nobel!')
                        input('Enter To Continue...')
                        return year, month, day, dayday, matharc, music, film, litr, paintt, money, fame, happiness
                else:
                    print('Unfortunautlly, You did not even nominated for Nobel!')
                    input('Enter To Continue...')
                    return year, month, day, dayday, matharc, music, film, litr, paintt, money, fame, happiness
            else:
                return year, month, day, dayday, matharc, music, film, litr, paintt, money, fame, happiness
        else:
            return year, month, day, dayday, matharc, music, film, litr, paintt, money, fame, happiness
    elif month == 6:
        if year % 4 == 2:
            if dayday == 1:
                if 14 < day < 21:
                    if paintt != []:
                        temp = matharc
                        temp.sorted(key=lambda x: x[1])
                        i = 0
                        while flag != 1:
                            if temp[i][5] == 'Nobel':
                                i += 1
                            else:
                                flag = 0
                        best = temp[i][1]
                        pos = 0.04 * best - 3
                        res = random.random()
                        if res <= pos:
                            print('You Won JSM Award!! ')
                            print('Fame + 500')
                            print('Happiness + 100')
                            fame += 500
                            happiness += 100
                            paintt[paintt.index(temp[i])][5] = 'JSM'
                            input('Enter To Continue...')
                        else:
                            print('Unfortunautlly, You did not even nominated for JSM!')
                            input('Enter To Continue...')
                            return year, month, day, dayday, matharc, music, film, litr, paintt, money, fame, happiness
                    else:
                        print('Unfortunautlly, You did not even nominated for JSM!')
                        input('Enter To Continue...')
                        return year, month, day, dayday, matharc, music, film, litr, paintt, money, fame, happiness
                else:
                    return year, month, day, dayday, matharc, music, film, litr, paintt, money, fame, happiness
            else:
                return year, month, day, dayday, matharc, music, film, litr, paintt, money, fame, happiness
        else:
            return year, month, day, dayday, matharc, music, film, litr, paintt, money, fame, happiness
    else:
        return year, month, day, dayday, matharc, music, film, litr, paintt, money, fame, happiness


def richlist(money, name):
    os.system('cls')
    rich = [[147000000000, 'Musk'],
            [125800000000, 'Gates'],
            [188400000000, 'Bezos'],
            [10800000000, 'Buffet'],
            [99999999999, 'Jiang', ],
            [88500000000, 'Ortega'],
            [100400000000, 'Thilikos'],
            [115300000000, 'Zuckerberg'],
            [99999999999, 'Dracopoulos'],
            [100000000000, 'Jack Ma']]
    for i in range(10):
        rich[i][0] *= random.uniform(0.1, 10)
        rich[i][0] = round(rich[i][0])
    rich.sort(reverse=True)
    if money >= rich[9][0]:
        rich.pop()
        rich.append([round(money), name])
        rich.sort(reverse=True)
        print('No.          Name          Money')
        for i in range(10):
            print(f'{i + 1:<12} {rich[i][1]:<13} {rich[i][0]}')
    else:
        print('No.          Name          Money')
        for i in range(10):
            print(f'{i + 1:<12} {rich[i][1]:<13} {rich[i][0]}')
        print('.' * 50)
        print(f'{"Not in List":<12} {name:<13} {money}')
    input('Press Enter to Continue...')


def stores(money, store):
    upgrades = [[(0, 'Apartment', 200000), (1, 'House', 2000000), (2, 'Villa', 20000000), (3, 'Castle', 'Max')],
                [(0, 'Smart', 200000), (1, 'BMW', 2000000), (2, 'Porsche', 20000000), (3, 'Lamborghini', 'Max')],
                [(0, 'No Boat', 200000), (1, 'Small Boat', 2000000), (2, 'Big Sail Boat', 20000000),
                 (3, 'Luxary Yacht', 'Max')],
                [(0, 'Casio', 200000), (1, 'Catier', 2000000), (2, 'Vacheron Constantin', 20000000),
                 (3, 'Patek Philippe', 'Max')],
                [(0, 'H&M', 2000000), (1, 'Dior', 2000000), (2, 'Louis Vuitton', 2000000), (3, 'Gucci', 'Max')]]
    while True:
        os.system('cls')
        print('        Level    Type                Money to Upgrade')
        print(f'Property {upgrades[0][store[0]][0]:<8} {upgrades[0][store[0]][1]:<19} {upgrades[0][store[0]][2]}')
        print(f'Car      {upgrades[1][store[1]][0]:<8} {upgrades[1][store[1]][1]:<19} {upgrades[1][store[1]][2]}')
        print(f'Boat     {upgrades[2][store[2]][0]:<8} {upgrades[2][store[2]][1]:<19} {upgrades[2][store[2]][2]}')
        print(f'Watch    {upgrades[3][store[3]][0]:<8} {upgrades[3][store[3]][1]:<19} {upgrades[3][store[3]][2]}')
        print(f'Clothes  {upgrades[4][store[4]][0]:<8} {upgrades[4][store[4]][1]:<19} {upgrades[4][store[4]][2]}')
        c = int(input('''What To Upgrade?
1. Property
2. Car
3. Boat
4. Watches
5. Clothes
6. Back to Main Menu
'''))
        if c == 6:
            break
        if store[c - 1] != 3:
            if money < upgrades[c - 1][store[c]][2]:
                os.system('cls')
                print('You do not have the money!')
                time.sleep(0.5)
            else:
                money -= upgrades[c - 1][store[c]][2]
                store[c - 1] += 1
                input('Success! Enter To Back to Main Menu...')
                break
        else:
            os.system('cls')
            print('Max Level Reached!')
            time.sleep(0.5)
    return money, store


def myfc(money, myclub):
    divisionmoney = [[395, 170], [482, 207], [714, 306], [1284, 550], [2791, 1196], [7318, 3136], [23078, 9891],
                     [87317, 37422], [395357, 169439], [2136988, 915852]]
    if myclub == [0, 0, 0, 0, 1] or myclub == [0, 0, 0, 0, 0] or myclub == ['0', 0, 0, 0, 0] or myclub == ['0', 0, 0, 0,
                                                                                                           1]:
        myclub = [0, 0, 0, 0, 0]
        os.system('cls')
        myclub[0] = input('You have not a club yet! Please, tell me your club name! ')
        myclub[1] = 1
        myclub[2] = 10
    while True:
        if myclub[3] == 5:
            os.system('cls')
            if myclub[2] < 10:
                myclub[2] -= 1
                input(f'You Got Promotion! Your Team is now at Division {myclub[2]} Enter to continue.')
        if myclub[3] == -5:
            os.system('cls')
            if myclub[2] > 1:
                myclub[2] += 1
                input(f'You Got Relegation... Your Team is now at Division {myclub[2]} Enter to continue.')
        if myclub[4] == 0:
            os.system('cls')
            while True:
                random.shuffle(teams)
                opppp = teams[0]
                if opppp[1] <= 10 * (11 - myclub[2]):
                    break
            print(f'''Your Money:{money}
======================================
Your Team:          {myclub[0]}
Ability:            {myclub[1]}
Division:           {myclub[2]}
Win/Loss of a Reel: {myclub[3]}
(without counting Draw)
======================================
Wage:              {round((1 + myclub[1] / 1000) ** (myclub[1]) * 100 * 5, 2)}
Money To Upgrade:  {round((1 + myclub[1] / 1000) ** (myclub[1]) * 100 * 50 * 5, 2)}
Sponsor per Week:  {divisionmoney[(10 - myclub[2])][0]}
Bonus For Win:     {divisionmoney[(10 - myclub[2])][1]}
Bonus For Draw:    {divisionmoney[(10 - myclub[2])][1] / 2}
======================================
Next Opponent:{opppp[0]}
Ability:{opppp[1]}
Country:{opppp[2]}
''')
            c = int(input('''Tell Me What To Do!
1. Upgrade Team
2. Change Team Name
3. Play Match
4. Back To Main Menu
'''))
            if c == 1:
                os.system('cls')
                if money >= round((1 + myclub[1] / 1000) ** (myclub[1]) * 100 * 50 * 5, 2):
                    input('You Upgraded your Team! Enter To Continue...')
                    myclub[1] += 1
                    money -= round((1 + myclub[1] / 1000) ** (myclub[1]) * 100 * 50 * 5, 2)
            elif c == 2:
                os.system('cls')
                myclub[0] = input('Tell me the New Team Name!')
            elif c == 3:
                os.system('cls')
                h = [myclub[1], myclub[0]]
                a = [0, 0]
                a[0] = opppp[1]
                a[1] = opppp[0]
                odd_h, odd_d, odd_a, odd_1x, odd_x2, odd_12, odddnb1, odddnb2, ph, pd, pa = wldodd(h, a)
                r = result(ph, pd)
                pg = poisson(h, a)
                g = goal(r, pg)
                homeg, awayg = hag(r, g)
                if homeg > awayg:
                    print('You Win! The Result is', homeg, '-', awayg)
                    if myclub[3] >= 0:
                        myclub[3] += 1
                    elif myclub[3] <= 0:
                        myclub[3] = 1
                    money += divisionmoney[(10 - myclub[2])][1]
                elif homeg == awayg:
                    print('You Draw! The Result is', homeg, '-', awayg)
                    money += divisionmoney[(10 - myclub[2])][1] / 2
                elif homeg < awayg:
                    print('You Loss! The Result is', homeg, '-', awayg)
                    if myclub[3] <= 0:
                        myclub[3] -= 1
                    elif myclub[3] >= 0:
                        myclub[3] = -1
                myclub[4] = 1
                input('Enter To Continue...')
            elif c == 4:
                return money, myclub
        elif myclub[4] == 1:
            os.system('cls')
            print(f'''Your Money:{money}
======================================
Your Team:          {myclub[0]}
Ability:            {myclub[1]}
Division:           {myclub[2]}
Win/Loss of a Reel: {myclub[3]}
(without counting Draw)
======================================
Wage:              {round((1 + myclub[1] / 1000) ** (myclub[1]) * 100 * 5, 2)}
Money To Upgrade:  {round((1 + myclub[1] / 1000) ** (myclub[1]) * 100 * 50 * 5, 2)}
Sponsor per Week:  {divisionmoney[(10 - myclub[2])][0]}
Bonus For Win:     {divisionmoney[(10 - myclub[2])][1]}
Bonus For Draw:    {divisionmoney[(10 - myclub[2])][1] / 2}
======================================
You have no match to play now!
''')
            c = int(input('''Tell Me What To Do!
1. Upgrade Team
2. Change Team Name
3. Back To Main Menu
'''))
            if c == 1:
                os.system('cls')
                if money >= round((1 + myclub[1] / 1000) ** (myclub[1]) * 100 * 50 * 5, 2):
                    input('You Upgraded your Team! Enter To Continue...')
                    myclub[1] += 1
                    money -= round((1 + myclub[1] / 1000) ** (myclub[1]) * 100 * 50 * 5, 2)
            elif c == 2:
                os.system('cls')
                myclub[0] = input('Tell me the New Team Name!')
            elif c == 3:
                return money, myclub


def seematch(money, myclub, dayday, timep):
    if myclub == [] or myclub == [0, 0, 0, 0, 1] or myclub == [0, 0, 0, 0, 0] or myclub == ['0', 0, 0, 0,
                                                                                            0] or myclub == ['0', 0, 0,
                                                                                                             0, 1]:
        myclub = [0, 0, 0, 0, 1]
    return money, myclub
    divisionmoney = [[395, 170], [482, 207], [714, 306], [1284, 550], [2791, 1196], [7318, 3136], [23078, 9891],
                     [87317, 37422], [395357, 169439], [2136988, 915852], [0, 0]]
    if timep == 1:
        if dayday == 1:
            money += divisionmoney[(10 - myclub[2])][0]
            money -= round((1 + myclub[1] / 1000) ** (myclub[1]) * 100, 2) * 5
            if dayday == 3 or dayday == 7:
                myclub[4] = 0
            else:
                myclub[4] = 1
    return money, myclub


# The Functions For The Bet


def randgame(h, a, hn, an, hc, ac):
    random.shuffle(teams)
    i = teams[0]
    j = teams[1]
    h[0] = h[1]
    a[0] = a[1]
    h[1] = i[1]
    a[1] = j[1]
    hn[0] = hn[1]
    an[0] = an[1]
    hn[1] = i[0]
    an[1] = j[0]
    hc[0] = hc[1]
    ac[0] = ac[1]
    hc[1] = i[2]
    ac[1] = j[2]
    return h, a, hn, an, hc, ac


def wldodd(h, a):
    dha = abs(h[0] - a[0])
    ha = abs(h[0] + a[0] - 90)
    pd = 0.38 - ha * 0.002 - dha * 0.0035
    if pd >= 0.31:
        pd = 0.31
    ph = (1 - pd) * (h[0] * (h[0] / a[0]) * 0.95) / (h[0] + a[0]) * (math.log2(h[0]) / math.log2(a[0])) * (
            math.pi / 3) ** ((h[0] / a[0]) * ((math.pi + math.e) / math.e))
    if ph >= 1 - pd:
        ph = 1 - pd - 0.005
        pa = 0.005
    elif ph <= 0.005:
        ph = 0.005
        pa = 1 - pd - 0.005
    else:
        pa = 1 - ph - pd
    odd_d = (1 / pd) * 0.95
    odd_h = (1 / ph) * 0.95
    odd_a = (1 / pa) * 0.95
    odd_1x = 1 / (1 - pa) * 0.95
    odd_x2 = 1 / (1 - ph) * 0.95
    odd_12 = 1 / (1 - pd) * 0.95
    odddnb1 = (1 / ph) * 0.925
    odddnb2 = (1 / pa) * 0.925
    if odd_h < 1:
        odd_h = 1
    if odd_a < 1:
        odd_a = 1
    if odd_1x < 1:
        odd_1x = 1
    if odd_12 < 1:
        odd_12 = 1
    if odd_x2 < 1:
        odd_x2 = 1
    if odd_12 < 1:
        odd_12 = 1
    if odddnb1 < 1:
        odddnb1 = 1
    if odddnb2 < 1:
        odddnb2 = 1
    odd_h = round(odd_h, 2)
    odd_d = round(odd_d, 2)
    odd_a = round(odd_a, 2)
    odd_1x = round(odd_1x, 2)
    odd_x2 = round(odd_x2, 2)
    odd_12 = round(odd_12, 2)
    odddnb1 = round(odddnb1, 2)
    odddnb2 = round(odddnb2, 2)
    return odd_h, odd_d, odd_a, odd_1x, odd_x2, odd_12, odddnb1, odddnb2, ph, pd, pa


def result(ph, pd):
    r = random.random()
    if r < ph:
        r = 1
        return r
    elif ph <= r <= (ph + pd):
        r = 0
        return r
    elif (ph + pd) < r:
        r = 2
        return r


def poisson(h, a):
    lamda = 2.15 + (h[0] + a[0]) * 0.002 + (h[0] - a[0]) * 0.01
    pg = list(range(11))
    pg[0] = (lamda ** 0 * math.e ** (-lamda)) / math.factorial(0)
    for i in range(1, 11):
        pg[i] = pg[i - 1] + (lamda ** i * math.e ** (-lamda)) / math.factorial(i)
    return pg


def poisson1(h, a):
    lamda = 2.15 + (h + a) * 0.002 + (h - a) * 0.01
    pg = list(range(11))
    pg[0] = (lamda ** 0 * math.e ** (-lamda)) / math.factorial(0)
    for i in range(1, 11):
        pg[i] = pg[i - 1] + (lamda ** i * math.e ** (-lamda)) / math.factorial(i)
    return pg


def oddou(pg):
    odd_ou = list(range(11))
    for i in range(11):
        odd_ou[i] = [round((1 / pg[i] * 0.95), 2), round((1 / (1 - pg[i]) * 0.95), 2)]
        if odd_ou[i][0] < 1:
            odd_ou[i][0] = '-'
        elif odd_ou[i][1] < 1:
            odd_ou[i][1] = '-'
    return odd_ou


def oddgn(pg):
    odd_gn = list(range(11))
    odd_gn[0] = round((1 / pg[0] * 0.95), 2)
    for i in range(1, 11):
        odd_gn[i] = round((1 / (pg[i] - pg[i - 1]) * 0.95), 2)
    return odd_gn


def oddtg(pg):
    odd_tg = list(range(4))
    odd_tg[0] = round((1 / (pg[1]) * 0.95), 2)
    odd_tg[1] = round((1 / (pg[3] - pg[1]) * 0.95), 2)
    odd_tg[2] = round((1 / (pg[6] - pg[3]) * 0.95), 2)
    odd_tg[3] = round((1 / (1 - pg[7]) * 0.95), 2)
    return odd_tg


def oddcomb(odd_h, odd_d, odd_a, odd_ou, gg, ngg):
    odd_1gg = round(gg * odd_h / 0.95, 2)
    odd_2gg = round(gg * odd_a / 0.95, 2)
    odd_xgg = round(gg * odd_d / 0.95, 2)
    odd_1ngg = round(ngg * odd_h / 0.95, 2)
    odd_2ngg = round(ngg * odd_a / 0.95, 2)
    odd_xngg = round(ngg * odd_d / 0.95, 2)
    odd_ou12dh = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    odd_ouggng = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(1, 4):
        odd_ou12dh[i][0] = round(odd_h * odd_ou[i][1], 2)
        odd_ou12dh[i][1] = round(odd_d * odd_ou[i][1], 2)
        odd_ou12dh[i][2] = round(odd_a * odd_ou[i][1], 2)
        odd_ou12dh[i][3] = round(odd_h * odd_ou[i][0], 2)
        odd_ou12dh[i][4] = round(odd_d * odd_ou[i][0], 2)
        odd_ou12dh[i][5] = round(odd_a * odd_ou[i][0], 2)
    for i in range(1, 4):
        odd_ouggng[i][0] = round(gg * odd_ou[i][1], 2)
        odd_ouggng[i][1] = round(ngg * odd_ou[i][1], 2)
        odd_ouggng[i][2] = round(gg * odd_ou[i][0], 2)
        odd_ouggng[i][3] = round(ngg * odd_ou[i][0], 2)
    return odd_1gg, odd_xgg, odd_2gg, odd_1ngg, odd_xngg, odd_2ngg, odd_ou12dh, odd_ouggng


def goal(r, pg):
    g = 0.5
    while 0 < g < 1:
        g = random.random()
        if g <= pg[0]:
            g = 0
        elif pg[0] < g <= pg[1]:
            g = 1
        elif pg[1] < g <= pg[2]:
            g = 2
        elif pg[2] < g <= pg[3]:
            g = 3
        elif pg[3] < g <= pg[4]:
            g = 4
        elif pg[4] < g <= pg[5]:
            g = 5
        elif pg[5] < g <= pg[6]:
            g = 6
        elif pg[6] < g <= pg[7]:
            g = 7
        elif pg[7] < g <= pg[8]:
            g = 8
        elif pg[8] < g:
            g = 9
        if r == 0:
            if g % 2 == 0:
                return g
            else:
                return goal(r, pg)
        else:
            return g


def hag(r, g):
    if g == 0:
        homeg = 0
        awayg = 0
        return homeg, awayg
    else:
        homeg = random.randint(0, g)
        awayg = g - homeg
        if r == 1:
            if homeg > awayg:
                return homeg, awayg
            else:
                return hag(r, g)
        if r == 2:
            if homeg < awayg:
                return homeg, awayg
            else:
                return hag(r, g)
        if r == 0:
            if homeg == awayg:
                return homeg, awayg
            else:
                return hag(r, g)


def rec(record):
    for i in range(len(record)):
        print('Home:', record[i][0])
        print('Away:', record[i][3])
        print('Score:', record[i][1], '-', record[i][2])
        print('')


# Odd printing


def oddprint(money, happiness, hn, an, hc, ac, odd_h, odd_a, odd_d, odd_1x, odd_x2, odd_12, odd_ou, gg, ngg):
    print('══════════════════════════════════════════════')
    print('My Money:', money)
    print('My Happiness:', happiness)
    print('══════════════════════════════════════════════')
    print('Next Match:\n')
    print(f'{hn[0]}({hc[0]})')
    print('VS')
    print(f'{an[0]}({ac[0]})\n')
    print('Home:', odd_h, 'Draw:', odd_d, 'Away:', odd_a)
    print('1/X:', odd_1x, 'X/2:', odd_x2, '1/2:', odd_12)
    print('Over 1.5:', odd_ou[1][1], 'Under 1.5:', odd_ou[1][0])
    print('Over 2.5:', odd_ou[2][1], 'Under 2.5:', odd_ou[2][0])
    print('Over 3.5:', odd_ou[3][1], 'Under 3.5:', odd_ou[3][0])
    print('Goal/Goal:', gg, 'No Goal', ngg)


def oddcsprint(pos):
    print(f'1-0 {pos[1][0]:<8} 0-0 {pos[0][0]:<8} 0-1 {pos[0][1]:<8}')
    print(f'2-0 {pos[2][0]:<8} 1-1 {pos[1][1]:<8} 0-2 {pos[0][2]:<8}')
    print(f'2-1 {pos[2][1]:<8} 2-2 {pos[2][2]:<8} 1-2 {pos[1][2]:<8}')
    print(f'3-0 {pos[3][0]:<8} 3-3 {pos[3][3]:<8} 0-3 {pos[0][3]:<8}')
    print(f'3-1 {pos[3][1]:<8} 4-4 {pos[4][4]:<8} 1-3 {pos[1][3]:<8}')
    print(f'3-2 {pos[3][2]:<8}              2-3 {pos[2][3]:<8}')
    print(f'4-0 {pos[4][0]:<8}              0-4 {pos[0][4]:<8}')
    print(f'4-1 {pos[4][1]:<8}              1-4 {pos[1][4]:<8}')
    print(f'4-2 {pos[4][2]:<8}              2-4 {pos[2][4]:<8}')
    print(f'4-3 {pos[4][3]:<8}              3-4 {pos[3][4]:<8}')
    print(f'5-0 {pos[5][0]:<8}              0-5 {pos[0][5]:<8}')
    print(f'5-1 {pos[5][1]:<8}              1-5 {pos[1][5]:<8}')
    print(f'5-2 {pos[5][2]:<8}              2-5 {pos[2][5]:<8}')
    print(f'5-3 {pos[5][3]:<8}              3-5 {pos[3][5]:<8}')
    print(f'5-4 {pos[5][4]:<8}              4-5 {pos[4][5]:<8}')
    print(f'6-0 {pos[6][0]:<8}              0-6 {pos[0][6]:<8}')
    print(f'6-1 {pos[6][1]:<8}              1-6 {pos[1][6]:<8}')
    print(f'6-2 {pos[6][2]:<8}              2-6 {pos[2][6]:<8}')
    print(f'6-3 {pos[6][3]:<8}              3-6 {pos[3][6]:<8}')
    print(f'7-0 {pos[7][0]:<8}              0-7 {pos[0][7]:<8}')
    print(f'7-1 {pos[7][1]:<8}              1-7 {pos[1][7]:<8}')
    print(f'7-2 {pos[7][2]:<8}              2-7 {pos[2][7]:<8}')
    print(f'8-0 {pos[8][0]:<8}              0-8 {pos[0][8]:<8}')
    print(f'8-1 {pos[8][1]:<8}              1-8 {pos[1][8]:<8}')
    print(f'9-0 {pos[9][0]:<8}              0-9 {pos[0][9]:<8}')


def oddresultprint(odd_h, odd_a, odd_d, odd_1x, odd_x2, odd_12, odddnb1, odddnb2):
    print('Result:')
    print('Home:', odd_h, 'Draw:', odd_d, 'Away:', odd_a, '\n')
    print('Double Chance:')
    print('1/X:', odd_1x, 'X/2:', odd_x2, '1/2:', odd_12, '\n')
    print('Draw No Bet:')
    print('Home:', odddnb1, 'Away:', odddnb2)


def ouoddprint(odd_ou):
    for i in range(10):
        print(f'Over {i}.5: {odd_ou[i][1]:<8} Under {i}.5: {odd_ou[i][0]}')


def odddgprint(dg):
    print('Goal Difference:')
    for i in range(10):
        print(f'{i}: {dg[i]}')
    print(' ')


def oddhagprint(hg, ag):
    print('Home Team Goals         Away team Goals\n')
    for i in range(10):
        print(f'{i}: {hg[i]:<8}             {i}: {ag[i]}')


def oddtgprint(odd_gn, odd_tg):
    print('Exact Total Goals:')
    for i in range(10):
        print(f'{i}: {odd_gn[i]:<8}')
    print('')
    print('Total Goals:')
    print(f'0-1: {odd_tg[0]:<8}')
    print(f'2-3: {odd_tg[1]:<8}')
    print(f'4-5: {odd_tg[2]:<8}')
    print(f'6+: {odd_tg[3]:<8}')


def oddt2g(gg, ngg, h2g, a2g, h2n, a2n):
    print('Both Teams to Score:')
    print('Yes:', gg, 'No', ngg, '\n')
    print('Home Team to Score:')
    print('Yes:', h2g, 'No:', h2n, '\n')
    print('Away Team to Score:')
    print('Yes:', a2g, 'No:', a2n)


def oddcombprt(odd_1gg, odd_xgg, odd_2gg, odd_1ngg, odd_xngg, odd_2ngg, odd_ou12dh, odd_ouggng):
    print('Result and Over:')
    print('          Home  Draw  Away')
    for i in range(1, 4):
        print(f'Over {i}.5: {odd_ou12dh[i][0]:<5} {odd_ou12dh[i][1]:<5} {odd_ou12dh[i][2]:<5}')
    print('')
    print('Result and Under:')
    print('           Home  Draw  Away')
    for i in range(1, 4):
        print(f'Under {i}.5: {odd_ou12dh[i][3]:<5} {odd_ou12dh[i][4]:<5} {odd_ou12dh[i][5]:<5}')
    print('')
    print('Over and Both Teams to Goal:')
    print('          Yes   No')
    for i in range(1, 4):
        print(f'Over {i}.5: {odd_ouggng[i][0]:<5} {odd_ouggng[i][1]:<5}')
    print('')
    print('Under and Both Teams to Goal:')
    print('           Yes   No')
    for i in range(1, 4):
        print(f'Under {i}.5: {odd_ouggng[i][2]:<5} {odd_ouggng[i][3]:<5}')
    print('')
    print('Result and Both Teams to Goal:')
    print('     Home  Draw  Away')
    print(f'Yes: {odd_1gg:<5} {odd_xgg:<5} {odd_2gg:<5}')
    print(f'No : {odd_1ngg:<5} {odd_xngg:<5} {odd_2ngg:<5}')


# Check win or not


def checkdnb(play, homeg, awayg, money, happiness, odddnb1, odddnb2, bn):
    if play.upper() == '1':
        if homeg > awayg:
            money += odddnb1 * bn
            print('You win!')
            happiness += 2
            return money, happiness
        elif homeg < awayg:
            print('You loss!')
            happiness -= 1
            return money, happiness
    elif play.upper() == '2':
        if homeg < awayg:
            money += odddnb2 * bn
            print('You win!')
            return money, happiness
        elif homeg > awayg:
            print('You loss!')
            happiness -= 1
            return money, happiness


def check12x(play, homeg, awayg, money, happiness, odd_h, odd_d, odd_a, bn):
    if play.upper() == 'X':
        if homeg == awayg:
            money += odd_d * bn
            print('You win!')
            happiness += 2
            return money, happiness
        else:
            print('You loss!')
            happiness -= 1
            return money, happiness
    elif play.upper() == '1':
        if homeg > awayg:
            money += odd_h * bn
            print('You win!')
            happiness += 2
            return money, happiness
        else:
            print('You loss!')
            happiness -= 1
            return money, happiness
    elif play.upper() == '2':
        if homeg < awayg:
            money += odd_a * bn
            print('You win!')
            happiness += 2
            return money, happiness
        else:
            print('You loss!')
            happiness -= 1
            return money, happiness


def checkdc(play, homeg, awayg, money, happiness, odd_12, odd_x2, odd_1x, bn):
    if play.upper() == '12':
        if homeg == awayg:
            print('You loss!')
            happiness -= 1
            return money, happiness
        else:
            money += odd_12 * bn
            print('You win!')
            happiness += 2
            return money, happiness
    elif play.upper() == '1X':
        if homeg < awayg:
            print('You loss!')
            happiness -= 1
            return money, happiness
        else:
            money += odd_1x * bn
            print('You win!')
            happiness += 2
            return money, happiness
    elif play.upper() == 'X2':
        if homeg > awayg:
            print('You loss!')
            happiness -= 1
            return money, happiness
        else:
            money += odd_x2 * bn
            print('You win!')
            happiness += 2
            return money, happiness


def checkou(play, money, happiness, ou, odd_ou, bn, g):
    if play.upper() == 'O':
        if g > ou:
            money += (odd_ou[ou][1]) * bn
            print('You win!')
            happiness += 2
            return money, happiness
        else:
            print('You loss!')
            happiness -= 1
            return money, happiness
    elif play.upper() == 'U':
        if g <= ou:
            money += (odd_ou[ou][0]) * bn
            print('You win!')
            happiness += 2
            return money, happiness
        else:
            print('You loss!')
            happiness -= 1
            return money, happiness


def checkgg(play, money, happiness, homeg, awayg, gg, ngg, bn):
    if play.upper() == 'GG':
        if homeg > 0:
            if awayg > 0:
                money += gg * bn
                print('You win!')
                happiness += 2
                return money, happiness
            else:
                print('You loss!')
                happiness -= 1
                return money, happiness
        else:
            print('You loss!')
            happiness -= 1
            return money, happiness
    if play.upper() == 'NG':
        if homeg == 0:
            money += ngg * bn
            print('You win!')
            happiness += 2
            return money, happiness
        if awayg == 0:
            money += ngg * bn
            print('You win!')
            happiness += 2
            return money, happiness
        else:
            print('You loss!')
            happiness -= 1
            return money, happiness


def checkdg(play, money, happiness, homeg, awayg, dg, bn):
    if int(play) == homeg - awayg:
        money += dg[homeg - awayg] * bn
        print('You win!')
        happiness += 2
        return money, happiness
    else:
        print('You loss!')
        happiness -= 1
        return money, happiness


def checkhagg(play, money, happiness, homeg, awayg, h2g, h2n, a2g, a2n, bn):
    if play.upper() == 'HG':
        if homeg > 0:
            money += h2g * bn
            print('You win!')
            happiness += 2
            return money, happiness
        else:
            print('You loss!')
            happiness -= 1
            return money, happiness
    if play.upper() == 'HNG':
        if homeg == 0:
            money += h2n * bn
            print('You win!')
            happiness += 2
            return money, happiness
        else:
            print('You loss!')
            happiness -= 1
            return money, happiness
    if play.upper() == 'AG':
        if awayg > 0:
            money += a2g * bn
            print('You win!')
            happiness += 2
            return money, happiness
        else:
            print('You loss!')
            happiness -= 1
            return money, happiness
    if play.upper() == 'ANG':
        if awayg == 0:
            money += a2n * bn
            print('You win!')
            happiness += 2
            return money, happiness
        else:
            print('You loss!')
            happiness -= 1
            return money, happiness


def checkcs(play, money, happiness, homeg, awayg, pos, bn):
    if int(play[0]) == homeg:
        if int(play[2]) == awayg:
            money += pos[homeg][awayg] * bn
            print('You win!')
            happiness += 2
            return money, happiness
        else:
            print('You loss!')
            happiness -= 1
            return money, happiness
    else:
        print('You loss!')
        happiness -= 1
        return money, happiness


def checktgs(play, money, happiness, g, bn, odd_tg):
    if play[0] == '0':
        if g < 2:
            money += odd_tg[0] * bn
            print('You win!')
            happiness += 2
            return money, happiness
        else:
            print('You loss!')
            happiness -= 1
            return money, happiness
    if play[0] == '2':
        if 1 < g < 4:
            money += odd_tg[1] * bn
            print('You win!')
            happiness += 2
            return money, happiness
        else:
            print('You loss!')
            happiness -= 1
            return money, happiness
    if play[0] == '4':
        if 3 < g < 6:
            money += odd_tg[2] * bn
            print('You win!')
            happiness += 2
            return money, happiness
        else:
            print('You loss!')
            happiness -= 1
            return money, happiness
    if play[0] == '6':
        if g > 2:
            money += odd_tg[3] * bn
            print('You win!')
            happiness += 2
            return money, happiness
        else:
            print('You loss!')
            happiness -= 1
            return money, happiness


def checkegs(play, money, happiness, g, bn, odd_gn):
    play = int(play)
    if g == play:
        money += odd_gn[play] * bn
        print('You win!')
        happiness += 2
        return money, happiness
    else:
        print('You loss!')
        happiness -= 1
        return money, happiness


def checkhaegs(play, no, money, happiness, g, bn, hg, ag, homeg, awayg):
    no = int(no)
    if play.upper() == 'H':
        if no == homeg:
            money += hg[no] * bn
            print('You win!')
            happiness += 2
            return money, happiness
        else:
            print('You loss!')
            happiness -= 1
        return money, happiness
    elif play.upper() == 'A':
        if no == awayg:
            money += ag[no] * bn
            print('You win!')
            happiness += 2
            return money, happiness
        else:
            print('You loss!')
            happiness -= 1
        return money, happiness


def check12xou(play, ou, nou, homeg, awayg, money, happiness, bn, odd_ou12dh):
    if ou.upper() == 'O':
        if nou < homeg + awayg:
            if play.upper() == 'X':
                if homeg == awayg:
                    money += odd_ou12dh[nou][1] * bn
                    print('You win!')
                    happiness += 2
                    return money, happiness
                else:
                    print('You loss!')
                    happiness -= 1
                    return money, happiness
            elif play.upper() == '1':
                if homeg > awayg:
                    money += odd_ou12dh[nou][0] * bn
                    print('You win!')
                    happiness += 2
                    return money, happiness
                else:
                    print('You loss!')
                    happiness -= 1
                    return money, happiness
            elif play.upper() == '2':
                if homeg < awayg:
                    money += odd_ou12dh[nou][2] * bn
                    print('You win!')
                    happiness += 2
                    return money, happiness
                else:
                    print('You loss!')
                    happiness -= 1
                    return money, happiness
            else:
                print('You loss!')
                happiness -= 1
                return money, happiness
        else:
            print('You loss!')
            happiness -= 1
            return money, happiness
    elif ou.upper() == 'U':
        if nou > homeg + awayg:
            if play.upper() == 'X':
                if homeg == awayg:
                    money += odd_ou12dh[nou][4] * bn
                    print('You win!')
                    happiness += 2
                    return money, happiness
                else:
                    print('You loss!')
                    happiness -= 1
                    return money, happiness
            elif play.upper() == '1':
                if homeg > awayg:
                    money += odd_ou12dh[nou][3] * bn
                    print('You win!')
                    happiness += 2
                    return money, happiness
                else:
                    print('You loss!')
                    happiness -= 1
                    return money, happiness
            elif play.upper() == '2':
                if homeg < awayg:
                    money += odd_ou12dh[nou][5] * bn
                    print('You win!')
                    happiness += 2
                    return money, happiness
                else:
                    print('You loss!')
                    happiness -= 1
                    return money, happiness
            else:
                print('You loss!')
                happiness -= 1
                return money, happiness
        else:
            print('You loss!')
            happiness -= 1
            return money, happiness


def check12xgg(play, ggng, homeg, awayg, money, happiness, bn, odd_1gg, odd_xgg, odd_2gg, odd_1ngg, odd_xngg, odd_2ngg):
    if ggng.upper() == 'GG':
        if homeg != 0 and awayg != 0:
            if play.upper() == 'X':
                if homeg == awayg:
                    money += odd_xgg * bn
                    print('You win!')
                    happiness += 2
                    return money, happiness
                else:
                    print('You loss!')
                    happiness -= 1
                    return money, happiness
            elif play.upper() == '1':
                if homeg > awayg:
                    money += odd_1gg * bn
                    print('You win!')
                    happiness += 2
                    return money, happiness
                else:
                    print('You loss!')
                    happiness -= 1
                    return money, happiness
            elif play.upper() == '2':
                if homeg < awayg:
                    money += odd_2gg * bn
                    print('You win!')
                    happiness += 2
                    return money, happiness
                else:
                    print('You loss!')
                    happiness -= 1
                    return money, happiness
            else:
                print('You loss!')
                happiness -= 1
                return money, happiness
        else:
            print('You loss!')
            happiness -= 1
            return money, happiness
    elif ggng.upper() == 'NG':
        if homeg == 0 or awayg == 0:
            if play.upper() == 'X':
                if homeg == awayg:
                    money += odd_xngg * bn
                    print('You win!')
                    happiness += 2
                    return money, happiness
                else:
                    print('You loss!')
                    happiness -= 1
                    return money, happiness
            elif play.upper() == '1':
                if homeg > awayg:
                    money += odd_1ngg * bn
                    print('You win!')
                    happiness += 2
                    return money, happiness
                else:
                    print('You loss!')
                    happiness -= 1
                    return money, happiness
            elif play.upper() == '2':
                if homeg < awayg:
                    money += odd_2ngg * bn
                    print('You win!')
                    happiness += 2
                    return money, happiness
                else:
                    print('You loss!')
                    happiness -= 1
                    return money, happiness
            else:
                print('You loss!')
                happiness -= 1
                return money, happiness
        else:
            print('You loss!')
            happiness -= 1
            return money, happiness


def checkggou(play, ou, nou, homeg, awayg, money, happiness, bn, odd_ouggng):
    if ou.upper() == 'O':
        if nou < homeg + awayg:
            if play.upper() == 'GG':
                if homeg != 0 and awayg != 0:
                    money += odd_ouggng[nou][1] * bn
                    print('You win!')
                    happiness += 2
                    return money, happiness
                else:
                    print('You loss!')
                    happiness -= 1
                    return money, happiness
            elif play.upper() == 'NG':
                if homeg > awayg:
                    money += odd_ouggng[nou][1] * bn
                    print('You win!')
                    happiness += 2
                    return money, happiness
                else:
                    print('You loss!')
                    happiness -= 1
                    return money, happiness
        else:
            print('You loss!')
            happiness -= 1
            return money, happiness
    elif ou.upper() == 'U':
        if nou > homeg + awayg:
            if play.upper() == 'GG':
                if homeg != 0 and awayg != 0:
                    money += odd_ouggng[nou][0] * bn
                    print('You win!')
                    happiness += 2
                    return money, happiness
                else:
                    print('You loss!')
                    happiness -= 1
                    return money, happiness
            elif play.upper() == 'NG':
                if homeg > awayg:
                    money += odd_ouggng[nou][0] * bn
                    print('You win!')
                    happiness += 2
                    return money, happiness
                else:
                    print('You loss!')
                    happiness -= 1
                    return money, happiness
        else:
            print('You loss!')
            happiness -= 1
            return money, happiness


# Monte Carlo Calculation


def wld(h, a):
    dha = abs((h[1]) - (a[1]))
    ha = abs(h[1] + a[1] - 140)
    pd = 0.38 - ha * 0.002 - dha * 0.004
    ph = (1 - pd) * (h[1] * (h[1] / a[1]) * 0.95) / (h[1] + a[1]) * (math.log2(h[1]) / math.log2(a[1])) * (
            math.pi / 3) ** ((h[1] / a[1]) * ((math.pi + math.e) / math.e))
    if ph >= 1 - pd:
        ph = 1 - pd - 0.01
    pa = 1 - ph - pd
    return ph, pd, pa


def wld1(h, a):
    dha = abs(h - a)
    ha = abs(h + a - 140)
    pd = 0.38 - ha * 0.002 - dha * 0.004
    ph = (1 - pd) * (h * (h / a) * 0.95) / (h + a) * (math.log2(h) / math.log2(a)) * (math.pi / 3) ** (
            (h / a) * ((math.pi + math.e) / math.e))
    if ph >= 1 - pd:
        ph = 1 - pd - 0.01
    pa = 1 - ph - pd
    return ph, pd, pa


def ggn(homeg, awayg, gg, ngg, h2g, h2n, a2g, a2n):
    if homeg != 0 and awayg != 0:
        gg += 1
    else:
        ngg += 1
    if homeg == 0:
        h2n += 1
    else:
        h2g += 1
    if awayg == 0:
        a2n += 1
    else:
        a2g += 1
    return gg, ngg, h2g, h2n, a2g, a2n


def ddg(homeg, awayg, dg, hg, ag):
    dg[abs(homeg - awayg)] += 1
    hg[homeg] += 1
    ag[awayg] += 1
    return dg, hg, ag


def once(h, a, pos):
    ph, pd, pa = wld(h, a)
    pg = poisson(h, a)
    r = result(ph, pd)
    g = goal(r, pg)
    homeg, awayg = hag(r, g)
    pos[homeg][awayg] += 1
    return homeg, awayg, pos


def once1(h, a, pos):
    ph, pd, pa = wld1(h, a)
    pg = poisson1(h, a)
    r = result(ph, pd)
    g = goal(r, pg)
    homeg, awayg = hag(r, g)
    pos[homeg][awayg] += 1
    return homeg, awayg, pos


# System to complain


def complain():
    say = ['Did the forward take money from the bet company?',
           'One more goal please, please!',
           'Fake match! They have taken money!',
           'Stupid team! Why do not attack?',
           'That was a penalty! The referee is controlling the odds!',
           'The dog-like bookmaker!',
           'Noooooooooooo!',
           'I am losing money continuously!',
           'Why is this match so fake?',
           'Over 2.5 sure money!',
           'The stupid goalkeeper is just idiot!',
           'Why the world will not just stop this?']
    random.shuffle(say)
    print(f'\n{say[0]}\n')
    time.sleep(3)
    os.system('cls')


#


# The System of Bet


def bet(money, happiness):
    print('''
Loading...
''')

    h = [[], []]
    a = [[], []]
    hn = [[], []]
    an = [[], []]
    hc = [[], []]
    ac = [[], []]
    h, a, hn, an, hc, ac = randgame(h, a, hn, an, hc, ac)
    h = h[1]
    a = a[1]
    gg = 0
    ngg = 0
    h2g = 0
    a2g = 0
    h2n = 0
    a2n = 0
    record = []
    dg = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    hg = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ag = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    pos = []
    for i in range(11):
        pos.append([])
        for j in range(11):
            pos[i].append(0)

    for ttttt in range(300000):
        homeg, awayg, pos = once1(h, a, pos)
        gg, ngg, h2g, h2n, a2g, a2n = ggn(homeg, awayg, gg, ngg, h2g, h2n, a2g, a2n)
        dg, hg, ag = ddg(homeg, awayg, dg, hg, ag)

    gg = round(1 / (gg / 300000) * 0.95, 2)
    ngg = round(1 / (ngg / 300000) * 0.95, 2)
    h2g = round(1 / (h2g / 300000) * 0.95, 2)
    h2n = round(1 / (h2n / 300000) * 0.95, 2)
    a2g = round(1 / (a2g / 300000) * 0.95, 2)
    a2n = round(1 / (a2n / 300000) * 0.95, 2)

    for i in range(10):
        dg[i] = round(1 / (dg[i] / 300000) * 0.95, 2)

    for i in range(10):
        if hg[i] != 0:
            hg[i] = round(1 / (hg[i] / 300000) * 0.95, 2)
        else:
            hg[i] = 114514.00

    for i in range(10):
        if ag[i] != 0:
            ag[i] = round(1 / (ag[i] / 300000) * 0.95, 2)
        else:
            ag[i] = 114514.00

    for i in range(10):
        for j in range(10):
            if pos[i][j] != 0:
                pos[i][j] = round((1 / (pos[i][j] / 300000)) * 0.95, 2)
            else:
                pos[i][j] = 114514.00
    h = [[], h]
    a = [[], a]
    os.system('cls')
    while money > 0:
        h, a, hn, an, hc, ac = randgame(h, a, hn, an, hc, ac)
        odd_h, odd_d, odd_a, odd_1x, odd_x2, odd_12, odddnb1, odddnb2, ph, pd, pa = wldodd(h, a)
        pg = poisson(h, a)
        odd_ou = oddou(pg)
        odd_gn = oddgn(pg)
        odd_tg = oddtg(pg)
        odd_1gg, odd_xgg, odd_2gg, odd_1ngg, odd_xngg, odd_2ngg, odd_ou12dh, odd_ouggng = oddcomb(odd_h, odd_d, odd_a,
                                                                                                  odd_ou, gg, ngg)
        flag = 0
        while flag != 1:
            oddprint(money, happiness, hn, an, hc, ac, odd_h, odd_a, odd_d, odd_1x, odd_x2, odd_12, odd_ou, gg, ngg)
            c = input('''
══════════════════════════════════════════════
1. Detailed Odds
2. Bet
3. Results
4. Skip
5. Complain
6. Back To Main Menu
══════════════════════════════════════════════
''')
            if c == '1':
                os.system('cls')
                pick = input('''
══════════════════════════════════════════════
1. Result
2. Over/Under
3. Teams to Goal
4. Correct Score
5. Total Goals
6. Home & Away Goals
7. Goal Difference
8. Combination
9. Back
══════════════════════════════════════════════
''')
                if pick == '1':
                    os.system('cls')
                    oddresultprint(odd_h, odd_a, odd_d, odd_1x, odd_x2, odd_12, odddnb1, odddnb2)
                    print('')
                    input('Press Enter to Quit')
                    os.system('cls')
                elif pick == '2':
                    os.system('cls')
                    ouoddprint(odd_ou)
                    print('')
                    input('Press Enter to Quit')
                    os.system('cls')
                elif pick == '3':
                    os.system('cls')
                    oddt2g(gg, ngg, h2g, a2g, h2n, a2n)
                    print('')
                    input('Press Enter to Quit')
                    os.system('cls')
                elif pick == '4':
                    os.system('cls')
                    oddcsprint(pos)
                    print('')
                    input('Press Enter to Quit')
                    os.system('cls')
                elif pick == '5':
                    os.system('cls')
                    oddtgprint(odd_gn, odd_tg)
                    print('')
                    input('Press Enter to Quit')
                    os.system('cls')
                elif pick == '6':
                    os.system('cls')
                    oddhagprint(hg, ag)
                    input('Press Enter to Quit')
                    os.system('cls')
                elif pick == '7':
                    os.system('cls')
                    odddgprint(dg)
                    print('')
                    input('Press Enter to Quit')
                    os.system('cls')
                elif pick == '8':
                    os.system('cls')
                    oddcombprt(odd_1gg, odd_xgg, odd_2gg, odd_1ngg, odd_xngg, odd_2ngg, odd_ou12dh, odd_ouggng)
                    print('')
                    input('Press Enter to Quit')
                    os.system('cls')
                elif pick == '9':
                    os.system('cls')
            if c == '2':
                os.system('cls')
                pick = input('''
══════════════════════════════════════════════
1.  Result
2.  Double Chance
3.  Draw No Bet
4.  Over/Under
5.  Both Teams to Goal
6.  Correct Score
7.  Total Goals
8.  Exact Total Goals
9.  Home & Away Team to Goal
10. Home & Away Goals
11. Goal Difference
12. Result and Over/Under
13. Result and Both Teams to Goal
14. Over/Under and Both Teams to Goal
15. Back
══════════════════════════════════════════════
''')
                os.system('cls')
                if pick != '15':
                    if pick == '1':
                        os.system('cls')
                        flag = 0
                        while flag != 1:
                            oddresultprint(odd_h, odd_a, odd_d, odd_1x, odd_x2, odd_12, odddnb1, odddnb2)
                            print('')
                            res = input('Please! Tell me what you want to bet! (1/X/2) ')
                            if res.upper() == '1' or res.upper() == '2' or res.upper() == 'X':
                                flag = 1
                            else:
                                os.system('cls')
                                print('You are very wrong!')
                                time.sleep(0.5)
                    if pick == '2':
                        flag = 0
                        while flag != 1:
                            oddresultprint(odd_h, odd_a, odd_d, odd_1x, odd_x2, odd_12, odddnb1, odddnb2)
                            print('')
                            dch = input('Please! Tell me what you want to bet! (1X/X2/12) ')
                            if dch.upper() == '1X' or dch.upper() == 'X2' or dch.upper() == '12':
                                flag = 1
                            else:
                                os.system('cls')
                                print('You are very wrong!')
                                time.sleep(0.5)
                    if pick == '3':
                        flag = 0
                        while flag != 1:
                            oddresultprint(odd_h, odd_a, odd_d, odd_1x, odd_x2, odd_12, odddnb1, odddnb2)
                            print('')
                            dnbp = input('Please! Tell me what you want to bet! (1/2) ')
                            if dnbp == '1' or dnbp == '2':
                                flag = 1
                            else:
                                os.system('cls')
                                print('You are very wrong!')
                                time.sleep(0.5)
                    if pick == '4':
                        flag = 0
                        while flag != 1:
                            ouoddprint(odd_ou)
                            print('')
                            pou = input('Please! Tell me Over or Under! (O/U) ')
                            ou = int(float(input('Please tell me Over/Under how many! ')) - 0.5)
                            if pou.upper() == 'O' or pou.upper() == 'U':
                                if ou > 9 or ou < 0:
                                    flag = 1
                            else:
                                os.system('cls')
                                print('You are very wrong!')
                                time.sleep(0.5)
                    if pick == '5':
                        flag = 0
                        while flag != 1:
                            oddt2g(gg, ngg, h2g, a2g, h2n, a2n)
                            print('')
                            ggng = input('Please! Tell me Goal Goal/No Goal! (GG/NG) ')
                            if ggng == 'GG' or ggng == 'NG':
                                flag = 1
                            else:
                                os.system('cls')
                                print('You are very wrong!')
                                time.sleep(0.5)
                    if pick == '6':
                        flag = 0
                        while flag != 1:
                            oddcsprint(pos)
                            print('')
                            csp = input('Please! Tell me the Correct Score! (X-X or X:X) ')
                            if csp[1] == '-' or csp[1] == ':':
                                flag = 1
                            else:
                                os.system('cls')
                                print('You are very wrong!')
                                time.sleep(0.5)
                    if pick == '7':
                        flag = 0
                        while flag != 1:
                            oddtgprint(odd_gn, odd_tg)
                            print('')
                            tgs = input('Please! Tell me the Range of Goals! (0-1/2-3/4-5/6+) ')
                            if tgs == '0-1' or tgs == '2-3' or tgs == '4-5' or tgs == '6+':
                                flag = 1
                            else:
                                os.system('cls')
                                print('You are very wrong!')
                                time.sleep(0.5)
                    if pick == '8':
                        flag = 0
                        while flag != 1:
                            oddtgprint(odd_gn, odd_tg)
                            print('')
                            gns = input('Please! Tell me the Exact Goal! (0 to 9) ')
                            if gns == '0' or gns == '1' or gns == '2' or gns == '3' or gns == '4' or gns == '5' or gns == '6' or gns == '7' or gns == '8' or gns == '9':
                                flag = 1
                            else:
                                os.system('cls')
                                print('You are very wrong!')
                                time.sleep(0.5)
                    if pick == '9':
                        flag = 0
                        while flag != 1:
                            oddt2g(gg, ngg, h2g, a2g, h2n, a2n)
                            print('')
                            hagn = input('Please! Tell me Home/Away to Score/no Score! (HG/HNG/AG/ANG) ')
                            if hagn == 'HG' or hagn == 'HNG' or hagn == 'AG' or hagn == 'ANG':
                                flag = 1
                            else:
                                os.system('cls')
                                print('You are very wrong!')
                                time.sleep(0.5)
                    if pick == '10':
                        flag = 0
                        while flag != 1:
                            oddhagprint(hg, ag)
                            print('')
                            ha = input('Please! Tell me Home or Away! (H/A) ')
                            no = input('Please! Tell me the Goal Number! (0-9) ')
                            if ha == 'H' or ha == 'A':
                                if no == '0' or no == '1' or no == '2' or no == '3' or no == '4' or no == '5' or no == '6' or no == '7' or no == '8' or no == '9':
                                    flag = 1
                            else:
                                os.system('cls')
                                print('You are very wrong!')
                                time.sleep(0.5)
                    if pick == '11':
                        flag = 0
                        while flag != 1:
                            odddgprint(dg)
                            print('')
                            gdp = input('Please! Tell me the Goal Difference! (0-9) ')
                            if gdp == '0' or gdp == '1' or gdp == '2' or gdp == '3' or gdp == '4' or gdp == '5' or gdp == '6' or gdp == '7' or gdp == '8' or gdp == '9':
                                flag = 1
                            else:
                                os.system('cls')
                                print('You are very wrong!')
                                time.sleep(0.5)
                    if pick == '12':
                        flag = 0
                        while flag != 1:
                            oddcombprt(odd_1gg, odd_xgg, odd_2gg, odd_1ngg, odd_xngg, odd_2ngg, odd_ou12dh, odd_ouggng)
                            print('')
                            resu = input('Please! Tell me the Result! (1/X/2) ')
                            ou = input('Please! Tell me Over or Under! (O/U) ')
                            nou = int(float(input('Please tell me Over/Under how many! ')) - 0.5)
                            if resu == '1' or resu == '2' or resu.upper() == 'X':
                                if ou.upper() == 'O' or ou.upper() == 'U':
                                    if nou == 0 or nou == 1 or nou == 2 or nou == 3 or nou == 4 or nou == 5 or nou == 6 or nou == 7 or nou == 8 or nou == 9:
                                        flag = 1
                            else:
                                os.system('cls')
                                print('You are very wrong!')
                                time.sleep(0.5)
                    if pick == '13':
                        flag = 0
                        while flag != 1:
                            oddcombprt(odd_1gg, odd_xgg, odd_2gg, odd_1ngg, odd_xngg, odd_2ngg, odd_ou12dh, odd_ouggng)
                            print('')
                            resu = input('Please! Tell me the Result! (1/X/2) ')
                            ggng = input('Please! Tell me Goal Goal or No Goal! (GG/NG) ')
                            if ggng == 'NG' or ggng == 'GG':
                                if resu == '1' or resu == '2' or resu.upper() == 'X':
                                    flag = 1
                            else:
                                os.system('cls')
                                print('You are very wrong!')
                                time.sleep(0.5)
                    if pick == '14':
                        flag = 0
                        while flag != 1:
                            oddcombprt(odd_1gg, odd_xgg, odd_2gg, odd_1ngg, odd_xngg, odd_2ngg, odd_ou12dh, odd_ouggng)
                            print('')
                            ggng = input('Please! Tell me Goal Goal or No Goal! (GG/NG) ')
                            ou = input('Please! Tell me Over or Under! (O/U) ')
                            nou = int(float(input('Please tell me Over/Under how many! ')))
                            if ggng == 'NG' or ggng == 'GG':
                                if ou.upper() == 'O' or ou.upper() == 'U':
                                    if nou == 0 or nou == 1 or nou == 2 or nou == 3 or nou == 4 or nou == 5 or nou == 6 or nou == 7 or nou == 8 or nou == 9:
                                        flag = 1
                            else:
                                os.system('cls')
                                print('You are very wrong!')
                                time.sleep(0.5)
                    bn = float(input('Please! Tell me how much you want to bet! '))
                    money -= bn
                    flag = 1
                    os.system('cls')
            elif c == '3':
                os.system('cls')
                rec(record)
                print('')
                input('Press Enter to Quit')
                os.system('cls')
            elif c == '4':
                pick = '0'
                os.system('cls')
                flag = 1
            elif c == '5':
                os.system('cls')
                complain()
            elif c == '6':
                break
        if c == '6':
            break
        r = result(ph, pd)
        g = goal(r, pg)
        homeg, awayg = hag(r, g)
        if pick == '1':
            money, happiness = check12x(res, homeg, awayg, money, happiness, odd_h, odd_d, odd_a, bn)
        if pick == '4':
            money, happiness = checkou(pou, money, happiness, ou, odd_ou, bn, g)
        if pick == '2':
            money, happiness = checkdc(dch, homeg, awayg, money, happiness, odd_12, odd_x2, odd_1x, bn)
        if pick == '3':
            money, happiness = checkdnb(dnbp, homeg, awayg, money, happiness, odddnb1, odddnb2, bn)
        if pick == '5':
            money, happiness = checkgg(ggng, money, happiness, homeg, awayg, gg, ngg, bn)
        if pick == '6':
            money, happiness = checkcs(csp, money, happiness, homeg, awayg, pos, bn)
        if pick == '7':
            money, happiness = checktgs(tgs, money, happiness, g, bn, odd_tg)
        if pick == '8':
            money, happiness = checkegs(gns, money, happiness, g, bn, odd_gn)
        if pick == '9':
            money, happiness = checkhagg(hagn, money, happiness, homeg, awayg, h2g, h2n, a2g, a2n, bn)
        if pick == '10':
            money, happiness = checkhaegs(ha, no, money, happiness, g, bn, hg, ag, homeg, awayg)
        if pick == '11':
            money, happiness = checkdg(gdp, money, happiness, homeg, awayg, dg, bn)
        if pick == '12':
            money, happiness = check12xou(resu, ou, nou, homeg, awayg, money, happiness, bn, odd_ou12dh)
        if pick == '13':
            money, happiness = check12xgg(resu, ggng, homeg, awayg, money, happiness, bn, odd_1gg, odd_xgg, odd_2gg,
                                          odd_1ngg, odd_xngg, odd_2ngg)
        if pick == '14':
            money, happiness = checkggou(ggng, ou, nou, homeg, awayg, money, happiness, bn, odd_ouggng)
        print('The score is', homeg, '-', awayg)
        if len(record) >= 20:
            del record[0]
            record.append((hn[0], homeg, awayg, an[0]))
        else:
            record.append((hn[0], homeg, awayg, an[0]))
        print('''
Loading...
''')
        gg = 0
        ngg = 0
        h2g = 0
        a2g = 0
        h2n = 0
        a2n = 0
        dg = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        hg = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ag = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        pos = []
        for i in range(11):
            pos.append([])
            for j in range(11):
                pos[i].append(0)

        for ttttt in range(300000):
            homeg, awayg, pos = once(h, a, pos)
            gg, ngg, h2g, h2n, a2g, a2n = ggn(homeg, awayg, gg, ngg, h2g, h2n, a2g, a2n)
            dg, hg, ag = ddg(homeg, awayg, dg, hg, ag)

        gg = round(1 / (gg / 300000) * 0.95, 2)
        ngg = round(1 / (ngg / 300000) * 0.95, 2)
        h2g = round(1 / (h2g / 300000) * 0.95, 2)
        h2n = round(1 / (h2n / 300000) * 0.95, 2)
        a2g = round(1 / (a2g / 300000) * 0.95, 2)
        a2n = round(1 / (a2n / 300000) * 0.95, 2)

        for i in range(10):
            dg[i] = round(1 / (dg[i] / 300000) * 0.95, 2)

        for i in range(10):
            if hg[i] != 0:
                hg[i] = round(1 / (hg[i] / 300000) * 0.95, 2)
            else:
                hg[i] = 114514.00

        for i in range(10):
            if ag[i] != 0:
                ag[i] = round(1 / (ag[i] / 300000) * 0.95, 2)
            else:
                ag[i] = 114514.00

        for i in range(10):
            for j in range(10):
                if pos[i][j] != 0:
                    pos[i][j] = round((1 / (pos[i][j] / 300000)) * 0.95, 2)
                else:
                    pos[i][j] = 114514.00
        os.system('cls')
    print('You have finally:', money)
    time.sleep(3)
    os.system('cls')
    return money, happiness


intro()
