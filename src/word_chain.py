def check_max_word_chain_length(input_path: str, output_path: str):
    num_of_words, words = read_input_file(input_path)
    if num_of_words != len(words):
        write_output_file(output_path, -1)
        return

    if num_of_words == 0:
        write_output_file(output_path, 0)
        return

    words.sort(key=len, reverse=True)

    word_chains_length = {word: 1 for word in words}

    for word in words:
        for i in range(len(word)):
            new_word = word[0:i] + word[i+1:]
            if new_word not in word_chains_length:
                continue
            word_chains_length[new_word] = max(
                word_chains_length[word] + 1, word_chains_length[new_word]
            )

    write_output_file(output_path, max(word_chains_length.values()))


def read_input_file(input_path: str):
    with open(input_path, "r", encoding="utf-8") as file:
        num_of_words = int(file.readline())
        words = [file.readline().strip("\n") for _ in range(num_of_words)]
    return num_of_words, list(filter(None, words))


def write_output_file(output_path: str, output: int):
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(str(output))
