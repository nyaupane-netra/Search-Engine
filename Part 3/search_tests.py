from search import keyword_to_titles, title_to_info, search, article_length,key_by_author, filter_to_author, filter_out, articles_from_year
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_metadata
from unittest.mock import patch
from unittest import TestCase, main

class TestSearch(TestCase):

    ##############
    # UNIT TESTS #
    ##############

    def test_example_unit_test(self):
        dummy_keyword_dict = {
            'cat': ['title1', 'title2', 'title3'],
            'dog': ['title3', 'title4']
        }
        expected_search_results = ['title3', 'title4']
        self.assertEqual(search('dog', dummy_keyword_dict), expected_search_results)


    def test_keyword_to_titles(self):
        data1 = [
            ['title1', 'author1', 'timestamp1', 'article_length1', ['keyword', 'keyword1']],
            ['title2', 'author2', 'timestamp2', 'article_length2', ['keyword2', 'keyword', 'keyword3']],
            ['title3', 'author3', 'timestamp3', 'article_length3', []]
        ]
        expected_output1 = {
            'keyword' : ['title1', 'title2'],
            'keyword1' : ['title1']
            'keyword2' : ['title2'],
            'keyword3' : ['title2']

        }

        data2 = []
        expected_output2 = {}

        data3 = [
            ['List of Canadian musicians', 'Jack Ma', 1181623340, 21023, ['nabin']],
            ['Edogawa, Tokyo', 'jack johnson', 1222607041, 4526, ['Shyam', 'bijan']]
        ]
        expected_output3 = {
            'nabin' : ['List of Canadian musicians'],
            'Shyam' : ['Edogawa, Tokyo'],
            'bijan' : ['Edogawa, Tokyo']
        }

        self.assertEqual(keyword_to_titles(data1), expected_output1)
        self.assertEqual(keyword_to_titles(data2), expected_output2)
        self.assertEqual(keyword_to_titles(data3), expected_output3)

    def test_title_to_info(self):
        data1 = [
            ['title1', 'author1', 'timestamp1', 'article_length1', ['keyword', 'keyword1']],
            ['title2', 'author2', 'timestamp2', 'article_length2', ['keyword2', 'keyword', 'keyword3']],
            ['title', 'author', 'timestamp', 'article_length', []]
        ]
        expected_output1 = {
            'title1' : {
                'author': 'author1',
                'timestamp': 'timestamp1',
                'length': 'article_length1'
            },
            'title2' :{
                'author': 'author2',
                'timestamp': 'timestamp2',
                'length': 'article_length2'
            },
            'title' : {
                'author': 'author',
                'timestamp': 'timestamp',
                'length': 'article_length'
            }
        }

        data2 = []
        expected_output2 = {}

        data3 = [
            ['List of Canadian musicians', 'Jack Ma', 1181623340, 21023, ['nabin']],
            ['Edogawa, Tokyo', 'jack johnson', 1222607041, 4526, ['Shyam', 'bijan']]
        ]
        expected_output3 = {
            'List of Canadian musicians' : {
                'author': 'Jack Ma',
                'timestamp': 1181623340,
                'length': 21023
            }, 
            'Edogawa, Tokyo' : {
                'author': 'jack johnson',
                'timestamp': 1222607041,
                'length': 4526
            }
        }

        self.assertEqual(title_to_info(data1), expected_output1)
        self.assertEqual(title_to_info(data2), expected_output2)
        self.assertEqual(title_to_info(data3), expected_output3)

    
    def test_search(self):
        keyword_to_titles = {
            'nabin' : ['title1', 'title2'],
            'college' : ['title3', 'title4'],
            'NabIn' : ['title5']
        }

        keyword1 = 'nabin'
        expected_output1 =  ['title1', 'title2']


        keyword2 = 'nepal'
        expected_output2 = []

        keyword_to_titles1 = {}

        self.assertEqual(search(keyword1, keyword_to_titles), expected_output1)
        self.assertEqual(search(keyword2, keyword_to_titles), expected_output2)
        self.assertEqual(search('', keyword_to_titles), [])
        self.assertEqual(search('NABIN', keyword_to_titles), [])
        self.assertEqual(search('', keyword_to_titles1), [])

    
    def test_article_length(self):
        article_titles =  ['List of Canadian musicians', 'Edogawa, Tokyo']
        title_to_info = {
            'List of Canadian musicians' : {
                'author': 'Jack Ma',
                'timestamp': 1181623340,
                'length': 21023
            }, 
            'Edogawa, Tokyo' : {
                'author': 'jack johnson',
                'timestamp': 1222607041,
                'length': 4526
            }
        }


        self.assertEqual(article_length(2000, article_titles, title_to_info), [])
        self.assertEqual(article_length(100000, [], {}), [])
        self.assertEqual(article_length(25000, article_titles, title_to_info), ['List of Canadian musicians', 'Edogawa, Tokyo'])
        self.assertEqual(article_length(4527, article_titles, title_to_info), ['Edogawa, Tokyo'])


    def test_key_by_author(self):
        article_titles =  ['List of Canadian musicians', 'Edogawa, Tokyo']
        title_to_info1 = {
            'List of Canadian musicians' : {
                'author': 'Jack Ma',
                'timestamp': 1181623340,
                'length': 21023
            }, 

            'Edogawa, Tokyo' : {
                'author': 'jack johnson',
                'timestamp': 1222607041,
                'length': 4526
            }
        } 
        expected_output1 = {
           'Jack Ma': ['List of Canadian musicians'],
           'jack johnson': ['Edogawa, Tokyo'] 
        }

        article_title2 = ['title1', 'title2', 'title3']
        title_to_info2 = {
            'title1' : {
                'author': 'nabin',
                'timestamp': '2013',
                'length': 'length1'
            },
            'title2' :{
                'author': 'netra',
                'timestamp': 'stamp2',
                'length': 'length2'
            },
            'title3' : {
                'author': 'nabin',
                'timestamp': 'stamp3',
                'length': 'length3'
            }
        }
        expected_output2 = {
            'nabin' : ['title1', 'title3'],
            'netra': ['title2']
        }

        self.assertEqual(key_by_author([], {}), {})
        self.assertEqual(key_by_author(article_title1, title_to_info1), expected_output1)
        self.assertEqual(key_by_author(article_title2, title_to_info2), expected_output2)
        
        
    def test_filter_to_author(self):
        article_titles =  ['List of Canadian musicians', 'Edogawa, Tokyo']
        title_to_info = {
            'List of Canadian musician' : {
                'author': 'Jack Ma',
                'timestamp': 118162,
                'length': 21047
            }, 

            'Edogawa, Tokyo' : {
                'author': 'jack johnson',
                'timestamp': 1222607789,
                'length': 4574
            }
        } 
        
        author1 = 'Jack Ma'
        expected_output1 = ['List of Canadian musician']

        author2 = 'Nabin'
        expected_output2 =[]

        self.assertEqual(filter_to_author(author1, article_titles, title_to_info), expected_output1)
        self.assertEqual(filter_to_author('', article_titles, title_to_info), [])
        self.assertEqual(filter_to_author('', [], {}), [])
        self.assertEqual(filter_to_author('Hi', [], {}), [])
        self.assertEqual(filter_to_author(author2, article_titles, title_to_info), expected_output2)
        

    def test_filter_out(self):
        article_titles = ['Nabin', 'Netra']
        keyword_to_titles = {
            'coder' : ['Nabin'],
            'college' : ['Netra'],
            'student' : ['Netra']
        }

        keyword1 = 'coder'
        expected_output1 = ['Netra']

        keyword2 = 'college'
        expected_output2 = ['Nabin']

        keyword3 = ''
        expected_output3 = ['Nabin', 'Netra']

        self.assertEqual(filter_out(keyword1, article_titles, keyword_to_titles), expected_output1)
        self.assertEqual(filter_out(keyword2, article_titles, keyword_to_titles), expected_output2)
        self.assertEqual(filter_out('', [], {}), [])
        self.assertEqual(filter_out(keyword3, article_titles, keyword_to_titles), expected_output3)
        

    def test_articles_from_year(self):
        article_titles =  ['Nepal', 'Japan']
        title_to_info = {
            'Nepal' : {
                'author': 'Netra',
                'timestamp': 1259384898,
                'length': 21047
            }, 

            'Japan' : {
                'author': 'Naruto',
                'timestamp': 1222607789,
                'length': 4574
            }
        } 

        year1 = 2009
        expected_output1 = ['Nepal']

        year2 = 2008
        expected_output2 = ['Japan']

        year3 = 2000
        expected_output3 = []

        self.assertEqual(articles_from_year(157, [], {}), [])
        self.assertEqual(articles_from_year(year1, article_titles, title_to_info), expected_output1)
        self.assertEqual(articles_from_year(year2, article_titles, title_to_info), expected_output2)
        self.assertEqual(articles_from_year(year3, article_titles, title_to_info), expected_output3)
        

    #####################
    # INTEGRATION TESTS #
    #####################

    @patch('builtins.input')
    def test_example_integration_test(self, input_mock):
        keyword = 'soccer'
        advanced_option = 5
        advanced_response = 2009

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Spain national beach soccer team', 'Steven Cohen (soccer)']\n"

        self.assertEqual(output, expected)

    
    @patch('builtins.input')
    def test_advanced_option_1(self, input_mock):
        keyword = 'nabin'
        advanced_option = 1
        advanced_response = 5000

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nNo articles found\n"

        self.assertEqual(output, expected)


    @patch('builtins.input')
    def test_advanced_option_2(self, input_mock):
        keyword = 'football'
        advanced_option = 2

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: {'Burna Boy': ['Georgia Bulldogs football']}\n"

        self.assertEqual(output, expected)


    @patch('builtins.input')
    def test_advanced_option_3(self, input_mock):
        keyword = 'college'
        advanced_option = 3
        advanced_response = 'Mike'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nNo articles found\n"

        self.assertEqual(output, expected)


    @patch('builtins.input')
    def test_advanced_option_4(self, input_mock):
        keyword = 'college'
        advanced_option = 4
        advanced_response = 'nepal'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Rock music', 'Fisk University']\n"

        self.assertEqual(output, expected)

    
    @patch('builtins.input')
    def test_advanced_option_5(self, input_mock):
        keyword = 'university'
        advanced_option = 5
        advanced_response = 1998

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nNo articles found\n"

        self.assertEqual(output, expected)


    @patch('builtins.input')
    def test_advanced_option_6(self, input_mock):
        keyword = 'university'
        advanced_option = 6

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: ['Embryo drawing', 'Georgia Bulldogs football', 'Fisk University', 'Indian classical music']\n"

        self.assertEqual(output, expected)

# Write tests above this line. Do not remove.
if __name__ == "__main__":
    main()
