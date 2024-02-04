import re

# template to remove html tags
clearn = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')


def cleanhtml(raw_html):
    cleantext = re.sub(clearn, '', raw_html)

    # remove quoters
    # cleantext = re.sub('“|”|"', '', cleantext)
    cleantext = re.sub('[“”"]', '', cleantext)

    # remove all text after first dot or "?"
    # return re.sub('(?<=\.|\?).*', '', cleantext)
    return re.sub('(?<=[.?]).*', '', cleantext)


if __name__ == '__main__':
    assert cleanhtml("Button. Stephen King. Dolan.Cadillac.") == 'Button.'
    assert cleanhtml("Animal? Dog. Fox. Bird?") == 'Animal?'
    assert cleanhtml(
        '<span style="color: rgba(26, 38, 51, 0.6); background-color: rgb(255, 255, 255);">"mozegett"</span>') == 'mozegett'
    assert cleanhtml(
        '<div><div><div><div><div><span style="color: rgba(26, 38, 51, 0.6);">ett</span></div></div></div></div></div>') == 'ett'
