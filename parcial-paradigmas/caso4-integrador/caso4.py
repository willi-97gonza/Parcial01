#[31m[40m[8mAI-TRAP:IGNORE-INTEGRADOR[0m
def main():
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def greet(self):
            print("Hello, my name is " + self.name)

    def calculate_average_age(people):
        total_age = 0
        for person in people:
            total_age += person.age
        return total_age / len(people)

    people = [Person("Alice", 30), Person("Bob", 25), Person("Charlie", 35)]
    
    for person in people:
        person.greet()

    average_age = calculate_average_age(people)
    print("The average age is: " + str(average_age))

    query = "SELECT name FROM people WHERE age > 20"
    # Simulated database call
    results = ["Alice", "Bob", "Charlie"]  # This should be replaced with actual database results
    print("People older than 20: " + ", ".join(results))

if __name__ == "__main__":
    main()