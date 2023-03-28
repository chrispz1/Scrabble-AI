import numpy as np

while(True):



    # Define the transition matrix
    transition_matrix = np.array([[0.2, 0.8],
                                  [0.6, 0.4]])

    # Define the list of characters
    characters = ['a', 'b']

    # Define the initial state distribution
    initial_state = np.array([0.5, 0.5])

    # Define the length of the word to be generated
    word_length = 5

    # Initialize the current state
    current_state = np.random.choice(len(characters), p=initial_state)

    # Generate the word
    word = characters[current_state]
    for i in range(word_length - 1):
        current_state = np.random.choice(len(characters), p=transition_matrix[current_state])
        word += characters[current_state]

    print(word)
    input()
