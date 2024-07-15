class AgeVerificationError(Exception):
    def __init__(self, age):
        self.age = age
        super().__init__(f"You must be 18 years or older to vote. Your age is {age}.")
def verify_age_for_voting(age):
    if age < 18:
        raise AgeVerificationError(age)
    else:
        print("Age verification successful. You are eligible to vote!")
try:
    age = int(input("Enter your age to verify eligibility for voting: "))
    verify_age_for_voting(age)
except AgeVerificationError as e:
    print(f"Age Verification Error: {e}")
except ValueError:
    print("Invalid input. Please enter a valid age as an integer.")
except Exception as ex:
    print(f"An unexpected error occurred: {ex}")
