# TODO: Fix get histogram logic
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

        # self.histogram = {}

        if word_list is not None:

            self.tokens = len(word_list)

            self.get_histogram(word_list)

            self.types = len(self)

    def add_count(self, histogram, word):
        '''Increase frequency count of given word by given count amount.'''
        if word not in histogram:
            histogram[word] = 1

        histogram[word] += 1

        return histogram

    def get_histogram(self, word_list):

            for index, word in enumerate(word_list):
                try:
                    next_word = word_list[index + 1]
                except:
                    break

                if word not in self:

                    self[word] = {next_word: 1}

                else:
                    # {
                        # 'fish': {'one': 1, 'red: 2'},
                        # 'red': {'fish': 1, 'one': 2}
                    # }

                    if next_word not in self[word]:
                        self[word].update({next_word: 1})
                    else:
                         self[word][next_word] += 1

                # self[word][] = {word_list[index + 1]: 1}

    def frequency(self, word):
        '''
        Word: String
        Computes frequency count of given word, or 0 if word is not found
        Returns Int
        '''
        if word in self:

            return self[word]

        return 0


def main():

    # with open('one_fish_text.txt') as file:
    with open('testing_markov.text') as file:

        raw_data = file.read().lower()

    l = raw_data.strip().split(' ')
    test = Dictogram(l)
    print(test)

        # clean_data = get_clean_data(raw_data)

        # histogram = get_histogram(clean_data)

        # histogram_words_count = get_total_unique_words(histogram)

        # print(histogram)

if __name__=='__main__':
    main()
