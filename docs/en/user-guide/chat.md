# Using AI chat

!!! info
    AI chat requires Gramps Web API version 2.5.0 or higher and Gramps Web version 24.10.0 or higher. Gramps Web API version 3.6.0 introduced tool calling capabilities for more intelligent interactions.



The chat view in Gramps Web (if available in your installation) gives access to an AI assistant that can answer questions about your family tree.

!!! warning
    Since this is still a new and evolving feature, some types of question work well while others don't. Also, as with any AI assistant, it can give factually incorrect answers, so be sure to always double check.

## How it works

To understand which types of question the assistant can answer, it is helpful to understand how it works below the hood:

1. The user asks a question.
2. The AI assistant can use multiple approaches to find answers:
   - **Semantic Search**: Gramps Web identifies objects in your family tree that are most likely to contain relevant information. For instance, if you ask "What's the name of John Doe's children?", families with John Doe as father will be among the top results.
   - **Tool Calling (Gramps Wev API v3.6.0+)**: The assistant can directly query your database using specialized tools to search, filter people/events/families/places by specific criteria, calculate relationships between individuals, and retrieve detailed information.
3. Gramps Web feeds the question along with the retrieved information to a large language model to formulate an answer.
4. The answer is displayed to you.

## What you can ask

With the tool calling capabilities introduced in Gramps Web API version 3.6.0, the AI assistant can now handle more complex questions:

- **Family relationships**: "Who are the grandparents of Jane Smith?" or "How is John Doe related to Mary Johnson?"
- **Filtered searches**: "Show me all people born in London after 1850" or "Which events happened in Paris?"
- **Date-based queries**: "Who died before 1900?" or "List marriages that took place between 1920 and 1950"
- **Place information**: "What places are in France?" or "Tell me about St. Mary's Church"
- **General questions**: "What's the name of John Doe's children?" or "When was Mary Smith born?"

## Tips for asking questions

To get the best results from the AI assistant:

- **Be specific**: Formulate your question with as much detail as possible to avoid ambiguities. For example, "When did John Smith born in 1850 in Boston marry?" is better than "When did John Smith marry?"
- **Use proper names**: Mention specific names, places, and dates when relevant.
- **Ask one thing at a time**: Break complex questions into simpler parts for better results.
- **Use your language**: Large language models are multilingual, so you can ask questions in your own language and receive answers in the same language.

!!! tip
    Please share your experience about things that work and don't work with the community.