#Image à appeler
FROM debian
# Installation des mises à jour
RUN apt-get update
#Installation de git (pour appeler le clone)
RUN apt-get install -y git
#Installation de java (nécessaire au parser)
RUN apt-get install -y default-jre
#Installation de nano (optionnel pour ouvrir les formats JSON après utilisation du parser)
RUN apt-get install -y nano
#Installation du clone 
RUN git clone https://github.com/antonydeepak/ResumeParser.git
#Changement du répertoire courant
WORKDIR ResumeParser/ResumeTransducer
#Environnement
ENV GATE_HOME = ..\GATEFiles
#Volume : répertoire à partager avec le host
VOLUME /home/exploit/parser/input
