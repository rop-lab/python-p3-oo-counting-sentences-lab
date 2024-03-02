import re

class MyString:
    def __init__(self, value=''):
        # Verify that the value is a string before assigning it
        if not isinstance(value, str):
            raise ValueError("The value must be a string.")
        self.value = value

    def is_sentence(self):
        """Returns True if the value ends in a period, False otherwise."""
        return self.value.endswith('.')

    def is_question(self):
        """Returns True if the value ends with a question mark, False otherwise."""
        return self.value.endswith('?')

    def is_exclamation(self):
        """Returns True if the value ends with an exclamation mark, False otherwise."""
        return self.value.endswith('!')

    def count_sentences(self):
        """
        Returns the count of sentences in the value.

        It splits the value on '.', '!', and '?' and eliminates empty strings from the list.
        """
        sentences = [sentence for sentence in re.split('[.!?]', self.value) if sentence]
        return len(sentences)

# Example usage:
try:
    string = MyString("This is a string! It has three sentences. Right?")
    print("Is a sentence?", string.is_sentence())        # Output: True
    print("Is a question?", string.is_question())        # Output: False
    print("Is an exclamation?", string.is_exclamation())  # Output: True
    print("Count of sentences:", string.count_sentences()) # Output: 3
except ValueError as e:
    print(f"Error: {e}")
