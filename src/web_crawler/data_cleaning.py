
def convert_sting_to_int(number_str : str) -> int:
    return int(number_str.replace(" ", ""))

def clean_string_data(data_string : str):
    return data_string.upper().strip().strip(":")

