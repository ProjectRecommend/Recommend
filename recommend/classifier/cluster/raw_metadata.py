from mutagen.id3 import ID3


def getRawMetadata(mp3file):
    metaText = []

    audio = ID3(mp3file)
    tags = audio.items()

    for tag in tags:
        if tag[0] == 'APIC:':
            # pass
            print("cover art image")
            # this is becuse we don't want to parse Cover Art image as Text'
        else:
            # print("\n")
            print(str(tag[0]).encode(encoding='utf_8'))
            print(str(tag[1]).encode(encoding='utf_8'))
            metaText.append(str(tag[1]).encode(encoding='utf_8'))
    return metaText
