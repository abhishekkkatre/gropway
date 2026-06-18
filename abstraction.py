from abc import ABC,abstractmethod
class ATM(ABC):
    @abstractmethod

    def withdraw(self):
        
        pass
    @abstractmethod
    def check_balance(self):
        pass
    class SBI(ATM):
        def check_balance(self):
            server = 'SBI CORE BANKING SERVER'
            language = 'JAVA B '
            
    