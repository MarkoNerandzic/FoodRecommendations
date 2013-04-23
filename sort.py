#-------------------------------------------------------------------------------
# Name:        Sort - Class of FoodRecommendations
# Purpose:     To sort the results and create recommendations for the user.
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

class Sort():

    recommendations = []
    weights = []

    def __init__(self, gender, nationality, age, spicy, favourites, location, genders, nationalities, ages, spicys, locations, nationalityOne, nationalityTwo, nationalityThree):
        self.rankNationalities(gender, nationality, age, spicy, favourites, location, genders, nationalities, ages, spicys, locations, nationalityOne, nationalityTwo, nationalityThree)

    def rankNationalities(self, gender, nationality, age, spicy, favourites, location, genders, nationalities, ages, spicys, locations, nationalityOne, nationalityTwo, nationalityThree):
        weightFactor = 0
        index = 0

        while index < len(nationalityOne):
            if favourites[0] == nationalityOne[index]:
                weightFactor += 1.0
                if gender == genders[index]:
                    weightFactor += 1.0
                if nationality == nationalities[index]:
                    weightFactor += 1.0
                if age == ages[index]:
                    weightFactor += 1.0
                if spicy == spicys[index]:
                    weightFactor += 1.0
                if location == locations[index]:
                    weightFactor += 1.0
                indexTwo = -1
                indexThree = -1

                counter = 0
                while counter < len(self.recommendations):
                    if nationalityTwo[index] == self.recommendations[counter]:
                        indexTwo = counter
                    counter += 1

                counter = 0
                while counter < len(self.recommendations):
                    if nationalityThree[index] == self.recommendations[counter]:
                        indexThree = counter
                    counter += 1

                if indexTwo == -1:
                    self.recommendations.append(nationalityTwo[index])
                    self.weights.append(weightFactor)
                else:
                    self.weights[indexTwo] += weightFactor

                if indexThree == -1:
                    self.recommendations.append(nationalityThree[index])
                    self.weights.append((weightFactor / 2))
                else:
                    self.weights[indexThree] += weightFactor

            weightFactor = 0
            index += 1

        index = 0
        while index < len(nationalityOne):
            if favourites[1] == nationalityOne[index]:
                weightFactor += 0.5
                if gender == genders[index]:
                    weightFactor += 0.5
                if nationality == nationalities[index]:
                    weightFactor += 0.5
                if age == ages[index]:
                    weightFactor += 0.5
                if spicy == spicys[index]:
                    weightFactor += 0.5
                if location == locations[index]:
                    weightFactor += 0.5
                indexTwo = -1
                indexThree = -1

                counter = 0
                while counter < len(self.recommendations):
                    if nationalityTwo[index] == self.recommendations[counter]:
                        indexTwo = counter
                    counter += 1

                counter = 0
                while counter < len(self.recommendations):
                    if nationalityThree[index] == self.recommendations[counter]:
                        indexThree = counter
                    counter += 1

                if indexTwo == -1:
                    self.recommendations.append(nationalityTwo[index])
                    self.weights.append(weightFactor)
                else:
                    self.weights[indexTwo] += weightFactor

                if indexThree == -1:
                    self.recommendations.append(nationalityThree[index])
                    self.weights.append((weightFactor / 2))
                else:
                    self.weights[indexThree] += weightFactor

            weightFactor = 0
            index += 1

        index = 0
        while index < len(nationalityOne):
            if favourites[2] == nationalityOne[index]:
                weightFactor += 0.25
                if gender == genders[index]:
                    weightFactor += 0.25
                if nationality == nationalities[index]:
                    weightFactor += 0.25
                if age == ages[index]:
                    weightFactor += 0.25
                if spicy == spicys[index]:
                    weightFactor += 0.25
                if location == locations[index]:
                    weightFactor += 0.25
                indexTwo = -1
                indexThree = -1

                counter = 0
                while counter < len(self.recommendations):
                    if nationalityTwo[index] == self.recommendations[counter]:
                        indexTwo = counter
                    counter += 1

                counter = 0
                while counter < len(self.recommendations):
                    if nationalityThree[index] == self.recommendations[counter]:
                        indexThree = counter
                    counter += 1

                if indexTwo == -1:
                    self.recommendations.append(nationalityTwo[index])
                    self.weights.append(weightFactor)
                else:
                    self.weights[indexTwo] += weightFactor

                if indexThree == -1:
                    self.recommendations.append(nationalityThree[index])
                    self.weights.append((weightFactor / 2))
                else:
                    self.weights[indexThree] += weightFactor

            weightFactor = 0
            index += 1

        counter = 0
        while counter < len(self.recommendations):
            if favourites[0] == self.recommendations[counter]:
                self.recommendations.pop(counter)
                self.weights.pop(counter)
                counter = 0
            elif favourites[1] == self.recommendations[counter]:
                self.recommendations.pop(counter)
                self.weights.pop(counter)
                counter = 0
            elif favourites[2] == self.recommendations[counter]:
                self.recommendations.pop(counter)
                self.weights.pop(counter)
                counter = 0
            counter += 1

    def getRankings(self):
        return (self.recommendations, self.weights)