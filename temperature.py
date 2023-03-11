class Temperature:
    def_init_(self,temp):
       self,temp=temp
    def convertFahrenheit(self):
       result=float((9*self.temp)/5*32)
       return result
    def convertCelcius(self):
        result=float((self.temp-32)*5/9)
        return result
input_temp=float(input("input temperature in celcius:"))
temp1=Temperature(input_temp)
print(temp1.convertFahrenheit())
input_temp=float(input("input temperature in fahrenheit:"))
temp1= Temperature(input_temp)
print(temp1.convertCelcius())




