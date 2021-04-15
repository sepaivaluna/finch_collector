class Finch:
    def __init__(self, name, family, description, age):
        self.name = name
        self.family = family
        self.description = description
        self.age = age


finches = [
    Finch(
        'Blue Finch', 'Thraupidae',
        'The blue finch is a small tanager originating in South America, specifically in Brazil and Bolivia. The males have a bright cobalt blue plumage, although after the molt the feathers have a rufous-brown hue with broad edges. Females, on the other hand, have a rufous brown upper plumage, with buffy white underparts marked with dusky streaks.',
        5),
    Finch(
        'Owl Finch', 'Estrildidae',
        'The owl finch, also known as the double-barred or Bicheno finch, is characterized by a dark patch around their face. It gives them a barn owl like appearance, gaining them the name ‘owl’ finch. The males and females of the species looks almost the same, whereas the young ones have a more brownish appearance.',
        4),
    Finch(
        'Zebra Finch', 'Estrildidae',
        'Zebra finch, commonly found in Central Australia, is a small gray-white bird with a thick, pointed triangular beak. Being a popular choice of pet, these birds have been bred in captivity for many years.',
        2)
]