#-------------------------------------------------------------------------------
# Name:        FileIO - Class of FoodRecommendations
# Purpose:     To gather the survey results from the .csv file and write out the
#              user's inputs to the file.
#
# Author:      Justin Moulton & Marko Nerandzic
#
# Created:     April 9, 2013
# Copyright:   (c) Justin Moulton & Marko Nerandzic 2013
# Licence:     This work is licensed under the Creative Commons
#              Attribution-NonCommercial-ShareAlike 3.0 Unported License.
#              To view a copy of this license, visit
#              http://creativecommons.org/licenses/by-nc-sa/3.0/.
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

            self.genderArray.append(gender.lower())

            self.nationalityArray.append(nationality.lower())

            self.ageArray.append(age.lower())

            self.spicyArray.append(spicy.lower())

            self.favNationalityArray.append(favNationality.lower())

            self.secondFavNationalityArray.append(secondFavNationality.lower())

            self.thirdFavNationalityArray.append(thirdFavNationality.lower())

            self.countryArray.append(country.lower())

            counter = 0
            while counter < len(self.favNationalityArray):
                if self.favNationalityArray[counter] not in self.allNationalityArray:
                    self.allNationalityArray.append(self.favNationalityArray[counter])
                counter += 1
            counter = 0
            while counter < len(self.secondFavNationalityArray):
                if self.secondFavNationalityArray[counter] not in self.allNationalityArray:
                    self.allNationalityArray.append(self.secondFavNationalityArray[counter])
                counter += 1
            counter = 0
            while counter < len(self.thirdFavNationalityArray):
                if self.thirdFavNationalityArray[counter] not in self.allNationalityArray:
                    self.allNationalityArray.append(self.thirdFavNationalityArray[counter])
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
