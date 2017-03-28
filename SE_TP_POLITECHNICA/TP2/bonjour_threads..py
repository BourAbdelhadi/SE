import sys, threading, logging, os
from Queue import Queue
class Bonjour(threading.Thread):
    def __init__(self, personne):
        threading.Thread.__init__(self)
        self.personne = personne
    def run(self):
        #Fonction polie - saluer une personne
        print "Bonjour %(personne)s!\n" % \
          {"personne":self.personne},
        logging.info("Bonjour : %(personne)s" %{"personne":self.personne})
   
def utilisation():
    #Affichage mode d'utilisation
    print """
          Le programme doit etre appelle avec minimum 1 argument:
          python bonjour_listes.py Dragos
          """
def main(argv=None):
    working_dir = os.path.dirname(os.path.abspath("__file__")) + os.path.sep
    
    #log file
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                        filename = working_dir + 'bonjour.log',
                        level=logging.INFO)    
    logging.info("Main start")
    print "[+] Loading"
    #La boucle principale
    if argv is None:
        argv = sys.argv
        print "[+] We've nothing to show you"
    if len(argv) == 1:
        utilisation()
    else:
#using the queue
        qMme = Queue(30)
        qMlle = Queue(30)
        qM = Queue(30)
        myfile =working_dir +""+ argv
        with open(myfile,'r') as f:
            #Dites bonjour a chaque personne
            for ligne in f:
                if ligne[0:4] == "Mme." : 
                    mme_local = Bonjour(ligne.strip(' \r\n'))
                    qMme.put(mme_local)
                elif ligne[0:5] == "Mlle.":
                    mlle_local = Bonjour(ligne.strip(' \r\n'))
                    qMlle.put(mlle_local)
                elif ligne[0:2] == "M.":
                    m_local = Bonjour(ligne.strip(' \r\n'))
                    qM.put(m_local)
    while not qMlle.empty():
        qMlle.get().start()
    qMlle.task_done()
    while not qMme.empty():                      
        qMme.get().start()
    qMme.task_done()
    while not qM.empty():
        qM.get().start()
    qM.task_done()  
    print "[+] STOP"
    logging.info("Main stop")
    return 

if __name__ == "__main__":
    #Simplifiez la logique de la fonction principale
    myfile = "Liste_Noms.txt"   
    try:
        sys.exit(main(myfile))
    except SystemExit:
        print("[+] done")
    except:
        print("[+] error")
