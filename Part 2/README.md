A search engine takes a given search phrase or word and finds pages on the internet that are relevant, ranks the pages, and then displays the pages in the order of ranking.

In part 1 of this project, we searched a list of article titles to see if they contain a user provided keyword as a part of the title. In part 2, we will instead be searching through a 2D list of article metadata in order to find articles that are relevant to our keyword rather than having titles that strictly include it.

All article metadata can be fetched by calling the wiki.article_metadata(). It returns a 2D list where each individual "row" represents a single article. Each article is represented as a list with the following information provided in this exact order:

Article title (string)

Author name (string)

Timestamp of when the article was published (int). The timestamp is stored as the # of seconds since January 1st, 1970 (also known as Unix/Epoch Time)

The number of characters in the article (int)

A list of keywords that are related to the article content (list of strings)

To demonstrate, here is a potential example row in the 2D list:

['Spongebob - the legacy', 'Mr Jake', 1172208041, 5569, ['Spongebob', 'cartoon', 'pineapple', 'tv', 'sponge', 'nickelodean', 'legacy']]

We will use this data to create a more powerful search engine that returns results based on this metadata. Just like in part 1, our search will have two parts:

Basic Search

To run a basic search, ask the user for a keyword and use the keyword to search through the complete list of article metadata (from wiki.article_metadata()). For each article, include it in the search results if the user keyword is a (case-insensitive) match for one of the words in the article's relevant keywords list (note this is different than part 1 where we were checking if the user keyword was a substring of the article title). For example, given the example article above ("Spongebob - the legacy"), it would be included in the search result if the user keyword was "SpONgE" but excluded if the user keyword was "car". The metadata returned should include the article name, author, publishing timestamp, and character count, but not include the article's relevant keywords.

If the user does not enter anything or no results are found, return an empty list.

When running a search, the basic search will always be run, and it will always be run before the advanced search.

Advanced Search

The user is then prompted for different options to perform an advanced search. There will be 7 advanced search options:

Article length - user provides a max article length (in characters). After searching for articles with the user’s keyword, return the article metadata for articles that do not exceed the max article length. For example, if the user searched for “dog” and wants a maximum article length of 8000 characters, only return a list of article metadata with articles containing the word “dog” and a maximum article length of 8000 characters.

Unique authors - user provides a max number of articles they would like to receive, with the added caveat that each must have a unique author. After searching for article metadata with the user’s keyword, return the number of articles requested by the user, starting from the first article and each with a unique author. If two or more articles have the same author, include the first in the results and skip the others. If the number of articles requested by the user exceeds the number of unique authors, return the entire list with duplicate authors removed.

Most recent article - After searching for article metadata with the user’s keyword, return only the article metadata that was published most recently. If there are no articles return an empty string.

Check whether favorite author in list - user provides a favorite author. After searching for article metadata with the user’s keyword, return True if the provided author is included (case-insensitive) in the returned list of article metadata and False otherwise.

Receive only title and author - After searching for article metadata with the user’s keyword, do not return all the metadata; only return a list of title and author for articles containing the user’s keyword. Each title and author should be stored as a Tuple.

Refine search - user provides another keyword to search. After searching for article metadata with the user’s basic search keyword, search all of the articles again using this second keyword. Return article metadata for only those articles that were found in both searches: the results should be in the same order they appeared after the basic search.

None - user does not want an advanced search. (There is no function for this)
