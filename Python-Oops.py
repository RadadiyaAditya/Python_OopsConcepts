class School:
  def __init__(self, name:str, level:str, NOS:int):
    self.sname = name
    self.slevel = level
    self.numberOfStudents = NOS

  @property
  def name(self):
    return self.sname

  @name.setter
  def name(self,name:str):
    self.sname = name

  @property  
  def level(self):
    return self.slevel

  @property
  def nos(self):
    return self.numberOfStudents

  @nos.setter
  def nos(self,number:int):
    self.numberOfStudents = number

  @nos.deleter
  def nos(self):
    del self.numberOfStudents

  def __repr__(self):
    print("A {} school named {} with {} students".format(self.level,self.name,self.numberOfStudents))

class PrimarySchool(School):
  def __init__(self,name,NOS,policy):
    super().__init__(name,"Primary",NOS)
    self.pickupPolicy = policy

  def get_policy(self):
    return self.pickupPolicy

  def __repr__(self):
    super().__repr__()
    print("has a pickup policy is for picking {}".format(self.pickupPolicy))

class MiddleSchool(School):
  pass

class HighSchool(School):
  def __init__(self,name,NOS,sport:list):
    super().__init__(name,"High",NOS)
    self.sportsTeams = sport

  def get_sport(self):
    return self.sportsTeams

  def __repr__(self):
    super().__repr__()
    print("This school has teams for following sports {}".format(self.sportsTeams))

S1 = School("Gurukul","Primary",300)
P1 = PrimarySchool("SAL",400,"By 4 PM")
H1 = HighSchool("Rosery",100,["basletball","cricket","Volleyball"])