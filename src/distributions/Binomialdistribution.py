import math
import numpy as np
import matplotlib.pyplot a plt
from .Generaldistribution import Distribution

class Binomial(object , Distribution):
    """
    Binomial Distribution class fro calculating and
    visualizing a Binomial distribution

    Attributes:
        mean (float): representing the mean value od the distribution
        stdev (float): representing the standard deviation of the distribution
        data ([] floats): a list of floats to be extracted from the data file
        p (float): representing the probability of an event occuring
        n (int): nth trials
    """
    def __init__(self, prob = .5 , n = 20):
        Distribution.__init__(self.calculate_mean() , self.calaculate_std())
        
        self.prob = prob
        self.n_trials = n

    def calculate_mean(self):
        """
        Function calculates the mean from p and n_trials

        Args:
            None
        Returns:
            float: mean of the dataset
        """
        self.mean = self.p * self.n_trials
        return self.mean

    def calculates_stdev(self):
        """
        Function calcualtes standard deviation from p and n_trials

        Args:
            None
        Returns:
            float: standard deviation of the dataset
        """
        self.stdev = np.sqrt(self.n_trials * self.p * (1 - self.p))
        return self.stdev

    def relace_stats_with_data(self):
        """
        Function calculates p and n_trials from the dataset

        Args:
            None
        Returns:
            float : p value
            float : n_trials value
        """

        self.n_trials = len(self.data)
        self.p = 1.0 * sum(self.data) / len(self.data)
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()

        return self.p , self.n_trials

    
    def plot_bar(self):
        """Function to output a histogram of the instance variable data using
        matplotlib pyplot library.

        Args:
            None

        Returns:
            None
        """

        plt.bar(x = ['0' , '1'] , height = [(1 - self.p) * self.n_trials, self.p * self.n_trials])
        plt.title('Bar Chart of Data')
        plt.xlabel('outcome')
        plt.ylabel('count')

    def pdf(self, k):
          """
          Probability density function calculator for the binomial distribution.
        
          Args:
             x (float): point for calculating the probability density function
            
        
          Returns:
             float: probability density function output
        """

        a = math.factorial(self.n_trials / (math.factorial(k) * (math.factorial(self.n_trials - k)))
        b = (self.p **k) * (1 - self.p) ** (self.n_trials - k)

        return a * b
        

    def plot_bar_pdf(self):

        """Function to plot the pdf of the binomial distribution
        
        Args:
            None
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """
        
        x = []
        y = []
        
        # calculate the x values to visualize
        for i in range(self.n_trials + 1):
            x.append(i)
            y.append(self.pdf(i))

        # make the plots
        plt.bar(x, y)
        plt.title('Distribution of Outcomes')
        plt.ylabel('Probability')
        plt.xlabel('Outcome')

        plt.show()

        return x, y
        
    def __add__(self, other):
        
        """Function to add together two Binomial distributions with equal p
        
        Args:
            other (Binomial): Binomial instance
            
        Returns:
            Binomial: Binomial distribution
            
        """
        
        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise
        
        result = Binomial()
        result.n = self.n_trials + other.n_trials
        result.p = self.p
        result.calculate_mean()
        result.calculate_stdev()
        
        return result
        
        
    def __repr__(self):
    
        """Function to output the characteristics of the Binomial instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Gaussian
        
        """
        
        return "mean {}, standard deviation {}, p {}, n {}".\
        format(self.mean, self.stdev, self.p, self.n_trials)
