# 'Cleaning' Epigraphia Carnatica for Knowledge Graphs

This repo will contain code and documentation for data cleaning that will be done for **Epigraphia Carnatica** PDFs sourced from [archive.org](https://archive.org/search.php?query=epigraphia%20carnatica)  

The database of 'cleaned' information and APIs to access them is being developed at [REST APIs for Epigraphia Carnatica database](https://github.com/ShreyasKolpe/epigraphia-rest-apis)

## Why does data need to be cleaned?
  

The entire series of Epigraphia Carnatica is available online as part of a digitization project by Microsoft.  
  
The files have been prepared with some basic OCR that recognizes most of the typeset English characters. However, the books record inscriptions in several Indian languages and many scripts. The transliterations in English also make use of an extended character set with diacriritcs to accurately represent the entire phonetic range of the Indian languages. Unfortunately, these characters are not correctly recognized by the OCR system. In addition, the character set used by the publishers at that time varies from the transliteration schemes of nowadays.  
  
Ignoring for now the inscription text in the Indic scripts, the purpose is to make available the text of the translations and transliterations with 'corrections'.  
  
## Process
  

This process (currently manual) involves
1. Copying the text from the PDFs to a text editor.
2. Correcting the text by substituting wrongly identified characters with the correct character from a standard. To validate, the inscription text in Indic script might need to be consulted.
3. Cleaning up any other distortions caused during copying.
4. Saving the corrected text in a database.  

The repo will contain code for eventual automation, after substantial insights gained from the manual process.  

This project uses the relatively large [ISO 15919](https://en.wikipedia.org/wiki/ISO_15919) character set for transliteration keeping in mind future extensibility.  

The table below lists the common substitutions from EC and observations  
  

| Indic Character(s) | EC character  | ISO 15919 character | Comments |
|--------------------|---------------|---------------------|----------|
| ???/???               | ??             | ??                   |          |
| ???/???               | ??             | ??                   |          |
| ???????/???              | ??             | ??                   |          |
| ???/???               | ???             | ???                   | Same character|
| ???                  | ??             | ??                   | Long vowel in Dravidian languages|
| ???                  | ??             | ??                   | Long vowel in Dravidian languages|
|  ???/???              | ???             | ???                   | Final anusvara|
|  ???/???              | ???             | ???                   | Same character|
| ???/???                | ???             | ???                   | Same character|
| ???/???               | ??             | ??                   | Same character|
| ???/???                | ???             | ???                   | Same character|
| ???/???                | ???             | ???                   | Same character|
| ???/???                | ???             | ???                   | Same character|
| ???                  | <img width="11" alt="r_with_two_dots" src="https://user-images.githubusercontent.com/13967444/163586068-5ae9a75f-cac6-4011-a085-bfc3a284d005.png">| ??? | Old Kannada character|
| ???                  | ???             | ???                   |          |
| ???                  | <img width="9" alt="l_with_two_dots" src="https://user-images.githubusercontent.com/13967444/163586110-fa6cebaa-6a75-4905-8d31-b9c61c772116.png">| ???  | Old Kannada character|
| ???/???                  | <img width="13" alt="s_with_left_acute" src="https://user-images.githubusercontent.com/13967444/163586201-4632fac8-8c1d-452a-8105-75b96a14554d.png">| ?? | Used in EC Vol 2, character has fallen into disuse. EC Vol 3 uses ??|
| ???/???                  | ??             | ???                   | Used in EC Vol 2. EC Vol 3 uses compound character of sh |
| ????????? (?????? + ???)/????????? (?????? + ???)| j??            |j??                   | Same characters|


### Example

<img width="650" alt="text_sample" src="https://user-images.githubusercontent.com/13967444/163585979-8b65ab14-748d-4dc0-93f6-df5a25f2c284.png">

is copied as  

**Mallis??na-bhatarara guddain Charengayyam tirtthamain bandisidam**  

and after correction becomes

**Mallis??na-bha?????rara gu??????a??? Cha???e???gayya??? t??rtthama??? bandisida???**  


**Note**:  

Only character level substitutions and corrections are made to render text human-readable and partially standards-compliant. No attempt has been made to make entire translation/transliteration text fully in line with the standard. This might need to be done in the future.  

For example, 
1. ???/??? is written in EC as ???i, such as in k???i?????a. This is retained, instead of changing the original text to k????????a.

2. ???/??? is written in EC Vol 3 as ??, while ???/??? is written as sh. During data cleaning, ?? is corrected but sh is retained.

3. The anusv??ra poses problems. In Sanskrit, this character changes depending on the following consonant. The usage of the ???/??? is also common. Correctness would require consulting the inscription in Indic characters to make sure that the anusv??ra carries over accurately. This is done in a few cases, but ignored in the vast majority.

## Thoughts on automation

1. Some observations from repeatedly cleaning up texts manually could help in automation. 

    For Kannada inscriptions, the following are made:
    * The OCR text consistently copies ?? as ??. Thus, this could be automated. Similarly, it sometimes copies ?? instead of ??.
    * The character sequence ??r?? is very common and can be inserted into a few variants that happen during OCR copying.
    * Largely, the anusv??ra is used properly by the ancient and medieval scribes. So when n is followed by a consonant, the appropriate cluster can be inserted properly.
    * OCR copies ti for ?? quite often. A possible rule would be to search for ti between two consonants. (to implement)
    * Similarly, fi for ??. A rule might be to look for fi between a preceding vowel and a few consonants (k, j). (to implement)

2. A large enough corpus of uncorrected and corrected texts could allow ML/DL to take a go at it.

3. A UI should provide a diff between the original and the automatically corrected and provide an approve/reject mechanism. (to implement)

## Using the software (in-development)

As and when the automation code goes through milestones, it will be released so that it can be used as a UI tool, part 
of [REST APIs for Epigraphia Carnatica database](https://github.com/ShreyasKolpe/epigraphia-rest-apis).

The current version is epiclean==0.0.1 and can be found [here](https://pypi.org/project/epiclean/0.0.1/)

To install, run
```
pip install epiclean
```

Optionally, create a `requirements.txt` with the content
```
epiclean==<version>
```

and install with 
```bash
pip install -r requirements.txt
```