class ExamException(Exception):
    pass


class CSVTimeSeriesFile():
    def __init__(self, name):

        if name.endswith('.csv') == False:
            raise ExamException('Should be CSV type')

        self.name = name

    def get_data(self):
        values = []

        opened_csv = open(self.name, "r")

        for line in opened_csv:
            elements = line.split(',')

            ""#converti i convertibili
            if elements[0] != int:
                try:
                    elements[0] = int(elements[0])
                except:
                    continue

            if values != []:
                if elements[0] <= epoch:
                    raise ExamException('Timestamp value is not higher than previous one')
            try:
                elements[1] = float(elements[1])
            except:
                continue

            epoch = elements[0]
            temperature = elements[1]

            values.append([epoch, temperature])
            
        return(values)


variance_list = []

def compute_daily_variance(x):
    period_temperatures = []
    actual_day = None
    sum_temperature = None
    for y in x:
        y[0] = int((y[0])/86400)
    #notando che l'output non richiede le date delle temperature, ho scelto di trasformare i timestamp in giorni

    for y in x:
        if sum_temperature != None:
            if y[0] == actual_day:
                sum_temperature = sum_temperature + y[1]
                period_temperatures.append(y[1])
            else:
                if len(period_temperatures) == 1:
                    variance_list.append(0)
                    actual_day = y[0]
                    sum_temperature = y[1]
                else:
                    mean_temperature = sum_temperature / len(period_temperatures)
                    sum_of_differences_squares = 0

                    for k in period_temperatures:
                        sum_of_differences_squares = sum_of_differences_squares + (k - mean_temperature)**2
                    
                    var = (sum_of_differences_squares / (len(period_temperatures)-1))

                    variance_list.append(var)
                    actual_day = y[0]
                    sum_temperature = y[1]
                    period_temperatures = [y[1]]
                    sum_of_differences_squares = 0

        else:
            actual_day = y[0]
            sum_temperature = y[1]
            period_temperatures = [y[1]]

    return variance_list

data ='C:/Users/Ezio Auditore/OneDrive/Desktop/LABORATORIO/ESAME/data.csv'

time_series_file = CSVTimeSeriesFile(data)
time_series = time_series_file.get_data()

compute_daily_variance(time_series)

print(variance_list)

                
        

        
         






