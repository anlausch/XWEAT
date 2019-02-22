import numpy as np
import random
from itertools import filterfalse
from itertools import combinations
import codecs
from scipy.spatial import distance
import utils
import os

class WEAT(object):
  """
  Perform WEAT (Word Embedding Association Test) bias tests on a language model.
  Follows from Caliskan et al 2017 (10.1126/science.aal4230).

  Credits: Basic implementation based on https://gist.github.com/SandyRogers/e5c2e938502a75dcae25216e4fae2da5
  """

  def weat_1(self):
    """
    WEAT 1 (universally accepted): Targets 1=Flowers, Targets 2=Insects, Attributes 1=pleasant, Attributes 2=unpleasant
    :return: targets_1, targets_2, attributes_1, attributes_2
    """
    targets_1 = ["aster", "clover", "hyacinth", "marigold", "poppy", "azalea", "crocus", "iris", "orchid", "rose",
               "blue-bell", "daffodil", "lilac", "pansy", "tulip", "buttercup", "daisy", "lily", "peony", "violet",
               "carnation", "gladiola", "magnolia", "petunia", "zinnia"]
    targets_2 = ["ant", "caterpillar", "flea", "locust", "spider", "bedbug", "centipede", "fly", "maggot", "tarantula",
               "bee", "cockroach", "gnat", "mosquito", "termite", "beetle", "cricket", "hornet", "moth", "wasp",
               "blackfly",
               "dragonfly", "horsefly", "roach", "weevil"]
    attributes_1 = ["caress", "freedom", "health", "love", "peace", "cheer", "friend", "heaven", "loyal", "pleasure",
                "diamond", "gentle", "honest", "lucky", "rainbow", "diploma", "gift", "honor", "miracle", "sunrise",
                "family",
                "happy", "laughter", "paradise", "vacation"]
    attributes_2 = ["abuse", "crash", "filth", "murder", "sickness", "accident", "death", "grief", "poison", "stink",
                  "assault", "disaster", "hatred", "pollute", "tragedy", "divorce", "jail", "poverty", "ugly", "cancer",
                  "kill", "rotten",
                  "vomit", "agony", "prison"]
    return targets_1, targets_2, attributes_1, attributes_2


  # WEAT 2: Target 1=Musical instruments, Target 2= Weapons, Attributes 1: pleasant, Attributes 2=unpleasant
  def weat_2(self):
    targets_1 = ["bagpipe", "cello", "guitar", "lute", "trombone", "banjo", "clarinet", "harmonica", "mandolin",
                 "trumpet", "bassoon", "drum", "harp", "oboe", "tuba", "bell", "fiddle", "harpsichord", "piano",
                 "viola", "bongo",
                 "flute", "horn", "saxophone", "violin"]
    targets_2 = ["arrow", "club", "gun", "missile", "spear", "axe", "dagger", "harpoon", "pistol", "sword", "blade",
             "dynamite", "hatchet", "rifle", "tank", "bomb", "firearm", "knife", "shotgun", "teargas", "cannon",
             "grenade",
             "mace", "slingshot", "whip"]
    attributes_1 = ["caress", "freedom", "health", "love", "peace", "cheer", "friend", "heaven", "loyal", "pleasure",
                "diamond", "gentle", "honest", "lucky", "rainbow", "diploma", "gift", "honor", "miracle", "sunrise",
                "family", "happy", "laughter", "paradise", "vacation"]
    attributes_2 = ["abuse", "crash", "filth", "murder", "sickness", "accident", "death", "grief", "poison", "stink",
                  "assault", "disaster", "hatred", "pollute", "tragedy", "divorce", "jail", "poverty", "ugly", "cancer",
                  "kill", "rotten",
                  "vomit", "agony", "prison"]

    return targets_1, targets_2, attributes_1, attributes_2


  # Here they deleted the infrequent african american names, and the same number randomly choosen from the european american names
  def weat_3(self):
    # excluded as in the original paper: Chip, Ian, Fred, Jed, Todd, Brandon, Wilbur, Sara, Amber, Crystal, Meredith, Shannon, Donna,
    # Bobbie-Sue, Peggy, Sue-Ellen, Wendy
    targets_1 = ["Adam", "Harry", "Josh", "Roger", "Alan", "Frank", "Justin", "Ryan", "Andrew", "Jack", "Matthew", "Stephen",
                 "Brad", "Greg", "Paul", "Hank", "Jonathan", "Peter", "Amanda", "Courtney", "Heather", "Melanie",
                 "Katie", "Betsy", "Kristin", "Nancy", "Stephanie", "Ellen", "Lauren",  "Colleen", "Emily", "Megan", "Rachel"]

    # excluded: Lerone, Percell, Rasaan, Rashaun, Everol, Terryl, Aiesha, Lashelle, Temeka, Tameisha, Teretha, Latonya, Shanise,
    # Sharise, Tashika, Lashandra, Shavonn, Tawanda,
    targets_2 = ["Alonzo", "Jamel",  "Theo", "Alphonse", "Jerome", "Leroy", "Torrance", "Darnell", "Lamar", "Lionel",
                 "Tyree", "Deion", "Lamont", "Malik", "Terrence", "Tyrone",  "Lavon", "Marcellus", "Wardell", "Nichelle",
                 "Shereen", "Ebony", "Latisha", "Shaniqua", "Jasmine", "Tanisha", "Tia", "Lakisha", "Latoya",  "Yolanda",
                 "Malika",  "Yvette"]

    attributes_1 = ["caress", "freedom", "health", "love", "peace", "cheer", "friend", "heaven", "loyal", "pleasure",
                "diamond", "gentle", "honest", "lucky", "rainbow", "diploma", "gift", "honor", "miracle", "sunrise",
                "family", "happy", "laughter", "paradise", "vacation"]

    # same as before but agony and prison are replaced with bomb and evil
    attributes_2 = ["abuse", "crash", "filth", "murder", "sickness", "accident", "death", "grief", "poison", "stink",
                  "assault", "disaster", "hatred", "pollute", "tragedy", "divorce", "jail", "poverty", "ugly", "cancer",
                  "kill", "rotten",
                  "vomit", "bomb", "evil"]

    return targets_1, targets_2, attributes_1, attributes_2


  # again: african american names vs. european american names and pleasant vs unpleasant but with different names
  def weat_4(self):
    # excluded as in the original paper: Jay, Kristen, (here only excluded in the glove experiments)
    targets_1 = ["Brad", "Brendan", "Geoffrey", "Greg", "Brett",  "Matthew", "Neil", "Todd", "Allison", "Anne",
                 "Carrie", "Emily", "Jill", "Laurie",  "Meredith", "Sarah"]

    # excluded in GloVe experiments:  Tremayne, Latonya,
    targets_2 = ["Darnell", "Hakim", "Jermaine", "Kareem", "Jamal", "Leroy", "Rasheed", "Tyrone", "Aisha", "Ebony",
                 "Keisha", "Kenya",  "Lakisha", "Latoya", "Tamika", "Tanisha"]

    attributes_1 = ["caress", "freedom", "health", "love", "peace", "cheer", "friend", "heaven", "loyal", "pleasure",
                    "diamond", "gentle", "honest", "lucky", "rainbow", "diploma", "gift", "honor", "miracle", "sunrise",
                    "family", "happy", "laughter", "paradise", "vacation"]

    # same as before but agony and prison are replaced with bomb and evil
    attributes_2 = ["abuse", "crash", "filth", "murder", "sickness", "accident", "death", "grief", "poison", "stink",
                    "assault", "disaster", "hatred", "pollute", "tragedy", "divorce", "jail", "poverty", "ugly",
                    "cancer",
                    "kill", "rotten",
                    "vomit", "bomb", "evil"]

    return targets_1, targets_2, attributes_1, attributes_2


  # again african american vs european american names, but with different attributes
  def weat_5(self):
    # excluded as in the original paper: Jay, Kristen, (here only excluded in the glove experiments)
    targets_1 = ["Brad", "Brendan", "Geoffrey", "Greg", "Brett",  "Matthew", "Neil", "Todd", "Allison", "Anne",
                 "Carrie", "Emily", "Jill", "Laurie",  "Meredith", "Sarah"]

    # excluded in GloVe experiments:  Tremayne, Latonya,
    targets_2 = ["Darnell", "Hakim", "Jermaine", "Kareem", "Jamal", "Leroy", "Rasheed", "Tyrone", "Aisha", "Ebony",
                 "Keisha", "Kenya",  "Lakisha", "Latoya", "Tamika", "Tanisha"]

    attributes_1 = ["joy", "love", "peace", "wonderful", "pleasure", "friend", "laughter", "happy"]

    attributes_2 = ["agony", "terrible", "horrible", "nasty", "evil", "war", "awful", "failure"]

    return targets_1, targets_2, attributes_1, attributes_2


  # sex- career
  def weat_6(self):
    targets_1 = ["John", "Paul", "Mike", "Kevin", "Steve", "Greg", "Jeff", "Bill"]
    targets_2 = ["Amy", "Joan", "Lisa", "Sarah", "Diana", "Kate", "Ann", "Donna"]
    attributes_1 = ["executive", "management", "professional", "corporation", "salary", "office", "business", "career"]
    attributes_2 = ["home", "parents", "children", "family", "cousins", "marriage", "wedding", "relatives"]

    return targets_1, targets_2, attributes_1, attributes_2


  # sex - math
  def weat_7(self):
    targets_1 = ["math", "algebra", "geometry", "calculus", "equations", "computation", "numbers", "addition"]
    targets_2 = ["poetry", "art", "dance", "literature", "novel", "symphony", "drama", "sculpture"]
    attributes_1 = ["male", "man", "boy", "brother", "he", "him", "his", "son"]
    attributes_2 = ["female", "woman", "girl", "sister", "she", "her", "hers", "daughter"]
    return targets_1, targets_2, attributes_1, attributes_2


  # sex - science
  def weat_8(self):
    targets_1 = ["science", "technology", "physics", "chemistry", "Einstein", "NASA", "experiment", "astronomy"]
    targets_2 = ["poetry", "art", "Shakespeare", "dance", "literature", "novel", "symphony", "drama"]
    attributes_1 = ["brother", "father", "uncle", "grandfather", "son", "he", "his", "him"]
    attributes_2 = ["sister", "mother", "aunt", "grandmother", "daughter", "she", "hers", "he"]
    return targets_1, targets_2, attributes_1, attributes_2


  # desease - uncontrollability
  def weat_9(self):
    targets_1 = ["sad", "hopeless", "gloomy", "tearful", "miserable", "depressed"]
    targets_2 = ["sick", "illness", "influenza", "disease", "virus", "cancer"]
    # in w2v experiments, the've replaced short-term with short
    attributes_1 = ["impermanent", "unstable", "variable", "fleeting", "short-term", "brief", "occasional"]
    attributes_2 = ["stable", "always", "constant", "persistent", "chronic", "prolonged", "forever"]

    return targets_1, targets_2, attributes_1, attributes_2


  # old - pleasant
  def weat_10(self):
    targets_1 = ["Tiffany", "Michelle", "Cindy", "Kristy", "Brad", "Eric", "Joey", "Billy"]
    targets_2 = ["Ethel", "Bernice", "Gertrude", "Agnes", "Cecil", "Wilbert", "Mortimer", "Edgar"]
    attributes_1 = ["joy", "love", "peace", "wonderful", "pleasure", "friend", "laughter", "happy"]
    attributes_2 = ["agony", "terrible", "horrible", "nasty", "evil", "war", "awful", "failure"]

    return targets_1, targets_2, attributes_1, attributes_2
  # missing from the original IAT: arab-muslim


  # occupations
  def wefat_1(self):
    # occupations derived from th bureau of labor statistics
    targets = ["technician", "accountant", "supervisor", "engineer", "worker", "educator", "clerk", "counselor", "inspector",
              "mechanic", "manager", "therapist", "administrator", "salesperson", "receptionist", "librarian", "advisor", "pharmacist",
              "janitor", "psychologist", "physician", "carpenter", "nurse", "investigator", "bartender", "specialist", "electrician",
              "officer", "pathologist", "teacher", "lawyer", "planner", "practitioner", "plumber", "instructor",
              "surgeon", "veterinarian", "paramedic",
              "examiner", "chemist", "machinist", "appraiser", "nutritionist", "architect", "hairdresser", "baker",
              "programmer", "paralegal", "hygienist", "scientist"]

    attributes_1 = ["male", "man", "boy", "brother", "he", "him", "his", "son"]
    attributes_2 = ["female", "woman", "girl", "sister", "she", "her", "hers", "daughter"]
    return targets, attributes_1, attributes_2


  # androgynous names
  def wefat_2(self):
    targets = ["Kelly", "Tracy", "Jamie", "Jackie", "Jesse", "Courtney", "Lynn", "Taylor", "Leslie", "Shannon",
              "Stacey", "Jessie", "Shawn", "Stacy", "Casey", "Bobby", "Terry", "Lee", "Ashley", "Eddie", "Chris", "Jody", "Pat",
              "Carey", "Willie", "Morgan", "Robbie", "Joan", "Alexis", "Kris", "Frankie", "Bobbie", "Dale", "Robin", "Billie",
              "Adrian", "Kim", "Jaime", "Jean", "Francis", "Marion", "Dana", "Rene", "Johnnie", "Jordan", "Carmen", "Ollie",
              "Dominique", "Jimmie", "Shelby"]

    attributes_1 = ["male", "man", "boy", "brother", "he", "him", "his", "son"]
    attributes_2 = ["female", "woman", "girl", "sister", "she", "her", "hers", "daughter"]
    return targets, attributes_1, attributes_2

  def __init__(self, embd_dict):
    self.embd_dict = embd_dict


  def _euclidean(self, w1, w2):
    return 1-distance.euclidean(w1, w2)

  def _cosine(self, w1, w2):
    return 1-distance.cosine(w1, w2)


  def similarity(self, w1, w2, type="cosine"):
    if type == "cosine":
      return self._cosine(w1, w2)
    return self._euclidean(w1, w2)


  def word_association_with_attribute(self, w, A, B):
    return np.mean([self.similarity(w, a) for a in A]) - np.mean([self.similarity(w, b) for b in B])


  def differential_association(self, T1, T2, A1, A2):
    return np.sum([self.word_association_with_attribute(t1, A1, A2) for t1 in T1]) \
           - np.sum([self.word_association_with_attribute(t2, A1, A2) for t2 in T2])

  def weat_effect_size(self, T1, T2, A1, A2):
    return (
             np.mean([self.word_association_with_attribute(t1, A1, A2) for t1 in T1]) -
             np.mean([self.word_association_with_attribute(t2, A1, A2) for t2 in T2])
           ) / np.std([self.word_association_with_attribute(w, A1, A2) for w in T1 + T2])


  def _random_permutation(self, iterable, r=None):
    pool = tuple(iterable)
    r = len(pool) if r is None else r
    return tuple(random.sample(pool, r))


  def weat_p_value(self, T1, T2, A1, A2, sample):
    size_of_permutation = min(len(T1), len(T2))
    T1_T2 = T1 + T2
    observed_test_stats_over_permutations = []

    if not sample:
      permutations = combinations(T1_T2, size_of_permutation)
    else:
      permutations = [self._random_permutation(T1_T2, size_of_permutation) for s in range(sample)]

    for Xi in permutations:
      Yi = filterfalse(lambda w: w in Xi, T1_T2)
      observed_test_stats_over_permutations.append(self.differential_association(Xi, Yi, A1, A2))

    unperturbed = self.differential_association(T1, T2, A1, A2)
    is_over = np.array([o > unperturbed for o in observed_test_stats_over_permutations])
    return is_over.sum() / is_over.size

  def weat_stats(self, T1, T2, A1, A2, sample_p=None):
    test_statistic = self.differential_association(T1, T2, A1, A2)
    effect_size = self.weat_effect_size(T1, T2, A1, A2)
    p = self.weat_p_value(T1, T2, A1, A2, sample=sample_p)
    return test_statistic, effect_size, p

  def _create_vocab(self):
    """
    >>> weat = WEAT(None); weat._create_vocab()
    :return: all
    """
    all = []
    for i in range(1, 10):
      t1, t2, a1, a2 = getattr(self, "weat_" + str(i))()
      all = all + t1 + t2 + a1 + a2
    for i in range(1, 2):
      t1, a1, a2 = getattr(self, "wefat_" + str(i))()
      all = all + t1 + a1 + a2
    all = set(all)
    return all

  def _output_vocab(self, path="./data/vocab_en.txt"):
    """
    >>> weat = WEAT(None); weat._output_vocab()
    """
    vocab = self._create_vocab()
    with codecs.open(path, "w", "utf8") as f:
      for w in vocab:
        f.write(w)
        f.write("\n")
      f.close()


  def run_test(self, target_1, target_2, attributes_1, attributes_2, sample_p=None, lower=False):
    """Run the WEAT test for differential association between two
    sets of target words and two sets of attributes.

    RETURNS:
        (d, e, p). A tuple of floats, where d is the WEAT Test statistic,
        e is the effect size, and p is the one-sided p-value measuring the
        (un)likeliness of the null hypothesis (which is that there is no
        difference in association between the two target word sets and
        the attributes).

        If e is large and p small, then differences in the model between
        the attribute word sets match differences between the targets.
    """
    if not lower:
      T1 = [self.embd_dict[w] for w in target_1 if w in self.embd_dict]
      T2 = [self.embd_dict[w] for w in target_2 if w in self.embd_dict]
      A1 = [self.embd_dict[w] for w in attributes_1 if w in self.embd_dict]
      A2 = [self.embd_dict[w] for w in attributes_2 if w in self.embd_dict]
    else:
      T1 = [self.embd_dict[w.lower()] for w in target_1 if w.lower() in self.embd_dict]
      T2 = [self.embd_dict[w.lower()] for w in target_2 if w.lower() in self.embd_dict]
      A1 = [self.embd_dict[w.lower()] for w in attributes_1 if w.lower() in self.embd_dict]
      A2 = [self.embd_dict[w.lower()] for w in attributes_2 if w.lower() in self.embd_dict]
    return self.weat_stats(T1, T2, A1, A2, sample_p)

def main():
  print("XWEAT started")
  if os.name == "nt":
    # embd_dict = utils.load_embeddings(
    #    "C:/Users/anlausch/workspace/cnn-text-classification/data/GoogleNews-vectors-negative300.bin", word2vec=True)
    embd_dict = utils.load_embeddings("C:/Users/anlausch/workspace/embedding_files/glove.6B/glove.6B.300d.txt",
                                      word2vec=False)
  else:
    # embd_dict = utils.load_embeddings("~/GoogleNews-vectors-negative300.bin", word2vec=True)
    embd_dict = utils.load_embeddings("/work/anlausch/glove.6B.300d.txt", word2vec=False)
  print("Embeddings loaded")
  weat = WEAT(embd_dict)
  targets_1, targets_2, attributes_1, attributes_2 = weat.weat_1()
  print("Running test")
  print(weat.run_test(targets_1, targets_2, attributes_1, attributes_2, 1000, lower=True))


if __name__ == "__main__":
  main()