# - solicit a language in which to query the time, then
# - solicit an \"option 1 or 2\" answer from a user in one of several languages, then
# - print the current time in response to this response

import time   # - allows for fetching current time from OS

class GetTimeInLanguage:
  # - Dictionary containing prompts in various languages with language codes as keys corresponding to those languages (i.e. EN = English)
  promptsInLanguage = {'EN': 'Please enter 1 for 24 hour format, 2 for AM / PM format: ',
                       'FR': 'S\'il vous plaOt entrer 1 pour le format de 24 heaures, 2 pour le format AM / PM: ',
                       'ES': 'Por favor, introduzca 1 para el formato de 24 horas, 2 para el formato AM / PM: ',
                       'IT': 'Per favore, inserisci 1 per il formato 24 ore, 2 per il formato AM / PM: '}

  # - Dictionary containing format strings for time output with the imported 'time',
  # - here 1 corresponds to 12 hour time and 2 to 24 hour time
  optstrings = { '1': "%H:%M", '2': "%I:%M %p"}

  # - Collects language choice from user, looping until valid entry collected
  def PromptForLanguage(self):
    while True:
      language = input("enter 'EN' for English/ entrez 'FR' pour francais/ entrad 'ES' pour espanol/ entrate 'IT' por italiana: ")
      if language in promptsInLanguage: return language

  # - Takes a language code and collects time format choice from user in specified language, looping until valid entry collected
  def PromptForTimeFormat(self, languageCode):
    while True:
      format = input(promptsInLanguage[languageCode])
      if format in optstrings: return format

  # - Takes in a format, and returns the current time from the OS in that format (formats contained in 'optstrings')
  def GetTime(self, format):
    return time.strftime(optstrings[format])

if __name__ == "__main__":
    getTimeHelper = GetTimeInLanguage()
    language = getTimeHelper.PromptForLanguage()
    format = getTimeHelper.PromptForTimeFormat(language)
    print(getTimeHelper.GetTime(format))
