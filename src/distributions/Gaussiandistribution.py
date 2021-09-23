import numpy as np
import matplotlib.pyplot as plt
from Generaldistribution import Distribution

class Gaussian (Distribution):

    """
    Gaussian distribution class for calculating and
    visualizing a Gaussian distribution.

    Attributes:
        mean (float) represent the mean values of the distribution
        stdev (float) represent standard deviation of the distribution
        dat_list (list of float) extracted from the text file
    """
    def __init__(self, mu = 0 , sigma = 1):

        Distribution.__init__(self, mu , sigma)

    def calcualte_mean(self):
        """
        Function calculated the mean of the dataset

        Args:
            None
        Returns:
            float: mean of the dataset
        """

        avg = float(sum(self.data / len(self.data)))
        self.mean = avg

        return self.mean

    def calculate_stdev(self, sample=True):
        """
        Function calculates the standard deviation of the dataset

        Args:
            sample (bool) whether the data is population or a sample
        Returns:
            float: standard deviation of the data set
        """

        if sample:
            n = len(self.data) - 1
        else:
            n = len(self.data)
        mean = self.calcualte_mean()
        sigma = 0

        for data in self.data:
            sigma += (data - mean)**2
        sigma = np.sqrt(sigma/n)

        self.stdev = sigma

        return self.stdev


     def plot_histogram(self):
        """
        Function to output a histogram of the instance variable data
        using matplotlib.pyplot library

        Args:
            None
        Returns:
            None
        """

        plt.hist(self.data)
        plt.title("Histogram of data")
        plt.xlabel('data')
        pltylable('count')

    def pdf(self , x):
        """
        Probability Density Function calculates the Gaussian distribution

        Args:
            x (float): point for calculating the probability density function
        
        Returns:
            float: probability density function as output
        """

        prob = (1. /(self.stdev * np.sqrt(2*math.pi))) * np.exp(-.5*((x - self.mean) / self.stdev)**2)
        return prob


    def plot_histogram_pdf(self, n_spaces = 50):

        """Function to plot the normalized histogram of the data and a plot of the 
        probability density function along the same range
        
        Args:
            n_spaces (int): number of data points 
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """
        
        mu = self.mean
        sigma = self.stdev

        min_range = min(self.data)
        max_range = max(self.data)
        
         # calculates the interval between x values
        interval = 1.0 * (max_range - min_range) / n_spaces

        x = []
        y = []
        
        # calculate the x values to visualize
        for i in range(n_spaces):
            tmp = min_range + interval*i
            x.append(tmp)
            y.append(self.pdf(tmp))

        # make the plots
        fig, axes = plt.subplots(2,sharex=True)
        fig.subplots_adjust(hspace=.5)
        axes[0].hist(self.data, density=True)
        axes[0].set_title('Normed Histogram of Data')
        axes[0].set_ylabel('Density')

        axes[1].plot(x, y)
        axes[1].set_title('Normal Distribution for \n Sample Mean and Sample Standard Deviation')
        axes[0].set_ylabel('Density')
        plt.show()

        return x, y

    def __add__(self, other):

        """Function to add together two Gaussian distributions

        Args:
            other (Gaussian): Gaussian instance

        Returns:
            Gaussian: Gaussian distribution

        """

        result = Gaussian()
        result.mean = self.mean + other.mean
        result.stdev = math.sqrt(self.stdev ** 2 + other.stdev ** 2)

        return result


    def __repr__(self):

        """Function to output the characteristics of the Gaussian instance

        Args:
            None

        Returns:
            string: characteristics of the Gaussian

        """

        return "mean {}, standard deviation {}".format(self.mean, self.stdev)



if __name__ == "__main__":
    # initialize two gaussian distributions
    gaussian_one = Gaussian(25, 3)
    gaussian_two = Gaussian(30, 2)
    
    # initialize a third gaussian distribution reading in a data efile
    gaussian_three = Gaussian()
    gaussian_three.read_data_file('numbers.txt')
    gaussian_three.calculate_mean()
    gaussian_three.calculate_stdev()


    # print out the mean and standard deviations
    print(gaussian_one.mean)
    print(gaussian_two.mean)
    
    print(gaussian_one.stdev)
    print(gaussian_two.stdev)

    print(gaussian_three.mean)
    print(gaussian_three.stdev)


    # plot histogram of gaussian three
    gaussian_three.plot_histogram_pdf()


    # add gaussian_one and gaussian_two together
    gaussian_one + gaussian_two

