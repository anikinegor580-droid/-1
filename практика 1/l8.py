from datetime import date
current_year = date.today().year
def  century_message(name, age, current_year):
    return f"{name}, тебе исполнится 100 лет в {current_year+100-age} году"
print(century_message("Аня",20,current_year))

