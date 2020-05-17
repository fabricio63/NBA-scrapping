import statistics

def calculadora (operacion,lista):
    if operacion == "average":
        avg = sum(lista)/len(lista)
        return str(avg)
    if operacion == "max":
        return str(max(lista))
    if operacion == "min":
        return str(min(lista))
    if operacion == "stdev":
        avg = sum(lista)/len(lista)
        return str(statistics.stdev(lista,avg))
    if operacion == "range":
        return str(max(lista)-min(lista))
    else:
        return "our calc doesnt support your request"