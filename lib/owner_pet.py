class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None) -> None:
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    def get_pet_type(self):
        return self._pet_type
    def set_pet_type(self, pet_type):
        if pet_type in Pet.PET_TYPES:
            self._pet_type = pet_type
        else:
            raise Exception()
    pet_type = property(get_pet_type, set_pet_type)


    def __repr__(self):
        return self.name


class Owner:
    def __init__(self, name) -> None:
        self.name = name
        self.pet_list = []

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception()
        
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)