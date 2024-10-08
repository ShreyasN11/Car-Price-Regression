import streamlit as st
import joblib
import numpy as np

model = joblib.load('model1.pkl')

st.title('Car Price Prediction Model')

array = [0] * 696

car_names = [
    'Ambassador CLASSIC 1500',
    'Ambassador Classic 2000',
    'Ambassador Grand 1500',
    'Ambassador Grand 2000',
    'Ashok Leyland Stile',
    'Audi A3 35',
    'Audi A3 40',
    'Audi A4 1.8',
    'Audi A4 2.0',
    'Audi A4 35',
    'Audi A6 2.0',
    'Audi A6 35',
    'Audi Q3 2.0',
    'Audi Q3 35',
    'Audi Q5 2.0',
    'Audi Q5 3.0',
    'Audi Q5 35TDI',
    'Audi Q5 45',
    'Audi Q7 3.0',
    'Audi Q7 35',
    'BMW 3 Series',
    'BMW 5 Series',
    'BMW 6 Series',
    'BMW 7 Series',
    'BMW X1 sDrive',
    'BMW X1 sDrive20d',
    'BMW X1 sDrive20i',
    'BMW X3 xDrive20d',
    'BMW X4 M',
    'BMW X5 3.0d',
    'BMW X6 xDrive30d',
    'BMW X7 xDrive',
    'Chevrolet Aveo 1.4',
    'Chevrolet Aveo U-VA',
    'Chevrolet Beat Diesel',
    'Chevrolet Beat LS',
    'Chevrolet Beat LT',
    'Chevrolet Captiva 2.2',
    'Chevrolet Captiva LT',
    'Chevrolet Cruze LT',
    'Chevrolet Cruze LTZ',
    'Chevrolet Enjoy 1.3',
    'Chevrolet Enjoy 1.4',
    'Chevrolet Enjoy Petrol',
    'Chevrolet Enjoy TCDi',
    'Chevrolet Optra 1.6',
    'Chevrolet Optra Magnum',
    'Chevrolet Sail 1.2',
    'Chevrolet Sail 1.3',
    'Chevrolet Sail Hatchback',
    'Chevrolet Sail LT',
    'Chevrolet Spark 1.0',
    'Chevrolet Tavera B1-10',
    'Chevrolet Tavera B2',
    'Chevrolet Tavera B3',
    'Chevrolet Tavera LS',
    'Chevrolet Tavera Neo',
    'Chevrolet Trailblazer LTZ',
    'Daewoo Matiz SD',
    'Daewoo Matiz SS',
    'Datsun GO A',
    'Datsun GO Anniversary',
    'Datsun GO D',
    'Datsun GO Plus',
    'Datsun GO T',
    'Datsun RediGO 1.0',
    'Datsun RediGO A',
    'Datsun RediGO AMT',
    'Datsun RediGO S',
    'Datsun RediGO SV',
    'Datsun RediGO Sport',
    'Datsun RediGO T',
    'Fiat Avventura MULTIJET',
    'Fiat Avventura Power',
    'Fiat Grande Punto',
    'Fiat Linea 1.3',
    'Fiat Linea Classic',
    'Fiat Linea Emotion',
    'Fiat Palio 1.2',
    'Fiat Punto 1.2',
    'Fiat Punto 1.3',
    'Fiat Punto EVO',
    'Fiat Punto Pure',
    'Force Gurkha Hard',
    'Force One EX',
    'Force One SX',
    'Ford Aspire Titanium',
    'Ford Aspire Trend',
    'Ford Classic 1.4',
    'Ford Classic 1.6',
    'Ford EcoSport 1.5',
    'Ford EcoSport S',
    'Ford Ecosport 1.0',
    'Ford Ecosport 1.5',
    'Ford Ecosport Sports',
    'Ford Endeavour 2.2',
    'Ford Endeavour 2.5L',
    'Ford Endeavour 3.0L',
    'Ford Endeavour 3.2',
    'Ford Endeavour 4x2',
    'Ford Endeavour Hurricane',
    'Ford Fiesta 1.4',
    'Ford Fiesta 1.5',
    'Ford Fiesta 1.6',
    'Ford Fiesta Classic',
    'Ford Fiesta Diesel',
    'Ford Fiesta EXi',
    'Ford Fiesta Titanium',
    'Ford Figo 1.2P',
    'Ford Figo 1.5',
    'Ford Figo 1.5D',
    'Ford Figo 1.5P',
    'Ford Figo Aspire',
    'Ford Figo Diesel',
    'Ford Figo Petrol',
    'Ford Figo Titanium',
    'Ford Freestyle Titanium',
    'Ford Freestyle Trend',
    'Ford Fusion 1.4',
    'Ford Fusion Plus',
    'Ford Ikon 1.3',
    'Ford Ikon 1.4',
    'Ford Ikon 1.6',
    'Ford Ikon 1.8',
    'Honda Accord 2.4',
    'Honda Accord V6',
    'Honda Accord VTi-L',
    'Honda Amaze Anniversary',
    'Honda Amaze E',
    'Honda Amaze EX',
    'Honda Amaze S',
    'Honda Amaze SX',
    'Honda Amaze V',
    'Honda Amaze VX',
    'Honda Amaze i-VTEC',
    'Honda BR-V i-DTEC',
    'Honda BR-V i-VTEC',
    'Honda BRV i-DTEC',
    'Honda BRV i-VTEC',
    'Honda Brio 1.2',
    'Honda Brio E',
    'Honda Brio Exclusive',
    'Honda Brio S',
    'Honda Brio V',
    'Honda CR-V 2.0L',
    'Honda CR-V 2.4',
    'Honda CR-V 2.4L',
    'Honda City 1.3',
    'Honda City 1.5',
    'Honda City 2017-2020',
    'Honda City Corporate',
    'Honda City E',
    'Honda City S',
    'Honda City V',
    'Honda City VX',
    'Honda City ZXi',
    'Honda City i',
    'Honda City i-DTEC',
    'Honda City i-VTEC',
    'Honda Civic 1.8',
    'Honda Civic Hybrid',
    'Honda Civic ZX',
    'Honda Jazz 1.2',
    'Honda Jazz 1.5',
    'Honda Jazz Basic',
    'Honda Jazz Select',
    'Honda Jazz V',
    'Honda Jazz VX',
    'Honda Mobilio RS',
    'Honda Mobilio S',
    'Honda Mobilio V',
    'Honda WR-V i-DTEC',
    'Honda WR-V i-VTEC',
    'Hyundai Accent CRDi',
    'Hyundai Accent DLS',
    'Hyundai Accent Executive',
    'Hyundai Accent GLE',
    'Hyundai Accent GLS',
    'Hyundai Accent GLX',
    'Hyundai Accent Gvs',
    'Hyundai Accent VIVA',
    'Hyundai Creta 1.4',
    'Hyundai Creta 1.6',
    'Hyundai EON 1.0',
    'Hyundai EON D',
    'Hyundai EON Era',
    'Hyundai EON LPG',
    'Hyundai EON Magna',
    'Hyundai EON Sportz',
    'Hyundai Elantra CRDi',
    'Hyundai Elantra GLS',
    'Hyundai Elantra GT',
    'Hyundai Elantra S',
    'Hyundai Elantra SX',
    'Hyundai Elite i20',
    'Hyundai Getz 1.1',
    'Hyundai Getz 1.3',
    'Hyundai Getz 1.5',
    'Hyundai Getz GLE',
    'Hyundai Getz GLS',
    'Hyundai Getz GLX',
    'Hyundai Grand i10',
    'Hyundai Santa Fe',
    'Hyundai Santro AT',
    'Hyundai Santro Asta',
    'Hyundai Santro DX',
    'Hyundai Santro Era',
    'Hyundai Santro GLS',
    'Hyundai Santro GS',
    'Hyundai Santro LE',
    'Hyundai Santro LP',
    'Hyundai Santro LS',
    'Hyundai Santro Magna',
    'Hyundai Santro Sportz',
    'Hyundai Santro Xing',
    'Hyundai Sonata 2.0L',
    'Hyundai Sonata 2.4',
    'Hyundai Sonata 2.4L',
    'Hyundai Sonata CRDi',
    'Hyundai Tucson 2.0',
    'Hyundai Tucson CRDi',
    'Hyundai Venue SX',
    'Hyundai Verna 1.4',
    'Hyundai Verna 1.6',
    'Hyundai Verna CRDi',
    'Hyundai Verna S',
    'Hyundai Verna SX',
    'Hyundai Verna Transform',
    'Hyundai Verna VTVT',
    'Hyundai Verna XXi',
    'Hyundai Verna Xi',
    'Hyundai Xcent 1.1',
    'Hyundai Xcent 1.2',
    'Hyundai i10 Asta',
    'Hyundai i10 Era',
    'Hyundai i10 LPG',
    'Hyundai i10 Magna',
    'Hyundai i10 Sportz',
    'Hyundai i20 1.2',
    'Hyundai i20 1.4',
    'Hyundai i20 2015-2017',
    'Hyundai i20 Active',
    'Hyundai i20 Asta',
    'Hyundai i20 Diesel',
    'Hyundai i20 Era',
    'Hyundai i20 Magna',
    'Hyundai i20 Petrol',
    'Hyundai i20 Sportz',
    'Isuzu D-Max V-Cross',
    'Isuzu MU 7',
    'Isuzu MUX 2WD',
    'Jaguar XE 2016-2019',
    'Jaguar XF 2.0',
    'Jaguar XF 2.2',
    'Jaguar XF 3.0',
    'Jaguar XF Diesel',
    'Jeep Compass 1.4',
    'Jeep Compass 2.0',
    'Jeep Wrangler 2016-2019',
    'Kia Seltos HTE',
    'Kia Seltos HTX',
    'Land Rover Discovery',
    'Land Rover Freelander',
    'Land Rover Range',
    'Lexus ES 300h',
    'MG Hector Sharp',
    'MG Hector Smart',
    'Mahindra Bolero 2011-2019',
    'Mahindra Bolero B2',
    'Mahindra Bolero B4',
    'Mahindra Bolero DI',
    'Mahindra Bolero GLX',
    'Mahindra Bolero LX',
    'Mahindra Bolero PLUS',
    'Mahindra Bolero Pik-Up',
    'Mahindra Bolero Power',
    'Mahindra Bolero SLE',
    'Mahindra Bolero SLX',
    'Mahindra Bolero VLX',
    'Mahindra Bolero XL',
    'Mahindra Bolero ZLX',
    'Mahindra Ingenio CRDe',
    'Mahindra Jeep CL',
    'Mahindra Jeep Classic',
    'Mahindra Jeep MM',
    'Mahindra KUV 100',
    'Mahindra Logan Diesel',
    'Mahindra Logan Petrol',
    'Mahindra Marazzo M2',
    'Mahindra Marazzo M6',
    'Mahindra Marazzo M8',
    'Mahindra Marshal DI',
    'Mahindra NuvoSport N8',
    'Mahindra Quanto C2',
    'Mahindra Quanto C4',
    'Mahindra Quanto C6',
    'Mahindra Quanto C8',
    'Mahindra Renault Logan',
    'Mahindra Scorpio 1.99',
    'Mahindra Scorpio 2.6',
    'Mahindra Scorpio 2006-2009',
    'Mahindra Scorpio 2009-2014',
    'Mahindra Scorpio EX',
    'Mahindra Scorpio Gateway',
    'Mahindra Scorpio Getaway',
    'Mahindra Scorpio Intelli',
    'Mahindra Scorpio LX',
    'Mahindra Scorpio M2DI',
    'Mahindra Scorpio S10',
    'Mahindra Scorpio S11',
    'Mahindra Scorpio S2',
    'Mahindra Scorpio S3',
    'Mahindra Scorpio S4',
    'Mahindra Scorpio S5',
    'Mahindra Scorpio S7',
    'Mahindra Scorpio SLE',
    'Mahindra Scorpio SLX',
    'Mahindra Scorpio VLS',
    'Mahindra Scorpio VLX',
    'Mahindra Ssangyong Rexton',
    'Mahindra Supro LX',
    'Mahindra TUV 300',
    'Mahindra Thar 4X4',
    'Mahindra Thar CRDe',
    'Mahindra Thar DI',
    'Mahindra Verito 1.4',
    'Mahindra Verito 1.5',
    'Mahindra Verito 1.6',
    'Mahindra Verito Vibe',
    'Mahindra Willys CJ',
    'Mahindra XUV300 W6',
    'Mahindra XUV300 W8',
    'Mahindra XUV500 AT',
    'Mahindra XUV500 W10',
    'Mahindra XUV500 W11',
    'Mahindra XUV500 W4',
    'Mahindra XUV500 W5',
    'Mahindra XUV500 W6',
    'Mahindra XUV500 W7',
    'Mahindra XUV500 W8',
    'Mahindra XUV500 W9',
    'Mahindra Xylo D2',
    'Mahindra Xylo D4',
    'Mahindra Xylo E4',
    'Mahindra Xylo E6',
    'Mahindra Xylo E8',
    'Mahindra Xylo H4',
    'Mahindra Xylo H9',
    'Maruti 800 AC',
    'Maruti 800 DX',
    'Maruti 800 EX',
    'Maruti 800 Std',
    'Maruti 800 Uniq',
    'Maruti A-Star Lxi',
    'Maruti A-Star Vxi',
    'Maruti A-Star Zxi',
    'Maruti Alto 800',
    'Maruti Alto AX',
    'Maruti Alto Green',
    'Maruti Alto K10',
    'Maruti Alto LX',
    'Maruti Alto LXI',
    'Maruti Alto LXi',
    'Maruti Alto STD',
    'Maruti Alto Std',
    'Maruti Baleno Alpha',
    'Maruti Baleno Delta',
    'Maruti Baleno LXI',
    'Maruti Baleno RS',
    'Maruti Baleno Sigma',
    'Maruti Baleno Zeta',
    'Maruti Celerio LDi',
    'Maruti Celerio LXI',
    'Maruti Celerio VDi',
    'Maruti Celerio VXI',
    'Maruti Celerio VXi',
    'Maruti Celerio X',
    'Maruti Celerio ZDi',
    'Maruti Celerio ZXI',
    'Maruti Ciaz 1.3',
    'Maruti Ciaz 1.4',
    'Maruti Ciaz AT',
    'Maruti Ciaz Alpha',
    'Maruti Ciaz Delta',
    'Maruti Ciaz RS',
    'Maruti Ciaz S',
    'Maruti Ciaz VDI',
    'Maruti Ciaz VDi',
    'Maruti Ciaz VXi',
    'Maruti Ciaz ZDi',
    'Maruti Ciaz ZXi',
    'Maruti Ciaz Zeta',
    'Maruti Dzire LXI',
    'Maruti Dzire VXI',
    'Maruti Dzire ZXI',
    'Maruti Eeco 5',
    'Maruti Eeco 7',
    'Maruti Eeco CNG',
    'Maruti Eeco Smiles',
    'Maruti Ertiga 1.5',
    'Maruti Ertiga BSIV',
    'Maruti Ertiga LDI',
    'Maruti Ertiga LXI',
    'Maruti Ertiga SHVS',
    'Maruti Ertiga VDI',
    'Maruti Ertiga VXI',
    'Maruti Ertiga ZDI',
    'Maruti Ertiga ZXI',
    'Maruti Esteem AX',
    'Maruti Esteem DI',
    'Maruti Esteem LX',
    'Maruti Esteem Lxi',
    'Maruti Esteem Vxi',
    'Maruti Estilo LXI',
    'Maruti Gypsy King',
    'Maruti Ignis 1.2',
    'Maruti Ignis 1.3',
    'Maruti Ignis Zeta',
    'Maruti Omni 5',
    'Maruti Omni 8',
    'Maruti Omni BSIII',
    'Maruti Omni CNG',
    'Maruti Omni E',
    'Maruti Omni LPG',
    'Maruti Omni Limited',
    'Maruti Omni MPI',
    'Maruti Ritz Genus',
    'Maruti Ritz LDi',
    'Maruti Ritz LXI',
    'Maruti Ritz LXi',
    'Maruti Ritz VDi',
    'Maruti Ritz VXI',
    'Maruti Ritz VXi',
    'Maruti Ritz ZDi',
    'Maruti Ritz ZXi',
    'Maruti S-Cross 2017-2020',
    'Maruti S-Presso VXI',
    'Maruti SX4 Celebration',
    'Maruti SX4 Green',
    'Maruti SX4 S',
    'Maruti SX4 VDI',
    'Maruti SX4 Vxi',
    'Maruti SX4 ZDI',
    'Maruti SX4 ZXI',
    'Maruti SX4 Zxi',
    'Maruti Swift 1.2',
    'Maruti Swift 1.3',
    'Maruti Swift AMT',
    'Maruti Swift DDiS',
    'Maruti Swift Dzire',
    'Maruti Swift Glam',
    'Maruti Swift LDI',
    'Maruti Swift LXI',
    'Maruti Swift LXi',
    'Maruti Swift Ldi',
    'Maruti Swift Lxi',
    'Maruti Swift Star',
    'Maruti Swift VDI',
    'Maruti Swift VDi',
    'Maruti Swift VVT',
    'Maruti Swift VXI',
    'Maruti Swift VXi',
    'Maruti Swift Vdi',
    'Maruti Swift ZDI',
    'Maruti Swift ZDi',
    'Maruti Swift ZXI',
    'Maruti Vitara Brezza',
    'Maruti Wagon R',
    'Maruti XL6 Alpha',
    'Maruti Zen Base',
    'Maruti Zen Classic',
    'Maruti Zen D',
    'Maruti Zen Estilo',
    'Maruti Zen LX',
    'Maruti Zen LXI',
    'Maruti Zen LXi',
    'Maruti Zen Std',
    'Maruti Zen VXI',
    'Maruti Zen VXi',
    'Mercedes-Benz B Class',
    'Mercedes-Benz CLA 200',
    'Mercedes-Benz E-Class E',
    'Mercedes-Benz E-Class E250',
    'Mercedes-Benz E-Class E270',
    'Mercedes-Benz E-Class E350',
    'Mercedes-Benz E-Class Exclusive',
    'Mercedes-Benz GL-Class 220d',
    'Mercedes-Benz GL-Class 350',
    'Mercedes-Benz GLA Class',
    'Mercedes-Benz GLC 220d',
    'Mercedes-Benz M-Class ML',
    'Mercedes-Benz New C-Class',
    'Mercedes-Benz S-Class S',
    'Mitsubishi Lancer 2.0',
    'Mitsubishi Pajero 2.8',
    'Mitsubishi Pajero Sport',
    'Nissan Kicks XL',
    'Nissan Kicks XV',
    'Nissan Micra Active',
    'Nissan Micra Diesel',
    'Nissan Micra Fashion',
    'Nissan Micra XE',
    'Nissan Micra XL',
    'Nissan Micra XV',
    'Nissan Sunny Diesel',
    'Nissan Sunny XE',
    'Nissan Sunny XL',
    'Nissan Sunny XV',
    'Nissan Teana XL',
    'Nissan Terrano XE',
    'Nissan Terrano XL',
    'Nissan Terrano XV',
    'Opel Astra 1.6',
    'Peugeot 309 GLD',
    'Renault Captur 1.5',
    'Renault Duster 110PS',
    'Renault Duster 4x4',
    'Renault Duster 85PS',
    'Renault Duster Adventure',
    'Renault Duster Petrol',
    'Renault Duster RXL',
    'Renault Duster RXZ',
    'Renault Fluence 1.5',
    'Renault Fluence 2.0',
    'Renault Fluence Diesel',
    'Renault KWID 1.0',
    'Renault KWID AMT',
    'Renault KWID Climber',
    'Renault KWID RXE',
    'Renault KWID RXL',
    'Renault KWID RXT',
    'Renault Koleos 2.0',
    'Renault Lodgy 85PS',
    'Renault Lodgy Stepway',
    'Renault Lodgy World',
    'Renault Pulse RxL',
    'Renault Pulse RxZ',
    'Renault Scala Diesel',
    'Renault Triber RXT',
    'Renault Triber RXZ',
    'Skoda Fabia 1.2',
    'Skoda Fabia 1.2L',
    'Skoda Fabia 1.4',
    'Skoda Fabia Scout',
    'Skoda Kodiaq 2.0',
    'Skoda Laura Ambiente',
    'Skoda Octavia Ambiente',
    'Skoda Octavia Ambition',
    'Skoda Octavia Classic',
    'Skoda Octavia Elegance',
    'Skoda Octavia L',
    'Skoda Octavia RS',
    'Skoda Octavia Rider',
    'Skoda Octavia Style',
    'Skoda Rapid 1.5',
    'Skoda Rapid 1.6',
    'Skoda Rapid Monte',
    'Skoda Rapid Ultima',
    'Skoda Superb 1.8',
    'Skoda Superb Elegance',
    'Skoda Superb LK',
    'Skoda Yeti Ambition',
    'Tata Aria Pleasure',
    'Tata Aria Prestige',
    'Tata Aria Pride',
    'Tata Aria Pure',
    'Tata Bolt Quadrajet',
    'Tata Bolt Revotron',
    'Tata Estate Std',
    'Tata Harrier XZ',
    'Tata Hexa XE',
    'Tata Hexa XM',
    'Tata Hexa XT',
    'Tata Hexa XTA',
    'Tata Indica DLS',
    'Tata Indica DLX',
    'Tata Indica GLS',
    'Tata Indica V2',
    'Tata Indica Vista',
    'Tata Indigo CR4',
    'Tata Indigo CS',
    'Tata Indigo GLS',
    'Tata Indigo GLX',
    'Tata Indigo Grand',
    'Tata Indigo LS',
    'Tata Indigo LX',
    'Tata Indigo TDI',
    'Tata Indigo V',
    'Tata Indigo VS',
    'Tata Indigo eCS',
    'Tata Manza Aqua',
    'Tata Manza Aura',
    'Tata Manza Club',
    'Tata Manza ELAN',
    'Tata Nano CX',
    'Tata Nano Cx',
    'Tata Nano LX',
    'Tata Nano Lx',
    'Tata Nano STD',
    'Tata Nano Twist',
    'Tata Nano XE',
    'Tata Nano XTA',
    'Tata New Safari',
    'Tata Nexon 1.2',
    'Tata Nexon 1.5',
    'Tata Safari DICOR',
    'Tata Safari Storme',
    'Tata Spacio Gold-10/6',
    'Tata Sumo CX',
    'Tata Sumo EX',
    'Tata Sumo GX',
    'Tata Sumo Gold',
    'Tata Sumo MKII',
    'Tata Sumo SE',
    'Tata Tiago 1.05',
    'Tata Tiago 1.2',
    'Tata Tiago 2019-2020',
    'Tata Tiago NRG',
    'Tata Tiago Wizz',
    'Tata Tiago XT',
    'Tata Tigor 1.05',
    'Tata Tigor 1.2',
    'Tata Tigor 2017-2020',
    'Tata Venture EX',
    'Tata Venture LX',
    'Tata Winger Deluxe',
    'Tata Xenon XT',
    'Tata Zest Quadrajet',
    'Tata Zest Revotron',
    'Toyota Camry 2.5',
    'Toyota Camry V4',
    'Toyota Camry W4',
    'Toyota Corolla AE',
    'Toyota Corolla Altis',
    'Toyota Corolla DX',
    'Toyota Corolla H2',
    'Toyota Etios 1.4',
    'Toyota Etios 1.5',
    'Toyota Etios Cross',
    'Toyota Etios Diesel',
    'Toyota Etios G',
    'Toyota Etios GD',
    'Toyota Etios Liva',
    'Toyota Etios V',
    'Toyota Etios VD',
    'Toyota Etios VX',
    'Toyota Etios VXD',
    'Toyota Fortuner 2.5',
    'Toyota Fortuner 2.8',
    'Toyota Fortuner 3.0',
    'Toyota Fortuner 4x2',
    'Toyota Fortuner 4x4',
    'Toyota Glanza G',
    'Toyota Glanza V',
    'Toyota Innova 2.5',
    'Toyota Innova Crysta',
    'Toyota Land Cruiser',
    'Toyota Platinum Etios',
    'Toyota Premio Base',
    'Toyota Qualis FS',
    'Toyota Qualis Fleet',
    'Toyota Qualis GS',
    'Toyota Yaris V',
    'Volkswagen Ameo 1.0',
    'Volkswagen Ameo 1.2',
    'Volkswagen Ameo 1.5',
    'Volkswagen CrossPolo 1.5',
    'Volkswagen GTI 1.8',
    'Volkswagen Jetta 1.6',
    'Volkswagen Jetta 2.0',
    'Volkswagen Jetta 2.0L',
    'Volkswagen Multivan TDI',
    'Volkswagen Passat 1.8',
    'Volkswagen Passat 2.0',
    'Volkswagen Passat Highline',
    'Volkswagen Polo 1.0',
    'Volkswagen Polo 1.2',
    'Volkswagen Polo 1.5',
    'Volkswagen Polo 2015-2019',
    'Volkswagen Polo Diesel',
    'Volkswagen Polo GT',
    'Volkswagen Polo Petrol',
    'Volkswagen Polo Select',
    'Volkswagen Vento 1.5',
    'Volkswagen Vento 1.6',
    'Volkswagen Vento Diesel',
    'Volkswagen Vento IPL',
    'Volkswagen Vento Konekt',
    'Volkswagen Vento Petrol',
    'Volvo S60 D4',
    'Volvo S90 D4',
    'Volvo V40 Cross',
    'Volvo V40 D3',
    'Volvo XC40 D4',
    'Volvo XC60 Inscription',
    'Volvo XC90 T8'
]

car_name = st.selectbox('Car Model', car_names)
for i in range(0, 696):
    if(car_name == car_names[i]):
        array[i] = 1
car_name_encoded = array         

engine = st.number_input('Engine Size (cc)', value=1500)
mileage = st.number_input('Mileage (km/ltr/kg)', value=18)
km_driven = st.number_input('Kilometers Driven', value=50000)
year = st.number_input('Year of Manufacture', value=2018)
max_power = st.number_input('Max Power (bhp)', value=120)

owner_type = st.selectbox('Owner Type', ['First Owned', 'Second Owned', 'Third Owned', 'Fouth Owned','Test-Drive-Car'])
owner_encoded = [1 if owner_type == 'First Owned' else 0,
                 1 if owner_type == 'Fourth Owned' else 0,
                 1 if owner_type == 'Second Owned' else 0,
                 1 if owner_type == 'Test-Drive-Car' else 0,
                 1 if owner_type == 'Third Owned' else 0]

fuel_type = st.selectbox('Fuel Type', ['Petrol', 'Diesel', 'CNG','LPG'])
fuel_encoded = [1 if fuel_type == 'CNG' else 0,
                1 if fuel_type == 'Diesel' else 0,
                1 if fuel_type == 'LPG' else 0,
                1 if fuel_type == 'Petrol' else 0]

transmission_type = st.selectbox('Transmission Type', ['Manual', 'Automatic'])
transmission_encoded = [1 if transmission_type == 'Automatic' else 0,
                        1 if transmission_type == 'Manual' else 0]

seller_type = st.selectbox('Seller Type', ['Dealer', 'Individual','TrustMark Dealer'])
seller_type_encoded = [1 if seller_type == 'Dealer' else 0,
                       1 if seller_type == 'Individual' else 0,
                       1 if seller_type == 'TrustMark Dealer' else 0]

input_features = np.array([[engine, mileage, km_driven, year, max_power] + 
                           car_name_encoded + owner_encoded + fuel_encoded + 
                           transmission_encoded + seller_type_encoded])

if st.button('Predict Selling Price'):
    prediction = model.predict(input_features)
    
    # Display the predicted price with larger font size (30px)
    st.markdown(
        f"""
        <div style="font-size:30px; font-weight:bold;">
            Predicted Selling Price: ₹{prediction[0]:,.2f}
        </div>
        """,
        unsafe_allow_html=True
    )
