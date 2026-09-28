import listarandom=[]
temperatura alta=0
temperaturabassa=0
for i in range(0,20):
    listarandom.append(random.randint(-20,40))
    
    

if listarandom[i]>0:
     temperaturaalta=temperaturaalta+1
 
else:
     temperaturabassa=temperaturabassa+1


if temperaturabassa>0:
    print("freddo estremo")
else:
    print("caldo estremo")
                               
                           
                           