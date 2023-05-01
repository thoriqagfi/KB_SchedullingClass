class Data:
    ROOMS = [["R1", 25], ["R2", 45], ["R3", 35], ["R4", 50], ["R5", 30]]
    MEETING_TIMES = [["MT1", "MWF 09:00 - 10:00"], ["MT2", "MWF 10:00 - 11:00"], ["MT3", "TTH 09:00 - 10:30"], ["MT4", "TTH 10:30 - 12:00"]]
    INSTRUCTORS = [["I1", "Dr James Web"], ["I2", "Mr Mike Brown"], ["I3", "Dr Steve Day"], ["I4", "Mrs Jane Doe"]]
    DEPARTMENTS = [["D1", "Computer Science", [ "CSC 101", "CSC 103", "CSC 105", "CSC 203", "CSC 301", "CSC 399", "CSC 499"]],
                    ["D2", "Mechanical Engineering", ["ME 101", "ME 203", "ME 399", "ME 499"]],
                    ["D3", "Civil Engineering", ["CE 101", "CE 203", "CE 399", "CE 499"]],
                    ["D4", "Electrical Engineering", ["EE 101", "EE 203", "EE 399", "EE 499"]]]
    COURSES = [["CSC 101", "Introduction to Computer Science", "I1", 25, 4, []],
                ["CSC 103", "Web Programming", "I1", 25, 4, ["CSC 101"]],
                ["CSC 105", "Advanced Programming", "I1", 25, 4, ["CSC 101"]],
                ["CSC 203", "Data Structures", "I1", 25, 4, ["CSC 103", "CSC 105"]],
                ["CSC 301", "Algorithms", "I1", 25, 4, ["CSC 203"]],
                ["CSC 399", "Introduction to AI", "I1", 25, 4, ["CSC 203"]],
                ["CSC 499", "Machine Learning", "I1", 25, 4, ["CSC 399"]],
                ["ME 101", "Introduction to Mechanical Engineering", "I2", 45, 4, []],
                ["ME 203", "Mechanical Engineering Design", "I2", 45, 4, ["ME 101"]],
                ["ME 399", "Introduction to Robotics", "I2", 45, 4, ["ME 203"]],
                ["ME 499", "Advanced Robotics", "I2", 45, 4, ["ME 399"]],
                ["CE 101", "Introduction to Civil Engineering", "I3", 35, 4, []],
                ["CE 203", "Civil Engineering Design", "I3", 35, 4, ["CE 101"]],
                ["CE 399", "Introduction to Environmental Engineering", "I3", 35, 4, ["CE 203"]],
                ["CE 499", "Advanced Environmental Engineering", "I3", 35, 4, ["CE 399"]],
                ["EE 101", "Introduction to Electrical Engineering", "I4", 30, 4, []],
                ["EE 203", "Electrical Engineering Design", "I4", 30, 4, ["EE 101"]],
                ["EE 399", "Introduction to Power Systems", "I4", 30, 4, ["EE 203"]],
                ["EE 499", "Advanced Power Systems", "I4", 30, 4, ["EE 399"]]]
    def __init__(self):
        self._rooms = []; self._meetingTimes = []; self._instructors = []; self._depts = []; self._courses = []
        for i in range(0, len(self.ROOMS)):
            self._rooms.append(Room(self.ROOMS[i][0], self.ROOMS[i][1]))
        for i in range(0, len(self.MEETING_TIMES)):
            self._meetingTimes.append(MeetingTime(self.MEETING_TIMES[i][0], self.MEETING_TIMES[i][1]))
        for i in range(0, len(self.INSTRUCTORS)):
            self._instructors.append(Instructor(self.INSTRUCTORS[i][0], self.INSTRUCTORS[i][1]))
        for i in range(0, len(self.DEPARTMENTS)):
            self._depts.append(Department(self.DEPARTMENTS[i][0], self.DEPARTMENTS[i][1], self.DEPARTMENTS[i][2]))
        for i in range(0, len(self.COURSES)):
            self._courses.append(Course(self.COURSES[i][0], self.COURSES[i][1], self._findInstructor(self.COURSES[i][2]), self.COURSES[i][3], self.COURSES[i][4], self._findCourses(self.COURSES[i][5])))
        deptIndex = 0
        for i in range(0, len(self.COURSES)):
            deptIndex = self._findDept(self.COURSES[i][0])
            if (deptIndex != -1):
                self._depts[deptIndex].addCourse(self._courses[len(self._courses) - 1])
    def _findInstructor(self, instructorId):
        for i in range(0, len(self._instructors)):
            if (instructorId == self._instructors[i].getId()):
                return self._instructors[i]
        return None
    def _findDept(self, courseId):
        for i in range(0, len(self._depts)):
            if (courseId == self._depts[i].getId()):
                return i
        return -1
    def _findCourses(self, courseIds):
        courses = []
        for i in range(0, len(courseIds)):
            for j in range(0, len(self._courses)):
                if (courseIds[i] == self._courses[j].getNumber()):
                    courses.append(self._courses[j])
        return courses
    def getRooms(self): return self._rooms
    def getMeetingTimes(self): return self._meetingTimes
    def getInstructors(self): return self._instructors
    def getDepts(self): return self._depts
    def getCourses(self): return self._courses
class Schedule:
    ''' '''
class Population:
    ''' '''
class GeneticAlgorithm:
    ''' '''
class Course:
    def __init__(self, number, name, instructor, maxNumberOfStudents, numberOfMeetings, prerequisites):
        self._number = number
        self._name = name
        self._instructor = instructor
        self._maxNumberOfStudents = maxNumberOfStudents
        self._numberOfMeetings = numberOfMeetings
        self._prerequisites = prerequisites
    def getNumber(self):
        return self._number
    def getName(self):
        return self._name
    def getInstructor(self):
        return self._instructor
    def getMaxNumberOfStudents(self):
        return self._maxNumberOfStudents
    def getNumberOfMeetings(self):
        return self._numberOfMeetings
    def getPrerequisites(self):
        return self._prerequisites
    def __str__(self):
        return str(self._number) + "," + str(self._name) + "," + str(self._instructor) + "," + str(self._maxNumberOfStudents) + "," + str(self._numberOfMeetings) + "," + str(self._prerequisites)
class Instructor:
    def __init__(self, name, department):
        self._name = name
        self._department = department
    def getName(self):
        return self._name
    def getDepartment(self):
        return self._department
    def __str__(self):
        return str(self._name) + "," + str(self._department)
class Room:
    def __init__(self, number, seatingCapacity):
        self._number = number
        self._seatingCapacity = seatingCapacity
    def getNumber(self):
        return self._number
    def getSeatingCapacity(self):
        return self._seatingCapacity
    def __str__(self):
        return str(self._number) + "," + str(self._seatingCapacity)
class MeetingTime:
    def __init__(self, id, time):
        self._id = id
        self._time = time
    def getId(self):
        return self._id
    def getTime(self):
        return self._time
class Department:
    def __init__(self, name, courses):
        self._name = name
        self._courses = courses
    def getName(self):
        return self._name
    def getCourses(self):
        return self._courses
class Class:
    def __init__(self, id, dept, course):
        self._id = id
        self._dept = dept
        self._course = course
        self._instructor = None
        self._meetingTime = None
        self._room = None
    def getClassId(self):
        return self._id
    def getDept(self):
        return self._dept
    def getCourse(self):
        return self._course
    def getInstructor(self):
        return self._instructor
    def getMeetingTime(self):
        return self._meetingTime
    def getRoom(self):
        return self._room
    def setInstructor(self, instructor):
        self._instructor = instructor
    def setMeetingTime(self, meetingTime):
        self._meetingTime = meetingTime
    def setRoom(self, room):
        self._room = room
    def __str__(self):
        return str(self._dept.name) + "," + str(self._course.number) + "," + \
               str(self._room.number) + "," + str(self._instructor.name) + "," + str(self._meetingTime.time)