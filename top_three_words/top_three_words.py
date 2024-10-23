import re


def top_three_words_extractor(text):
    # Find words that include letters and apostrophes
    words = re.findall(r"[a-zA-Z']+", text.lower())
    words_dict = {}

    for word in words:
        if len(word) > 1 or (len(word) == 1 and word != "'"):  # Ignore single apostrophes
            words_dict[word] = words_dict.get(word, 0) + 1

    # Sort the dictionary by word count in descending order
    sorted_dict = sorted(words_dict.items(), key=lambda item: item[1], reverse=True)

    # Return the top 3 words as a list
    return [key[0] for key in sorted_dict[:3]]
