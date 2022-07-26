class Pet():
    def __init__(self, xxx: str):
        self.type = xxx

    def get_type(self):
        return self.type


class Cat(Pet):
    def __init__(self):
        super().__init__('Cat')


class Dog(Pet):
    def __init__(self):
        super().__init__('Dog')


class EnterPetQueue():
    def __init__(self, pet, count):
        self.pet = pet
        self.count = count

    def get_pet(self):
        return self.pet

    def get_count(self):
        return self.count

    def get_enter_pet_type(self):
        return self.pet.get_type()


class DogCatQueue():
    def __init__(self):
        self.dogQ = []
        self.catQ = []
        self.count = 0

    def add(self, pet):
        if "Dog".__eq__(pet.get_type()):
            self.dogQ.append(EnterPetQueue(Dog(), self.count))
            self.count += 1
        elif "Cat".__eq__(pet.get_type()):
            self.catQ.append(EnterPetQueue(Cat(), self.count))
            self.count += 1
        else:
            raise RuntimeError("error,not dog or cat")

    def poll_all(self):
        if (not self.is_dog_empty()) and (not self.is_cat_empty()):
            if self.dogQ[0].get_count() < self.catQ[0].get_count():
                return self.dogQ.pop(0)
            else:
                return self.catQ.pop(0)
        elif not self.is_dog_empty():
            return self.dogQ.pop(0)
        elif not self.is_cat_empty():
            return self.catQ.pop(0)
        else:
            raise RuntimeError("your queue is empty")

    def poll_dog(self):
        if not self.is_dog_empty():
            return self.dogQ.pop(0)
        else:
            raise RuntimeError("your dog queue is empty")

    def poll_cat(self):
        if not self.is_cat_empty():
            return self.catQ.pop(0)
        else:
            raise RuntimeError("your cat queue is empty")

    def is_empty(self):
        return len(self.dogQ) == 0 and len(self.catQ) == 0

    def is_dog_empty(self):
        return len(self.dogQ) == 0

    def is_cat_empty(self):
        return len(self.catQ) == 0


if __name__ == '__main__':
    test = DogCatQueue()
    dog1=Dog()
    dog2=Dog()
    dog3=Dog()
    cat1=Cat()
    cat2=Cat()
    cat3=Cat()

    test.add(dog1)
    test.add(cat1)
    test.add(dog2)
    test.add(cat2)
    test.add(dog3)
    test.add(cat3)

    test.add(dog1)
    test.add(cat1)
    test.add(dog2)
    test.add(cat2)
    test.add(dog3)
    test.add(cat3)

    test.add(dog1)
    test.add(cat1)
    test.add(dog2)
    test.add(cat2)
    test.add(dog3)
    test.add(cat3)

    print("=========")
    # print(test.is_empty())
    # while not test.is_empty():
    #     print(test.poll_all().get_enter_pet_type())
    #
    # print(test.is_empty())
    print("=========")
    while not test.is_dog_empty():
        print(test.poll_dog().get_enter_pet_type())
    print("=========")
    while not test.is_cat_empty():
        # print(test.poll_cat().get_type())
        # 无法调用返回Pet类型，这个类型中无get_type()方法（不知如何向下转型（python不知））
        print(test.poll_cat().get_enter_pet_type())

