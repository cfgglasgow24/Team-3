import json, random

class Question:

    def __init__(self, letter : str = None) -> None:
        """Represents a Question

        Attributes
        -----------
        letter: :class:`str`
            The questions letter
        button_numbers: :class:`int`
            The buttons corresponding to the correct answer
        asset: :class:`str`
            The path to the image asset
        description: :class:`str`
            The description of the correct answer
        """

        if letter == None:
            return

        self.letter = letter

        with open("static/questions.json", "r", encoding="UTF-8") as f:
            questions = json.load(f)

        if self.letter not in questions:
            raise ValueError(f"{self.letter} does not exist as a registered letter!")
        
        self.button_number = questions[self.letter]["button_number"]
        self.asset = questions[self.letter]["asset"]
        self.description = questions[self.letter]["description"]
    
    @classmethod
    def get_random_letter(cls) -> str:
        """ Class method to get a random letter. """

        with open("static/questions.json", "r", encoding="UTF-8") as f:
            questions = json.load(f)
        
        return random.choice(list(questions.keys()))

    @classmethod
    def add_question(cls, letter : str, button_number : int, asset : str, description : str) -> None:
        """ A class method to add a question into the questions.json file. """

        with open("static/questions.json", "r", encoding="UTF-8") as f:
            questions = json.load(f)
        
        if letter in questions:
            raise ValueError(f"{letter} already exists in the file.")
        
        questions[letter.lower()] = {}
        questions[letter.lower()]["button_numbers"] = button_number
        questions[letter.lower()]["asset"] = asset
        questions[letter.lower()]["description"] = description

        with open("static/questions.json", "w", encoding="UTF-8") as f:
            json.dump(questions,f)
    
    @classmethod
    def delete_question(cls, letter : str) -> None:
        """ A class method to delete a specific question in the file. """

        with open("static/questions.json", "r", encoding="UTF-8") as f:
            questions = json.load(f)

        letter = letter.lower()

        if letter not in questions:
            raise ValueError("No such question exists!")
        
        del questions[letter]

        with open("static/questions.json", "w", encoding="UTF-8") as f:
            json.dump(questions,f)