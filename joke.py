from jokeapi import Jokes # Import the Jokes class

j = Jokes()  # Initialise the class
joke = j.get_joke()  # Retrieve a random joke
print(joke)
if joke["type"] == "single": # Print the joke
  print(joke["joke"])
else:
  print(joke["setup"])
  print(joke["delivery"])

# import requests

# def get_meaning_dictionary_api(word, session=False):
#     url = f"https://api.dictionaryapi.dev/api/v2/entries/en_US/{word}"

#     payload = {}
#     headers = {}
#     if session:  # using session for speed( https://stackoverflow.com/questions/34512646/how-to-speed-up-api-requests )
#         response = session.request("GET", url, headers=headers, data=payload)
#     else:
#         response = requests.request("GET", url, headers=headers, data=payload)
#     response = response.json()
#     output_list = list()

#     print(response)

#     for i in response:
#         output_list.append(f'Word : {i["word"]}')
#         for meanings in i['meanings']:
#             output_list.append(' ' * 4 + f'Part of Speech : {meanings["partOfSpeech"]}')
#             output_list.append(' ' * 4 + "Definitions")
#             for definitions in meanings['definitions']:
#                 output_list.append(' ' * 8 + f'definition :')
#                 output_list.append(' ' * 12 + definitions["definition"])
#                 if 'synonyms' in definitions.keys():
#                     output_list.append(' ' * 8 + 'Synonym : ')
#                     for synonym in definitions['synonyms']:
#                         output_list.append(' ' * 12 + synonym)
#                 if 'example' in definitions.keys():
#                     output_list.append(' ' * 8 + f'Examples : {definitions["example"]}')
#     return output_list


# print(get_meaning_dictionary_api('good'))