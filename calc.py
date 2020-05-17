import statistics

def calculadora (operacion,lista):
    if operacion == "average":
        avg = sum(lista)/len(lista)
        return str(avg)
    if operacion == "max":
        return max(lista)
    if operacion == "min":
        return min(lista)
    if operacion == "stdev":
        avg = sum(lista)/len(lista)
        return str(statistics.stdev(lista,avg))
    if operacion == "median":
        ln = len(lista)
        sorted_list= sorted(lista)
        middle = (ln / 2) + 0.5
        return str(sorted_list[middle])
    if operacion == "mode":
        return str(statistics.mode(lista))
    if operacion == "range":
        return str(max(lista)-min(lista))
    else:
        return "Our calc doesnt support your request"