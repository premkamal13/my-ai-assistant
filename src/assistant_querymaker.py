import wikipedia
import wolframalpha

def assist_me():
    while True:
        query = input("Ask me something: ")
        try:
            # search in wolframalpha
            app_id = "9GUW84-976QLUJHXP"
            client = wolframalpha.Client(app_id)
            result = client.query(query)
            answer = next(result.results).text
            print(answer)
        except:
            # search in wikipedia
            print(wikipedia.summary(query))

assist_me()
