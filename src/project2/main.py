from crewai.flow.flow import Flow,start,listen,router
from litellm import completion
import random


API_KEY = "AIzaSyBADoh8sBZ008t25txcDB0WhYyhcWb4boQ"


class practice(Flow):

    @start()
    def select_city(self):
        cities = ["Karachi","Islamabad","Lahore","Faislabad"]
        city = random.choice(cities)
        print(city)
        return city


    @router(select_city)
    def route(self,city):
        if city == "Karachi":
            return "Karachi"
        elif city == "Islamabad":
            return "Islamabad"
        elif city == "Lahore":
            return "Lahore"
        else:
            return "Faislabad"
    
    @listen("Karachi")
    def karachi(self):
        result = completion(
            model="gemini/gemini-1.5-flash",
            api_key= API_KEY,
            messages=[
                {"content":"write famous line about Karachi","role":"user"}
            ]
        )
        about =  result["choices"][0]["message"]["content"]
        print(about)
    
    @listen("Islamabad")
    def islamabad(self):
        result1 = completion(
            model="gemini/gemini-1.5-flash",
            api_key= API_KEY,
            messages=[
                {"content":"write famous line about Karachi",
                 "role":"user"}
            ]
        )
        about =  result1["choices"][0]["message"]["content"]
        print(about)
    
    @listen("Lahore")
    def lahore(self):
        result1 = completion(
            model="gemini/gemini-1.5-flash",
            api_key= API_KEY,
            messages=[
                {"content":"write famous line about Lahore",
                 "role":"user"}
            ]
        )
        about = result1["choices"][0]["message"]["content"]
        print(about)


    @listen("Faislabad")
    def faislabad(self):
        result1 = completion(
            model="gemini/gemini-1.5-flash",
            api_key= API_KEY,
            messages=[
                {"content":"write famous line about Faislabad",
                 "role":"user"}
            ]
        )
        about = result1["choices"][0]["message"]["content"]
        print(about)


def kickoff():
    obj = practice()
    obj.kickoff()
    obj.plot()        