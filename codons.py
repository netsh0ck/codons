from itertools import islice
import hashlib
from random import randint

def getCodon():
 running = True
 while (running == True):
  inputCodons = generateCodons()
  converted = convertToAmino(inputCodons)
  print(converted)
  if (converted == "Stop"):
   running = False

def generateCodons():
 toReturn = ""
 for i in range(0, 3):
  generated = randint(0, 3)
  if(generated == 0):
   toReturn += "A"
  elif (generated == 1):
   toReturn += "U"
  elif (generated == 2):
   toReturn += "C"
  elif (generated == 3):
   toReturn += "G"
 return toReturn

def convertToAmino(codon):
 # THERE WAS PROBABLY A BETTER WAY OF DOING THIS:
 if (codon == "UUU" or codon == "UUC"):
  return "Phe"
 elif (codon == "UUA" or codon == "UUG"):
  return "Leu"
 elif (codon == "CUU" or codon == "CUC" or codon == "CUA" or codon == "CUG"):
  return "Leu"
 elif (codon == "AUU" or codon == "AUC" or codon == "AUA"):
  return "Ile"
 elif (codon == "AUG"):
  return "Met"
 elif (codon == "GUU" or codon == "GUC" or codon == "GUA" or codon == "GUG"):
  return "Val"
 elif (codon == "UCU" or codon == "UCC" or codon == "UCA" or codon == "UCG"):
  return "Ser"
 elif (codon == "CCU" or codon == "CCC" or codon == "CCA" or codon == "CCG"):
  return "Pro"
 elif (codon == "ACU" or codon == "ACC" or codon == "ACA" or codon == "ACG"):
  return "Thr"
 elif (codon == "GCU" or codon == "GCC" or codon == "GCA" or codon == "GCG"):
  return "Ala"
 elif (codon == "UAU" or codon == "UAC"):
  return "Tyr"
 elif (codon == "CAU" or codon == "CAC"):
  return "His"
 elif (codon == "CAA" or codon == "CAG"):
  return "Gln"
 elif (codon == "AAU" or codon == "AAC"):
  return "Asn"
 elif (codon == "AAA" or codon == "AAG"):
  return "Lys"
 elif (codon == "GAU" or codon == "GAC"):
  return "Asp"
 elif (codon == "GAA" or codon == "GAG"):
  return "Glu"
 elif (codon == "UGU" or codon == "UGC"):
  return "Cys"
 elif (codon == "UGG"):
  return "Trp"
 elif (codon == "CGU" or codon == "CGC" or codon == "CGA" or codon == "CGG"):
  return "Arg"
 elif (codon == "AGU" or codon == "AGC"):
  return "Ser"
 elif (codon == "AGA" or codon == "AGG"):
  return "Arg"
 elif (codon == "GGU" or codon == "GGC" or codon == "GGA" or codon == "GGG"):
  return "Gly"
 elif (codon == "UAA" or codon == "UAG" or codon == "UGA"):
  return "Stop"


def initLoop():
 getCodon()

def main():
 initLoop()

if __name__ == "__main__":
    main()
