"""
This is a rough code for a general idea
"""

class Details:
    def __init__(self, first, date):
        self.firstname = first
        self.date = date

    def Name(self):
        return "Applied for " + self.firstname + " on " + self.date

class Company(Details):
    def __init__(self, first, date, portal):
        Details.__init__(self,first, date)
        self.portal = portal

    def GetDetails(self):
        return self.Name() + ", " + "through " + self.portal

    def log_this_job(self,t_J_no,t_a,t_d,t_p):
        t = str(t_J_no) + " " + t_a + " " + t_d + " " + t_p + "\n\n"
        try:
          with open("job_log.txt","a+") as fo:
            print("Opening file to log jobs")
            fo.write(t)
            print(f"Done. See your file at {fo.name}")
            fo.close()
        except FileNotFoundError as fne:
            print(fne)
#This is fun this is edited 
yes = True
ans1r = 'N'
j_no = 0
while yes:
  print("Enter Details of company.\n")
  a = input("Enter Name: ")
  d = input("Enter Date: ")
  p = input("Enter portal: ")
  y = Company(a, d, p)
  print(y.GetDetails())
  ans1r = input("Should I log it? (Y/N):")
  if ans1r == 'Y':
    j_no += 1
    y.log_this_job(j_no,a,d,p)
  ans = input("Continue Y/N?")
  if ans == 'Y':
    continue
  else:
    print("bBye")
    yes = False
