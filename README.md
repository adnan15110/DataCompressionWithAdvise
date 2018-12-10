# Data compresssion with Advise
project assignment code.

RCB book1 --> Free ex: 0 AC: 0 compressed size: 796738
RCB news --> Free ex: 0 AC: 0 compressed size: 383334
RCB progc --> Free ex: 0 AC: 0 compressed size: 38544
RCB trans --> Free ex: 0 AC: 0 compressed size: 86335


RCB new model

RCB trans --> Free ex: 0 AC: 2178938 compressed size: 51742
RCB book1 --> Free ex: 0 AC: 13755907 compressed size: 444503
RCB news --> Free ex: 0 AC: 8640890 compressed size: 229417
RCB progc --> Free ex: 0 AC: 840019 compressed size: 20582

RCB book1 --> Free ex: 0 AC: 13755907 STD: 13755907 MRM: 13755907 cc_linear: 13755907 cc_log:4324800 Compressed Size: 444503
RCB news --> Free ex: 0 AC: 8641149 STD: 8641149 MRM: 8641149 cc_linear: 8641149 cc_log:2212519 Compressed Size: 229426
RCB progc --> Free ex: 0 AC: 842762 STD: 842762 MRM: 842762 cc_linear: 842762 cc_log:204386 Compressed Size: 20596
RCB trans --> Free ex: 0 AC: 2178956 STD: 2178956 MRM: 2178956 cc_linear: 2178956 cc_log:505635 Compressed Size: 51742

CB new model
CB trans --> Free ex: 0 AC: 1046042 compressed size: 39997
CB book1 --> Free ex: 0 AC: 15514255 compressed size: 476770
CB news --> Free ex: 0 AC: 8556148 compressed size: 232718
CB progc --> Free ex: 0 AC: 548589 compressed size: 18237
CB progc --> Free ex: 0 AC: 548589 STD: 548589 MRM: 548589 cc_linear: 548589 cc_log:185513 Compressed Size: 18237
CB trans --> Free ex: 0 AC: 1046042 STD: 1046042 MRM: 1046042 cc_linear: 1046042 cc_log:411674 Compressed Size: 39997
CB news --> Free ex: 0 AC: 8556148 STD: 8556148 MRM: 8556148 cc_linear: 8556148 cc_log:2238854 Compressed Size: 232718
CB book1 --> Free ex: 0 AC: 15514255 STD: 15514255 MRM: 15514255 cc_linear: 15514255 cc_log:4582935 Compressed Size: 476770
####################################

C:\inspection_app_venv\Scripts\python.exe "C:/AdnanKhan/code repository/DataCompression/main.py"
Path to CALGARY dataset: C:\AdnanKhan\code repository\DataCompression\dataset\calgary
Skipped: 0
MTF bib --> Free ex: 2200099 AC: 2202608 STD: 2202608 MRM: 2202608 cc_linear: 2202608 cc_log:633586 Compressed Size: 65290
Skipped: 0
MTF book1 --> Free ex: 9758044 AC: 9774749 STD: 9774749 MRM: 9774749 cc_linear: 9774749 cc_log:3844072 Compressed Size: 384412
Skipped: 0ed: 0
MTF news --> Free ex: 6391665 AC: 6415035 STD: 6415035 MRM: 6415035 cc_linear: 6415035 cc_log:1990025 Compressed Size: 201614
Skipp
MTF progc --> Free ex: 685876 AC: 688904 STD: 688904 MRM: 688904 cc_linear: 688904 cc_log:209666 Compressed Size: 21256
Skipped: 0
MTF trans --> Free ex: 1549717 AC: 1558018 STD: 1558018 MRM: 1558018 cc_linear: 1558018 cc_log:476025 Compressed Size: 48041


################################
Path to CALGARY dataset: C:\AdnanKhan\code repository\DataCompression\dataset\calgary
Skipped: 0
TS bib --> Free ex: 2086302 AC: 2205229 STD: 2205229 MRM: 2205229 cc_linear: 2205229 cc_log:633621 Compressed Size: 65295
Skipped: 0
TS book1 --> Free ex: 9005242 AC: 9774638 STD: 9774638 MRM: 9774638 cc_linear: 9774638 cc_log:3844058 Compressed Size: 384410
Skipped: 0
TS news --> Free ex: 6037006 AC: 6415402 STD: 6415402 MRM: 6415402 cc_linear: 6415402 cc_log:1990035 Compressed Size: 201615
Skipped: 0
TS progc --> Free ex: 649293 AC: 688904 STD: 688904 MRM: 688904 cc_linear: 688904 cc_log:209666 Compressed Size: 21256
Skipped: 0
TS trans --> Free ex: 1466168 AC: 1558138 STD: 1558138 MRM: 1558138 cc_linear: 1558138 cc_log:476036 Compressed Size: 48043


##################### after bwt
C:\inspection_app_venv\Scripts\python.exe "C:/AdnanKhan/code repository/DataCompression/main.py"
Path to CALGARY dataset: C:\AdnanKhan\code repository\DataCompression\dataset\calgary
Skipped: 2
MTF-bwt book1_bwt --> Free ex: 4686701 AC: 4939123 STD: 4939123 MRM: 4939123 cc_linear: 4939123 cc_log:2362578 Compressed Size: 201192
Skipped: 2
MTF-bwt news_bwt --> Free ex: 3048373 AC: 3200746 STD: 3200746 MRM: 3200746 cc_linear: 3200746 cc_log:1156135 Compressed Size: 99385
Skipped: 1
MTF-bwt progc_bwt --> Free ex: 216557 AC: 233109 STD: 233109 MRM: 233109 cc_linear: 233109 cc_log:85561 Compressed Size: 6763
Skipped: 2
MTF-bwt trans_bwt --> Free ex: 468281 AC: 515175 STD: 515175 MRM: 515175 cc_linear: 515175 cc_log:193034 Compressed Size: 14463

######################

ADVICE RCB
book1.advice - total node 15204 bytes count 1090512 bytes data 95400 total 1185912
news.advice - total node 31360 bytes count 2225680 bytes data 220400 total 2446080
progc.advice - total node 7822 bytes count 518166 bytes data 91950 total 610116
trans.advice - total node 9274 bytes count 620472 bytes data 102900 total 723372

ADVICE CB should be same
book1.cb.advice - total node 15204 bytes count 1090512 bytes data 95400 total 1185912
news.cb.advice - total node 31360 bytes count 2225680 bytes data 220400 total 2446080
progc.cb.advice - total node 7820 bytes count 518060 bytes data 91900 total 609960
trans.cb.advice - total node 9271 bytes count 620338 bytes data 102800 total 723138


