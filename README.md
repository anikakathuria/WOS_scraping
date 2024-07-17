# Scraping the Web of Science Database

Here is a guide to using python scripts to help in searching Web of Science for hundreds of different fossil fuel companies’ affiliations with your school without access to their API. The searching itself will still have to be manual, but these scripts will help you automatically generate queries (each is a group of 49 companies – the maximum terms per search on WOS) and then consolidate all your results. For Columbia this was able to garner almost 850 results!

You will have to use the terminal and have python installed but even if you are not familiar with coding, this guide should be fairly straightforward and you shouldn’t have to code at all!

Please reach out to me (Anika Kathuria, ak4748@columbia.edu, (908) 635-2451) if you have any questions or run into any issues!!

Note: All of my results are uploaded here to look at an example, but delete those files if you want to have the same names for your own or just replace them as you generate your own. 

## Steps:

1. Download the ZIP file of this repository and unzip it. For the rest of the guide I’ll refer to this as the `WOS_Scraping` folder
2. Install python
Make sure that python works. Open “Terminal” and type “python3” then click enter…
You should see something like 

```
Python 3.9.6 (default, Feb  3 2024, 15:58:27) 
[Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

If you see something like
```
 zsh: command not found: python3
 ```
Then it isn’t installed. 


3. Open Terminal into the `WOS_scraping` folder
If you don’t know how to use the terminal, you can right click on the folder Finder and select “New Terminal at Folder”

**NOTE:** if you are using GOGEL (Global Oil and Gas Exit List)  and GCEL (Global Coal Exit List) as your lists of fossil fuel companies, you can skip steps 4 and 5 and use the folder titled “cleaned_queries” as your folder of cleaned queries directly. (Since I have already done this process on them). If you are using other lists, read the details on the instructions carefully to get the format to match the expected format of your lists. 

4. Generating Queries:
   
This is to generate the groups of 49 companies as search terms (each company in quotes separated by 'OR')

We will be using the script `generate_queries.py` in the `scripts` folder. The general usage of this script is:
```
python3 generate_queries.py <excel_file> <sheet_name> <column_name> <output_file>
```

Notes:
The script expects that your list of companies is contained in an excel file column and the column name is listed in the 4th row. If this is different, change the “header=3” in line 7 to the row number the column name is at minus 1 (e.g. if your column name is on row 1 put 0). 

Example usage with a terminal opened in `WOS_scraping`:
```
python3 scripts/generate_queries.py “GOGEL.xlsx” “Upstream” “Company Name” uncleaned_queries/GOGEL_upstream.txt
```
Typing the above into terminal will run `generate_queries.py` in the scripts folder, look through the 'Upstream' Sheet in `GOGEL.xlsx`, and group every item under the “Company Column” into groups of 49 where each term is in quotes and separated by the word OR and place these results into `uncleaned_queries/GOGEL_upstream.txt`. Each line in this output text file is a group of 49 terms. 

For example, line 1 of `GOGEL_upstream.txt` is:
```
"1876 Resources LLC" OR "88 Energy Ltd" OR "89 Energy III LLC" OR "AAG Energy Holdings Ltd" OR "Abu Dhabi National Energy Company PJSC (TAQA)" OR "Abu Dhabi National Oil Company (ADNOC)" OR "Adani Welspun Exploration Ltd" OR "Advantage Energy Ltd" OR "Aethon Energy Management LLC" OR "Africa Oil Corp" OR "Ageron Energy LLC  " OR "Aker BP ASA" OR "Alpine Summit Energy Partners Inc" OR "Alvopetro Energy Ltd" OR "Ameredev II LLC" OR "Amni International Petroleum Development Company Ltd" OR "Amplify Energy Corp" OR "Anschutz Exploration Corporation" OR "Antelopus Energy Pvt Ltd" OR "Antero Resources Corporation" OR "APA Corporation" OR "Apex Energy LLC" OR "Apex International Energy Management LLC" OR "APR Operating LLC (Admiral Permian Resources)" OR "ARAR Oil & Gas Inc" OR "ARC Resources Ltd" OR "Arsenal Resources LLC" OR "Artis Exploration Ltd" OR "Ascent Resources LLC" OR "Aspenleaf Energy Ltd" OR "Athabasca Oil Corporation" OR "Atlas Petroleum International Ltd" OR "Avant Natural Resources LLC" OR "Azule Energy Holdings Ltd" OR "Ballard Petroleum Holdings LLC " OR "Banco BTG Pactual SA" OR "Bangladesh Oil, Gas & Mineral Corporation (Petrobangla)" OR "Bapco Energies BSC" OR "Basra Oil Company (BOC)" OR "Battalion Oil Corporation " OR "Bayswater Exploration and Production LLC" OR "Baytex Energy Corp" OR "BCE-Mach LLC" OR "Beach Energy Ltd" OR "Beacon Offshore Energy LLC" OR "Bedrock Energy Partners LLC" OR "Belemaoil Producing Ltd" OR "Benchmark Energy LLC" OR "Berry Corporation (bry)"
```

5. Cleaning Queries:
   
This is to clean the queries of the various corporation endings (Ltd, LLC, Corporation...etc) because I had noticed significantly fewer results when they were included (probably due to naming discrepancies). It also goes through items contained in paranthesis in these company names because they were also messing with the results, but these terms are appended as an additional line at the end just in case they have their own results.

We will be using the script `clean_queries.py` in the `scripts` folder. The general usage of this script is:
```
python3 clean_queries.py <input_file> <output_file>
```

Example Usage with a terminal opened in `WOS_scraping`:
```
python3 scripts/clean_queries.py uncleaned_queires/GOGEL_upstream.txt cleaned_queries/GOGEL_upstream.txt
```

This will read in the `GOGEL_upstream.txt` file previously created in the `uncleaned_queries` folder, clean it, and put the result in `cleaned_queries/GOGEL_upstream_cleaned.txt`

For example, line 1 of `GOGEL_upstream_cleaned.txt` is:
```
"1876 Resources " OR "88 Energy " OR "89 Energy III " OR "AAG Energy Holdings " OR "Abu Dhabi National Energy PJSC " OR "Abu Dhabi National Oil " OR "Adani Welspun Exploration " OR "Advantage Energy " OR "Aethon Energy Management " OR "Africa Oil " OR "Ageron Energy " OR "Aker BP ASA" OR "Alpine Summit Energy Partners " OR "Alvopetro Energy " OR "Ameredev II " OR "Amni International Petroleum Development " OR "Amplify Energy " OR "Anschutz Exploration " OR "Antelopus Energy Pvt " OR "Antero Resources " OR "APA " OR "Apex Energy " OR "Apex International Energy Management " OR "APR Operating " OR "ARAR Oil & Gas " OR "ARC Resources " OR "Arsenal Resources " OR "Artis Exploration " OR "Ascent Resources " OR "Aspenleaf Energy " OR "Athabasca Oil " OR "Atlas Petroleum International " OR "Avant Natural Resources " OR "Azule Energy Holdings " OR "Ballard Petroleum Holdings " OR "Banco BTG Pactual " OR "Bangladesh Oil, Gas & Mineral " OR "Bapco Energies BSC" OR "Basra Oil " OR "Battalion Oil " OR "Bayswater Exploration and Production " OR "Baytex Energy " OR "BCE-Mach " OR "Beach Energy " OR "Beacon Offshore Energy " OR "Bedrock Energy Partners " OR "Belemaoil Producing " OR "Benchmark Energy " OR "Berry "
```

6. Searching WOS and Saving Results:
   
Now that the cleaned queries are generated, its time to search with them in Web of Science. This is the manual process -- go to Web of Science and copy each of the lines into the "Funding Agency" searchbar and put your school into "Affiliation". Each time, if there are any results, click:
- Export
- Excel
- Click Record Content, Edit the Custom Selection
- Choose whichever you want, make sure to select Funding Information (which is not automatic)
- For example, I had just chosen Author, Title, Source, Conf.Info/Sponsors, ISSN, PubMed ID, and Funding Information -- if you're doing this all at once, you should only have to select this once and it will maintain for all your searches

Save it into a folder, and I suggest maintaining high organization in this process. For example, I saved all the results corresponding to a single sheet (e.g. GOGEL Upstream or GOGEL Midstream) in their own folder, where every individual Excel export was named the number line of the queries I was searching. This made it a lot easier for me to go back and trace certain queries and funding information, all the way back to the lists. 
You can look into "WOS_results" to see my results (for Columbia University) and how they are organized. 

Make sure what you have selected to save into the Excel file is the same every time. 

7. Consolidating Results:
   
Now we want to combine all the different results and get rid of any duplicates which there are sure to be. For this we use `scripts\consolidate_files.py`
The general usage of this file is:
```
python3 consolidate_files.py <root_folder> <output_file>
```

Example Usage with a terminal opened in `WOS_scraping`:
```
python3 scripts/consolidate_files.py WOS_results "all_WOS_results.xlsx"
```

This will go through every xls file (how WOS exports the excel files) in `cleaned_queries` folder (even if they are within even deeper folders) and consollidates it into one large file, `all_WOS_results.xlsx` with the duplicates removed. 

### Optional additional scripts:

8. Reformatting Columns:
   
If you want to reformat the column order of this excel file, the script `scripts/reorganize_columns.py` will help you do that. For our group, we had come up with a format we wanted all of our results to follow beforehand with a certain order of columns, so this script currently reformats the excel file into the following column order:
```
Funder	Donation Amount	Year	Type of Donations: (gift, sponsored projects...)	Columbia school	Columbia Affiliates	Which Specific Columbia Program?	Source	Specific Study DOI	Notes	Author Full Names	Article Title	Source Title	Affiliations	Funding Text	ISSN										
```
Many of them also remain blank because there was no WOS information for those columns, but this is how `reorganize_columns.py` is set up right now. Feel free to tweak it for your needs. 

General Usage:
```
python3 reorganize_columns.py <input_file> <output_file>
```

Example Usage:
```
python3 scripts/reorganize_columns.py "all_WOS_results.xlsx" "all_WOS_results_standardized.xlsx"
```

9. Search:
    
This is just a helpful file to search for any term in your `WOS_results` folder full of excel files. I had a gap in funder information in my final resutls and figured out where it was by using the `scripts/search.py` file, was able to easily access which query I had used that had produced that excel file with the gaps due to the naming organization in my query folders, re-search, and re-consolidate!

General usage:
```
python3 search_excel.py <folder_path> <search_term>
```


Additional Note:
Something we noticed was that some companies have the same names as others and might show up as funding research when the actual company funding is not fossil fuel related. One example is APA, because APA Corporation is a fossil fuel company and the APA is the American Psychological Association. Cleaning the company names makes it possible for most results to reveal but I do recommend manually skimming your results and making sure that there is always a fossil fuel funder before publishing them. 


