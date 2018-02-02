import matplotlib.pyplot as plt
import random
import unittest

def final_test(weights, data): #this function we use to test our neuro
        #print('kek')
        for i in range(4):
                print (data[i][0:2], sgn(summer(weights,data[i])))
          
def sgn (dot):#graphic of activated function (we have sign)
        return 1 if dot>=0 else  0

def gui_interface(errors,weights):# Here we construct our graph of errors
        #print (errors)
        plt.plot(errors)
        plt.show()

def summer(list1, list2):#calculate sum of weights and data (main conception of neuro)
        summa = 0.0;
        for i in range(len(list1)):
                summa+=list1[i]*list2[i]
        return summa

def perceptron(data,answers,num):
        errors = [] #errors list to make a plot
        learning_level = 0.1 #level of learning (accuracy)
        weights = [random.random() for i in range(3)]#first weight balance
        for i in range(num):
                random_value = random.randint(0,3)#Choise 1 random value to learn
                current_data, current_answer = data[random_value], answers[random_value] #choise 1 data from list
                result = summer(weights, current_data)
                error = current_answer - sgn(result)# count error of prediction
                #print (type(error))
                errors.append(error)
                for j in range(len(current_data)):
                        weights[j] += learning_level * error * current_data[j]#makesome edits to neuro
        return errors, weights
                
def main():
        train_data = [(0,0,1), #or function table
                      (0,1,1), #3d column is bias
                      (1,0,1),
                      (1,1,1)]
        right_answers = [0,1,1,1]# answers fo or func
        num_of_iterations = 100
        errors,weights = perceptron(train_data, right_answers, num_of_iterations)
        gui_interface(errors,weights)
        final_test(weights, train_data)

class TestPerceptronMethods(unittest.TestCase):

        def test_summer(self):#3 tests for fifferent types of construction
                self.assertEqual(summer([1,2,3],[3,4,5]), 3+8+15)
                self.assertEqual(summer([1,2,3],(3,4,5)), 3+8+15)
                self.assertEqual(summer((1,2,3),(3,4,5)), 3+8+15)
        def test_perceptron(self):#This is a big function with lot of logic so will check only types and +-sizes
                train_data = [(0,0,1), #or function table
                      (0,1,1), #3d column is bias
                      (1,0,1),
                      (1,1,1)]
                right_answers = [0,1,1,1]# answers fo or func
                num_of_iterations = 100
                errors,weights = perceptron(train_data, right_answers, num_of_iterations)
                self.assertTrue(type(errors)==type([]))
                self.assertTrue(type(weights)==type([]))
                self.assertTrue(errors.pop()==0, 'your net is not teached, try to make more iteration')
                self.assertTrue(sum(weights)<=num_of_iterations and sum(weights)>=num_of_iterations*(-1))
                
if __name__ == "__main__":
        unittest.main()
