import random

all_countries = [
    "Afghanistan",
    "Albania",
    "Algeria",
    "American Samoa",
    "Andorra",
    "Angola",
    "Anguilla",
    "Antarctica",
    "Antigua and Barbuda",
    "Argentina",
    "Armenia",
    "Aruba",
    "Australia",
    "Austria",
    "Azerbaijan",
    "Bahamas",
    "Bahrain",
    "Bangladesh",
    "Barbados",
    "Belarus",
    "Belgium",
    "Belize",
    "Benin",
    "Bermuda",
    "Bhutan",
    "Bolivia",
    "Bosnia and Herzegovina",
    "Botswana",
    "Bouvet Island",
    "Brazil",
    "British Indian Ocean Territory",
    "Brunei",
    "Bulgaria",
    "Burkina Faso",
    "Burundi",
    "Cambodia",
    "Cameroon",
    "Canada",
    "Cape Verde",
    "Cayman Islands",
    "Central African Republic",
    "Chad",
    "Chile",
    "China",
    "Christmas Island",
    "Cocos (Keeling) Islands",
    "Colombia",
    "Comoros",
    "Congo",
    "The Democratic Republic of Congo",
    "Cook Islands",
    "Costa Rica",
    "Ivory Coast",
    "Croatia",
    "Cuba",
    "Cyprus",
    "Czech Republic",
    "Denmark",
    "Djibouti",
    "Dominica",
    "Dominican Republic",
    "East Timor",
    "Ecuador",
    "Egypt",
    "England",
    "El Salvador",
    "Equatorial Guinea",
    "Eritrea",
    "Estonia",
    "Ethiopia",
    "Falkland Islands",
    "Faroe Islands",
    "Fiji Islands",
    "Finland",
    "France",
    "French Guiana",
    "French Polynesia",
    "French Southern territories",
    "Gabon",
    "Gambia",
    "Georgia",
    "Germany",
    "Ghana",
    "Gibraltar",
    "Greece",
    "Greenland",
    "Grenada",
    "Guadeloupe",
    "Guam",
    "Guatemala",
    "Guernsey",
    "Guinea",
    "Guinea-Bissau",
    "Guyana",
    "Haiti",
    "Heard Island and McDonald Islands",
    "Holy See (Vatican City State)",
    "Honduras",
    "Hong Kong",
    "Hungary",
    "Iceland",
    "India",
    "Indonesia",
    "Iran",
    "Iraq",
    "Ireland",
    "Israel",
    "Isle of Man",
    "Italy",
    "Jamaica",
    "Japan",
    "Jersey",
    "Jordan",
    "Kazakhstan",
    "Kenya",
    "Kiribati",
    "Kuwait",
    "Kyrgyzstan",
    "Laos",
    "Latvia",
    "Lebanon",
    "Lesotho",
    "Liberia",
    "Libyan Arab Jamahiriya",
    "Liechtenstein",
    "Lithuania",
    "Luxembourg",
    "Macao",
    "North Macedonia",
    "Madagascar",
    "Malawi",
    "Malaysia",
    "Maldives",
    "Mali",
    "Malta",
    "Marshall Islands",
    "Martinique",
    "Mauritania",
    "Mauritius",
    "Mayotte",
    "Mexico",
    "Micronesia, Federated States of",
    "Moldova",
    "Monaco",
    "Mongolia",
    "Montserrat",
    "Montenegro",
    "Morocco",
    "Mozambique",
    "Myanmar",
    "Namibia",
    "Nauru",
    "Nepal",
    "Netherlands",
    "Netherlands Antilles",
    "New Caledonia",
    "New Zealand",
    "Nicaragua",
    "Niger",
    "Nigeria",
    "Niue",
    "Norfolk Island",
    "North Korea",
    "Northern Ireland",
    "Northern Mariana Islands",
    "Norway",
    "Oman",
    "Pakistan",
    "Palau",
    "Palestine",
    "Panama",
    "Papua New Guinea",
    "Paraguay",
    "Peru",
    "Philippines",
    "Pitcairn",
    "Poland",
    "Portugal",
    "Puerto Rico",
    "Qatar",
    "Reunion",
    "Romania",
    "Russian Federation",
    "Rwanda",
    "Saint Helena",
    "Saint Kitts and Nevis",
    "Saint Lucia",
    "Saint Pierre and Miquelon",
    "Saint Vincent and the Grenadines",
    "Samoa",
    "San Marino",
    "Sao Tome and Principe",
    "Saudi Arabia",
    "Scotland",
    "Senegal",
    "Serbia",
    "Seychelles",
    "Sierra Leone",
    "Singapore",
    "Slovakia",
    "Slovenia",
    "Solomon Islands",
    "Somalia",
    "South Africa",
    "South Georgia and the South Sandwich Islands",
    "South Korea",
    "South Sudan",
    "Spain",
    "SriLanka",
    "Sudan",
    "Suriname",
    "Svalbard and Jan Mayen",
    "Swaziland",
    "Sweden",
    "Switzerland",
    "Syria",
    "Tajikistan",
    "Tanzania",
    "Thailand",
    "Timor-Leste",
    "Togo",
    "Tokelau",
    "Tonga",
    "Trinidad and Tobago",
    "Tunisia",
    "Turkey",
    "Turkmenistan",
    "Turks and Caicos Islands",
    "Tuvalu",
    "Uganda",
    "Ukraine",
    "United Arab Emirates",
    "United Kingdom",
    "United States",
    "United States Minor Outlying Islands",
    "Uruguay",
    "Uzbekistan",
    "Vanuatu",
    "Venezuela",
    "Vietnam",
    "Virgin Islands, British",
    "Virgin Islands, U.S.",
    "Wales",
    "Wallis and Futuna",
    "Western Sahara",
    "Yemen",
    "Yugoslavia",
    "Zambia",
    "Zimbabwe",
]
commonwealth_states = [
    "Antigua and Barbuda",
    "Australia",
    "Bahamas",
    "Bangladesh",
    "Barbados",
    "Belize",
    "Botswana",
    "Brunei",
    "Cameroon",
    "Canada",
    "Cyprus",
    "Dominica",
    "Eswatini",
    "Fiji",
    "Gambia",
    "Ghana",
    "Grenada",
    "Guyana",
    "India",
    "Jamaica",
    "Kenya",
    "Kiribati",
    "Lesotho",
    "Malawi",
    "Malaysia",
    "Maldives",
    "Malta",
    "Mauritius",
    "Mozambique",
    "Namibia",
    "Nauru",
    "New Zealand",
    "Nigeria",
    "Pakistan",
    "Papua New Guinea",
    "Rwanda",
    "Saint Kitts and Nevis",
    "Saint Lucia",
    "Saint Vincent and the Grenadines",
    "Samoa",
    "Seychelles",
    "Sierra Leone",
    "Singapore",
    "Solomon Islands",
    "South Africa",
    "Sri Lanka",
    "Tanzania",
    "Tonga",
    "Trinidad and Tobago",
    "Tuvalu",
    "Uganda",
    "United Kingdom",
    "Vanuatu",
    "Zambia",
]

# verzin voor elk gegeven het goede datatype, voor grafische gegevens
paspoort = {
    "pasfoto": "Elmo_from_Sesame_Street.gif",
    "achternaam": "Puppet",
    "voornamen": "Elmo",
    "geboortedatum": "3-02-1980",
    "geboorteplaats": "Sesame Street",
    "geslacht": "male",
    "lengte": 75,
    "handtekening": "elmoSign.jpg",
    "burgerservicenummer": 123,
    "nationaliteit": "United States",
    "vingerafdrukL": "tickle_handsL.jpg",
    "vingerafdrukR": "tickle_handsR.jpg",
}

# lees voor de volgende velden de waarden uit het paspoort dict en stop ze in een nieuwe variabele met een geschikte naam
geboortedatum = paspoort["geboortedatum"]
lengte = paspoort["lengte"]
geboorteplaats = paspoort["geboorteplaats"]
print(geboortedatum, lengte, geboorteplaats)

foto = ["1.jpg", "2.jpg", "3.jpg"]
achternaam = ["de Vries", "Jansen", "Xi'lantulupuxsa"]
voornaam = ["Piet", "Jan", "Umbulula"]
geboortedatum = random.randint(1, 28), random.randint(
    1, 12), random.randint(1900, 2020)
geboorteplaats = ["Lutjebroek", "Sesamstraat", "Timboektoe"]
geslacht = ["Agender", "Androgyne", "Androgynous", "Bigender", "Cis", "Cisgender", "Cis Female", "Cis Male", "Cis Man", "Cis Woman", "Cisgender Female", "Cisgender Male", "Cisgender Man", "Cisgender Woman", "Female to Male", "FTM", "Gender Fluid", "Gender Nonconforming", "Gender Questioning", "Gender Variant", "Genderqueer", "Intersex", "Male to Female", "MTF", "Neither", "Neutrois", "Non-binary", "Other", "Pangender", "Trans", "Trans*",
            "Trans Female", "Trans* Female", "Trans Male", "Trans* Male", "Trans Man", "Trans* Man", "Trans Person", "Trans* Person", "Trans Woman", "Trans* Woman", "Transfeminine", "Transgender", "Transgender Female", "Transgender Male", "Transgender Man", "Transgender Person", "Transgender Woman", "Transmasculine", "Transsexual", "Transsexual Female", "Transsexual Male", "Transsexual Man", "Transsexual Person", "Transsexual Woman", "Two-Spirit"]
lengte = random.randint(50, 200)
bsn = random.randint(1111111111, 9999999999)

print(geboortedatum)

paspoort2 = {}
paspoort2["pasfoto"] = random.choice(foto)
paspoort2["achternaam"] = random.choice(achternaam)
paspoort2["voornamen"] = random.choice(voornaam)
paspoort2["geboortedatum"] = geboortedatum
paspoort2["geboorteplaats"] = random.choice(geboorteplaats)
paspoort2["geslacht"] = random.choice(geslacht)
paspoort2["lengte"] = lengte
paspoort2["handtekening"] = random.choice(foto)
paspoort2["burgerservicenummer"] = bsn
paspoort2["nationaliteit"] = random.choice(all_countries)
paspoort2["vingerafdrukL"] = random.choice(foto)
paspoort2["vingerafdrukR"] = random.choice(foto)

print(paspoort)
