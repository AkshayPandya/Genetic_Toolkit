"""

*****************************************************
*                                                   *
*            "creator" : "dr.akshay_pandya"         *
*            "address" : "Gujarat,India"            *
*         "contact_no" : "6355631960"               *
*            "mail_id" : "akkypan99@gmail.com"      *
*   "date_of_creation" : "2020-04-24"               *
*               "size" : "24 kb(*aprx)"             *
*                "use" : "to process genetic data"  *
*                                                   *
*****************************************************

*******************************************************************************************************************
*                                                                                                                 *
*  THIS MODULE IS ONLY FOR PERSONAL USE.                                                                          *
*  ANYONE WILLING TO USE THIS MODULE PROFESSIONALLY PLEASE CONTACT CREATOR.                                       *
*  IF YOU WANT TO PUBLISH ANY PAPER CONTAINING DATA FETCHED(PROCESSED) USING THIS MODULE PLEASE CONTACT CREATER   *
*                                                                                                                 *
*******************************************************************************************************************

"""

"#################################################################################################################"

"""

*** FILE_STRUCTURE NEEDED TO USE THIS MODULE *

> [MAIN]
    > [DATABASE]
        > [__init__.py]
        > [CODON.py]
        > [EXAMPLE_DATABASE.py]
        > [TEMPLATE.py]
    > [LogFiles]
    > [TOOLS]
        > [__init__.py]
        > [log.py]
        > [Genetic_Toolkit.py]
    > [research.py]

-------------------------------------------------------------------------------------------------------------------

-- [MAIN] - A Main Directory.

-- [DATABASE] - A Database Directory >>> Put All Database Files There.

-- [LogFiles] - A Directory In Which Log Files(as a result of  "Compare_DataBase" class) Will Be Created.

-- [TOOLS] - TOOLS Directory Containing log.py And Genetic_Toolkit.py.

-- [__init__.py] - These Are Just init Files Forgot Them.

-- [CODON.py] - A File Containing A Dictionary With RNA_CODON Information.

-- [EXAMPLE_DATABASE.py] - A Example Of Database File(Your Database File Should Look Like That).

-- [TEMPLATE.py] - A File Containing Template For Creating Database Files.

-- [log.py] - A Logging Script Created By Creater Of This Module.

-- [Genetic_Toolkit.py] - This File.

-- [research.py] - Finally A Python File To Do Your All Work And Research.

-------------------------------------------------------------------------------------------------------------------

"""

"#################################################################################################################"

"""

*** INFORMATION ABOUT THIS MODULE *

~ This Genetic Toolkit Is Made To Process The Genetic Information.
~ Currently It Is Only Able To Process RNA(+ss)
~ In Future I Will Try My Best To Add Support For DNA And RNA(-ss).

~ As You Know, Genetic Data Is Very Large Data, To Process Such Big Data More Time Is Needed.
~ It May Be Useful To Use Threading, Multiprocessing And Concurrent Modules In Code To Speed-Up The Process.
~ On Linux Machines It Is Easy To Use Multiprocessing, But In Case Of Windows It Is Not A Straight-Forward Process.
~ For Best Performance, It Is Advised To Use A Linux Machine With Good RAM And Powerful Processor.

~ In Compare_DataBase Class Output Is In Form Of A Log File.
~ For That I've Used My Own Module Based On Built-In logging Module. 

~ Currently Thre Are Following Classes In This Module
    
    1. Scan_DataBase
    2. Compare_DataBase
    3. Amino_Acid_Dict
    4. Translate
    5. Identical_Scan
    6. Performance_Index

[1] Scan_DataBase
    
    ~ This Class Compares Amino-Acid Sequence Of Every Protein Of "Proteins" Dictionary Provided By User With Amino-Acid Sequences Of Every Possible Coding Region That Can Be Generated Using "Amino_Acids" Dictionary Provided By User.

    ~ It Will Return A Dictionary. 

    ~ It Takes Following Args
    1. genome_data=dict,
      - It Takes "Amino_Acids" Dictionary As An Argument.
    2. protein_data=dict,
      - It Takes "Proteins" Dictionary As An Argument.
    3. full_mode=False,
      - If It Is Set True, The Script Will Also Try To Find Proteins As A Part Of Coding Region.
    4. level = 0
      - Set Level To One Of The Following
      > 0 : It Will Bypass All "#" Containing Coding Regions.
      > 1 : It Will Split Thode Coding Regions From "#" And Will Use All Of Them Ecxept The One Starting With "M" As That Would Repeat Later.(It Will Also Check For Every Sequence That Doesn't Begin With "M" But Ends With "#")
      > 2 : It Will Do All The Work Done By Level-1 But In Addition, It Will Replace "#" with "U" & "O"(21st and 22nd Amino-Acids) And Use Them In Comparision.

[2] Compare_DataBase

    ~ This Class Compares Amino-Acid Sequence Of Every Possible Coding Region Of First "Amino_Acids" Dictionary Provided By User With Amino-Acid Sequence Of Every Possible Coding Region Of Second "Amino_Acids" Dictionary Provided By User.(In Short It Compares Two Genetic Databases For All That Amino-Acid Sequences That Either Begin With "M" Or End With "#")
    
    ~ It Will Create A Log File Inside "LogFiles" Folder, Containing Pairs Of Matched Sequences With Reading-Frame And Index Details. 
    
    ~ It Takes Following Args
    1. Genome_Data_1=dict,
      - It Takes "Amino_Acids" Dictionary As An Argument.
    2. Sample_Data_1=dict,
      - It Takes "Sample" Dictionary As An Argument.
    3. Genome_Data_2=dict,
      - It Takes "Amino_Acids" Dictionary As An Argument.
    4. Sample_Data_2=dict,
      - It Takes "Sample" Dictionary As An Argument.
    5. forced=False,
      - If It Is Set True, The Script Will Also Try To Find Proteins As A Part Of Coding Region.(It Will Take Care Of All Those Sequense Which Neither Begin With "M" Nor End With "#", It Will Try To Search Those Sequences As A Part Of Full Coding Regions)
    6. level = 0
      - Set Level To One Of The Following
      > 0 : It Will Bypass All "#" Containing Coding Regions.
      > 1 : It Will Split Thode Coding Regions From "#" And Will Use All Of Them Ecxept The One Starting With "M" As That Would Repeat Later.(It Will Also Check For Every Sequence That Doesn't Begin With "M" But Ends With "#")
      > 2 : It Will Do All The Work Done By Level-1 But In Addition, It Will Replace "#" with "U" & "O"(21st and 22nd Amino-Acids) And Use Them In Comparision.

[3] Amino_Acid_Dict

    ~ This Class Creates A Dictionary Containing Amino-Acid Chains Sorted By Their Reading-Frame.(In Short It Creates "Amino_Acids" Dictionary Mentioned Above)

    ~ It Takes Following Args
    1. G=dict,
      - It Takes "Mod_Genome" String As An Argument.
    2. C=dict
      - It Takes "rna_codon" Dictionary As An Argument.

[4] Translate

    ~ This Class Creates A Amino-Acid Chain According To User's Passed Information.

    ~ It Takes Following Args
    1. C=dict,
      - It Takes "rna_codon" Dictionary As An Argument.
    2. x=str,
      - It Takes "Mod_Genome" String As An Argument.
    3. m=int,
      - It Takes Starting Position Of Protein On Gene As An Argument.
    4. n=int
      - It Takes Ending Position Of Protein On Gene As An Argument.

[5] Identical_Scan

    ~ This Class Compares Two Identical Databases.

    ~ It Takes Following Args
    1. genome_1=str,
      - It Takes "Mod_Genome" String of database-1 As An Argument.
    2. genome_2=str,
      - It Takes "Mod_Genome" String of database-2 As An Argument.
    3. Amino_Acid_1=dict,
      - It Takes "Amino_Acids" Dictionary of database-1 As An Argument.
    4. Amino_Acid_2=dict
      - It Takes "Amino_Acids" Dictionary of database-2 As An Argument.

[6] Performance_Index

    ~ This Class Creates A List.
    ~ Structure Of List -- [No. Of "M", No. Of "#", Total Of Both]
    ~ Higher The Values Of List, Longer It Will Take To Process That Genome.  
    ~ But The Speed Of Process Will Also Depend On The Hardware And Condition Of Your Machine.

    ~ It Takes Following Args
    1. genome=dict
      - It Takes "Mod_Genome" Dictionary As An Argument.


"""

"#################################################################################################################"

"""

*** PERFORMANCE ADVICE *


~ SETTING LEVEL TO 1 OR 2 WILL COST A LOT OF TIME 
~ SETTING FORCED TO TRUE WILL ALSO LEAD TO TIME CONSUPTION
~ DO THIS ONLY IF YOU HAVE GOOD HARDWARE OR A LOT OF TIME


"""

"#################################################################################################################"

########################################
### %%% IMPORTING NECESSARY MODULES %%% ###
########################################

try:
    from TOOLS.log import Logger
    from time import perf_counter
except:
    print("UNABLE TO IMPORT NECESSARY MODULES")
    print("CHECK THAT MODULES ARE IN CORRECT PLACE AND __INIT__.PY IS THERE")
    print("NEXT PART OF SCRIPT WILL NOT BE EXECUTED")
    exit()

######################################################
### %%% CREATING A CLASS NAMED "Scan_DataBase" %%% ###
######################################################

class Scan_DataBase:

    # CREATING INIT FUNCTION

    def __init__(self, genome_data=dict, protein_data=dict, forced=False, level=0):
        
        # DECLARING VARIABLES

        self.genome = genome_data
        self.proteins = protein_data
        self.mode = forced
        self.level = level

        # CHECKING IF LEVEL IS CORRECT
        
        if self.level not in (0, 1, 2):
            print("INCORRECT LEVEL")
            print("NEXT PART OF SCRIPT WILL NOT BE EXECUTED")
            exit()
        else:
            pass
    
    ### %%% CREATE GENERATOR FUNCTIONS %%% ###
    
    # DEFINING A FUNCTION THAT HANDLES GENOME DICTIONARY
    
    def Genomic_Data(self):
        for i in self.genome:
            yield [i, self.genome[i]]

    # DEFINING A FUNCTION THAT HANDLES PROTEIN DICTIONARY

    def Protein_Data(self):
        for i in self.proteins:
            yield [i, self.proteins[i]]

    # DEFINING A FUNCTION THAT LOOKS FOR "M" IN GENOME READING FRAMES

    def Start(self, genome):
        for i, j in enumerate(genome):
            if j == "M":
                yield i
            else:
                continue

    # DEFINING A FUNCTION THAT LOOKS FOR "#" IN GENOME READING FRAMES

    def Stop(self, genome):
        for i, j in enumerate(genome):
            if j == "#":
                yield i
            else:
                continue

    # DEFINING A FUNCTION THAT GENERATES CODING REGIONS FROM GENOME BASED ON STOP AND START FUNCTIONS

    def Codes(self, genome):
        for i in self.Start(genome):
            for j in self.Stop(genome):
                if i<j:
                    if "#" in genome[i:j]:
                        if self.level in [1, 2]:
                            cod_e = genome[i:j].split("#")
                            del cod_e[0]
                            for k in cod_e:
                                yield [i, j, k]
                        else:
                            pass

                        if self.level == 2:
                            for k in "UO":
                                yield [i, j, genome[i:j].replace("#", k)]
                        else:
                            pass
                    else:
                        yield [i, j, genome[i:j]]
                else:
                    pass

    # DEFINING A FUNCTION THAT COMPARES EVERY CODING REGION OF GENOME WITH SEQUENCE OF AMINO-ACIDS OF PROTEINS

    def Compare(self):
        start = perf_counter()
        data = {
            "Reading_Frame:0" : {
                "EXACT_MATCH" : [],
                "MATCHED_AS_PART" : []
            },
            "Reading_Frame:1" : {
                "EXACT_MATCH" : [],
                "MATCHED_AS_PART" : []
            },
            "Reading_Frame:2" : {
                "EXACT_MATCH" : [],
                "MATCHED_AS_PART" : []
            }
        }
        total = 0
        counter = 0
        for reading_frame, genome in self.Genomic_Data():
            for _, _, code in self.Codes(genome):
                for name, protein in self.Protein_Data():
                    if protein == code:
                        if name not in data[reading_frame]["EXACT_MATCH"]:
                            data[reading_frame]["EXACT_MATCH"].append(name)
                        print("[{}/{}] EXACT MATCH FOUND :: {} :: PROTEIN : {}".format(counter, total, reading_frame, name))
                        counter += 1
                    elif self.mode == True:
                        if protein in code:
                            if name not in data[reading_frame]["MATCHED_AS_PART"]:
                                data[reading_frame]["MATCHED_AS_PART"].append(name)
                            else:
                                pass
                            print("[{}/{}] MATCH FOUND :: {} :: PROTEIN : {}".format(counter, total, reading_frame, name))
                            counter += 1
                        else:
                            pass
                    else:
                        pass
                    total += 1
        stop = perf_counter()
        t = stop - start
        print("Total Pairs Processed:{}".format(total))
        print("Time:{} min {} sec".format((t-t%60)/60, t%60))
        return data

#########################################################
### %%% CREATING A CLASS NAMED "Compare_DataBase" %%% ###
#########################################################

class Compare_DataBase:

    # CREATING INIT FUNCTION

    def __init__(self, Genome_Data_1=dict, Sample_Data_1=dict, Genome_Data_2=dict, Sample_Data_2=dict, forced=False, level=0):

        # DECLARING VARIABLES

        self.genome_1 = Genome_Data_1
        self.genome_2 = Genome_Data_2
        self.sample_1 = Sample_Data_1
        self.sample_2 = Sample_Data_2
        self.mode = forced
        self.level = level

        # CHECKING IF LEVEL IS CORRECT

        if self.level not in (0, 1, 2):
            print("INCORRECT LEVEL")
            print("NEXT PART OF SCRIPT WILL NOT BE EXECUTED")
            exit()
        else:
            pass

        # CREATING A LOGGER FOR EXACT MATCHES

        self.ex = "Comparision_Result[EXACT_MATCH]_[{}-{}]_[{}-{}].log".format(self.sample_1["ACCESSION"], self.sample_1["COLLECTION_DATE"], self.sample_2["ACCESSION"], self.sample_2["COLLECTION_DATE"])
        self.exact = Logger("EXACT", logfile="LogFiles\\{}".format(self.ex))
        self.exact.File_Formatter = "%(message)s"
        self.exact.Stream_Formatter = "%(message)s"
        self.exact.File_Formatter = "%(message)s"
        self.exact.Stream_Formatter = "%(message)s"
        self.exact.Set_File = True
        self.exact.Set_Stream = True

        # CREATING A LOGGER FOR PARTIAL MATCHES

        if self.mode == True:
            self.pt = "Comparision_Result[PARTIAL_MATCH]_[{}-{}]_[{}-{}].log".format(self.sample_1["ACCESSION"], self.sample_1["COLLECTION_DATE"], self.sample_2["ACCESSION"], self.sample_2["COLLECTION_DATE"])
            self.part = Logger("PART", logfile="LogFiles\\{}".format(self.pt))
            self.part.File_Formatter = "%(message)s"
            self.part.Stream_Formatter = "%(message)s"
            self.part.Set_File = True
            self.part.Set_Stream = True
        else:
            pass

    ### %%% CREATEING GENERATOR FUNCTIONS %%% ###
    
    # DEFINING FUNCTIONS THAT HANDLES GENOME DICTIONARY

    def Genomic_Data_1(self):
        for i in self.genome_1:
            yield [i, self.genome_1[i]]

    def Genomic_Data_2(self):
        for i in self.genome_2:
            yield [i, self.genome_2[i]]

    # DEFINING A FUNCTION THAT LOOKS FOR "M" IN GENOME READING FRAMES

    def Start(self, genome):
        for i, j in enumerate(genome):
            if j == "M":
                yield i
            else:
                continue

    # DEFINING A FUNCTION THAT LOOKS FOR "#" IN GENOME READING FRAMES

    def Stop(self, genome):
        for i, j in enumerate(genome):
            if j == "#":
                yield i
            else:
                continue

    # DEFINING A FUNCTION THAT GENERATES CODING REGIONS FROM GENOME BASED ON STOP AND START FUNCTIONS

    def Codes(self, genome):
        for i in self.Start(genome):
            for j in self.Stop(genome):
                if i<j:
                    if "#" in genome[i:j]:
                        if self.level in [1, 2]:
                            cod_e = genome[i:j].split("#")
                            del cod_e[0]
                            for k in cod_e:
                                yield [i, j, k]
                        else:
                            pass

                        if self.level == 2:
                            for k in "UO":
                                yield [i, j, genome[i:j].replace("#", k)]
                        else:
                            pass
                    else:
                        yield [i, j, genome[i:j]]
                else:
                    pass

    # DEFINING A FUNCTION THAT COMPARES EVERY CODING REGION OF ONE GENOME WITH EVERY CODING REGION OF OTHER GENOME

    def Compare_CDR(self):
        start = perf_counter()
        total = 0
        counter = 0
        for reading_frame_1, genome_1 in self.Genomic_Data_1():
            for reading_frame_2, genome_2 in self.Genomic_Data_2():
                for i_1, j_1, code_1 in self.Codes(genome_1):
                    for i_2, j_2, code_2 in self.Codes(genome_2):
                        if code_1==code_2:
                            self.exact.D("{}][{}]\t{}\t[code:{}-{}]\n[{}][{}]\t{}\t[code:{}-{}".format(counter, self.sample_1["LOCALITY"], reading_frame_1, i_1, j_1, counter, self.sample_2["LOCALITY"], reading_frame_2, i_2, j_2))
                            counter += 1
                        else:
                            if self.mode == True:
                                if code_1 in code_2:
                                    self.part.D("[{}]FOUND [{}]\t{}\t[code:{}-{}]\n[{}]IN [{}]\t{}\t[code:{}-{}]".format(counter, self.sample_1["LOCALITY"], reading_frame_1, i_1, j_1, counter, self.sample_2["LOCALITY"], reading_frame_2, i_2, j_2))
                                    counter += 1
                                elif code_2 in code_1:
                                    self.part.D("[{}]FOUND [{}]\t{}\t[code:{}-{}]\n[{}]IN [{}]\t{}\t[code:{}-{}]\n".format(counter, self.sample_2["LOCALITY"], reading_frame_2, i_2, j_2, counter, self.sample_1["LOCALITY"], reading_frame_1, i_1, j_1))
                                    counter += 1
                                else:
                                    pass
                            else:
                                pass
                        total += 1
                        print("{}-{}-{}".format(total, reading_frame_1, reading_frame_2))
        stop = perf_counter()
        t = stop - start
        self.exact.D("Total Pairs Matched:{}".format(total))
        self.exact.D("Time:{} min {} sec".format((t-t%60)/60, t%60))
        if self.mode == True:
            self.part.D("Total Pairs Matched:{}".format(total))
            self.part.D("Time:{}".format(stop-start))
        else:
            pass

########################################################
### %%% CREATING A CLASS NAMED "Amino_Acid_Dict" %%% ###
########################################################

class Amino_Acid_Dict:

    # CREATING INIT FUNCTION

    def __init__(self, G=dict, C=dict):

        # DECLARING VARIABLES

        self.G = G
        self.C = C
        

    # CREATING MAIN FUNCTION

    def Generate(self):
        self.Amino_Acid_Dict = {}
        for rf in range(3):
            A = ""
            for i in range(rf, len(self.G), 3):
                try:
                    A += self.C[self.G[i:i+3]]
                except:
                    pass
            self.Amino_Acid_Dict["Reading_Frame:{}".format(rf)] = A
        return self.Amino_Acid_Dict

##################################################
### %%% CREATING A CLASS NAMED "Translate" %%% ###
##################################################

class Translate:

    # CREATING INIT FUNCTION

    def __init__(self, C=dict, x=str, m=int, n=int):

        # DECLARING VARIABLES

        self.C = C
        self.x = x
        self.m = m
        self.n = n

    # CREATING MAIN FUNCTION

    def Translate(self):
        y = self.x[self.m-1:self.n-1]
        Amino_Acid_Sec = ""
        for i in range(0, len(y), 3):
            try:
                Amino_Acid_Sec += self.C[y[i:i+3]]
            except:
                pass
        return Amino_Acid_Sec

#######################################################
### %%% CREATING A CLASS NAMED "Identical_Scan" %%% ###
#######################################################

class Identical_Scan:

    # CREATING INIT FUNCTION

    def __init__(self, genome_1=str, genome_2=str, Amino_Acid_1=dict, Amino_Acid_2=dict):

        # DECLARING VARIABLES

        self.genome_1 = genome_1
        self.genome_2 = genome_2
        self.Amino_Acid_1 = Amino_Acid_1
        self.Amino_Acid_2 = Amino_Acid_2

    # DEFINING A GENERATOR FUNCTION THAT HANDLES GENOME DICTIONARY
    
    def Genomic_Data(self, genome):
        for i, j in enumerate(genome):
            yield [i, j]

    # CREATING Nucleotide_Scan FUNCTION
    
    def Nucleotide_Scan(self):
        for i, j in self.Genomic_Data(self.genome_1):
            _,k = next(self.Genomic_Data(self.genome_2))
            if j != k:
                print("MIS-MATCH FOUND IN NUCLEOTIDE SEQUENCE :: INDEX:[{}] :: GENOME-1:[{}] :: GENOME-2:[{}]".format(i, j, k))
            else:
                pass
    
    # CREATING Amino_Acid_Scan FUNCTION
    
    def Amino_Acid_Scan(self):
        for i in self.Amino_Acid_1:
            s1 = self.Amino_Acid_1[i]
            s2 = self.Amino_Acid_2[i]
            if len(s1) == len(s2):
                pass
            elif len(s1) > len(s2):
                print("LENGTH DIFFERENCE FOUND::RF:[{}]::G_1 is {} BP LONGER THAN G_2.".format(i, len(s1)-len(s2)))
            else:
                print("LENGTH DIFFERENCE FOUND::RF:[{}]::G_2 is {} BP LONGER THAN G_1.".format(i, len(s2)-len(s1)))
            for j, k in enumerate(s1):
                try:
                    l = s2[j]
                    if k != l:
                        print("MIS-MATCH FOUND IN AA SEQUENCE::RF:[{}]::INDEX:[{}]::GENOME-1:[{}]::GENOME-2:[{}]".format(i, j, k, l))
                    else:
                        pass
                except IndexError:
                    pass

##########################################################
### %%% CREATING A CLASS NAMED "Performance_Index" %%% ###
##########################################################

class Performance_Index:

    # CREATING INIT FUNCTION

    def __init__(self, genome=dict):

        # DECLARING VARIABLES

        self.genome = genome
        
        # CALLING MAIN FUNCTION
        self._index()

    # DEFINING A GENERATOR FUNCTION THAT HANDLES GENOME DICTIONARY

    def Genomic_Data(self):
        for i in self.genome:
            yield [self.genome[i]]

    # CREATING MAIN FUNCTION

    def _index(self):
        Start = 0
        Stop = 0
        for i in self.Genomic_Data():
            for j in i:
                if j == "M":
                    Start += 1
                elif j == "#":
                    Start += 1
                else:
                    pass
        return [Start, Stop, (Start+Stop)]