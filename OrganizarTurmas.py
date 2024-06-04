class Informacoes:
    ..... .....

class Schedule:
    def __init__(self):
        self._Informacoes=Informacoes 
        self._classes= []
        self._numeroDeConflitos= 0
        self._fitness=-1
        self._classNumb=0
        self._isFitnessChanged=True
    def get_classes(self):
        self._isFitnessChanged=True
        return self._classes
    def get_numeroDeConflitos(self): return self._numeroDeConflitos
    def get_fitnss(self): 
        if (self.isFitnessChanged==True):
            self._fitness=self.calculate_fitness()
            self._isFitnessChanged=False
        return self._fitness
    def initialize(self):
        profundidade=self._informacoes.getprofundidade()
        for i in range (0, len(profundidade)):
            materia=profundidade[i].get_materia()
            for j in range (0, len(materia)):
                newClass = Class(self._classnNumb, profundidade[i], materia[j])
                self._classNumb+=1
                newClass.setHoradaAula(Informacoes.HoradaAula()[rnd.randrange(0,len(Informacoes.get_HoradaAula()))])
                newClass.set_Sala(Informacoes.get_Sala()[rnd.randrange(0,len(Informacoes.get_Sala()))])
                newClass.set_Professor(Informacoes.get_Professor()[rnd.randrange(0,len(Informacoes.get_Professor()))])
                self._classes.apend(newClass)
        return self
        def calculate_fitness(self):
            self._numeroDeConflitos=0
            classes=self.get_classes()
            for i in range(0,len(classes)):
                if (classes[i].get_sala().get_capacidade<Mateira[i].get_MaxnumberOfstudents()):self._numeroDeConflitos+=1
                for j in range(0,len(class)):
                    if(j>=i):
                        if (classes[i]).get_horadaaula()== classes[j].get-haradaaula() and classes[i]get_id() !=classes[j]
                        if (classes)
class Populacao:
    .... ....

class AlgoritimoGenetico:
    ... ...

class Materia:
    def __init__(self,number,name,instructor,MaxnumberOfstudents):
        self.number=number
        self.name=name
        self.instructor=instructor
        self.MaxnumberOfstudents=MaxnumberOfstudents 
    def get_number(self): return self.get_number
    def get_name(self): return self.get_name
    def get_instructor(self): return self.get_instructor
    def get_MaxnumberOfstudents(self): return self.get_MaxnumberOfstudents
    def __str__(self): return self._name
class Professor:
    def __init__(self,id, name):
        self._id=id
        self._name=name
    def get_id(self): return self.get_id
    def get_name(self): return self.get_name
    def __str__(self): return self._name

class Sala:
    def __init__(self,numero, capacidade):
        self._numero=numero
        self._capacidade=capacidade
    def get_numero(self): return self.get_numero
    def get_capacidade(self): return self.get_capacidade

class HoradaAula:
    def __init__(self,id, hora):
        self._id=id
        self._hora=hora
    def get_id(self): return self.get_id
    def get_hora(self): return self.get_hora

class Periodo:
    def __init__(self,name,materias):
        self._name=name
        self._materias=materias 
    def get_name(self): return self._name 
    def get_materias(self): return self._materias 
    
class Horario:
    def __init__(self,id, periodo,materia):
        self._id=id
        self._periodo=periodo
        self._materia=materia
        self._professor=None
        self._horadaaula=None
        self._sala=None
    def get_id(self): return self.get_id
    def get_periodo(self): return self.get_periodo
    def get_materia(self): return self.get_materia
    def get_professor(self): return self.get_professor
    def get_horadaaula(self): return self.get_horadaaula
    def get_sala(self): return self.get_sala
    def set_professor(self, professor):self._professor=professor
    def set_horadaaula(self,horadaaula):self._horadaaula=horadaaula
    def set_sala(self,sala):self._sala=sala
    def __str__(self):
        return str(self._periodo.get_name())+ "," + str(self._materia.get_number()) + "," + \
        str(self._sala.get_numero())+ "," + str(self._professor.get_id()) + "," + str(self._horadaaula.getide())