class ProgramDirector:
    def __init__(self, preferences):
        self.courses = preferences["courses"]
        self.terms = preferences["terms"]
    def info(self):
        print ("N courses: ",len(self.courses))
        print ("N terms: ",len(self.terms))
    def find_term(self, id):
        for i in range(len(self.terms)):
            term = self.terms[i]            
            if term["id"] == id:
                return i
        return -1
    def test_schedule(self, starting_term, offerings, max_n_courses_per_term, max_n_terms_to_graduate):
        plan = []
        needed_take = []
        for course in self.courses:
            needed_take.append(course["id"])        
        starting_term_i = self.find_term(starting_term)
        if starting_term_i == -1:
            raise ValueError('Starting term is invalid.') 
        for i in range(max_n_terms_to_graduate):
            term = self.terms[(starting_term_i + i) % len(self.terms)]
            courses_offered = offerings[term]
            
            
            
        
        
