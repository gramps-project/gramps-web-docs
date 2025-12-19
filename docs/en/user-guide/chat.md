# Using AI chat

!!! info
    AI chat requires Gramps Web API version 2.5.0 or higher and Gramps Web version 24.10.0 or higher.



The chat view in Gramps Web (if available in your installation) gives access to an AI assistant that can answer questions about your family tree.

!!! warning
    Since this is still a new and evolving feature, some types of question work well while others don't. Also, as with any AI assistant, it can give factually incorrect answers, so be sure to always double check.

## How it works

To understand which types of question the assistant can answer, it is helpful to understand how it works below the hood:

1. The user asks a question.
2. Gramps Web identifies a number of (e.g., ten) Gramps objects that are most likely to contain the information that answers the question. To this end, it uses a technique called "semantic search". For instance, if you ask "What's the name of John Doe's children?", if a family exists with John Doe as father, it is likely to be among the top results.
3. Gramps Web feeds the user question along with the retrieved context information to a large language model ("chatbot") and asks it to extract the right answer.
4. The answer is displayed to the user.

## How to ask a question

Due to the way the chat works, it is (currently) not possible for the AI assistant to answer questions about specific relationships other than parents or children, unless this information is contained as text in a note.

Since each answer is based on a limited number of top semantic search results, it also cannot answer questions about statistics ("how many people in my database ...").

To avoid ambiguities and misunderstandings, it is helpful to formulate the question as detailed as possible.

Note that large language models are multilingual, so you can talk to it in your own language and it will answer in the same language.

!!! tip
    Please share your experience about things that work and don't work with the community.