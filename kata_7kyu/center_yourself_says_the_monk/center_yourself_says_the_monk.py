def center(strng, width, fill=' '):
    return strng if len(strng) >= width else fill*((width-len(strng)+1)//2) + strng + fill*((width-len(strng))//2)
