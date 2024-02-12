from KRIS_CALLIER_Plant import Plant


class Tree(Plant):
    """A class representing a tree, which is a subclass of Plant."""

    def __init__(self, species, height, num_leaves):
        """
        Initialize a new Tree object with a given species, height, and number of leaves.

        :param species: The species of the tree
        :type species: str
        :param height: The height of the tree in inches
        :type height: float
        :param num_leaves: The number of leaves on the tree
        :type num_leaves: int
        """
        super().__init__(species, height)
        self.num_leaves = num_leaves

    def __str__(self):
        """
        Return a string representation of the Tree object.

        :return: A string representation of the Tree object
        :rtype: str
        """
        return f"Tree species: {self.species}, height: {self.height} inches, number of leaves: {self.num_leaves}"

    def grow(self, growth_rate):
        """
        Grow the tree by a certain amount based on the given growth rate.

        :param growth_rate: The rate at which the tree should grow, either 'slow' or 'fast'
        :type growth_rate: str
        """
        if growth_rate == "slow":
            self.height += 10.0
        elif growth_rate == "fast":
            self.height += 20.0

    def fall(self):
        """
        Cause the tree to lose all of its leaves.
        """
        self.num_leaves = 0


if __name__ == "__main__":
    # Create an instance of Plant
    print("Flower Instance")
    p = Plant("Flower", 10)
    print(p)
    p.grow("slow")
    print("Height")
    print(p.height)
    print()

    print("Trees:")
    # Create two instances of Tree
    t1 = Tree("Oak", 60.0, 1000)
    t2 = Tree("Pine", 40.0, 500)

    # Test the methods of Tree
    print("Tree one instance:")
    print(t1)
    t1.grow("slow")
    print("Tree Height")
    print(t1.height)
    t1.fall()
    print("Number of Leaves")
    print(t1.num_leaves)
    print()
    print("Tree two instance:")
    print(t2)
    t2.grow("fast")
    print("Tree Height")
    print(t2.height)
    t2.fall()
    print("Number of Leaves")
    print(t2.num_leaves)




