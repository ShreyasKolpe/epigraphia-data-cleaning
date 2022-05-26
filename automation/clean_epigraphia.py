import re


def processor(input, lang, e, s, n):
    if lang == 'kn':
        output = None
        if e:
            output = re.sub('é', 'ē', input)
        if s:
            output = re.sub('[sS$gé]ri', 'śrī', input)
        if n:
            output = re.sub('nk', 'ṅk', input)
            output = re.sub('ng', 'ṅg', output)

            output = re.sub('nc', 'ñc', output)
            output = re.sub('nj', 'ñj', output)

            output = re.sub('nṭ', 'ṇṭ', output)
            output = re.sub('nḍ', 'ṇḍ', output)
            # print(output)
        return output
    else:
        return None
