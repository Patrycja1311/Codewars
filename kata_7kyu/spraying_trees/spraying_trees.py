def task(w, n, c):
    workers = {"Monday": "James", "Tuesday": "John", "Wednesday": "Robert", "Thursday": "Michael", "Friday": "William"}
    if w not in workers:
        return "Invalid weekday. Work is only scheduled from Monday to Friday."
    return f"It is {w} today, {workers[w]}, you have to work, you must spray {n} trees and you need {n * c} dollars to buy liquid"
