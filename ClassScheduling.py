from datetime import datetime
import random

# read the courses from the file
with open("tc.txt") as f:
    courses = [line.strip().split(",") for line in f.readlines()[1:]]

# create a list of course ids
course_ids = list(set([course[0] for course in courses]))
course_names = list(set([course[1] for course in courses]))

# create a dictionary of course schedules
schedules = {}
for course_id in course_ids:
    course_schedules = [course[2:] for course in courses if course[0] == course_id]
    schedules[course_id] = course_schedules

# dict of courses_names : courses_ids
courses_name_dict = {}
for name in course_names:
    for course in courses:
        if course[1] == name:
            courses_name_dict[name] = course[0]
            break
        
# dict of course_ids : courses_names
courses_id_dict = {}
for id in course_ids:
    for course in courses:
        if course[0] == id:
            courses_id_dict[id] = course[1]
            break

def coursesOverlap(individual: dict) -> dict:
    """
    Memeriksa apakah ada mata kuliah yang bertabrakan\n
    Fungsi ini akan dipanggil jika individual terbaik memiliki jadwal yang bertabrakan
    """
    res = {}
    position = 1
    for i in individual:
        day1, time1 = individual[i][0], individual[i][1]
        restOfIndividual = list(individual)[position:]
        for j in restOfIndividual:
            day2, time2 = individual[j][0], individual[j][1]
            if day1 == day2 and overlapping_hours(time1, time2):
                res[i] = individual[i]
                res[j] = individual[j]
        
        position += 1

    return res

def fitness_function(individual: dict) -> int:
    """
    Mengkalkulasi nilai fitness function dari sebuah individual\n
    Fitness function yang digunakan adalah banyak mata kuliah yang bertabrakan dalam sebuah individual
    """
    overlapping, position = 0, 1
    for i in individual.values():
        day1, time1 = i[0], i[1]
        restOfIndividual = list(individual.values())[position:]
        for j in restOfIndividual:
            day2, time2 = j[0], j[1]
            if day1 == day2 and overlapping_hours(time1, time2):
                overlapping += 1
            
        position += 1
            
    return len(individual) - overlapping

def overlapping_hours(time1, time2) -> bool:
    """
    Memeriksa jika dua kelas bertabrakan waktu
    """
    start1, end1 = [datetime.strptime(str(h), "%H:%M").time() for h in time1.split("-")]
    start2, end2 = [datetime.strptime(str(h), "%H:%M").time() for h in time2.split("-")]

    return not (end1 <= start2 or end2 <= start1)

def generate_individual(courseList: list) -> dict:
    """
    Menghasilkan populasi awal\n
    Fungsi ini dipanggil di awal Genetic Algorithm dijalankan
    """
    res = {}
    for i in courseList:
        courseId = courses_name_dict[i]
        classesSchedule = random.sample(schedules[courseId], 1)[0]
        res[courseId] = classesSchedule
        
    return res

def mutate(individual: dict, mutation_rate: int) -> dict:
    """
    Melakukan mutasi pada semua DNA individual\n
    Melakukan random.random() untuk menghasilkan nilai random
    dan jika nilai random.random() < mutation_rate, maka DNA tersebut dilakukan mutasi.
    """
    for i in individual:
        if random.random() < mutation_rate:
            new_course = random.choice(schedules[i])
            individual[i] = new_course

    return individual

def crossover(parent1, parent2) -> dict:
    """
    Menghasilkan anak baru dari parent1 dan parent2\n
    Sama seperti mutate(), dilakukan random.random(), jika nilai
    random.random() kurang dari 0.5, maka DNA dari parent1 akan diambil dan sebaliknya
    jika random.random() lebih dari 0.5
    """
    child = {}
    for i in parent1.keys():
        if random.random() < 0.5:
            child[i] = parent1[i]
        else:
            child[i] = parent2[i]
    
    return child

def select_parents(population):
    """
    Mengambil parent dari sebuah populasi menggunakan function tournamen_selection()
    """
    parent1 = tournament_selection(population)
    parent2 = tournament_selection(population)

    return parent1, parent2

def tournament_selection(population, tournament_size=5) -> dict:
    """
    Mengambil individual sebanyak tournament_size dari sebuah population\n
    Dari individual yang diambil dilakukan kembali fitness function
    kemudian individual dengan nilai fitness tertinggi akan diambil
    """
    tournament = random.sample(population, tournament_size)
    tournament.sort(key=lambda x: fitness_function(x), reverse=True)

    return tournament[0]

def genetic_algorithm(courseList, population_size=20, generations=20, mutation_rate=0.5) -> None:
    """
    Menjalankan Genetic Algorithm
    """
    population = [generate_individual(courseList) for _ in range(population_size)]

    option = []
    for generation in range(generations):
        population.sort(key=lambda x: fitness_function(x), reverse=True)
        print("Generation:", generation, "Best Fitness:", fitness_function(population[0]), "Best Individual:", population[0])
        new_population = [population[0]]
        while len(new_population) < population_size:
            parent1, parent2 = select_parents(population)
            child = crossover(parent1, parent2)
            mutate(child, mutation_rate)
            new_population.append(child)
        population = new_population
    population.sort(key=lambda x: fitness_function(x), reverse=True)
    for i in population:
        if fitness_function(i) == len(courseList) and i not in option:
            option.append(i)
    if fitness_function(population[0]) == len(courseList):
        print("Final Population Best Fitness:", fitness_function(population[0]), "\nFinal Population Best Individual:", population[0])
    else:
        print("There is one or more class that overlap:")
        print(coursesOverlap(population[0]))

    return option