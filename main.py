import requests
import mysql.connector
import random
import datetime,time,csv,os
import colorlog,logging
import shutil

#verificare insert user in baza de date
def test_1(id_manager,URL,cale,nume_tabel):
    users=[["Badea","Mihai","IT Shool",id_manager],
           ["Muntean","Paul","IT School",id_manager],
           ["Olteanu","Leontin","IT School",id_manager],
           ["Angiu","Natalia","Google",id_manager]]
    for user in users:
        jsonData={
            "nume":user[0],
            "prenume":user[1],
            "nume_companie":user[2],
            "id_manager":id_manager
        }
        session=requests.session()
        r=session.post(URL+cale,data=jsonData)

    connect=mysql.connector.connect(host="localhost",user="root",password="Afd3ufy250137@",database="users")
    cursor=connect.cursor()


    cursor.execute(f"SELECT * from {nume_tabel}")
    results=cursor.fetchall()

    for row in users:
        found=False
        contor=0
        while not found and contor<len(results):
            flag=True
            for i in range(len(row)):
                if row[i]!=results[contor][i+1]:
                    flag=False
            if flag==True:
                found=True
            else:
                contor+=1
        if found==False:
            return"Test 1 failed..."
        else:
            return"Test 1 passed.."
    cursor.close()
    connect.close()


#verificare intrare fisiere csv si txt
def test_2(cale_csv, nume_tabel,cale_csv_backup,):
    persoane = []
    linii = []
    
    final_path = "D:/phyton/PROIECT_FINAL/Intrari"
    
    for i in range(10):
        alegere = random.randint(0, 1)
        output = {
            "data": datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00", "Z"),
            "idPoarta": random.randint(1, 3)
        }

        aIntrat = False
        if alegere == 1:
            # intrare
            idPersoana = random.randint(1, 5)
            while idPersoana in persoane:
                idPersoana = random.randint(1, 5)
            output["sens"] = "in"
            output["idPersoana"] = idPersoana
            persoane.append(output['idPersoana'])
            aIntrat = True
        else:
            # iesire 
            if len(persoane) > 0:
                idPersoana = persoane[random.randint(0, len(persoane) - 1)]
                output["sens"] = "out"
                output["idPersoana"] = idPersoana
                persoane.remove(idPersoana)
                aIntrat = True
        
        if aIntrat:
            linii.append(output)

    with open(cale_csv, "w", newline="") as file:
        writer = csv.writer(file)
        header = ["IdPersoana", "Data", "Sens"]
        writer.writerow(header)
        for line in linii:
            array = [str(line["idPersoana"]), line["data"], line["sens"]]
            writer.writerow(array)
        
        
    

        
    time.sleep(5)
    shutil.move(cale_csv,final_path)
    
    
    time.sleep(5)
    connect=mysql.connector.connect(host="localhost",user="root",password="Afd3ufy250137@",database="users")
    cursor=connect.cursor()

    cursor.execute(f"SELECT * from {nume_tabel}")
    results=cursor.fetchall()

    cale_csv2="PROIECT_FINAL/Backup_Intrari/Poarta2.csv"

    extension=cale_csv2.split(".")[1]
    filename=cale_csv2.split(".")[0]
    cale_csv_backup = filename + "-" + str(datetime.datetime.now().date()) + "."+extension

    with open(cale_csv_backup, "r", newline="") as file_csv:
        csv_content = file_csv.readlines()[1:]  
        
        for line in csv_content:
                elements = line.strip().split(",")  
                for element in elements:
                    if element in str(results):
                        return True
        return False
        

def test_3(fisier_input):
    initial_path = os.listdir("PROIECT_FINAL/Intrari")
    backup_path = os.listdir("PROIECT_FINAL/Backup_Intrari")
    extension=fisier_input.split(".")[1]
    filename=fisier_input.split(".")[0]
    flag = False

    for file in initial_path:
        if file == fisier_input:
            flag = False

    for file in backup_path:
        if file == filename + "-" + str(datetime.datetime.now().date()) + "."+extension:
            flag = True

    return flag

    
# verificare ca nu exista fisiere mai vechi de 5 secunde in directorul de intrari
def test_4(path): 
    createdTime=os.path.getatime(path)
    current_time=time.time()
    flag=True

    for file in os.listdir(path):
        if createdTime<= current_time-5:
            flag=False
        else:
            flag=True
    return flag

 # Define the log format with colors
log_format = (
    '%(log_color)s%(levelname)s%(reset)s '
    '%(log_color)s%(asctime)s%(reset)s '
    '%(log_color)s%(message)s%(reset)s'
)

# Create a logger
logger = colorlog.getLogger()
logger.setLevel(logging.DEBUG)  # Set the desired log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)

# Create a stream handler to output logs to the console
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(colorlog.ColoredFormatter(log_format))
logger.addHandler(stream_handler)


def check():
    punctaj=0
    
    if test_1("1","http://127.0.0.1:5000","/register","registered_users"):
        punctaj+=2.5
        logging.info("Test 1 passed...")
    else:
        logging.error("Test 1 failed...")
    if test_2("Checker/Poarta2.csv","acces_porti","PROIECT_FINAL/Backup_Intrari/Poarta2.csv",):
        punctaj+=2.5
        logging.info("Test 2 passed...")
    else:
        logging.error("Test 2 failed...")
    if test_3("Poarta2.csv"):
        punctaj+=2.5
        logging.info("Test 3 passed...")
    else:
        logging.error("Test 3 failed...")
    if test_4("PROIECT_FINAL/Intrari/",):
        punctaj+=2.5
        logging.info("Test 4 passed...")
    else:
        logging.error("Test 4 failed...")

    time.sleep(3)
    if punctaj <=5:
        logging.error("Punctajul este "+str(punctaj))
    if punctaj > 5 and punctaj <=7.5:
        logging.warning("Punctajul este "+ str(punctaj))
    if punctaj >7.5:
        logging.info("Punctajul este "+ str(punctaj))

check()


    


