import csv
mapper = {
    'ሀ': "ha",
    'ሁ': "hu",
    'ሂ': "hi",
    'ሃ': "ha",
    'ሄ': "he",
    'ህ': "h", 
    'ሆ': "ho",

    'ለ': "le",
    'ሉ': "lu",
    'ሊ': "li",
    'ላ': "la",
    'ሌ': "le",
    'ል': "l", 
    'ሎ': "lo",

    'ሐ': "ha",
    'ሑ': "hu",
    'ሒ': "hi",
    'ሓ': "ha",
    'ሔ': "he",
    'ሕ': "h",  
    'ሖ': 'ho',

    'መ': "me",
    'ሙ': "mu",
    'ሚ': "mi",
    'ማ': "ma",
    'ሜ': "me",
    'ም': "m",  
    'ሞ': "mo",

    'ሠ': "se",
    'ሡ': "su",
    'ሢ': "si",
    'ሣ': "sa",
    'ሤ': "se",
    'ሥ': "s",  # repeat for different form
    'ሦ': "so",

    'ረ': "re",
    'ሩ': "ru",
    'ሪ': "ri",
    'ራ': "ra",
    'ሬ': "re",
    'ር': "r",  # repeat for different form
    'ሮ': "ro",

    'ሰ': 'se',
    'ሱ': 'su',
    'ሲ': 'si',
    'ሳ': 'sa',
    'ሴ': 'se',
    'ስ': 's',  
    'ሶ': 'so',

    'ሸ': 'she',
    'ሹ': 'shu',
    'ሺ': 'shi',
    'ሻ': 'sha',
    'ሼ': 'she',
    'ሽ': 'sh',  
    'ሾ': 'sho',

    'ቀ': 'ke',
    'ቁ': 'ku',
    'ቂ': 'ki',
    'ቃ': 'ka',
    'ቄ': 'ke',
    'ቅ': 'k',  
    'ቆ': 'ko',

    'ቐ': 'qe',
    'ቑ': 'qu',
    'ቒ': 'qi',
    'ቓ': 'qa',
    'ቔ': 'qe',
    'ቕ': 'q',  
    'ቖ': 'qo',

    'በ': 'be',
    'ቡ': 'bu',
    'ቢ': 'bi',
    'ባ': 'ba',
    'ቤ': 'be',
    'ብ': 'b',  # repeat for different form
    'ቦ': 'bo',

    'ተ': 'te',
    'ቱ': 'tu',
    'ቲ': 'ti',
    'ታ': 'ta',
    'ቴ': 'te',
    'ት': 't',  # repeat for different form
    'ቶ': 'to',
    'ቸ': 'cha' ,
    'ቹ': 'chu',
    'ቺ': 'chi',
    'ቻ': 'cha',
    'ቼ': 'che',
    'ች': 'ch',  # repeat for different form
    'ቾ': 'cho',
    'ኀ': 'ha',
    'ኁ': 'hu',
    'ኂ': 'hi',
    'ኃ': 'ha',
    'ኄ': 'he',
    'ኅ': 'h',  # repeat for different form
    'ኆ': 'ho',
    'ነ': 'ne',
    'ኑ': 'nu',
    'ኒ': 'ni',
    'ና': 'na',
    'ኔ': 'ne',
    'ን': 'n',  # repeat for different form
    'ኖ': 'no',
        
    'ኘ': 'gne',
    'ኙ': 'gnu',
    'ኚ': 'gni',
    'ኛ': 'gna',
    'ኜ': 'gne',
    'ኝ': 'gn',  # repeat for different form
    'ኞ': 'gno',

    'አ': 'a',
    'ኡ': 'u',
    'ኢ': 'i',
    'ኣ': 'a',
    'ኤ': 'e',
    'እ': 'e',  # repeat for different form
    'ኦ': 'o',

    'ከ': 'ke',
    'ኩ': 'ku',
    'ኪ': 'ki',
    'ካ': 'ka',
    'ኬ': 'ke',
    'ክ': 'k',  # repeat for different form
    'ኮ': 'ko',

    'ኸ': 'khe',
    'ኹ': 'khu',
    'ኺ': 'khi',
    'ኻ': 'kha',
    'ኼ': 'khe',
    'ኽ': 'kh',  # repeat for different form
    'ኾ': 'kho',

    'ወ': 'we',
    'ዉ': 'wu',
    'ዊ': 'wi',
    'ዋ': 'wa',
    'ዌ': 'we',
    'ው': 'w',  # repeat for different form
    'ዎ': 'wo',

    'ዐ': 'a',
    'ዑ': 'u',
    'ዒ': 'i',
    'ዓ': 'a',
    'ዔ': 'e',
    'ዕ': 'e',  # repeat for different form
    'ዖ': 'o',

    'ዘ': 'ze',
    'ዙ': 'zu',
    'ዚ': 'zi',
    'ዛ': 'za',
    'ዜ': 'ze',
    'ዝ': 'z',  # repeat for different form
    'ዞ': 'zo',

    'ዠ': 'zhe',
    'ዡ': 'zhu',
    'ዢ': 'zhi',
    'ዣ': 'zha',
    'ዤ': 'zhe',
    'ዥ': 'zh',  # repeat for different form
    'ዦ': 'zho',
    'ገ': 'ge',
    'ጉ': 'gu',
    'ጊ': 'gi',
    'ጋ': 'ga',
    'ጌ': 'ge',
    'ግ': 'ge',  # repeat for different form
    'ጎ': 'go',

    'ጸ': 'tse',
    'ጹ': 'tsu',
    'ጺ': 'tsi',
    'ጻ': 'tsa',
    'ጼ': 'tse',
    'ጽ': 'tse',  # repeat for different form
    'ጾ': 'tso',

    'ጠ': 'te',
    'ጡ': 'tu',
    'ጢ': 'ti',
    'ጣ': 'ta',
    'ጤ': 'te',
    'ጥ': 'te',  # repeat for different form
    'ጦ': 'to',

    'ፐ': 'pe',
    'ፑ': 'pu',
    'ፒ': 'pi',
    'ፓ': 'pa',
    'ፔ': 'pe',
    'ፕ': 'pe',  # repeat for different form
    'ፖ': 'po',

    'ፀ': 'tse',
    'ፁ': 'tsu',
    'ፂ': 'tsi',
    'ፃ': 'tsa',
    'ፄ': 'tse',
    'ፅ': 'tse',  # repeat for different form
    'ፆ': 'tso',

    'ፈ': 'fe',
    'ፉ': 'fu',
    'ፊ': 'fi',
    'ፋ': 'fa',
    'ፌ': 'fe',
    'ፍ': 'f',  # repeat for different form
    'ፎ': 'fo',
    'ጰ' : 'pe',
    'ጱ' : 'pu',
    'ጲ' : 'pi',
    'ጳ' : 'pa',
    'ጴ ' : 'pe',
    'ጵ' : 'pe',
    'ጶ' : 'po',
    "ጨ":"che",
    "ጩ":"chu",
    "ጪ":"chi",
    "ጫ":"cha",
    "ጬ":"che",
    "ጭ":"ch",
    "ጮ":"cho",
    "ኧ":"e",
    'ሟ' : 'mua',
    'ሿ' : 'shua',
    "ሏ"	: "lwa", 
    "ቧ" :"bwa", 
    "ዟ": "zwa", 
    "ጧ": "twa",
    "ቷ" :"twa", 
    "ዧ" :"zwa",
    "ጯ" :"chwa",
    "ቿ": "chua", 
    "ጿ" :"tswa",
    "ሷ": "swa", 
    "ኗ" :"nwa",
    "ዷ" :"dwa",
    "ኟ" :"gnwa",
    "ጇ": "jwa", 
    "ፏ":"fua"
}



def convert_word(word):
    converted_word = ""
    for char in word:
        converted_char = mapper.get(char, "")
        if not converted_char:
            return ""
        converted_word += converted_char
    return converted_word

def main():
    with open('amh2.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
        
    converted_data = []
    for row in data:
        words = row[1].split()
        converted_words = [convert_word(word) for word in words]
        converted_data.append([row[0], ' '.join(converted_words)])
    
    with open('mix.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(converted_data)

if __name__ == "__main__":
    main()
