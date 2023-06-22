import matplotlib.pyplot as plt


def plot_words(word_counts, n=10):
    """
    plot a bar chart of word counts.

    Parameters
    ----------
    word_counts : Counter
        uniques words with their presedence
    n : int, optional
        number of most common words, by default 10

    Returns
    -------
    _type_
        plot to be shown.
    """
    top_n_words = word_counts.most_common(n)
    word, count = zip(*top_n_words)
    fig = plt.bar(range(n), count)
    plt.xticks(range(n), labels=word, rotation=45)
    plt.xlabel("Word")
    plt.ylabel("Count")
    return fig
