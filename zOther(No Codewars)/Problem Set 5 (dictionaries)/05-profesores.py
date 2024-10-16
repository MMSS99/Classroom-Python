courses = {
    'feb2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Peter C.'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian',
                           'assistant': 'Andy'}},
    'apr2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Sarah'},
                 'cs212': {'name': 'The Design of Computer Programs',
                           'teacher': 'Peter N.',
                           'assistant': 'Andy',
                           'prereq': 'cs101'},
                 'cs253': {'name': 'Web Application Engineering - Building a Blog',
                           'teacher': 'Steve',
                           'prereq': 'cs101'},
                 'cs262': {'name': 'Programming Languages - Building a Web Browser',
                           'teacher': 'Wes',
                           'assistant': 'Peter C.',
                           'prereq': 'cs101'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian'},
                 'cs387': {'name': 'Applied Cryptography',
                           'teacher': 'Dave'}},
    'jan2044': { 'cs001': {'name': 'Building a Quantum Holodeck',
                           'teacher': 'Dorina'},
                 'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                           'teacher': 'Jasper'},
                     }
    }


def involved(courses, person):
    cursosprofesor = {}
    for hexamestre in courses:
        for curso in courses[hexamestre]:
            if person in courses[hexamestre][curso].values():
                if not hexamestre in cursosprofesor:
                    cursosprofesor[hexamestre] = [curso]
                else:
                    cursosprofesor[hexamestre] = cursosprofesor[hexamestre] + [curso]
    return cursosprofesor




print (involved(courses, 'Dave'))
# => {'apr2012': ['cs101', 'cs387'], 'feb2012': ['cs101']}
print (involved(courses, 'Peter C.'))
# => {'apr2012': ['cs262'], 'feb2012': ['cs101']}
print (involved(courses, 'Dorina'))
# => {'jan2044': ['cs001']}