from asyncore import read
import json

from numpy import true_divide

class LogData:

    def __init__(self) -> None:
        self.file = 'data.json'
        self.data = self.readData()

    def WriteData(self,time,val):
        self.data[time]= val
        with open(self.file,'w') as f:
            m = json.dumps(self.data,indent=4)
            f.write(m)
            f.close()
        print("Writed")
        
    
    def readData(self):
        with open(self.file,'r') as f:
            try:
                return json.loads(f.read())
            except Exception as e:
                print(str(e))
                return {}
import csv
def writecsv(data):
    with open('data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)


if __name__ == '__main__':
    writecsv([1,'fri 945.453',3,0])
    
            
