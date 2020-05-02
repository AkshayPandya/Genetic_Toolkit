# Genetic_Toolkit

             "creator" : "dr.akshay_pandya"
             "address" : "Gujarat,India"
          "contact_no" : "6355631960"
             "mail_id" : "akkypan99@gmail.com"
    "date_of_creation" : "2020-04-24"
                "size" : "140 kb(*aprx)"
                 "use" : "to process genetic data"

*******************************************************************************************************************
*  THIS MODULE IS ONLY FOR PERSONAL USE.                                                                          *
*  ANYONE WILLING TO USE THIS MODULE PROFESSIONALLY PLEASE CONTACT CREATOR.                                       *
*  IF YOU WANT TO PUBLISH ANY PAPER CONTAINING DATA FETCHED(PROCESSED) USING THIS MODULE PLEASE CONTACT CREATER   *
*******************************************************************************************************************

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


# *** PERFORMANCE ADVICE *
    ~ SETTING LEVEL TO 1 OR 2 WILL COST A LOT OF TIME
    ~ SETTING FORCED TO TRUE WILL ALSO LEAD TO TIME CONSUMPTION
    ~ DO THIS ONLY IF YOU HAVE GOOD HARDWARE OR A LOT OF TIME
 
