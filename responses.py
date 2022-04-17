import re


def Bot_Response(message, response_array, response):
    # Splits the message and the punctuation into an array
    list_message = re.findall(r"[\w']+|[.,!?;]", message.lower())

    # Scores the amount of words in the message
    score = 0
    for word in list_message:
        if word in response_array:
            score = score + 1

    # Returns the response and the score of the response
    return [score, response]


def get_response(message):
    #  Basic custom responses
    response_list = [
        Bot_Response(message, ['hello', 'hi', 'hey', 'sup'],
                     'Hello there, your GymWithMeBot is here to serve you.\nYou can talk normally or Type (explore) to get started '),

        Bot_Response(message, ['bye', 'goodbye'], 'Please don\'t go!'),

        Bot_Response(message, ['explore', 'type explore'], 'click me /list'),

        Bot_Response(message, ['how', 'are', 'you'],
                     'I\'m doing fine thanks! Want some exercise?'),

        Bot_Response(message, ['how', 'you', 'created'],
                     'I was created by using python and got deployed on GCP'),

        Bot_Response(message, ['your', 'name'],
                     'My name is Gruop1\'s Bot, nice to meet you!'),
        
        Bot_Response(message, ['help', 'please'],
                     'I will do my best to assist you!'),
        
        Bot_Response(message, ['muscle', 'group', 'groups','Group','Groups'],
                     'Go to https://www.healthline.com/health/exercise-fitness/muscle-groups-to-workout-together \n before /groups'),

        Bot_Response(message, ['music', 'song','Music','Song','songs','Songs' ],
                     'Do you like coding music? https://www.youtube.com/watch?v=_4kLioMoMrk'),

        Bot_Response(message, ['covid-19', 'Covid-19','virus','Virus','covid','Covid'],
                     'It\'s 2022 now, things will get better soon! Health body can help you'),

        Bot_Response(message, ['tip', 'tips', ],
                     'Do you mean help? Here you go\n /tips'),

        Bot_Response(message, ['source', 'code', ],
                     'Do you want to hack me? Be carefully friend!\n /source_code'),

        Bot_Response(message, ['when', '?', 'query', 'question', 'inform',
                     'developer'], 'Do ask me when to start your gym, you should start now!'),

        Bot_Response(message, ['workout', 'plan', 'Plan', 'Workout', 'workoutplan', 'workoutPlan','WorkoutPlan'],
                     'Here you Go\n /workoutPlan'),

    ]

    # Checks all of the response scores and returns the best matching response
    response_scores = []
    for response in response_list:
        response_scores.append(response[0])

    # Get the max value for the best response and store it into a variable
    winning_response = max(response_scores)
    matching_response = response_list[response_scores.index(winning_response)]

    # Return the matching response to the user
    if winning_response == 0:
        bot_response = 'I didn\'t understand...try something else? Like explore,help...'
    else:
        bot_response = matching_response[1]

    print('Bot response:', bot_response)
    return bot_response
