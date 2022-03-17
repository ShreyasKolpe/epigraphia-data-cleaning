# 'Cleaning' Epigraphia Carnatica for Knowledge Graphs

This repo will contain code and documentation for data cleaning that will be done for **Epigraphia Carnatica** PDFs sourced from [archive.org](https://archive.org/search.php?query=epigraphia%20carnatica)  


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
| ಆ/आ               | â             | ā                   |          |
| ಈ/ई               | î             | ī                   |          |
| 󠁲ಊ/ऊ              | û             | ū                   |          |
| ಋ/ऋ               | ṛ             | ṛ                   | Same character|
| ಏ                  | é             | ē                   | Long vowel in Dravidian languages|
| ಓ                  | ô             | ō                   | Long vowel in Dravidian languages|
|  ಂ/ं                | ṃ             | ṁ                   | Final anusvara|
|  ಃ/ः                | ḥ             | ḥ                   | Same character|
| ಙ/ङ                | ṅ             | ṅ                   | Same character|
| ಟ/ट                | ṭ             | ṭ                   |          |
| ಡ/ड                | ḍ             | ḍ                   |          |
| ಣ/ण                | ṇ             | ṇ                   |          |
| ಱ                  | ![](/images/r_with_two_dots.png)| ṟ | Old Kannada character|
| ಳ                  | ḷ             | ḷ                   |          |
| ೞ                  | ![](/images/l_with_two_dots.png)| ḻ  | Old Kannada character|
| ಶ/श                  | ![](/images/s_with_left_acute.png)| ś | Character has fallen into disuse|
| ಷ/ष                  | ś             | ṣ                   |          |
| ಜ್ಞ (ಜ್ + ಞ)/ज्ञ (ज् + ञ)| jñ            |jñ                   | Same characters|


### Example

![](/images/text_sample.png)  

is copied as  

**Malliséna-bhatarara guddain Charengayyam tirtthamain bandisidam**  

and after correction becomes

**Mallisēna-bhaṭārara guḍḍaṁ Chaṟeṅgayyaṁ tīrtthamaṁ bandisidaṁ**  


**Note**:  

Only character level substitutions and corrections are made to render text human-readable and partially standards-compliant. No attempt has been made to make entire translation/transliteration text fully in line with the standard. This might need to be done in the future.  

For example, ಋ/ऋ is written in EC as ṛi, such as in kṛiśṇa. This is retained, instead of changing the original text to kṛśṇa.