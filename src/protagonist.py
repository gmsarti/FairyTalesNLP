from dataclasses import dataclass, field
from enum import Enum
from random import choice

class Race(Enum):
    HUMAN = "Human"
    ANIMAL = "Animal"

class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"
    NONBINARY = "Nonbinary"

class AgeCategory(Enum):
    KID = "Kid"
    YOUNG = "Young"
    ADULT = "Adult"
    OLD = "Old"

@dataclass
class FairytaleProtagonist:
    race: Race = field(default_factory=lambda: choice(list(Race)))
    name: str = None 
    gender: Gender = field(default_factory=lambda: choice(list(Gender)))
    age_category: AgeCategory = field(default_factory=lambda: choice(list(AgeCategory)))
    distinctive_characteristic: str = field(default_factory=lambda: choice(["Brave", "Clever", "Kind", "Curious", "Wise"]))

    animal_type: str = None  # For animal protagonists
    profession: str = None  # For non-kid human protagonists

    def __post_init__(self):
        if self.race == Race.HUMAN:
            self.generate_human_name()
        else:
            self.animal_type = choice(["Fox", "Owl", "Rabbit", "Bear", "Wolf"])

        if self.race == Race.HUMAN and self.age_category != AgeCategory.KID:
            self.profession = choice(["Farmer", "Blacksmith", "Baker", "Woodcutter", "Knight"])

    def generate_human_name(self):
        if self.gender == Gender.MALE:
            self.name = choice(["Jack", "Finn", "Henry", "Oliver"])
        elif self.gender == Gender.FEMALE:
            self.name = choice(["Alice", "Willow", "Sophia", "Emma"])
        else:  # Nonbinary
            self.name = choice(["Rowan", "Riley", "Charlie", "Alex"])



if __name__ == "__main__":
    hero = FairytaleProtagonist(name="Luna", gender=Gender.FEMALE, age_category=AgeCategory.YOUNG) 
    print(hero)
    print(f"\n\n{'='*30}\n\n")
    protagonist = FairytaleProtagonist()
    print(protagonist)
