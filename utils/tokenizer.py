import re
def tokenizer_en(text):
    """
    from torchtext.data import get_tokenizer
    tokenizer = get_tokenizer("basic_english")
    とした方が性能がいいかも
    """
    text = re.sub("<[^>]*>","",text)
    emoticons = re.findall("(?::|;|=)(?:-)?(?:\)|\(|D|P)",text.lower())
    text = re.sub("[\W]+", " ",text.lower()) + " ".join(emoticons).replace("-","")
    tokenized = text.split()

    return tokenized