import sqlite3

# SQLite connection
connection = sqlite3.connect('Warframe.db')
cursor = connection.cursor()

# This is the gun dictionary.  It holds all of the different primaries in the game and their useful values
# All Discharge weapons have a damage in terms of damage per second and have a proc chance in terms of percent chance per second.
# The dictionary has the form....
# weapon type, damage vector, accuracy, fire rate, crit chance, crit damage multipler, status chance, ammo capacity, reload time
# followed by 8 values corresponding to possible polarities
# Damage vectors will take the form
# Impact Puncture Slash Cold Electricity Heat Toxin Blast Corrosive Gas Magnetic Radiation Viral

'''
A module containing dictionaries with all of the weapon/mod values.


Things to test:
 * Does serration effect elemental-only weapons
'''

PRIMARY_DICT={
"Amprex": ["Discharge",'Rifle',0,0,0,0,7.5,0,0,0,0,0,0,0,0,12.5,20,0.50,2.0,0.20,100,2.7,None,None,None,None,None,None,None,None]
,"Attica": ["Projectile",'Bow',6.25,93.75,25,0,0,0,0,0,0,0,0,0,0,40.0,3.33,0.20,1.5,0.10,16,2.8,'Madurai',None,None,None,None,None,None,None]
,"Boar": ["Hitscan",'Shotgun',96.8,26.4,52.8,0,0,0,0,0,0,0,0,0,0,5.0,4.17,0.10,1.5,0.20,20,2.7,None,None,None,None,None,None,None,None]
,"Boar Prime": ["Hitscan",'Shotgun',119.6,27.6,36.8,0,0,0,0,0,0,0,0,0,0,5.0,4.67,0.15,2.0,0.30,20,2.8,None,None,None,None,None,None,None,None]
,"Boltor": ["Projectile",'Rifle',2.5,20,2.5,0,0,0,0,0,0,0,0,0,0,25.0,8.75,0.05,1.5,0.10,60,2.6,'Vazarin',None,None,None,None,None,None,None]
,"Boltor Prime": ["Projectile",'Rifle',5.5,49.5,0,0,0,0,0,0,0,0,0,0,0,50.0,10,0.05,2.0,0.10,60,2.4,'Vazarin','Madurai',None,None,None,None,None,None]
,"Boltor Telos": ["Projectile",'Rifle',5,45,0,0,0,0,0,0,0,0,0,0,0,25.0,9.33,0.05,2.0,0.075,90,2.4,'Vazarin','Madurai',None,None,None,None,None,None]
,"Braton": ["Hitscan",'Rifle',6.6,6.6,6.8,0,0,0,0,0,0,0,0,0,0,28.6,8.75,0.10,1.5,0.05,45,2.0,None,None,None,None,None,None,None,None]
,"Braton MK1": ["Hitscan",'Rifle',4.5,4.5,9.0,0,0,0,0,0,0,0,0,0,0,40.0,7.5,0.8,1.5,0.05,60,2.0,None,None,None,None,None,None,None,None]
,"Braton Prime": ["Hitscan",'Rifle',1.75,12.25,21.0,0,0,0,0,0,0,0,0,0,0,28.6,9.58,0.10,2.0,0.20,75,2.2,None,None,None,None,None,None,None,None]
,"Braton Vandal": ["Hitscan",'Rifle',12.25,1.75,21.0,0,0,0,0,0,0,0,0,0,0,33.3,7.5,0.10,2.0,0.10,50,1.8,'Madurai',None,None,None,None,None,None,None]
,"Burston": ["Hitscan",'Rifle',10.0,10.0,10.0,0,0,0,0,0,0,0,0,0,0,25.0,7.83,0.05,1.5,0.10,45,2.0,'Madurai',None,None,None,None,None,None,None]
,"Burston Prime": ["Hitscan",'Rifle',11.7,11.7,15.6,0,0,0,0,0,0,0,0,0,0,25.0,13.64,0.05,1.5,0.15,45,2.0,'Madurai',None,None,None,None,None,None,None]
,"Buzlok": ["Projectile",'Rifle',33.8,4.5,6.7,0,0,0,0,0,0,0,0,0,0,13.3,6.25,0.10,2.0,0.10,75,3.0,None,None,None,None,None,None,None,None]
,"Cernos": ["Projectile",'Bow',180.0,10.0,10.0,0,0,0,0,0,0,0,0,0,0,16.7,1,0.35,2.0,0.10,1,0.6,'Madurai',None,None,None,None,None,None,None]
,"Cernos Mutalist": ["Projectile",'Bow',202.5,11.25,11.25,0,0,0,0,0,0,0,0,0,0,16.7,1,0.15,2.0,0.45,1,0.6,'Naramon',None,None,None,None,None,None,None]
,"Cernos Prime": ["Projectile",'Bow',324.0,18.0,18.0,0,0,0,0,0,0,0,0,0,0,16.7,1,0.35,2.0,0.10,1,1.0,'Madurai','Madurai',None,None,None,None,None,None]
,"Cernos Rakta": ["Projectile",'Bow',225,12.5,12.5,0,0,0,0,0,0,0,0,0,0,16.7,1,0.35,2.0,0.15,1,0.6,'Madurai','Madurai','Naramon',None,None,None,None,None]
,"Convectrix": ["Discharge",'Rifle',10.0,10.0,80.0,0,0,0,0,0,0,0,0,0,0,50.0,3,0.10,2.0,0.25,90,2.0,None,None,None,None,None,None,None,None]
,"Daikyu": ["Projectile",'Bow',70.0,210.0,70.0,0,0,0,0,0,0,0,0,0,0,16.7,1,0.15,2.0,0.45,1,0.6,'Madurai',None,None,None,None,None,None,None]
,"Dera": ["Projectile",'Rifle',4.4,16.5,1.1,0,0,0,0,0,0,0,0,0,0,100,11.25,0.025,1.5,0.10,45,2.4,None,None,None,None,None,None,None,None]
,"Dera Vandal": ["Projectile",'Rifle',6.2,23.25,1.55,0,0,0,0,0,0,0,0,0,0,100,11.3,0.05,2.0,0.15,60,2.4,None,None,None,None,None,None,None,None]
,"Drakgoon": ["Projectile",'Shotgun',90.0,90.0,720.0,0,0,0,0,0,0,0,0,0,0,1.4,3.33,0.075,2.0,0.10,7,2.3,None,None,None,None,None,None,None,None]
,"Dread": ["Projectile",'Bow',10.0,10.0,180.0,0,0,0,0,0,0,0,0,0,0,16.7,1,0.50,2.0,0.20,1,0.7,'Madurai','Madurai',None,None,None,None,None,None]
,"Flux Rifle": ["Discharge",'Rifle',22.5,2.25,2.25,0,0,0,0,0,0,0,0,0,0,100,10,0.05,2.0,0.25,200,2.0,None,None,None,None,None,None,None,None]
,"Glaxion": ["Discharge",'Rifle',0,0,0,12.5,0,0,0,0,0,0,0,0,0,12.5,20,0.05,2.0,0.35,300,1.5,None,None,None,None,None,None,None,None]
,"Gorgon": ["Hitscan",'Rifle',18.75,3.75,2.5,0,0,0,0,0,0,0,0,0,0,8.3,12.5,0.10,1.5,0.05,90,4.2,None,None,None,None,None,None,None,None]
,"Gorgon Prisma": ["Hitscan",'Rifle',18.75,3.75,2.5,0,0,0,0,0,0,0,0,0,0,14.3,14.2,0.15,2.0,0.05,120,3.0,None,None,None,None,None,None,None,None]
,"Gorgon Wraith": ["Hitscan",'Rifle',23.0,2.7,1.3,0,0,0,0,0,0,0,0,0,0,10.05,13.3,0.10,1.5,0.15,90,3.0,None,None,None,None,None,None,None,None]
,"Grakata": ["Hitscan",'Rifle',4.4,3.7,2.9,0,0,0,0,0,0,0,0,0,0,28.6,20,0.25,2.0,0.20,60,2.4,None,None,None,None,None,None,None,None]
,"Grakata Prisma": ["Hitscan",'Rifle',4.4,3.7,2.9,0,0,0,0,0,0,0,0,0,0,28.6,21.67,0.25,2.5,0.20,120,2.0,None,None,None,None,None,None,None,None]
,"Grinlok": ["Hitscan",'Rifle',60.0,12.0,48.0,0,0,0,0,0,0,0,0,0,0,28.6,1.67,0.15,2.0,0.35,6,2.1,'Madurai',None,None,None,None,None,None,None]
,"Harpak": ["Projectile",'Rifle',5.0,37.5,7.5,0,0,0,0,0,0,0,0,0,0,18.2,6,0.15,2.0,0.10,45,2.0,'Madurai',None,None,None,None,None,None,None]
,"Hek": ["Hitscan",'Shotgun',78.75,341.25,105.0,0,0,0,0,0,0,0,0,0,0,9.1,2.17,0.10,2.0,0.25,4,2.0,'Vazarin','Madurai',None,None,None,None,None,None]
,"Hek Vaykor": ["Hitscan",'Shotgun',78.75,341.25,105.0,0,0,0,0,0,0,0,0,0,0,9.1,3,0.25,2.0,0.25,8,2.3,None,None,None,None,None,None,None,None]
,"Hema": ["Discharge",'Rifle',0,0,0,0,0,0,0,0,0,0,0,0,45,20,6.0,0.075,2,0.25,60,2,None,None,None,None,None,None,None,None]
,"Hind": ["Hitscan",'Rifle',7.5,7.5,15.0,0,0,0,0,0,0,0,0,0,0,33.3,6.25,0.05,1.5,0.10,65,2.0,'Madurai',None,None,None,None,None,None,None]
,"Ignis": ["Discharge",'Rifle',0,0,0,0,0,27,0,0,0,0,0,0,0,100,10,0.05,2.0,25,150,2,None,None,None,None,None,None,None,None]
,"Ignis Wraith": ["Discharge",'Rifle',0,0,0,0,0,25,0,0,0,0,0,0,0,100,10,0.12,2.0,30,200,20,None,None,None,None,None,None,None,None]
,"Karak": ["Hitscan",'Rifle',12.1,8.1,6.8,0,0,0,0,0,0,0,0,0,0,28.6,11.67,0.025,1.5,0.075,30,2.0,'Madurai',None,None,None,None,None,None,None]
,"Karak Wraith": ["Hitscan",'Rifle',13.5,9.0,7.5,0,0,0,0,0,0,0,0,0,0,28.6,11.7,0.05,2.0,0.15,60,2.0,'Madurai',None,None,None,None,None,None,None]
,"Kohm": ["Hitscan",'Shotgun',6.0,6.0,18.0,0,0,0,0,0,0,0,0,0,0,3.6,3.67,0.10,2.0,0.25,245,2.0,'Vazarin',None,None,None,None,None,None,None]
,"Lanka": ["Projectile",'Rifle',0,0,0,0,525,0,0,0,0,0,0,0,0,100,1,0.25,2.0,0.25,10,2,None,None,None,None,None,None,None,None]
,"Latron": ["Hitscan",'Rifle',8.3,38.5,8.2,0,0,0,0,0,0,0,0,0,0,28.6,4.17,0.10,2.0,0.10,15,2.4,'Madurai',None,None,None,None,None,None,None]
,"Latron Prime": ["Hitscan",'Rifle',8.5,68.0,8.5,0,0,0,0,0,0,0,0,0,0,28.6,4.17,0.15,2.5,0.25,15,2.4,'Madurai','Naramon',None,None,None,None,None,None]
,"Latron Wraith": ["Hitscan",'Rifle',13.75,38.5,2.75,0,0,0,0,0,0,0,0,0,0,28.6,5.4,0.25,2.5,0.20,15,2.4,'Madurai',None,None,None,None,None,None,None]
,"Miter": ["Projectile",'Rifle',12.5,12.5,225.0,0,0,0,0,0,0,0,0,0,0,100,2.5,0,0,0.5,20,2.0,'Naramon',None,None,None,None,None,None,None]
,"Opticor": ["Hitscan",'Rifle',100.0,850.0,50.0,0,0,0,0,0,0,0,0,0,0,100,1,0.15,2.0,0.15,5,2.0,'Vazarin',None,None,None,None,None,None,None]
,"Panthera": ["Projectile",'Rifle',20.0,10.0,70.0,0,0,0,0,0,0,0,0,0,0,100,1.67,0,0,0.10,60,2.0,'Naramon',None,None,None,None,None,None,None]
,"Paracyst": ["Projectile",'Rifle',0,0,0,0,0,0,25,0,0,0,0,0,0,25.0,11.11,0.05,2.0,0.15,60,2,None,None,None,None,None,None,None,None]
,"Paris": ["Projectile",'Bow',9.0,144.0,27.0,0,0,0,0,0,0,0,0,0,0,16.7,1,0.30,2.0,0.10,1,0.7,'Naramon',None,None,None,None,None,None,None]
,"Paris MK1": ["Projectile",'Bow',6.0,96.0,18.0,0,0,0,0,0,0,0,0,0,0,16.7,1,0.30,2.0,0.15,1,0.6,'Naramon',None,None,None,None,None,None,None]
,"Paris Prime": ["Projectile",'Bow',5.0,160.0,35.0,0,0,0,0,0,0,0,0,0,0,16.7,1,0.45,2.0,0.20,1,0.7,'Naramon','Madurai',None,None,None,None,None,None]
,"Phage": ["Discharge",'Shotgun',0,0,0,0,0,0,0,0,0,0,0,0,330,50,1,0.1,2.0,15,40,2,'Naramon',None,None,None,None,None,None,None]
,"Quanta": ["Discharge",'Rifle',0,0,0,0,220,0,0,0,0,0,0,0,0,100,1,0.1,2,0.10,60,2,'Vazarin',None,None,None,None,None,None,None]
,"Quanta Mutalist": ["Projectile",'Rifle',2.5,15.0,7.5,0,0,0,0,0,0,0,0,0,0,100,10,0.025,1.5,0.15,60,3.0,'Vazarin',None,None,None,None,None,None,None]
,"Quanta Vandal": ["Discharge",'Rifle',0,0,0,0,220,0,0,0,0,0,0,0,0,100,1,0.10,2.0,0.25,90,2,'Madurai',None,None,None,None,None,None,None]
,"Rubico": ["Hitscan",'Rifle',160.0,30.0,10.0,0,0,0,0,0,0,0,0,0,0,13.3,1.5,0.25,3.0,0.05,5,3.0,None,None,None,None,None,None,None,None]
,"Simulor": ["Projectile",'Rifle',0,0,0,0,0,0,0,0,0,0,50,0,0,100,2,0.1,2.0,0.30,10,3,'Vazarin','Naramon',None,None,None,None,None,None]
,"Simulor Synoid": ["Projectile",'Rifle',0,0,0,0,0,0,0,0,0,0,50,0,0,100,2.67,0.1,2,0.35,15,2,'Vazarin','Naramon','Naramon',None,None,None,None,None]
,"Snipetron": ["Hitscan",'Rifle',17.5,140.0,17.5,0,0,0,0,0,0,0,0,0,0,13.3,1.5,0.20,1.5,0.10,4,3.5,'Madurai',None,None,None,None,None,None,None]
,"Snipetron Vandal": ["Hitscan",'Rifle',10.0,180.0,10.0,0,0,0,0,0,0,0,0,0,0,13.3,1.5,0.25,2.0,0.15,6,2.0,'Madurai',None,None,None,None,None,None,None]
,"Sobek": ["Hitscan",'Shotgun',262.5,43.75,43.75,0,0,0,0,0,0,0,0,0,0,9.1,2.5,0.10,2.0,0.15,20,4.0,None,None,None,None,None,None,None,None]
,"Soma": ["Hitscan",'Rifle',1.2,4.8,6.0,0,0,0,0,0,0,0,0,0,0,28.6,15,0.30,3.0,0.07,100,3.0,'Madurai','Madurai',None,None,None,None,None,None]
,"Soma Prime": ["Hitscan",'Rifle',1.2,4.8,6.0,0,0,0,0,0,0,0,0,0,0,28.6,15,0.30,3.0,0.10,200,3.0,'Madurai','Madurai',None,None,None,None,None,None]
,"Stradavar (Auto)": ["Hitscan",'Rifle',8.75,8.75,7.5,0,0,0,0,0,0,0,0,0,0,28.6,10,0.10,2.0,0.05,65,2.0,'Madurai','Madurai',None,None,None,None,None,None]
,"Stradavar (Semi-Auto)": ["Hitscan",'Rifle',7.5,30.0,12.5,0,0,0,0,0,0,0,0,0,0,28.6,5,0.20,2.0,0.15,65,2.0,'Madurai','Madurai',None,None,None,None,None,None]
,"Strun": ["Hitscan",'Shotgun',165.0,45.0,90.0,0,0,0,0,0,0,0,0,0,0,4.0,2.5,0.075,1.5,0.20,6,3.8,'Naramon',None,None,None,None,None,None,None]
,"Strun MK1": ["Hitscan",'Shotgun',99.0,27.0,54.0,0,0,0,0,0,0,0,0,0,0,4.0,2.08,0.075,2.0,0.20,6,3.8,'Naramon',None,None,None,None,None,None,None]
,"Strun Wraith": ["Hitscan",'Shotgun',195.0,45.0,60.0,0,0,0,0,0,0,0,0,0,0,6.7,2.5,0.15,2.0,0.40,10,5.0,'Naramon',None,None,None,None,None,None,None]
,"Supra": ["Projectile",'Rifle',4.5,33.8,6.7,0,0,0,0,0,0,0,0,0,0,8.3,12.5,0.025,1.5,0.05,180,3.0,None,None,None,None,None,None,None,None]
,"Sybaris": ["Hitscan",'Rifle',23.1,23.1,23.8,0,0,0,0,0,0,0,0,0,0,28.6,3.98,0.25,2.0,0.10,10,2.0,None,None,None,None,None,None,None,None]
,"Sybaris Dex": ["Hitscan",'Rifle',22.5,18.75,33.75,0,0,0,0,0,0,0,0,0,0,28.6,4.17,0.35,2.0,0.10,14,1.5,None,None,None,None,None,None,None,None]
,"Synapse": ["Discharge",'Rifle',0,0,0,0,12.5,0,0,0,0,0,0,0,0,12.5,10,0.50,2.0,0.10,100,1.5,None,None,None,None,None,None,None,None]
,"Tetra": ["Projectile",'Rifle',6.0,24.0,0,0,0,0,0,0,0,0,0,0,0,18.2,6.67,0.025,1.5,0.10,60,2.0,None,None,None,None,None,None,None,None]
,"Tetra Prisma": ["Projectile",'Rifle',7.0,28.0,0,0,0,0,0,0,0,0,0,0,0,18.2,7.08,0.10,2.0,0.15,60,2.0,None,None,None,None,None,None,None,None]
,"Tiberon": ["Hitscan",'Rifle',15.0,30.0,15.0,0,0,0,0,0,0,0,0,0,0,33.3,9.09,0.05,2.0,0.025,30,2.3,None,None,None,None,None,None,None,None]
,"Tigris": ["Hitscan",'Shotgun',105.0,105.0,840.0,0,0,0,0,0,0,0,0,0,0,9.1,2,0.05,2.0,0.25,2,1.8,None,None,None,None,None,None,None,None]
,"Tigris Prime": ["Hitscan",'Shotgun',156.0,156.0,1248.0,0,0,0,0,0,0,0,0,0,0,9.1,2,0.10,2.0,0.30,2,1.8,'Madurai','Naramon',None,None,None,None,None,None]
,"Tigris Sancti": ["Hitscan",'Shotgun',126.0,126.0,1008.0,0,0,0,0,0,0,0,0,0,0,6.5,2,0.15,1.5,0.25,2,1.5,'Vazarin','Naramon','Madurai',None,None,None,None,None]
,"Vectis": ["Hitscan",'Rifle',90.0,78.8,56.3,0,0,0,0,0,0,0,0,0,0,13.3,1.5,0.25,2.0,0.30,1,0.9,'Madurai',None,None,None,None,None,None,None]
,"Vectis Prime": ["Hitscan",'Rifle',130.0,146.3,48.7,0,0,0,0,0,0,0,0,0,0,13.3,1.5,0.25,2.0,0.30,2,0.9,'Madurai','Naramon',None,None,None,None,None,None]
,"Vulkar": ["Hitscan",'Rifle',180.0,33.8,11.2,0,0,0,0,0,0,0,0,0,0,13.3,1.5,0.20,2.0,0.25,6,3.0,None,None,None,None,None,None,None,None]
,"Vulkar Wraith": ["Hitscan",'Rifle',225.0,25.0,0,0,0,0,0,0,0,0,0,0,0,13.3,1.5,0.20,2.0,0.25,8,3.0,'Madurai',None,None,None,None,None,None,None]
,"Zhuge": ["Projectile",'Bow',5.0,75.0,20.0,0,0,0,0,0,0,0,0,0,0,40.0,4.17,0.20,2.0,0.35,20,2.5,'Madurai',None,None,None,None,None,None,None]}

PRIMARY_MOD_DICT = {'Serration':['Rifle', [1],  14, 'Madurai', 'True', 'pass', 1.65, 1.65, 1.65, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0, 0, 0],
                'Heavy Caliber': ['Rifle', [1,0],  16, 'Madurai', 'True', 'pass', 1.65, 1.65, 1.65, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-0.55, 0, 0, 0, 0, 0, 0],
                'Bane of Grineer': ['Rifle', [7], 9, 'Madurai', 'isinstance(characteristic, enemies.Grineer)', 'pass', 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0, 0, 0, 0, 0, 0, 0],
                'Bane of Corpus': ['Rifle', [7], 9, 'Madurai', 'isinstance(characteristic, enemies.Corpus)', 'pass', 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0, 0, 0, 0, 0, 0, 0],
                'Hellfire': ['Rifle', [2], 11, 'Naramon', 'True', 'pass', 0, 0, 0, 0, 0, 0.9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                'Infected Clip': ['Rifle', [2], 11, 'Naramon', 'True', 'pass', 0, 0, 0, 0.9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                'Vital Sense': ['Rifle', [0], 9, 'Madurai', 'True', 'pass', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1.2, 0, 0, 0]} 

# Table Creator
# Primary Weapons
cursor.execute('''DROP TABLE IF EXISTS primary_weapons''')
cursor.execute("CREATE TABLE IF NOT EXISTS primary_weapons (weapon_name TEXT, weapon_type TEXT, mod_type TEXT, impact REAL, puncture REAL, slash REAL, cold REAL, electricity REAL, heat REAL, toxin REAL, blast REAL, corrosive REAL, gas REAL, magnetic REAL, radiation REAL, viral REAL, accuracy REAL, fire_rate REAL, critical_chance REAL, critical_multipler REAL, status_chance REAL, ammo_capacity REAL, reload_time REAL, mod_polarity_1 TEXT, mod_polarity_2 TEXT, mod_polarity_3 TEXT, mod_polarity_4 TEXT, mod_polarity_5 TEXT, mod_polarity_6 TEXT, mod_polarity_7 TEXT, mod_polarity_8 TEXT)")

# Primary_Mods
#cursor.execute('''DROP TABLE IF EXISTS primary_mods''')
#cursor.execute('''DROP TABLE IF EXISTS PrimaryModPriorities''')
#cursor.execute("CREATE TABLE IF NOT EXISTS primary_mods (mod_name TEXT, mod_type TEXT, mod_cost REAL, mod_polarity TEXT, if_condition TEXT, else_condition TEXT, impact_bonus REAL, puncture_bonus REAL, slash_bonus REAL, cold_bonus REAL, electricity_bonus REAL, heat_bonus REAL, toxin_bonus REAL, blast_bonus REAL, corrosive_bonus REAL, gas_bonus REAL, magnetic_bonus REAL, radiation_bonus REAL, viral_bonus REAL, accuracy REAL, fire_rate REAL, critical_chance REAL, critical_multipler REAL, status_chance REAL, ammo_capacity REAL, reload_time REAL)")
#cursor.execute("CREATE TABLE IF NOT EXISTS PrimaryModPriorities (mod_name TEXT, mod_priority REAL)")

# Data Entry Function
def data_entry(table, dictionary):
    for key in dictionary.keys():
        if hasattr(dictionary[key], '__iter__'):
            num_entries = len(dictionary[key])
            entry_list = [key] + dictionary[key]
        else:
            num_entries = 1
            entry_list = [key, dictionary[key]]

        cursor.execute('INSERT INTO ' + table + ' VALUES (' + '?,' * num_entries + '?)', entry_list)

# Data Entry Loop
data_entry('primary_weapons', PRIMARY_DICT)




connection.commit()
connection.close()



