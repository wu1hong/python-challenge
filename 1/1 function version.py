text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
new_text=""
for x in text:
    if x >= 'a' and x <= 'z':
        new_text += chr((ord(x) - 95) % 26 + 97)
    else:
        new_text += x
print new_text


