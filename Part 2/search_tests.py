from search import search, article_length, unique_authors, most_recent_article, favorite_author, title_and_author, refine_search, display_result
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_metadata
from unittest.mock import patch
from unittest import TestCase, main

class TestSearch(TestCase):

    ##############
    # UNIT TESTS #
    ##############

    def test_example_unit_test(self):
        expected_search_soccer_results = [
            ['Spain national beach soccer team', 'jack johnson', 1233458894, 1526],
            ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562],
            ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]
        ]
        self.assertEqual(search('soccer'), expected_search_soccer_results)



    def test_search(self):
        expected_search_college_results = [['Rock music', 'Mack Johnson', 1258069053, 119498], ['Fisk University', 'RussBot', 1263393671, 16246]]
       
        self.assertEqual(search('COLLEGE'), expected_search_college_results)
        self.assertEqual(search('college'), expected_search_college_results)
        self.assertEqual(search('nabin'), [])
        self.assertEqual(search(''), [])

    def test_article_length(self):
        search_college_results = [['Rock music', 'Mack Johnson', 1258069053, 119498], ['Fisk University', 'RussBot', 1263393671, 16246]]
       
        self.assertEqual(article_length(4000, search_college_results), [])
        self.assertEqual(article_length(40000, search_college_results), [['Fisk University', 'RussBot', 1263393671, 16246]])
        self.assertEqual(article_length(400, search_college_results), [])
        self.assertEqual(article_length(0, search_college_results), [])

    def test_unique_authors(self):
        search_college_results = [['Rock music', 'Mack Johnson', 1258069053, 119498], ['Fisk University', 'RussBot', 1263393671, 16246]]
       
        self.assertEqual(unique_authors(4, search_college_results), [['Rock music', 'Mack Johnson', 1258069053, 119498], ['Fisk University', 'RussBot', 1263393671, 16246]])
        self.assertEqual(unique_authors(1, search_college_results), [['Rock music', 'Mack Johnson', 1258069053, 119498]])
        self.assertEqual(unique_authors(0, search_college_results), [])
        self.assertEqual(unique_authors(-1, search_college_results), [])

    def test_most_recent_article(self):
        search_football_results = [['Georgia Bulldogs football', 'Burna Boy', 1166567889, 43718]]
        search_college_results = [['Rock music', 'Mack Johnson', 1258069053, 119498], ['Fisk University', 'RussBot', 1263393671, 16246]]
       
        self.assertEqual(most_recent_article(search_college_results), ['Fisk University', 'RussBot', 1263393671, 16246])
        self.assertEqual(most_recent_article(search_football_results), ['Georgia Bulldogs football', 'Burna Boy', 1166567889, 43718])  

    def test_favorite_author(self):
        search_school_results = [['Edogawa, Tokyo', 'jack johnson', 1222607041, 4526], ['Fisk University', 'RussBot', 1263393671, 16246], ['Annie (musical)', 'Jack Johnson', 1223619626, 27558], ['Alex Turner (musician)', 'jack johnson', 1187010135, 9718]]
        
        self.assertEqual(favorite_author('jAck Johnson', search_school_results), True)
        self.assertEqual(favorite_author('JACK JOHNSON', search_school_results), True)
        self.assertEqual(favorite_author('RusSboT', search_school_results), True)
        self.assertEqual(favorite_author('Nabin', search_school_results), False)
        self.assertEqual(favorite_author('', search_school_results), False)


    def test_title_and_author(self):
        search_college_results = [['Rock music', 'Mack Johnson', 1258069053, 119498], ['Fisk University', 'RussBot', 1263393671, 16246]]
        search_football_results = [['Georgia Bulldogs football', 'Burna Boy', 1166567889, 43718]]
        
        self.assertEqual(title_and_author(search_college_results), [('Rock music', 'Mack Johnson'), ('Fisk University', 'RussBot')])
        self.assertEqual(title_and_author(search_football_results), [('Georgia Bulldogs football', 'Burna Boy')])
        self.assertEqual(title_and_author([]), [])

    
    def test_refine_search(self):
        search_college_results = [['Rock music', 'Mack Johnson', 1258069053, 119498], ['Fisk University', 'RussBot', 1263393671, 16246]]
        
        self.assertEqual(refine_search('student', search_college_results), [['Fisk University', 'RussBot', 1263393671, 16246]])
        self.assertEqual(refine_search('nabin', search_college_results), [])
        self.assertEqual(refine_search('', search_college_results), [])

    #####################
    # INTEGRATION TESTS #
    #####################

    @patch('builtins.input')
    def test_example_integration_test(self, input_mock):
        keyword = 'soccer'
        advanced_option = 1
        advanced_response = 3000

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: [['Spain national beach soccer team', 'jack johnson', 1233458894, 1526], ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]]\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_example_integration_test(self, input_mock):
        keyword = 'college'
        advanced_option = 1
        advanced_response = 5000

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nNo articles found\n"

        self.assertEqual(output, expected)
    
    @patch('builtins.input')
    def test_advanced_option_2(self, input_mock):
        keyword = 'college'
        advanced_option = 2
        advanced_response = 2
       
        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: [['Rock music', 'Mack Johnson', 1258069053, 119498], ['Fisk University', 'RussBot', 1263393671, 16246]]\n"
        
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced_option_3(self, input_mock):
        keyword = 'college'
        advanced_option = 3
       
        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: ['Fisk University', 'RussBot', 1263393671, 16246]\n"
        
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced_option_4(self, input_mock):
        keyword = 'college'
        advanced_option = 4
        advanced_response = 'nabin'
       
        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: [['Rock music', 'Mack Johnson', 1258069053, 119498], ['Fisk University', 'RussBot', 1263393671, 16246]]\nYour favorite author is not in the returned articles!\n"
        
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced_option_5(self, input_mock):
        keyword = 'college'
        advanced_option = 5
       
        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: [('Rock music', 'Mack Johnson'), ('Fisk University', 'RussBot')]\n"
        
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced_option_6(self, input_mock):
        keyword = 'college'
        advanced_option = 6
        advanced_response = 'fisk'
       
        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: [['Fisk University', 'RussBot', 1263393671, 16246]]\n"
        
        self.assertEqual(output, expected)

    
    @patch('builtins.input')
    def test_advanced_option_7(self, input_mock):
        keyword = 'college'
        advanced_option = 7
       
        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: [['Rock music', 'Mack Johnson', 1258069053, 119498], ['Fisk University', 'RussBot', 1263393671, 16246]]\n"
        
        self.assertEqual(output, expected)

# Write tests above this line. Do not remove.
if __name__ == "__main__":
    main()
