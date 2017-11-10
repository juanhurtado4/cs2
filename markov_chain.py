class Dictogram(dict):
    '''Dictogram is a histogram implemented as a subclass of the dict type.'''

    def __init__(self, word_list=None):
        '''Initialize this histogram as a new dict and count given words.'''
        super(Dictogram, self).__init__()

        self.types = 0  # Count of distinct word types in this histogram

        self.tokens = 0  # Total count of all word tokens in this histogram
        
        # Count words in given list, if any
        # if word_list is not None:
        #     self.tokens = len(word_list)
        #     for word in word_list:
        #         if word not in self:
        #             self[word] = word_list.count(word)
        #     self.types = len(self)

        self.histogram = {}

        if word_list is not None:

            self.tokens = len(word_list)

            self.get_histogram(word_list)

            self.types = len(self.histogram)

    def add_count(self, histogram, word):
        '''Increase frequency count of given word by given count amount.'''
        if word not in histogram:
            histogram[word] = 1

        histogram[word] += 1

        return histogram

    def get_histogram():

            for word in word_list:

                self.add_count(word)



    def frequency(self, word):
        '''
        Word: String
        Computes frequency count of given word, or 0 if word is not found
        Returns Int
        '''
        if word in self:

            return self[word]

        return 0
