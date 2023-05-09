class Dog(object):
    def work(self):
        print('指哪里咬哪里')


class drug_dog():
    def work(self):
        print('毒品在哪里！')


class Army_Dog():
    def work(self):
        print('击退敌人')


class person():
    def work_with_dog(self, dog):
        dog.work()

DrugDog = drug_dog()
ArmyDog = Army_Dog()

man = person()
man.work_with_dog(DrugDog)