def render(parsed_output):
  print(parsed_output["title"], "-", parsed_output["headers"][0], "\n")

  for p in parsed_output["paragraphs"]:
    print(p)
