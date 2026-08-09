class Subject:
    def __init__(self, name, description, checkpoint_1, checkpoint_2, final_exam):
        self.name = name
        self.description = description
        self.checkpoint_1 = checkpoint_1
        self.checkpoint_2 = checkpoint_2
        self.final_exam = final_exam

    def __str__(self):
        return f"""
        Subject: {self.name},
         Description: {self.description},
        """
    #getter
    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_checkpoint_1(self):
        return self.checkpoint_1

    def get_checkpoint_2(self):
        return self.checkpoint_2

    def get_final_exam(self):
        return self.final_exam
    #setter
    def set_name(self, name):
        if name: self.name = name
        else: raise ValueError("Name cannot be empty")

    def set_description(self, description):
        if description: self.description = description
        else: raise ValueError("Description cannot be empty")

    def set_checkpoint_1(self, checkpoint_1):
        if 0 <= checkpoint_1 <= 10: self.checkpoint_1 = checkpoint_1
        else: raise ValueError("Checkpoint 1 must be between 0 and 10")

    def set_checkpoint_2(self, checkpoint_2):
        if 0 <= checkpoint_2 <= 10: self.checkpoint_2 = checkpoint_2
        else: raise ValueError("Checkpoint 2 must be between 0 and 10")

    def set_final_exam(self, final_exam):
        if 0 <= final_exam <= 10: self.final_exam = final_exam
        else: raise ValueError("Final exam must be between 0 and 10")

class SubjectList:
    #create
    def __init__(self):
        self.subjects = []
    #update 
    def add_subject(self, subject:Subject):
        self.subjects.append(subject)

    #read
    def __str__(self):
        output = "Subject List:\n"
        for subject in self.subjects:   
            output += subject + "\n--------------------\n"
        return output
    #delete
    def remove_subject(self, name):
        #duyet tung mon de tim ten -> xoa
        for subject in self.subjects:
            if subject.get_name() == name:
                self.subjects.remove(subject)
                print(f"Subject '{name}' removed successfully.")
                return # ham ket thuc
        print(f"Subject '{name}' not found in the list.")
            
        











