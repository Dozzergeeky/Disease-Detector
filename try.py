import difflib

words = ['abdominal_pain', 'abnormal_menstruation', 'acidity', 'acute_liver_failure', 'altered_sensorium', 'anxiety']
# back_pain
# belly_pain
# blackheads
# bladder_discomfort
# blister
# blood_in_sputum
# bloody_stool
# blurred_and_distorted_vision
# breathlessness
# brittle_nails
# bruising
# burning_micturition


# words = ['hello', 'Hallo', 'hi', 'house', 'key', 'screen', 'hallo', 'question', 'format']
new_words = difflib.get_close_matches('', words, n=3, cutoff=0.1)
print(new_words)