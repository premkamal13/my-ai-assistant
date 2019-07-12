import wolframalpha as wa

input = input("Question: ")
app_id = "DEMO"
client = wa.Client(app_id)

result = client.query(input)

answer = next(result.results).text

print(answer)
