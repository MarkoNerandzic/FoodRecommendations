#-------------------------------------------------------------------------------
# Name:        UserIO - Class of FoodRecommendations
# Purpose:     To interact with the user to get their inputs and then display
#              their recommendations.
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

import jLibrary

class UserIO():

    spicyPreference = 0
    gender = 0
    age = ''
    foodNationalitiesFavorites = []
    location = ''
    nationality = ''

    def getInitialInformation(self):
        self.spicyPreference = self.getSpicyFromUser()
        self.gender = self.getGenderFromUser()
        self.age = self.getAgeRangeFromUser()
        self.foodNationalitiesFavorites = self.getFoodFavoritesFromUser()
        self.location = self.getLocationFromUser()
        self.nationality = self.getNationalityFromUser()

    def getNationalityFromUser(self):
        return jLibrary.getStrInput('What is your nationality?')

    def getSpicyFromUser(self):
        spicyTemp = jLibrary.getOption("Do you like spicy food?\n[1]Yes\n[2]No\n[3]Sometimes", 1, 3)
        if spicyTemp == 1:
            return "Yes"
        elif spicyTemp == 2:
            return "No"
        else:
            return "Sometimes"

    def getGenderFromUser(self):
        genderTemp = jLibrary.getOption("What is your gender?\n[1]Male\n[2]Female", 1, 2)
        if genderTemp == 1:
            return "Male"
        else:
            return "Female"

    def getAgeRangeFromUser(self):
        userInputTemp = jLibrary.getOption("What age group are you in?\n[1]0-19\n[2]20-39\n[3]40-59\n[4]60-79\n[5]80-99\n[6]100+\n", 1, 6)
        if userInputTemp == 1:
            return "0-19"
        elif userInputTemp == 2:
            return "20-39"
        elif userInputTemp == 3:
            return "40-59"
        elif userInputTemp == 4:
            return "60-79"
        elif userInputTemp == 5:
            return "80-99"
        else:
            return "100+"

    def getFoodFavoritesFromUser(self):
        foodFavorites = []
        finishedGettingInput = False
        while not finishedGettingInput:
            userInputTemp = jLibrary.getStrInput("Enter your next favorite food nationality or 'exit' to end your input!")
            if userInputTemp != "exit":
                foodFavorites.append(userInputTemp)
            else:
                finishedGettingInput = True
        return foodFavorites

    def getLocationFromUser(self):
        return jLibrary.getStrInput("What country do you currently reside in?")

    def displayReccomendations(self, recommendations):
        counter = 0
        moreSuggestions = False
        while counter < len(recommendations) and moreSuggestions:
            print "Your",
            if counter%10 != 0 and counter%10 != 1 and counter%10 != 2:
                print counter, "th",
            elif counter == 0:
                print counter+1,"st",
            elif counter == 1:
                print counter+1,"nd",
            else:
                print counter+1,"rd",
            print "recommendation is:", recommendations[counter]
            response = 1
            while response  == 1:
                response = jLibrary.getOption("What would you like to do next?\n[1]See more information about " + recommendations[counter] + "food\n[2]See another suggestion\n[3]Exit[3]", 1, 3)
                if response == 1:
                    print "Insert More Information here"
                elif response == 2:
                    counter += 1
                else:
                    moreSuggestions = False

    def getSpicy(self):
        return self.spicyPreference

    def getGender(self):
        return self.gender

    def getAgeRange(self):
        return self.age

    def getFoodFavorites(self):
        return self.foodNationalitiesFavorites

    def getLocation(self):
        return self.location

    def getNationality(self):
        return self.nationality