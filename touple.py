#we now touple data can not modify that is why we did transfer touple to list then we can modify when we complete our modify again 
# we did transfer list to touple 

Free = ('foods','warter','gas','electracity','service','hospital cost')

Free = list(Free)
Free.insert (2,'transformation')
Free = tuple(Free)

print(Free)


