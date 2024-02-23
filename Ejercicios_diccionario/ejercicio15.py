class Elections():
    def __init__(self):
        self.results = {}

    def add_candidate(self):
        canditate_id = str(len(self.results) + 1)
        nombre = input("Type the name of the candidate: ")
        votes_number = int(input("Type the number of votes: "))
        self.results[canditate_id] = { "name" : nombre, "votes_number" : votes_number }

    def show_results(self):
        print("Results: ")
        for id, candidate in self.results.items():
            print(f"Candidate {id}: ")
            candidate_info = f"Name: {candidate["name"].title()}, Number of vote: {candidate["votes_number"]}"
            print(candidate_info)

elections1 = Elections()
elections1.add_candidate()
elections1.show_results()