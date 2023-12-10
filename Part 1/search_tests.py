from search import search, title_length, article_count, random_article, favorite_article, multiple_keywords, display_result
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_titles
from unittest.mock import patch
from unittest import TestCase, main

class TestSearch(TestCase):

    ##############
    # UNIT TESTS #
    ##############

    def test_example_unit_test(self):
        # Storing into a variable so don't need to copy and paste long list every time
        # If you want to store search results into a variable like this, make sure you pass a copy of it when
        # calling a function, otherwise the original list (ie the one stored in your variable) might be
        # mutated. To make a copy, you may use the .copy() function for the variable holding your search result.
        expected_dog_search_results = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
        self.assertEqual(search('dog'), expected_dog_search_results)
        self.assertEqual(search('dOg'), expected_dog_search_results)
        self.assertEqual(search('Book'), [])
        self.assertEqual(search(''), [])
        self.assertEqual(search('hi'), ['Fiskerton, Lincolnshire', 'China national soccer team'])
    

    def test_title_length(self):
        titles = ['nabin', 'bhagirath', 'pneumonoultramicroscopicsilicovolcanoconiosis']
        self.assertEqual(title_length(6, titles), ['nabin'])
        self.assertEqual(title_length(50, titles), ['nabin', 'bhagirath', 'pneumonoultramicroscopicsilicovolcanoconiosis'])
        self.assertEqual(title_length(5, []), [])
        self.assertEqual(title_length(10, titles), ['nabin', 'bhagirath'])
        self.assertEqual(title_length(2, titles), [])
        self.assertEqual(title_length(0, titles), [])


    def test_article_count(self):
        titles = ['nabin', 'bhagirath', 'pneumonoultramicroscopicsilicovolcanoconiosis']
        self.assertEqual(article_count(0, titles), [])
        self.assertEqual(article_count(5, []), [])
        self.assertEqual(article_count(4, titles), ['nabin', 'bhagirath', 'pneumonoultramicroscopicsilicovolcanoconiosis'])
        self.assertEqual(article_count(1, titles), ['nabin'])
        self.assertEqual(article_count(2, titles), ['nabin', 'bhagirath'])

    def test_random_article(self):
        titles = ['nabin', 'bhagirath', 'pneumonoultramicroscopicsilicovolcanoconiosis']
        self.assertEqual(random_article(1, titles), 'bhagirath')
        self.assertEqual(random_article(0, titles), 'nabin')
        self.assertEqual(random_article(2, titles), 'pneumonoultramicroscopicsilicovolcanoconiosis')
        self.assertEqual(random_article(0, []), '')
        self.assertEqual(random_article(5, titles), '')

    
    def test_favorite_article(self):
        titles = ['nabin', 'bhagirath', 'pneumonoultramicroscopicsilicovolcanoconiosis']
        self.assertEqual(favorite_article('nAbIn', titles), True)
        self.assertEqual(favorite_article('bhagirath', titles), True)
        self.assertEqual(favorite_article('dog', titles), False)
        self.assertEqual(favorite_article('nabin', []), True)
        self.assertEqual(favorite_article('nabin', titles), True)

    def test_multiple_keywords(self):
        titles = ['nabin', 'bhagirath', 'pneumonoultramicroscopicsilicovolcanoconiosis']
        expected_search_results = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
        self.assertEqual(multiple_keywords('book', titles), titles + expected_search_results)
        self.assertEqual(multiple_keywords('dog', []), expected_search_results)
        self.assertEqual(multiple_keywords('book', titles), titles)
        self.assertEqual(multiple_keywords('books', []), [])
        

    #####################
    # INTEGRATION TESTS #
    #####################

    @patch('builtins.input')
    def test_example_integration_test(self, input_mock):
        keyword = 'dog'
        advanced_option = 6

        # Output of calling display_results() with given user input. If a different
        # advanced option is included, append further user input to this list (after `advanced_option`)
        output = get_print(input_mock, [keyword, advanced_option])
        # Expected print outs from running display_results() with above user input
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']\n"

        # Test whether calling display_results() with given user input equals expected printout
        self.assertEqual(output, expected)

    
    @patch('builtins.input')
    def test_advanced_1(self, input_mock):
        keyword = 'book'
        advanced_option = 1
        advanced_user_response = 6

        output = get_print(input_mock, [keyword, advanced_option, advanced_user_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_user_response) + "\n\nNo articles found\n"

        self.assertEqual(output, expected)


    @patch('builtins.input')
    def test_advanced_2(self, input_mock):
        keyword = 'football'
        advanced_option = 2
        advanced_user_response = 5

        output = get_print(input_mock, [keyword, advanced_option, advanced_user_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_user_response) + "\n\nHere are your articles: ['2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Georgia Bulldogs football under Robert Winston']\n"

        self.assertEqual(output, expected)

    
    @patch('builtins.input')
    def test_advanced_3(self, input_mock):
        keyword = 'football'
        advanced_option = 3
        advanced_user_response = 2

        output = get_print(input_mock, [keyword, advanced_option, advanced_user_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_user_response) + "\n\nHere are your articles: Georgia Bulldogs football under Robert Winston\n"

        self.assertEqual(output, expected)


    @patch('builtins.input')
    def test_advanced_4(self, input_mock):
        keyword = 'football'
        advanced_option = 4
        advanced_user_response = 'cowboy'

        output = get_print(input_mock, [keyword, advanced_option, advanced_user_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_user_response) + "\n\nHere are your articles: ['2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Georgia Bulldogs football under Robert Winston']\n" + "Your favorite article is not in the returned articles!\n"

        self.assertEqual(output, expected)


    @patch('builtins.input')
    def test_advanced_5(self, input_mock):
        self.maxDiff = None
        keyword = 'football'
        advanced_option = 5
        advanced_user_response = 'soccer'

        output = get_print(input_mock, [keyword, advanced_option, advanced_user_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_user_response) + "\n\nHere are your articles: ['2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Georgia Bulldogs football under Robert Winston', 'Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)', 'Craig Martin (soccer)', 'United States men's national soccer team 2009 results', 'China national soccer team', 'Wake Forest Demon Deacons men\'s soccer']\n"

        self.assertEqual(output, expected)

# Write tests above this line. Do not remove.
if __name__ == "__main__":
    main()
