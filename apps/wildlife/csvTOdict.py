__author__ = 'laurencharles-smith'

# Create file that reads csv data, parses the data into a list and adds to dictionary

##Creates a DictReader object which can parse the given file, returning a #dictionary of values for each line of the file.
# The dictionary keys are #typically the first line of the file. You can, optionally, provide the field #names if
# they are not the first line of the file. The csvfile can be any #iterable object.

###COYOTE DATA######################################################################################
import csv
from apps.wildlife.models import *
from apps.crawler.gpscollar.models import *
infile1 = open ('/opt/webapps/ncsu/wolfscout/sample_data/coyote-demographics.csv','rU')

#Set species. Note need to use Species class
#s = Species(name="Deer")
#s.save()

dem = csv.DictReader(infile1)

#Coyote Keys = Animal ID,Collar ID,Date,Time,Sex,Age,Location,Trap,Collar Freq.,Crown to rump (cm),
# Chest (cm),Neck (cm),Weight (Kg),Blood,Hair,Ticks,Feces,Notes,Status,Species

#for row in dem:
#        print row

for data in dem:
    try:
        #Load collar data for collar id
        animalCollar = Collar.objects.get(collarID=int(data["Collar ID"]))
    except:
        #If collar data doesn't exist, create collar
        animalCollar = Collar(collarID=int(data["Collar ID"]))
        animalCollar.save()

    try:
        #Load species data for animal species
        animalSpecies = Species.objects.get(name=data["Species"])
    except:
        #If species data doesn't exist, create species
        animalSpecies = Species(name=data["Species"])
        animalSpecies.save()

    #Load animal whose common name = animal id to upload demographic information
    testAnimal = Animal.objects.get(common_name=data["Animal ID"])
    #If the common name doesn't exist, create it
    if not testAnimal:
        testAnimal = Animal()
        testAnimal.common_name = data["Animal ID"]
        testAnimal.save()

    #Run through the rows (data) in the dictionary and add data to demographic fields
    if animalCollar:    #If the animal collar exists, load the collar
        testAnimal.collar = animalCollar
    if animalSpecies:   #If the animal species exists, load the species
        testAnimal.species = animalSpecies
    testAnimal.collar_frequency = data["Collar Freq."]
    testAnimal.age_class = data["Age Class"]
    testAnimal.location = data["Location"]
    testAnimal.trap = data["Trap"]
    testAnimal.crowntorump_cm = data["Crown to rump (cm)"]
    testAnimal.chest_cm = data["Chest (cm)"]
    testAnimal.neck_cm = data["Neck (cm)"]
    testAnimal.weight_Kg = data["Weight (Kg)"]
    testAnimal.blood = data["Blood"]
    testAnimal.hair = data["Hair"]
    testAnimal.ticks = data["Ticks"]
    testAnimal.feces = data["Feces"]
    testAnimal.notes = data["Notes"]
    testAnimal.status = data["Status"]
    testAnimal.sex = data["Sex"]

#NEED to change these to datetime module
#dt = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
  #  dt = datetime.strptime(data["Date"] data["Time"], "%m/%d/%y %H:%M")
    testAnimal.date = data["Date"]
    testAnimal.time = data["Time"]

    testAnimal.save()   #Save all loaded data for animal

    #print data["Trap"]
    print "Test animal is: ", testAnimal,
    print "Animal pk is: ", testAnimal.pk

infile1.close()

###Deer DATA######################################################################################

infile2 = open ('/opt/webapps/ncsu/wolfscout/sample_data/deer-demographics_ALL.csv','rU')

#Set species. Note need to use Species class
#s = Species(name="Deer")
#s.save()

dem2 = csv.DictReader(infile2)

#Deer Keys = Animal ID,Date,Shooter,Collar ID,Collar Freq,VIT Freq,Antenna Length,Location,
# GPS Shot,GPS Recovery,Flight Distance,Recovery (min),Drug Mix,Age Class,Age,Weight (Lb),Weight (Kg),
# Notes,Status,Species,Sex

#for row in dem:
#        print row

for data in dem2:
    try:
        #Load collar data for collar id
        animalCollar = Collar.objects.get(collarID=int(data["Collar ID"]))
    except:
        #If collar data doesn't exist, create collar
        animalCollar = Collar(collarID=int(data["Collar ID"]))
        animalCollar.save()

    try:
        #Load species data for animal species
        animalSpecies = Species.objects.get(name=data["Species"])
    except:
        #If species data doesn't exist, create species
        animalSpecies = Species(name=data["Species"])
        animalSpecies.save()

    #Load animal whose common name = animal id to upload demographic information
    try:
        testAnimal = Animal.objects.get(common_name=data["Animal ID"])
    except:
        testAnimal = Animal()
        testAnimal.common_name = data["Animal ID"]
        testAnimal.collar = animalCollar
        testAnimal.save()

    #If the common name doesn't exist, create it
#    if not testAnimal:
#        testAnimal = Animal()
#        testAnimal.common_name = data["Animal ID"]
#        testAnimal.save()

    #Run through the rows (data) in the dictionary and add data to demographic fields
    if animalCollar:    #If the animal collar exists, load the collar
        testAnimal.collar = animalCollar

    if animalSpecies:   #If the animal species exists, load the species
        testAnimal.species = animalSpecies

    testAnimal.collar_frequency = data["Collar Freq"]
    testAnimal.age_class = data["Age Class"]
    testAnimal.location = data["Location"]
    testAnimal.shooter = data["Shooter"]
    testAnimal.weight_Kg = data["Weight (Kg)"]
    testAnimal.notes = data["Notes"]
    testAnimal.status = data["Status"]
    testAnimal.sex = data["Sex"]

    testAnimal.frequency_VIT = data["VIT Freq"]
    testAnimal.antennaLength_VIT = data["Antenna Length"]
    testAnimal.shotGPS = data["GPS Shot"]
    testAnimal.recoveryGPS = data["GPS Recovery"]
    testAnimal.flightDist = data["Flight Distance"]
    testAnimal.recovery_min = data["Recovery (min)"]
    testAnimal.drugMix = data["Drug Mix"]
    testAnimal.estAge_yr = data["Age"]

    #NEED to change these to datetime module
    #dt = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
    #  dt = datetime.strptime(data["Date"] data["Time"], "%m/%d/%y %H:%M")
    testAnimal.date = data["Date"]
    #testAnimal.time = data["Time"]

    testAnimal.save()   #Save all loaded data for animal

    #print data["Trap"]
    print "Test animal is: ", testAnimal,
    print "Animal pk is: ", testAnimal.pk

infile2.close()