# Python Journey - Chapter 20
# Quizz file program

import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',\
    'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',\
    'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',\
    'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':\
    'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':\
    'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':\
    'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':\
    'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':\
    'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':\
    'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New\
    Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',\
    'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',\
    'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',\
    'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':\
    'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':\
    'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West\
    Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Generate 35 quiz files.
for quiz in range(35):
    # TODO: Create the quiz and answer key files.
    quiz_file = open('capitalsquiz%s.txt' % (quiz + 1), 'w')
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quiz + 1), 'w')

    # TODO: Write out the header for the quiz.
    quiz_file.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quiz_file.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quiz + 1))
    quiz_file.write('\n\n')

    # TODO: Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)

    # TODO: Loop through all 50 states, making a question for each.
    for question in range(50):
        # Get right and wrong answers.
        correct_answer = capitals[states[question]]
        wrong_answers = list(capitals.values())
        del wrong_answers[wrong_answers.index(correct_answer)]
        wrong_answers = random.sample(wrong_answers, 3)
        answer_options = wrong_answers + [correct_answer]
        random.shuffle(answer_options)

        # TODO: Write the question and answer options to the quiz file.

        # TODO: Write the answer key to a file.




