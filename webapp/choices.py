from dj.choices import Choices, Choice

class Category(Choices):
    normal = Choice("Pizza Normal")
    premium = Choice("Pizza Premium")
    sweet = Choice("Pizza Doce")



