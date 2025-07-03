from support_graph import support_graph

while True:
    user_question = input("\n🧾 Ask a customer support question (or type 'exit' to quit): ")
    
    if user_question.lower() in ["exit", "quit"]:
        print("👋 Exiting. Have a great day!")
        break

    result = support_graph.invoke({"question": user_question})
    print(f"\n🤖 Response: {result['response']}")
