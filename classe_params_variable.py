class Employee:
    def __init__(self, *args, **kwargs):
        self.lastname = args[0].split()[1]
        # grace à cette ligne c'est comme si j'écris self.lastname = la valeur contenue dans le kwargs
        # étant donnée que tout est en clé valeur alors mon update va retranscrire les attribut dans __init__
        self.__dict__.update(kwargs)
 
    


        
john = Employee('John Doe')
mary = Employee('Mary Major', salary=120000)
richard = Employee('Richard Roe', salary=110000, height=178)
giancarlo = Employee('Giancarlo Rossi', salary=115000, height=182, nationality='Italian')
peng = Employee('Peng Zhu', salary=500000, height=185, nationality='Chinese', subordinates=[1,2,3])

print("john.lastname : ", peng.lastname)