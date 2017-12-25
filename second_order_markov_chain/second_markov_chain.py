def get_histogram(word_list):
    result = {}
    for index, word in enumerate(word_list):
        try:
            next_word = word_list[index + 1]
            after_next = word_list[index + 2]
            next_state = next_word + ' ' + after_next
        except:
            break

        if word not in result:

            result[word] = {next_state: 1} # Implement as tuple or string

        else:

            if next_state not in result[word]:

                result[word].update({next_state: 1})

            else:
                 result[word][next_state] += 1
    return result