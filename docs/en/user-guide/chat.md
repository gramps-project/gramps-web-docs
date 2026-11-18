# Using the AI Assistant

The **Assistant** view in Gramps Web (if enabled in your installation) gives access to an AI assistant that answers questions about your family tree.

!!! warning
    As with any AI assistant, answers can be wrong. Use the links in the answer to check the records it is based on.

## How it works

The assistant doesn't know your tree in advance. To answer a question, a large language model looks up the records it needs, much as you would yourself:

- it searches the tree with the [full-text search](search.md),
- it filters people, events, and families by criteria such as names, dates, places, or the number of children,
- it finds ancestors, descendants, and other relatives of a person, with their relationship,
- it reads complete records of people, families, events, places, and notes.

It then answers based on the records it has found, with links to them. While it is working, the tools it is using are shown, so you can follow along. Questions that take longer run in the background – you can navigate away and come back.

The assistant answers only from your tree, not from the general knowledge of the language model – even about well-known people. If the tree does not record something, it says so, mentioning related information it found, for example in a note. It only sees what you are allowed to see: links to private records are shown as plain text for users who can't view them.

Follow-up questions keep the context of earlier questions in the same conversation, so you can ask "And when did he die?" after asking about a person.

## What you can ask

- **Facts about people**: "When was Mary Smith born?" or "What are the names of John Doe's children?"
- **Relatives**: "Who are the grandparents of Jane Smith?" or "Which descendants of Johann Meyer emigrated to America?"
- **Searches with criteria**: "Who was born in London after 1850?", "List marriages between 1920 and 1950", or "Which couples had five or more children?"
- **Places**: "Which events happened in Paris?" or "Who was born in Denmark?" – places within a larger place are included.
- **Notes**: "What do the notes say about the farm of the Meyer family?"

Questions that need the whole tree at once, such as "What is the most common first name?", work less well, since the assistant only sees a limited number of records per lookup.

## Asking about images

If the server administrator has enabled it, the prompt has a button to attach images. You can also paste an image or drop image files onto the prompt. Up to four images can be attached to a question, for example a scan of a church record to ask "Who is mentioned in this entry, and are they in my tree?"

The images are only sent with the question they are attached to. Follow-up questions can refer to what the assistant said about them, but not to the images themselves, so attach them again if needed. If your tree has a limit on AI usage, each image counts like an additional question.

## Letting the assistant change your tree

If the server administrator has enabled it, editors, owners, and administrators can ask the assistant to change the tree, for example "Add a baptism on 3 May 1802 in St. Mary's to Johann Meyer" or "Fix the birth year of Anna Smith, it should be 1871".

The assistant never changes anything on its own. It answers with a **Proposed changes** card that lists every record it would add, edit, or delete, with the old values struck through and the new values highlighted. Nothing happens until you click **Apply**. The changes are then made in one step, which you can undo like any other edit, from the message that appears or in the [revision history](revisions.md).

Check a proposal carefully before applying it – in particular that the assistant picked the right person, and that it didn't add a new record (such as a place or source) that already exists in your tree under a slightly different name. If a proposal is not quite right, say what to change, and the assistant proposes again.

Once a proposal has been applied, older proposals in the same conversation can no longer be applied, since they were made for the tree as it was before. The same happens if one of the affected records has been changed in the meantime.

## Tips for asking questions

- **Name the people.** The assistant doesn't know who you are or who your home person is, so instead of "my grandmother", ask about "the grandmother of Anna Smith (born 1950)". You can also use Gramps IDs, e.g. "the children of I0042".
- **Be specific** when names are common: "When did the John Smith born in 1850 in Boston marry?" is better than "When did John Smith marry?"
- **Use your language.** You can ask in your own language and receive answers in the same language.
- **Ask again differently** if an answer looks incomplete – for example by naming the place or time period you are interested in.

!!! tip
    Please share your experience about things that work and don't work with the community.
