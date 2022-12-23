from translate import Translator
s = Translator(from_lang="en", to_lang="pt-br")
res = s.translate("Hello World!")
print(res)
