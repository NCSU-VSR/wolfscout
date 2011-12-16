__author__ = 'laurencharles-smith'

# Create file that reads csv data, parses the data into a list and adds to dictionary

##Creates a DictReader object which can parse the given file, returning a #dictionary of values for each line of the file.
# The dictionary keys are #typically the first line of the file. You can, optionally, provide the field #names if
# they are not the first line of the file. The csvfile can be any #iterable object.

import csv
from apps.wildlife.models import *
from apps.crawler.gpscollar.models import *
infile = open ('/opt/webapps/ncsu/wolfscout/sample_data/coyote-demographics.csv','rU')

#Set species. Note need to use Species class
#s = Species(name="Deer")
#s.save()

dem = csv.DictReader(infile)

#Keys = Animal ID,Collar ID,Date,Time,Sex,Age,Location,Trap,Collar Freq.,Crown to rump (cm),
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
    testAnimal.age_class = data["Age"]
    testAnimal.location = data["Location"]
    testAnimal.trap = data["Trap"]
    testAnimal.crowntorump = data["Crown to rump (cm)"]
    testAnimal.chest = data["Chest (cm)"]
    testAnimal.neck = data["Neck (cm)"]
    testAnimal.weight = data["Weight (Kg)"]
    testAnimal.blood = data["Blood"]
    testAnimal.hair = data["Hair"]
    testAnimal.ticks = data["Ticks"]
    testAnimal.feces = data["Feces"]
    testAnimal.notes = data["Notes"]
    testAnimal.status = data["Status"]
    testAnimal.sex = data["Sex"]

#NEED to change these to datetime module
    testAnimal.date = data["Date"]
    testAnimal.time = data["Time"]

    testAnimal.save()   #Save all loaded data for animal

    #print data["Trap"]
    print "Test animal is: ", testAnimal,
    print "Animal pk is: ", testAnimal.pk

infile.close()


