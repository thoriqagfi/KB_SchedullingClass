from datetime import datetime
import random

# read the courses from the file
with open("schedule.txt") as f:
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

def fitness_function(individual) -> int:
    """
    Calculate the fitness value of an individual, which represents the number of non-overlapping courses
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
    Check if two courses schedules overlap
    """
    start1, end1 = [datetime.strptime(str(h), "%H:%M").time() for h in time1.split("-")]
    start2, end2 = [datetime.strptime(str(h), "%H:%M").time() for h in time2.split("-")]

    return not (end1 <= start2 or end2 <= start1)

def generate_individual(courseList) -> dict:
    """
    Generate a random individual
    """
    res = {}
    for i in range(len(courseList)):
        courseId = courses_name_dict[courseList[i]]
        classesSchedule = random.sample(schedules[courseId], 1)[0]
        res[courseId] = classesSchedule
        
    return res

def mutate(individual) -> dict:
    """
    Mutate an individual by randomly replacing a course with another
    """
    course_to_replace = random.choice(list(individual.keys()))
    new_course = random.choice(schedules[course_to_replace])
    individual[course_to_replace] = new_course

    return individual

def crossover(parent1, parent2) -> dict:
    """
    Create a new individual by randomly selecting courses from the two parents
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
    Select two parents from the population using tournament selection
    """
    parent1 = tournament_selection(population)
    parent2 = tournament_selection(population)

    return parent1, parent2

def tournament_selection(population, tournament_size=5) -> dict:
    """
    Select an individual from the population using tournament selection
    """
    tournament = random.sample(population, tournament_size)
    tournament.sort(key=lambda x: fitness_function(x), reverse=True)

    return tournament[0]

def genetic_algorithm(courseList, population_size=100, generations=10, mutation_rate=0.5):
    """
    Run the genetic algorithm to find the best combination of courses
    """
    population = [generate_individual(courseList) for _ in range(population_size)]
    for generation in range(generations):
        population.sort(key=lambda x: fitness_function(x), reverse=True)
        print("Generation:", generation, "Best Fitness:", fitness_function(population[0]), "Best Individual:", population[0])
        new_population = [population[0]]
        while len(new_population) < population_size:
            parent1, parent2 = select_parents(population)
            child = crossover(parent1, parent2)
            if random.random() < mutation_rate:
                child = mutate(child)
            new_population.append(child)
        population = new_population
    population.sort(key=lambda x: fitness_function(x), reverse=True)
    print("Final Population Best Fitness:", fitness_function(population[0]), "Final Population Best Individual:", population[0])

List = ["Data Structures and Algorithms", "Artificial Intelligence"]
genetic_algorithm(List)