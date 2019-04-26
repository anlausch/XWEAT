import os.path
import codecs

def main_results():
  with codecs.open("tables.txt", "w", "utf8") as o:
    for i in [1, 2, 5, 6, 7, 8, 9]:
      results = {}
      for attribute_language in ["en", "de", "es", "it", "hr", "ru", "tr"]:
        for target_language in ["en", "de", "es", "it", "hr", "ru", "tr"]:
          file = "/work/anlausch/xweat/results/ft_xling_space-" + target_language + "-" + attribute_language + "_ta-" + target_language + "-" + attribute_language + "_cosine_" + str(i) + ".res"

          if not os.path.isfile(file):
            file = "/work/anlausch/xweat/results/ft_xling_space-" + attribute_language + "-" + target_language + "_ta-" + target_language + "-" + attribute_language + "_cosine_" + str(
              i) + ".res"
          if os.path.isfile(file):
            with codecs.open(file, "r", "utf8") as f:
              for j,line in enumerate(f.readlines()):
                if j == 1:
                  tuple = line.split("Result: ")[1]
                  tuple = eval(tuple)
                  effect_size = tuple[1]
                  p = tuple[2]
                  if p < 0.05 or p > 0.95:
                    effect_size = str(effect_size)
                  else:
                    effect_size = str(effect_size) + "*"
                  results[(attribute_language, target_language)] = effect_size
      o.write("XWEAT " + str(
        i) + "(T/A) & \\textbf{\\textsc{en}} & \\textbf{\\textsc{de}} & \\textbf{\\textsc{es}} & \\textbf{\\textsc{it}} & \\textbf{\textsc{hr}} & \\textbf{\textsc{ru}} & \\textbf{\\textsc{tr}}) \\\\\n")
      for target_language in ["en", "de", "es", "it", "hr", "ru", "tr"]:
        o.write("\\textbf{\\textsc{"+ target_language+"}} ")
        for attribute_language in ["en", "de", "es", "it", "hr", "ru", "tr"]:
          if target_language == attribute_language:
            o.write("& -- ")
          else:
            if (attribute_language, target_language) in results:
              o.write("&" + results[(attribute_language, target_language)])
            else:
              o.write("& &")
          if attribute_language == "tr":
            o.write("\\\\\n")

def main():
  with codecs.open("tables_avg.txt", "w", "utf8") as o:
    results = {}
    for i in [1, 2, 6, 7, 8, 9]:
      for attribute_language in ["en", "de", "es", "it", "hr", "ru", "tr"]:
        for target_language in ["en", "de", "es", "it", "hr", "ru", "tr"]:
          file = "/work/anlausch/xweat/results/ft_xling_space-" + target_language + "-" + attribute_language + "_ta-" + target_language + "-" + attribute_language + "_cosine_" + str(i) + ".res"

          if not os.path.isfile(file):
            file = "/work/anlausch/xweat/results/ft_xling_space-" + attribute_language + "-" + target_language + "_ta-" + target_language + "-" + attribute_language + "_cosine_" + str(
              i) + ".res"
          if os.path.isfile(file):
            with codecs.open(file, "r", "utf8") as f:
              for j,line in enumerate(f.readlines()):
                if j == 1:
                  tuple = line.split("Result: ")[1]
                  tuple = eval(tuple)
                  effect_size = tuple[1]
                  p = tuple[2]
                  if (attribute_language, target_language) in results:
                    effect_sizes, old_significance = results[(attribute_language, target_language)]
                    effect_sizes.append(effect_size)
                    if not old_significance or not (p < 0.05 or p > 0.95):
                      results[(attribute_language, target_language)] = (effect_sizes, False)
                    else:
                      results[(attribute_language, target_language)] = (effect_sizes, True)
                  elif not (attribute_language, target_language) in results and (p < 0.05 or p > 0.95):
                    results[(attribute_language, target_language)] = ([effect_size], True)
                  elif not (attribute_language, target_language) in results and not (p < 0.05 or p > 0.95):
                    results[(attribute_language, target_language)] = ([effect_size], False)
                  else:
                    raise NotImplementedError()
    results_transformed = {}
    for key, value in results.items():
      effect_sizes, significance = value
      if not len(effect_sizes) == 6:
        print("Problem")
      assert len(effect_sizes) == 6
      effect_size = sum(effect_sizes)/len(effect_sizes)
      if significance:
        results_transformed[key] = str(effect_size)
      else:
        results_transformed[key] = str(effect_size) + "*"
    o.write("XWEAT " + str(
      i) + "(T/A) & \\textbf{\\textsc{en}} & \\textbf{\\textsc{de}} & \\textbf{\\textsc{es}} & \\textbf{\\textsc{it}} & \\textbf{\textsc{hr}} & \\textbf{\textsc{ru}} & \\textbf{\\textsc{tr}}) \\\\\n")
    for target_language in ["en", "de", "es", "it", "hr", "ru", "tr"]:
      o.write("\\textbf{\\textsc{"+ target_language+"}} ")
      for attribute_language in ["en", "de", "es", "it", "hr", "ru", "tr"]:
        if target_language == attribute_language:
          o.write("& -- ")
        else:
          if (attribute_language, target_language) in results_transformed:
            o.write("&" + results_transformed[(attribute_language, target_language)])
          else:
            o.write("& &")
        if attribute_language == "tr":
          o.write("\\\\\n")

if __name__=="__main__":
  main()