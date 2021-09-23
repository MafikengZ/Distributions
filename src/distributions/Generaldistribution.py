
class Distribution:

    def __init__(self, mu = 0 , sigma = 1):
         """
        General distribution class for calculating and
        visualizing a probability distribution.

        Attributes:
            mean (float) represent the mean value of the distribution
            stdev (float) represent the standard deviation of the distribution
            data (list of float) extracted from the data file
        """


        self.mean = mu
        self.std = sigma
        self.data = []

    def read_data_file(self, filename):
        """
        Function reads data from a text file. The text file have should have
        number (floats) per line. The numbers are stored in the data attribute.
        
        Args:
            filename (string) name of the file to read from.
        Returns:
            None
        """

        with open (filename) as file:
            data_list = []
            line = file.readline()
            while line:
                data_list.append(line)
                line = file.readline()
            file.close()

        self.data = data_list

        
