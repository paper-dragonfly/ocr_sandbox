import json
  
def get_data():
    # Opening JSON file
    f = open('results.json')
    # returns JSON object as a dictionary
    data = json.load(f)
    print(data)  
    # Closing file
    f.close()
    return data

ocr_dict = get_data() 
print('BREAK')

def basic_clean(data:dict):
    for key in ocr_dict:
        ocr_dict[key] = ocr_dict[key].strip('\n\'"~|°`‘-!')
        ocr_dict[key]=ocr_dict[key].replace("\n", ' ')
        ocr_dict[key]=ocr_dict[key].replace(",", '.')
        s2 = ""
        for i in range(len(ocr_dict[key])):
            if not ocr_dict[key][i] in ['\\','|','-']:
                s2 += ocr_dict[key][i]
        ocr_dict[key] = s2
        if not key == 'date':
            ocr_dict[key]=ocr_dict[key].replace("A", '4')
    return ocr_dict

print(basic_clean(ocr_dict))

