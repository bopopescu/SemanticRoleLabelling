from allennlp.predictors.predictor import Predictor
predictor = Predictor.from_path("https://s3-us-west-2.amazonaws.com/allennlp/models/srl-model-2018.05.25.tar.gz")

# Extracting relationships for:
#
# In June, an army soldier Aurangzeb of 44 Rashtriya Rifles posted in south Kashmir\x92s Shopian district was
# abducted by militants and his bullet-riddled body was found 10 kilometers away from the place of kidnapping.
# Soon after police came to know about abduction of the soldier, a joint police and army team was send to village
# and search operation was launched in the area.Officials said that Bhat was at his home at Qazipora when some
# unidentified gunmen abducted him from his house.


results = predictor.predict(sentence="In June, an army soldier Aurangzeb of 44 Rashtriya Rifles posted in south Kashmir\x92s Shopian district was abducted by militants and his bullet-riddled body was found 10 kilometers away from the place of kidnapping. Soon after police came to know about abduction of the soldier, a joint police and army team was send to village and search operation was launched in the area.Officials said that Bhat was at his home at Qazipora when some unidentified gunmen abducted him from his house.")
# for word, verb in zip(results["words"], results["verbs"]):
#     print(f"{word} \t {verb}")

for verb in results["verbs"]:
    print(verb["verb"])