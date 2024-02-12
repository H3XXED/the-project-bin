class Plant:
    def __init__(self, species: str, height: float):
        self.species = species
        self.height = height

    def __str__(self):
        return f"{self.species}  {self.height} inches tall"

    def grow(self, speed: str):
        if speed == "slow":
            self.height += 1
        elif speed == "fast":
            self.height += 2


# Example usage:
if __name__ == '__main__':
    # create three instances of the class Plant
    p1 = Plant("Orchid", 3.0)

    p2 = Plant("Sunflower", 7.2)

    p3 = Plant("Basil", 2.5)

    # print each class instance
    v = '***Original***'
    print(v.rjust(18))
    print(p1)
    print('****************************')
    print(p2)
    print('****************************')
    print(p3)
    print('****************************')
    s = '***Growth Rates***'
    print(s.rjust(20))

    # call the grow method for each class instance
    for p in [p1, p2, p3]:
        print(p)
        print(f"Before growth: {p.height}")
        p.grow("slow")
        print(f"After slow growth: {p.height}")
        p.grow("fast")
        print(f"After fast growth: {p.height}")
        print('****************************')
