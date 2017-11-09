## What are the key features of the application? Are these clearly separated into their own files, classes, and/or modules?

    The key features of the flask stochastic app are:

        * Cleaning raw data
        * Creating a histogram
        * Generating a random word
        * Generating a sentence from a histogram
    I have my cleaning and generating histogram functions as methods in a module


## Are the names of files, modules, functions, and variables appropriate and accurate? Would a new programmer be able to understand the names without too much contextual knowledge?

    My naming convention along with my docstrings are consistent and descriptive, to allow anyone understand what is happening in the code

## What are the scopes of variables and are they appropriate for their use case? If there are global variables, why are they needed?

    I do not have any global variables besides the configuration of flask

## Are the functions small and clearly specified, with as few side effects as possible?

    Functions are small with an avg of 8 lines per function


## Are there functions that could be better organized in an Object-Oriented Programming style by defining them as methods of a class?

    I believe almost the entire application could be rewritten with OOP

## Can files be used as both modules and as scripts?

    Yes they can. To run a file as a module it must be imported with the conditional " if __name__=='__main__' "

    To run it as a script it must also be ran from the file where the program was written. It CANNOT imported

## Do modules all depend on each other or can they be used independently?

    Some of the functions can be ran independently of each other. E.g. clean data, get_histogram

    Other functions such as test_get_random_word is dependent on the get_random_word function to run
