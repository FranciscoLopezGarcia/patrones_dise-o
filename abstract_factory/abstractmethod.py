from animal_factory import DogFactory, CatFactory

def main():
    dog_factory = DogFactory()
    dog = dog_factory.create_animal("dog")
    dog.make_sound()

    cat_factory = CatFactory()
    cat = cat_factory.create_animal("cat")
    cat.make_sound()

if __name__ == "__main__":
    main()
