import unittest
from enum import Enum
# from your_protagonist_file import FairytaleProtagonist, Race, Gender, AgeCategory  # Assuming your protagonist code is in 'your_protagonist_file.py'
from ..src.protagonist import FairytaleProtagonist, Race, Gender, AgeCategory


class TestFairytaleProtagonist(unittest.TestCase):

    def test_default_generation(self):
        protagonist = FairytaleProtagonist()

        # Assert race is generated
        self.assertIsNotNone(protagonist.race)
        self.assertIn(protagonist.race, Race)

        # Assert gender is generated 
        self.assertIsNotNone(protagonist.gender)
        self.assertIn(protagonist.gender, Gender)

        # ... Similar assertions for other default values

    def test_human_logic(self):
        protagonist = FairytaleProtagonist(race=Race.HUMAN)

        # Test name generation (might need multiple runs to cover)
        self.assertIsNotNone(protagonist.name) 
        if protagonist.gender == Gender.MALE:
            self.assertIn(protagonist.name, ["Jack", "Finn", "Henry", "Oliver"])
        # ... Similar checks for FEMALE and NONBINARY

        # Test profession logic
        if protagonist.age_category != AgeCategory.KID:
            self.assertIsNotNone(protagonist.profession)
        else:
            self.assertIsNone(protagonist.profession)

    def test_animal_logic(self):
        protagonist = FairytaleProtagonist(race=Race.ANIMAL)
        self.assertIsNotNone(protagonist.animal_type)
        self.assertIsNone(protagonist.name)
        self.assertIsNone(protagonist.profession)

    def test_customization(self):
        protagonist = FairytaleProtagonist(
            name="Luna", gender=Gender.FEMALE, age_category=AgeCategory.YOUNG
        )
        self.assertEqual(protagonist.name, "Luna")
        # ... similar tests for other customizations

if __name__ == '__main__':
    unittest.main()
