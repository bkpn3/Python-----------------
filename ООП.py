class Human:
    def __init__(self, name, age, iq):
        self.name = name
        self.age = age
        self.iq = iq
    def showInfo(self):
        print('Я человек. Информация обо мне:', self.name, self.age, self.iq)
        
class Worker(Human):
    def __init__(self, name, age, iq, salary, dolznost, staz):
        super().__init__(name, age, iq)
        self.salary = salary
        self.dolznost = dolznost
        self.staz = staz
    def showInfo(self):
        print('Я человек - сотрудник. мои данные на работе:',
              'Имя', self.name, 'Возраст', self.age, 'IQ', self.iq, 'Зарплата:', self.salary, 'Должность', self.dolznost, 'Стаж:', self.staz)

class Student(Human):
    def __init__(self, name, age, iq, facultet, spec, group):
        super().__init__(name, age, iq)
        self.facultet = facultet
        self.spec = spec
        self.group = group
    def showInfo(self):
        print('Я человек - студент. мои данные на учебе:', 'Имя', self.name,
              'Возраст', self.age, 'IQ', self.iq, 'Факультет:', self.facultet, 'Специальность:', self.spec, 'Группа:', self.group) 
    


petia = Human('Петя', 20, 100)
vasia = Human('Вася', 32, 54)

kolya = Worker(name = 'Коля', age = 31, iq = 78, dolznost = 'Программист', salary = 60000, staz = 0.5)

sergei = Student(name = 'Сергей', age = 20, iq = 86, facultet = 'ФИТ', spec = 'автоматизация производства', group = 'АП-308')
vladimir = Student(name = 'Владимир', age = 30, iq = 75, facultet = 'ФИТ', spec = 'Радиоэлектроника', group = 'РТ-122')
alexei = Student(name = 'Алексей', age =25, iq = 66, facultet = 'ии', spec = 'ии', group = 'ии-308')


people = [sergei, vasia, petia, alexei, vladimir, kolya]
for person in people:
    person.showInfo()