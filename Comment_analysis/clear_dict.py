import re


def get_dict(path, encoding="utf-8"):
    sentiment_dict = {}
    pattern = re.compile(r"\s+")
    with open(path, encoding=encoding) as f:
        for line in f:
            result = pattern.split(line.strip())
            if len(result) == 2:
                sentiment_dict[result[0]] = float(result[1])
    return sentiment_dict

root_filepath = "f_dict/"

positive_dict = get_dict(root_filepath + "positive_dict.txt")
denial_dict = get_dict(root_filepath + "denial_dict.txt")