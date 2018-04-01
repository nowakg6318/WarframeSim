''' A module containing dictionaries with all of the weapon/mod values.
'''
# This is the gun dictionary.  It holds all of the different primaries in the game and their useful values
# All Discharge weapons have a damage in terms of damage per second and have a proc chance in terms of percent chance per second.
# The dictionary has the form....
# weapon type, damage vector, accuracy, fire rate, crit chance, crit damage multipler, status chance, ammo capacity, reload time
# followed by 8 values corresponding to possible polarities
# Damage vectors will take the form
# Impact Puncture Slash Cold Electricity Heat Toxin Blast Corrosive Gas Magnetic Radiation Viral

PRIMARY_DICT={
"Amprex": ["Discharge",'Rifle',0,0,0,0,7.5,0,0,0,0,0,0,0,0,12.5,20,0.50,2.0,0.20,100,2.7,1,0,None,None,None,None,None,None,None,None]
,"Attica": ["Projectile",'Bow',6.25,93.75,25,0,0,0,0,0,0,0,0,0,0,40.0,3.33,0.20,1.5,0.10,16,2.8,1,0,'Madurai',None,None,None,None,None,None,None]
,"Boar": ["Hitscan",'Shotgun',12.1,3.3,6.6,0,0,0,0,0,0,0,0,0,0,5.0,4.17,0.10,1.5,0.20,20,2.7,8,0,None,None,None,None,None,None,None,None]
,"Boar Prime": ["Hitscan",'Shotgun',26,6,8,0,0,0,0,0,0,0,0,0,0,5.0,4.67,0.15,2.0,0.30,20,2.8,8,0,None,None,None,None,None,None,None,None]
,"Boltor": ["Projectile",'Rifle',2.5,20,2.5,0,0,0,0,0,0,0,0,0,0,25.0,8.75,0.05,1.5,0.10,60,2.6,1,0,'Vazarin',None,None,None,None,None,None,None]
,"Boltor Prime": ["Projectile",'Rifle',5.5,49.5,0,0,0,0,0,0,0,0,0,0,0,50.0,10,0.05,2.0,0.10,60,2.4,1,0,'Vazarin','Madurai',None,None,None,None,None,None]
,"Boltor Telos": ["Projectile",'Rifle',5,45,0,0,0,0,0,0,0,0,0,0,0,25.0,9.33,0.05,2.0,0.075,90,2.4,1,0,'Vazarin','Madurai',None,None,None,None,None,None]
,"Braton": ["Hitscan",'Rifle',6.6,6.6,6.8,0,0,0,0,0,0,0,0,0,0,28.6,8.75,0.10,1.5,0.05,45,2.0,1,0,None,None,None,None,None,None,None,None]
,"Braton MK1": ["Hitscan",'Rifle',4.5,4.5,9.0,0,0,0,0,0,0,0,0,0,0,40.0,7.5,0.8,1.5,0.05,60,2.0,1,0,None,None,None,None,None,None,None,None]
,"Braton Prime": ["Hitscan",'Rifle',1.75,12.25,21.0,0,0,0,0,0,0,0,0,0,0,28.6,9.58,0.10,2.0,0.20,75,2.2,1,0,None,None,None,None,None,None,None,None]
,"Braton Vandal": ["Hitscan",'Rifle',12.25,1.75,21.0,0,0,0,0,0,0,0,0,0,0,33.3,7.5,0.10,2.0,0.10,50,1.8,1,0,'Madurai',None,None,None,None,None,None,None]
,"Burston": ["Hitscan",'Rifle',10.0,10.0,10.0,0,0,0,0,0,0,0,0,0,0,25.0,7.83,0.05,1.5,0.10,45,2.0,1,0,'Madurai',None,None,None,None,None,None,None]
,"Burston Prime": ["Hitscan",'Rifle',11.7,11.7,15.6,0,0,0,0,0,0,0,0,0,0,25.0,13.64,0.05,1.5,0.15,45,2.0,1,0,'Madurai',None,None,None,None,None,None,None]
,"Buzlok": ["Projectile",'Rifle',33.8,4.5,6.7,0,0,0,0,0,0,0,0,0,0,13.3,6.25,0.10,2.0,0.10,75,3.0,1,0,None,None,None,None,None,None,None,None]
,"Cernos": ["Projectile",'Bow',180.0,10.0,10.0,0,0,0,0,0,0,0,0,0,0,16.7,1,0.35,2.0,0.10,1,0.6,1,0,'Madurai',None,None,None,None,None,None,None]
,"Cernos Mutalist": ["Projectile",'Bow',202.5,11.25,11.25,0,0,0,0,0,0,0,0,0,0,16.7,1,0.15,2.0,0.45,1,0.6,1,0,'Naramon',None,None,None,None,None,None,None]
,"Cernos Prime": ["Projectile",'Bow',324.0,18.0,18.0,0,0,0,0,0,0,0,0,0,0,16.7,1,0.35,2.0,0.10,1,1.0,3,0,'Madurai','Madurai',None,None,None,None,None,None]
,"Cernos Rakta": ["Projectile",'Bow',225,12.5,12.5,0,0,0,0,0,0,0,0,0,0,16.7,1,0.35,2.0,0.15,1,0.6,1,0,'Madurai','Madurai','Naramon',None,None,None,None,None]
,"Convectrix": ["Discharge",'Rifle',1.2,1.2,9.6,0,0,0,0,0,0,0,0,0,0,50.0,3,0.10,2.0,0.25,90,2.0,2,0,None,None,None,None,None,None,None,None]
,"Daikyu": ["Projectile",'Bow',70.0,210.0,70.0,0,0,0,0,0,0,0,0,0,0,16.7,1,0.15,2.0,0.45,1,0.6,1,0,'Madurai',None,None,None,None,None,None,None]
,"Dera": ["Projectile",'Rifle',4.4,16.5,1.1,0,0,0,0,0,0,0,0,0,0,100,11.25,0.025,1.5,0.10,45,2.4,1,0,None,None,None,None,None,None,None,None]
,"Dera Vandal": ["Projectile",'Rifle',6.2,23.25,1.55,0,0,0,0,0,0,0,0,0,0,100,11.3,0.05,2.0,0.15,60,2.4,1,0,None,None,None,None,None,None,None,None]
,"Drakgoon": ["Projectile",'Shotgun',7,7,56,0,0,0,0,0,0,0,0,0,0,1.4,3.33,0.075,2.0,0.10,7,2.3,10,0,None,None,None,None,None,None,None,None]
,"Dread": ["Projectile",'Bow',10.0,10.0,180.0,0,0,0,0,0,0,0,0,0,0,16.7,1,0.50,2.0,0.20,1,0.7,1,0,'Madurai','Madurai',None,None,None,None,None,None]
,"Flux Rifle": ["Discharge",'Rifle',22.5,2.25,2.25,0,0,0,0,0,0,0,0,0,0,100,10,0.05,2.0,0.25,200,2.0,1,0,None,None,None,None,None,None,None,None]
,"Glaxion": ["Discharge",'Rifle',0,0,0,12.5,0,0,0,0,0,0,0,0,0,12.5,20,0.05,2.0,0.35,300,1.5,1,0,None,None,None,None,None,None,None,None]
,"Gorgon": ["Hitscan",'Rifle',18.75,3.75,2.5,0,0,0,0,0,0,0,0,0,0,8.3,12.5,0.10,1.5,0.05,90,4.2,1,0,None,None,None,None,None,None,None,None]
,"Gorgon Prisma": ["Hitscan",'Rifle',18.75,3.75,2.5,0,0,0,0,0,0,0,0,0,0,14.3,14.2,0.15,2.0,0.05,120,3.0,1,0,None,None,None,None,None,None,None,None]
,"Gorgon Wraith": ["Hitscan",'Rifle',23.0,2.7,1.3,0,0,0,0,0,0,0,0,0,0,10.05,13.3,0.10,1.5,0.15,90,3.0,1,0,None,None,None,None,None,None,None,None]
,"Grakata": ["Hitscan",'Rifle',4.4,3.7,2.9,0,0,0,0,0,0,0,0,0,0,28.6,20,0.25,2.0,0.20,60,2.4,1,0,None,None,None,None,None,None,None,None]
,"Grakata Prisma": ["Hitscan",'Rifle',4.4,3.7,2.9,0,0,0,0,0,0,0,0,0,0,28.6,21.67,0.25,2.5,0.20,120,2.0,1,0,None,None,None,None,None,None,None,None]
,"Grinlok": ["Hitscan",'Rifle',60.0,12.0,48.0,0,0,0,0,0,0,0,0,0,0,28.6,1.67,0.15,2.0,0.35,6,2.1,1,0,'Madurai',None,None,None,None,None,None,None]
,"Harpak": ["Projectile",'Rifle',5.0,37.5,7.5,0,0,0,0,0,0,0,0,0,0,18.2,6,0.15,2.0,0.10,45,2.0,1,0,'Madurai',None,None,None,None,None,None,None]
,"Hek": ["Hitscan",'Shotgun',11.25,48.75,15,0,0,0,0,0,0,0,0,0,0,9.1,2.17,0.10,2.0,0.25,4,2.0,7,0,'Vazarin','Madurai',None,None,None,None,None,None]
,"Hek Vaykor": ["Hitscan",'Shotgun',11.25,48.75,15,0,0,0,0,0,0,0,0,0,0,9.1,3,0.25,2.0,0.25,8,2.3,7,0,None,None,None,None,None,None,None,None]
,"Hema": ["Discharge",'Rifle',0,0,0,0,0,0,0,0,0,0,0,0,45,20,6.0,0.075,2,0.25,60,2,1,0,None,None,None,None,None,None,None,None]
,"Hind": ["Hitscan",'Rifle',7.5,7.5,15.0,0,0,0,0,0,0,0,0,0,0,33.3,6.25,0.05,1.5,0.10,65,2.0,1,0,'Madurai',None,None,None,None,None,None,None]
,"Ignis": ["Discharge",'Rifle',0,0,0,0,0,27,0,0,0,0,0,0,0,100,10,0.05,2.0,25,150,2,1,0,None,None,None,None,None,None,None,None]
,"Ignis Wraith": ["Discharge",'Rifle',0,0,0,0,0,25,0,0,0,0,0,0,0,100,10,0.12,2.0,30,200,20,1,0,None,None,None,None,None,None,None,None]
,"Karak": ["Hitscan",'Rifle',12.1,8.1,6.8,0,0,0,0,0,0,0,0,0,0,28.6,11.67,0.025,1.5,0.075,30,2.0,1,0,'Madurai',None,None,None,None,None,None,None]
,"Karak Wraith": ["Hitscan",'Rifle',13.5,9.0,7.5,0,0,0,0,0,0,0,0,0,0,28.6,11.7,0.05,2.0,0.15,60,2.0,1,0,'Madurai',None,None,None,None,None,None,None]
,"Kohm": ["Hitscan",'Shotgun',6.0,6.0,18.0,0,0,0,0,0,0,0,0,0,0,3.6,3.67,0.10,2.0,0.25,245,2.0,12,0,'Vazarin',None,None,None,None,None,None,None]
,"Lanka": ["Projectile",'Rifle',0,0,0,0,525,0,0,0,0,0,0,0,0,100,1,0.25,2.0,0.25,10,2,1,0,None,None,None,None,None,None,None,None]
,"Latron": ["Hitscan",'Rifle',8.3,38.5,8.2,0,0,0,0,0,0,0,0,0,0,28.6,4.17,0.10,2.0,0.10,15,2.4,1,0,'Madurai',None,None,None,None,None,None,None]
,"Latron Prime": ["Hitscan",'Rifle',8.5,68.0,8.5,0,0,0,0,0,0,0,0,0,0,28.6,4.17,0.15,2.5,0.25,15,2.4,1,0,'Madurai','Naramon',None,None,None,None,None,None]
,"Latron Wraith": ["Hitscan",'Rifle',13.75,38.5,2.75,0,0,0,0,0,0,0,0,0,0,28.6,5.4,0.25,2.5,0.20,15,2.4,1,0,'Madurai',None,None,None,None,None,None,None]
,"Miter": ["Projectile",'Rifle',12.5,12.5,225.0,0,0,0,0,0,0,0,0,0,0,100,2.5,0,0,0.5,20,2.0,1,0,'Naramon',None,None,None,None,None,None,None]
,"Opticor": ["Hitscan",'Rifle',100.0,850.0,50.0,0,0,0,0,0,0,0,0,0,0,100,1,0.15,2.0,0.15,5,2.0,1,0,'Vazarin',None,None,None,None,None,None,None]
,"Panthera": ["Projectile",'Rifle',20.0,10.0,70.0,0,0,0,0,0,0,0,0,0,0,100,1.67,0,0,0.10,60,2.0,1,0,'Naramon',None,None,None,None,None,None,None]
,"Paracyst": ["Projectile",'Rifle',0,0,0,0,0,0,25,0,0,0,0,0,0,25.0,11.11,0.05,2.0,0.15,60,2,1,0,None,None,None,None,None,None,None,None]
,"Paris": ["Projectile",'Bow',9.0,144.0,27.0,0,0,0,0,0,0,0,0,0,0,16.7,1,0.30,2.0,0.10,1,0.7,1,0,'Naramon',None,None,None,None,None,None,None]
,"Paris MK1": ["Projectile",'Bow',6.0,96.0,18.0,0,0,0,0,0,0,0,0,0,0,16.7,1,0.30,2.0,0.15,1,0.6,1,0,'Naramon',None,None,None,None,None,None,None]
,"Paris Prime": ["Projectile",'Bow',5.0,160.0,35.0,0,0,0,0,0,0,0,0,0,0,16.7,1,0.45,2.0,0.20,1,0.7,1,0,'Naramon','Madurai',None,None,None,None,None,None]
,"Phage": ["Discharge",'Shotgun',0,0,0,0,0,0,0,0,0,0,0,0,4.29,50,1,0.1,2.0,15,40,2,7,0,'Naramon',None,None,None,None,None,None,None]
,"Quanta": ["Discharge",'Rifle',0,0,0,0,220,0,0,0,0,0,0,0,0,100,1,0.1,2,0.10,60,2,1,0,'Vazarin',None,None,None,None,None,None,None]
,"Quanta Mutalist": ["Projectile",'Rifle',2.5,15.0,7.5,0,0,0,0,0,0,0,0,0,0,100,10,0.025,1.5,0.15,60,3.0,1,0,'Vazarin',None,None,None,None,None,None,None]
,"Quanta Vandal": ["Discharge",'Rifle',0,0,0,0,220,0,0,0,0,0,0,0,0,100,1,0.10,2.0,0.25,90,2,1,0,'Madurai',None,None,None,None,None,None,None]
,"Rubico": ["Hitscan",'Rifle',160.0,30.0,10.0,0,0,0,0,0,0,0,0,0,0,13.3,1.5,0.25,3.0,0.05,5,3.0,1,0,None,None,None,None,None,None,None,None]
,"Simulor": ["Projectile",'Rifle',0,0,0,0,0,0,0,0,0,0,50,0,0,100,2,0.1,2.0,0.30,10,3,1,0,'Vazarin','Naramon',None,None,None,None,None,None]
,"Simulor Synoid": ["Projectile",'Rifle',0,0,0,0,0,0,0,0,0,0,50,0,0,100,2.67,0.1,2,0.35,15,2,1,0,'Vazarin','Naramon','Naramon',None,None,None,None,None]
,"Snipetron": ["Hitscan",'Rifle',17.5,140.0,17.5,0,0,0,0,0,0,0,0,0,0,13.3,1.5,0.20,1.5,0.10,4,3.5,1,0,'Madurai',None,None,None,None,None,None,None]
,"Snipetron Vandal": ["Hitscan",'Rifle',10.0,180.0,10.0,0,0,0,0,0,0,0,0,0,0,13.3,1.5,0.25,2.0,0.15,6,2.0,1,0,'Madurai',None,None,None,None,None,None,None]
,"Sobek": ["Hitscan",'Shotgun',52.5,8.75,8.75,0,0,0,0,0,0,0,0,0,0,9.1,2.5,0.10,2.0,0.15,20,4.0,5,0,None,None,None,None,None,None,None,None]
,"Soma": ["Hitscan",'Rifle',1.2,4.8,6.0,0,0,0,0,0,0,0,0,0,0,28.6,15,0.30,3.0,0.07,100,3.0,1,0,'Madurai','Madurai',None,None,None,None,None,None]
,"Soma Prime": ["Hitscan",'Rifle',1.2,4.8,6.0,0,0,0,0,0,0,0,0,0,0,28.6,15,0.30,3.0,0.10,200,3.0,1,0,'Madurai','Madurai',None,None,None,None,None,None]
,"Stradavar (Auto)": ["Hitscan",'Rifle',8.75,8.75,7.5,0,0,0,0,0,0,0,0,0,0,28.6,10,0.10,2.0,0.05,65,2.0,1,0,'Madurai','Madurai',None,None,None,None,None,None]
,"Stradavar (Semi-Auto)": ["Hitscan",'Rifle',7.5,30.0,12.5,0,0,0,0,0,0,0,0,0,0,28.6,5,0.20,2.0,0.15,65,2.0,1,0,'Madurai','Madurai',None,None,None,None,None,None]
,"Strun": ["Hitscan",'Shotgun',13.75,3.75,7.5,0,0,0,0,0,0,0,0,0,0,4.0,2.5,0.075,1.5,0.20,6,3.8,12,0,'Naramon',None,None,None,None,None,None,None]
,"Strun MK1": ["Hitscan",'Shotgun',9.9,2.70,5.4,0,0,0,0,0,0,0,0,0,0,4.0,2.08,0.075,2.0,0.20,6,3.8,10,0,'Naramon',None,None,None,None,None,None,None]
,"Strun Wraith": ["Hitscan",'Shotgun',26.0,6,8,0,0,0,0,0,0,0,0,0,0,6.7,2.5,0.15,2.0,0.40,10,5.0,10,0,'Naramon',None,None,None,None,None,None,None]
,"Supra": ["Projectile",'Rifle',4.5,33.8,6.7,0,0,0,0,0,0,0,0,0,0,8.3,12.5,0.025,1.5,0.05,180,3.0,1,0,None,None,None,None,None,None,None,None]
,"Sybaris": ["Hitscan",'Rifle',23.1,23.1,23.8,0,0,0,0,0,0,0,0,0,0,28.6,3.98,0.25,2.0,0.10,10,2.0,1,0,None,None,None,None,None,None,None,None]
,"Sybaris Dex": ["Hitscan",'Rifle',22.5,18.75,33.75,0,0,0,0,0,0,0,0,0,0,28.6,4.17,0.35,2.0,0.10,14,1.5,1,0,None,None,None,None,None,None,None,None]
,"Synapse": ["Discharge",'Rifle',0,0,0,0,12.5, 0,0,0,0,0,0,0,0,12.5,10,0.50,2.0,0.10,100,1.5,1,0,None,None,None,None,None,None,None,None]
,"Tetra": ["Projectile",'Rifle',6.0,24.0,0,0,0,0,0,0,0,0,0,0,0,18.2,6.67,0.025,1.5,0.10,60,2.0,1,0,None,None,None,None,None,None,None,None]
,"Tetra Prisma": ["Projectile",'Rifle',7.0,28.0,0,0,0,0,0,0,0,0,0,0,0,18.2,7.08,0.10,2.0,0.15,60,2.0,1,0,None,None,None,None,None,None,None,None]
,"Tiberon": ["Hitscan",'Rifle',15.0,30.0,15.0,0,0,0,0,0,0,0,0,0,0,33.3,9.09,0.05,2.0,0.025,30,2.3,1,0,None,None,None,None,None,None,None,None]
,"Tigris": ["Hitscan",'Shotgun',21,21,168,0,0,0,0,0,0,0,0,0,0,9.1,2,0.05,2.0,0.25,2,1.8,5,0,None,None,None,None,None,None,None,None]
,"Tigris Prime": ["Hitscan",'Shotgun',19.5,19.5,156,0,0,0,0,0,0,0,0,0,0,9.1,2,0.10,2.0,0.30,2,1.8,8,0,'Madurai','Naramon',None,None,None,None,None,None]
,"Tigris Sancti": ["Hitscan",'Shotgun',21,21,168,0,0,0,0,0,0,0,0,0,0,6.5,2,0.15,1.5,0.25,2,1.5,6,0,'Vazarin','Naramon','Madurai',None,None,None,None,None]
,"Vectis": ["Hitscan",'Rifle',90.0,78.8,56.3,0,0,0,0,0,0,0,0,0,0,13.3,1.5,0.25,2.0,0.30,1,0.9,1,0,'Madurai',None,None,None,None,None,None,None]
,"Vectis Prime": ["Hitscan",'Rifle',130.0,146.3,48.7,0,0,0,0,0,0,0,0,0,0,13.3,1.5,0.25,2.0,0.30,2,0.9,1,0,'Madurai','Naramon',None,None,None,None,None,None]
,"Vulkar": ["Hitscan",'Rifle',180.0,33.8,11.2,0,0,0,0,0,0,0,0,0,0,13.3,1.5,0.20,2.0,0.25,6,3.0,1,0,None,None,None,None,None,None,None,None]
,"Vulkar Wraith": ["Hitscan",'Rifle',225.0,25.0,0,0,0,0,0,0,0,0,0,0,0,13.3,1.5,0.20,2.0,0.25,8,3.0,1,0,'Madurai',None,None,None,None,None,None,None]
,"Zhuge": ["Projectile",'Bow',5.0,75.0,20.0,0,0,0,0,0,0,0,0,0,0,40.0,4.17,0.20,2.0,0.35,20,2.5,1,0,'Madurai',None,None,None,None,None,None,None]}

PRIMARY_MOD_DICT = {'Serration':['Rifle', [1],  4, 10, 'Madurai', 'True', 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                'Heavy Caliber': ['Rifle', [1,0],  6, 10, 'Madurai', 'True', 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15,-0.55, 0, 0, 0, 0, 0, 0, 0, 0],
                'Bane of Grineer': ['Rifle', [7], 4, 5, 'Madurai', 'characteristic.type = "Grineer"', 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                'Bane of Corpus': ['Rifle', [7], 4, 5, 'Madurai', 'characteristic.type = "Corpus"', 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                'Hellfire': ['Rifle', [2], 6, 5, 'Naramon', 'True', 0, 0, 0, 0, 0, 0.15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                'Infected Clip': ['Rifle', [2], 6, 5, 'Naramon', 'True', 0, 0, 0, 0, 0, 0, 0.15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                'Stormbringer': ['Rifle', [2], 6, 5, 'Naramon', 'True', 0, 0, 0, 0, 0.15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                'Cryo Rounds': ['Rifle', [2], 6, 5, 'Vazarin', 'True', 0, 0, 0, 0.15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                'Vital Sense': ['Rifle', [0], 4, 5, 'Madurai', 'True', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.2, 0, 0, 0, 0, 0],
                'Point Blank': ['Shotgun', [0], 4, 5, 'Madurai', 'True', 0.15, 0.15, 0.15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}

ENEMY_DICT = {'Grineer Lancer': ['Grineer', 1, 100, 'cloned flesh', 100, 'ferrite', 0, None],
              'Elite Lancer': ['Grineer', 15, 150, 'cloned flesh', 200, 'alloy', 0, None],
              'Elite Crewman': ['Corpus', 15, 100, 'flesh', 0, None, 200, 'shield']}
