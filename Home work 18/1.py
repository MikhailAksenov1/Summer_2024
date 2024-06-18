"""Разработать систему решения задач учениками курса «Разработчик на Питоне» и
проверке их преподавателем.
1. Преподаватель каждый урок задает некоторое количество задач в качестве
домашнего задания, для упрощения можно считать, что одну. Посылает их
каждому ученику.
2. Каждый ученик решает каждую задачу, переводит ее статус в решенную и
посылает решение преподавателю.
3. Преподаватель проверяет каждую задачу каждого ученика и подтверждает ее
статус как решенную или меняет ее статус на нерешенную, и посылает
результаты ученику.
• Разработайте систему классов (Teachers, Pupils). Можно создать другие классы,
например, Tasks.
• Разработайте систему атрибутов для каждого класса для хранения и
использования описанных процессов.
• Разработайте систему методов для каждого класса для реализации описанных
процессов.
• Проверьте ее работу на одном учителе и на 2-3 учениках."""


class Home_work:
    def __init__(self, sp_work, status=0):
        self.sp_work = sp_work
        self.status = status


class Teacher:
    def __init__(self):
        self.home_work = []

    def teach_ind(self, pupil, hw):
        hw.status = 0
        pupil.take(hw)

    def check_hm(self, pupil, hw, status):
        hw.status = status
        pupil.take(hw)

    def got_hw(self, pupil, hw):
        self.home_work.append({pupil.name: hw})


class Pupil:
    def __init__(self, name):
        self.name = name
        self.hw = []

    def take(self, hw):
        self.hw.append(hw)

    def send(self, hw, teacher, status):
        hw.status = status
        teacher.got_hw(self, hw)


hw = Home_work('object')
hw2 = Home_work('encapsulation')
t = Teacher()

p1 = Pupil('Mikhail')
t.teach_ind(p1, hw2)
p1.send(hw2, t, 1)
t.check_hm(p1, hw2, 1)
print(p1.name, p1.hw[0].sp_work, p1.hw[0].status)

p2 = Pupil('Kolya')
t.teach_ind(p2, hw)
p2.send(hw, t, 1)
t.check_hm(p2, hw, 1)
print(p2.name, p2.hw[0].sp_work, p2.hw[0].status)

p3 = Pupil('Vasya')
t.teach_ind(p3, hw)
p3.send(hw, t, 0)
t.check_hm(p3, hw, 0)
print(p3.name, p3.hw[0].sp_work, p3.hw[0].status)