# Import the Plant class from YOUR_NAME_plant.py file
from KRIS_CALLIER_Plant import Plant


# Define the Flower class
class Flower(Plant):
    def __init__(self, species, height, color):
        super().__init__(species, height)  # call the Plant class constructor
        self.color = color

    def __str__(self):
        return f"{self.species}, {self.height} inches, {self.color}"

    def bloom(self):
        print(f"The flower is blooming in {self.color} color.")


# If name main block
if __name__ == '__main__':
    # Create an instance of the Plant class
    plant = Plant("Some species", 10.5)

    # Print the instance of Plant class
    # Import the Plant class from YOUR_NAME_plant.py file
    from KRIS_CALLIER_Plant import Plant


    # Define the Flower class
    class Flower(Plant):
        def __init__(self, species, height, color):
            """
            Constructor of Flower class.

            Initialize all of the Flower class attributes and call the constructor of the Plant class.

            Args:
            - species: string representing the species of the flower
            - height: float representing the height in inches of the flower
            - color: string representing the color of the flower
            """
            super().__init__(species, height)  # call the Plant class constructor
            self.color = color

        def __str__(self):
            """
            Override the Plant's __str__ method to create a string with all of the attributes of the Flower class.

            Returns:
            - A string representation of the Flower object containing the species, height, and color attributes.
            """
            return f"{self.species}, {self.height} inches, {self.color}"

        def bloom(self):
            """
            Display the color of the flower to represent the flower "blooming".

            Returns:
            - None
            """
            print(f"The flower is blooming in {self.color} color.")


    # If name main block
    if __name__ == '__main__':
        # Create an instance of the Plant class
        plant = Plant("Some species", 10.5)

        # Print the instance of Plant class
        print(plant)

        # Display the height of the plant
        print(f"Height: {plant.height} inches")

        # Call the grow method
        plant.grow(5)

        # Display the height of the plant after growth
        print(f"Height after growth: {plant.height} inches")

        # Create two instances of the Flower class
        flower1 = Flower("Rose", 6.7, "Red")
        flower2 = Flower("Lily", 12.3, "White")

        # Print each instance of the Flower class
        print(flower1)
        print(flower2)

        # Call the bloom method for each flower instance
        flower1.bloom()
        flower2.bloom()

        # Display the height of each flower instance
        print(f"Height of {flower1.species}: {flower1.height} inches")
        print(f"Height of {flower2.species}: {flower2.height} inches")

        # Call the grow method for each flower instance
        flower1.grow(3.2)
        flower2.grow(7.1)

        # Display the height of each flower instance after growth
        print(f"Height of {flower1.species} after growth: {flower1.height} inches")
        print(f"Height of {flower2.species} after growth: {flower2.height} inches")
