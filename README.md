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
|--------------------|---------------|--------------------|----------|
| ಆ/आ               | â             | ā                  |          |
| ಈ/ई               | î             | ī                  |          |
| 󠁲ಊ/ऊ              | û             | ū                  |          |
| ಋ/ऋ               | ṛ             | r̥                   | |
| ಏ                  | é             | ē                  | Long vowel in Dravidian languages|
| ಓ                  | ô             | ō                  | Long vowel in Dravidian languages|
|  ಂ/ं              | ṃ/ṁ             | ṁ                  | Final anusvara|
|  ಃ/ः              | ḥ             | ḥ                  | Same character|
| ಙ/ङ                | ṅ             | ṅ                  | Same character|
| ಞ/ञ               | ñ             | ñ                  | Same character|
| ಟ/ट                | ṭ             | ṭ                  | Same character|
| ಡ/ड                | ḍ             | ḍ                  | Same character|
| ಣ/ण                | ṇ             | ṇ                  | Same character|
| ಱ                  | <img width="11" alt="r_with_two_dots" src="https://user-images.githubusercontent.com/13967444/163586068-5ae9a75f-cac6-4011-a085-bfc3a284d005.png">| ṟ | Old Kannada character|
| ಳ                  | ḷ             | ḷ                  |          |
| ೞ                  | <img width="9" alt="l_with_two_dots" src="https://user-images.githubusercontent.com/13967444/163586110-fa6cebaa-6a75-4905-8d31-b9c61c772116.png">| ḻ  | Old Kannada character|
| ಶ/श                  | <img width="13" alt="s_with_left_acute" src="https://user-images.githubusercontent.com/13967444/163586201-4632fac8-8c1d-452a-8105-75b96a14554d.png">/ś/š| ś | Used in EC Vol 2, character has fallen into disuse. EC Vol 3 uses ś. EC Vol 5 uses š|
| ಷ/ष                  | ś             | ṣ                  | Used in EC Vol 2. EC Vol 3 and later uses compound character of sh |
| ಜ್ಞ (ಜ್ + ಞ)/ज्ञ (ज् + ञ)| jñ            |jñ                  | Same characters|


### Example

<img width="650" alt="text_sample" src="https://user-images.githubusercontent.com/13967444/163585979-8b65ab14-748d-4dc0-93f6-df5a25f2c284.png">

is copied as  

**Malliséna-bhatarara guddain Charengayyam tirtthamain bandisidam**  

and after correction becomes

**Mallisēna-bhaṭārara guḍḍaṁ Chaṟeṅgayyaṁ tīrtthamaṁ bandisidaṁ**  


**Note**:  

Only character level substitutions and corrections are made to render text human-readable and partially standards-compliant. No attempt has been made to make entire translation/transliteration text fully in line with the standard. This might need to be done in the future.  

For example, 
1. ಋ/ऋ is written in EC as ṛi, such as in kṛiṣṇa. This is retained, instead of changing the original text to kṛṣṇa.

2. ಶ/श is written in EC Vol 3 as ś, while ಷ/ष is written as sh. During data cleaning, ś is corrected but sh is retained.

3. ಚ/च is represented in EC as ch. This is retained instead of correcting to the standards compliant c. Similarly ಛ/छ is retained as chh and not corrected to ch.

3. The anusvāra/anunāsikā poses problems. In Sanskrit, this character changes depending on the succeeding consonant. The usage of the ಂ/ं is also common. Correctness would require consulting the inscription in Indic characters to make sure that the anusvāra carries over accurately. This is done in a few cases, but ignored in the vast majority.

## Thoughts on automation

1. Some observations from repeatedly cleaning up texts manually could help in automation. 

    For Kannada inscriptions, the following are made:
    * The OCR text consistently copies ē as é. Thus, this could be automated. 
    * Similarly, it sometimes copies ô/ó instead of ō.
    * In some texts, â is copied as à or á. This could also be automated to replace these two characters with ā.
    * The $ and & characters are inserted by the OCR in place of ś. This can be easily identified and corrected. Similarly, S' might actually represent Ś.
    * The character sequence śrī is very common and can be inserted into a few variants that happen during OCR copying.
    * Largely, the anunāsikas is used properly by the ancient and medieval scribes. So when n is followed by a consonant, the appropriate cluster can be inserted properly.
    * OCR copies ti and ü for ū quite often. A possible rule would be to search for ti between two consonants. (to implement)
    * Similarly, fi for ñ. A rule might be to look for fi between a preceding vowel and a few consonants (c, j).
    * The character sequence śrī is very common and can be inserted into a few variants that happen during OCR copying.
    * An m at the end of a word or word in a compound-word-sequence, is possibly an ṁ if it is followed by a consonant (inscluding the extension characters, eg. ś).

2. A large enough corpus of uncorrected and corrected texts could allow ML/DL to take a go at it.

3. A UI should provide a diff between the original and the automatically corrected and provide an approve/reject mechanism. (to implement)

## Using the software (in-development)

As and when the automation code goes through milestones, it will be released so that it can be used as a UI tool, part 
of [REST APIs for Epigraphia Carnatica database](https://github.com/ShreyasKolpe/epigraphia-rest-apis).

The current version is epiclean==0.0.2 and can be found [here](https://pypi.org/project/epiclean/)

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