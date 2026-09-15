class CandidateProfile:
    def __init__(self,name,email,score):
        self.name = name        # public member
        self._email = email      # protected member
        self.__score = score     #private member

    def get_email(self):
        return self._email

    def get_score(self):
        return self.__score

name = input().strip()
email = input().strip()
score = int(input().strip())    
candidate = CandidateProfile(name,email,score)

print("CANDIDATE PROFILE")
print(f"Name: {candidate.name}")
print(f"Email: {candidate.get_email()}")
print(f"Score: {candidate.get_score()}")
    


    