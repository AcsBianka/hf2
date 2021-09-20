pentek_van = "péntek van"
length_pentek_van = len("péntek van")
print(length_pentek_van)

print(pentek_van[0:6]*7)

str2 = "hegy"
str3 = "tananyag"
str4 = "Hiába a hegynyi anyag, a hallgató gyorsan halag."

str4_contain_str2 = str2 in str4
print("A mondat tartalmazza a hegy szót: ", str4_contain_str2)

str4_contain_str3 = str3 in str4
print("A mondat tartalmazza a tananyag szót: ", str4_contain_str3)

word_one = "alma"
word_two = "Alma"
examine_word_one_and_word_two = word_one == word_two
print("Az alma és Alma azonos: ", examine_word_one_and_word_two)

compare_word_one_and_word_two = word_one > word_two
print("alma és Alma összehasonlításának eredménye: ", compare_word_one_and_word_two)
