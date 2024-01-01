import re

clearn = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')


def cleanhtml(raw_html):
    cleantext = re.sub(clearn, '', raw_html)

    # remove quoters
    cleantext = re.sub('“|”', '', cleantext)
    return cleantext



if __name__ == '__main__':
    # line_to_clear = '<div><div><div><div><div><span style="color: rgba(26, 38, 51, 0.6);">ett</span></div></div></div></div></div>'
    # line_to_clear = '<span style="color: rgba(26, 38, 51, 0.6); background-color: rgb(255, 255, 255);">"mozegett"</span>'
    line_to_clear ='“BAD ATTITUDE, the shirt proclaimed.”'
    print(cleanhtml(line_to_clear))


