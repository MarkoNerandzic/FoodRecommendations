#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      321599755
#
# Created:     15/04/2013
# Copyright:   (c) 321599755 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class FileIO:
    genderArray = []
    nationalityArray = []
    ageArray = []
    spicyArray = []
    favNationalityArray = []
    secondFavNationalityArray = []
    thirdFavNationalityArray = []
    allNationalityArray = []
    countryArray = []

    def ifNotInArrayAppendElseCount(self, data, array):
            counter = 0
            located = False
            while counter < len(array) and not located:
                if data == array[counter][0]:
                    array[counter][1] += 1
                    located = True
                counter += 1
            if not located:
                array.append([data, 1])

    def getInfoFromFile(self):
        fin = open("Favourite Food Survey (Responses).csv")
        for line in fin:
            line = line.strip()
            genderEndComma = line.find(",")
            nationalityEndComma = line.find(",", genderEndComma + 1)
            ageEndComma = line.find(",", nationalityEndComma + 1)
            spicyEndComma = line.find(",", ageEndComma + 1)
            favNationalityEndComma = line.find(",", spicyEndComma + 1)
            secondFavNationalityEndComma = line.find(",", favNationalityEndComma + 1)
            thirdFavNationalityEndComma = line.find(",", secondFavNationalityEndComma + 1)

            gender = line[:genderEndComma]
            nationality = line[genderEndComma + 1:nationalityEndComma]
            age = line[nationalityEndComma + 1:ageEndComma]
            spicy = line[ageEndComma + 1:spicyEndComma]
            favNationality = line[spicyEndComma + 1:favNationalityEndComma]
            secondFavNationality = line[favNationalityEndComma + 1:secondFavNationalityEndComma]
            thirdFavNationality = line[secondFavNationalityEndComma + 1:thirdFavNationalityEndComma]
            country = line[thirdFavNationalityEndComma + 1:]

            self.ifNotInArrayAppendElseCount(gender, self.genderArray)

            self.ifNotInArrayAppendElseCount(nationality, self.nationalityArray)

            self.ifNotInArrayAppendElseCount(age, self.ageArray)

            self.ifNotInArrayAppendElseCount(spicy, self.spicyArray)

            self.ifNotInArrayAppendElseCount(favNationality, self.favNationalityArray)

            self.ifNotInArrayAppendElseCount(secondFavNationality, self.secondFavNationalityArray)

            self.ifNotInArrayAppendElseCount(thirdFavNationality, self.thirdFavNationalityArray)

            self.ifNotInArrayAppendElseCount(country, self.countryArray)

            counter = 0
            while counter < len(self.favNationalityArray):
                if self.favNationalityArray[counter][0] not in self.allNationalityArray:
                    self.allNationalityArray.append(self.favNationalityArray[counter][0])
                counter += 1
            counter = 0
            while counter < len(self.secondFavNationalityArray):
                if self.secondFavNationalityArray[counter][0] not in self.allNationalityArray:
                    self.allNationalityArray.append(self.secondFavNationalityArray[counter][0])
                counter += 1
            counter = 0
            while counter < len(self.thirdFavNationalityArray):
                if self.thirdFavNationalityArray[counter][0] not in self.allNationalityArray:
                    self.allNationalityArray.append(self.thirdFavNationalityArray[counter][0])
                counter += 1

    def getGenderArray(self):
        return self.genderArray

    def getNationalityArray(self):
        return self.nationalityArray

    def getAgeArray(self):
        return self.ageArray

    def getSpicyArray(self):
        return self.spicyArray

    def getFavNationalityArray(self):
        return self.favNationalityArray

    def getSecondFavNationalityArray(self):
        return self.secondFavNationalityArray

    def getThirdFavNationalityArray(self):
        return self.thirdFavNationalityArray

    def getCountryArray(self):
        return self.countryArray
