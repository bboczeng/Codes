'''
**************** PLEASE READ ***************

Script that reads in spam and ham messages and converts each training example
into a feature vector

Code intended for UC Berkeley course CS 189/289A: Machine Learning

Requirements:
-scipy ('pip install scipy')

To add your own features, create a function that takes in the raw text and
word frequency dictionary and outputs a int or float. Then add your feature
in the function 'def generate_feature_vector'

The output of your file will be a .mat file. The data will be accessible using
the following keys:
    -'training_data'
    -'training_labels'
    -'test_data'

Please direct any bugs to kevintee@berkeley.edu
'''

from collections import defaultdict
import glob
import re
import scipy.io

NUM_TRAINING_EXAMPLES = 5172
NUM_TEST_EXAMPLES = 5857

BASE_DIR = './'
SPAM_DIR = 'spam/'
HAM_DIR = 'ham/'
TEST_DIR = 'test/'

# ************* Features *************

# Features that look for certain words
def freq_pain_feature(text, freq):
    return float(freq['pain'])

def freq_private_feature(text, freq):
    return float(freq['private'])

def freq_bank_feature(text, freq):
    return float(freq['bank'])

def freq_money_feature(text, freq):
    return float(freq['money'])

def freq_drug_feature(text, freq):
    return float(freq['drug'])

def freq_spam_feature(text, freq):
    return float(freq['spam'])

def freq_prescription_feature(text, freq):
    return float(freq['prescription'])

def freq_creative_feature(text, freq):
    return float(freq['creative'])

def freq_height_feature(text, freq):  
    return float(freq['height'])

def freq_featured_feature(text, freq):
    return float(freq['featured'])

def freq_differ_feature(text, freq):
    return float(freq['differ'])

def freq_width_feature(text, freq):
    return float(freq['width'])

def freq_other_feature(text, freq):
    return float(freq['other'])

def freq_energy_feature(text, freq):
    return float(freq['energy'])

def freq_business_feature(text, freq):
    return float(freq['business'])

def freq_message_feature(text, freq):
    return float(freq['message'])

def freq_volumes_feature(text, freq):
    return float(freq['volumes'])

def freq_revision_feature(text, freq):
    return float(freq['revision'])

def freq_path_feature(text, freq):
    return float(freq['path'])

def freq_meter_feature(text, freq):
    return float(freq['meter'])

def freq_memo_feature(text, freq):
    return float(freq['memo'])

def freq_planning_feature(text, freq):
    return float(freq['planning'])

def freq_pleased_feature(text, freq):
    return float(freq['pleased'])

def freq_record_feature(text, freq):
    return float(freq['record'])

def freq_out_feature(text, freq):
    return float(freq['out'])



# Features that look for certain characters
def freq_semicolon_feature(text, freq):
    return text.count(';')

def freq_dollar_feature(text, freq):
    return text.count('$')

def freq_sharp_feature(text, freq):
    return text.count('#')

def freq_exclamation_feature(text, freq):
    return text.count('!')

def freq_para_feature(text, freq):
    return text.count('(')

def freq_bracket_feature(text, freq):
    return text.count('[')

def freq_and_feature(text, freq):
    return text.count('&')


# --------- Add your own feature methods ----------
# added features:

# Added feature words (not all): buy, direct, order, shopper, clearance, status, buying, singles, score, babes, dirt, shopper, additional, boss, earn, extra, money, make, online
# biz, potential, diplomas, cheap, free, discount, cost, cash, bonus, check, easy, investment, insurance, lowest, loans, mortgage, fees, refinance, quote, debt, credit, debit, refund
# stock, lower, security, approved, refinance, click, ad, member, trial, offer, opt, junk, spam, 100%, #1, off, satisfied, billion, millions, thousands, million, guarantee, win
# won, casino, apply, now, today, get, great, limited, only, promotion, instant, all, real, new, promised, cancel, sign
# --------------------------------------------------

def example_feature(text, freq):
    return int('example' in text)

def freq_order_feature(text, freq): # added feature
    return float(freq['order'])

def freq_direct_feature(text, freq):
    return float(freq['direct'])

def freq_buy_feature(text, freq):
    return float(freq['buy'])

def freq_clearance_feature(text, freq):
    return float(freq['clearance'])

def freq_shopper_feature(text, freq):
    return float(freq['shopper'])

def freq_earn_feature(text, freq):
    return float(freq['earn'])

def freq_extra_feature(text, freq):
    return float(freq['extra'])

def freq_online_feature(text, freq):
    return float(freq['online'])

def freq_cash_feature(text, freq):
    return float(freq['cash'])

def freq_bonus_feature(text, freq):
    return float(freq['bonus'])

def freq_free_feature(text, freq):
    return float(freq['free'])

def freq_lowest_feature(text, freq):
    return float(freq['lowest'])

def freq_refund_feature(text, freq):
    return float(freq['refund'])

def freq_click_feature(text, freq):
    return float(freq['click'])

def freq_member_feature(text, freq):
    return float(freq['member'])

def freq_trial_feature(text, freq):
    return float(freq['trial'])

def freq_satisfied_feature(text, freq):
    return float(freq['satisfied'])

def freq_million_feature(text, freq):
    return float(freq['million'])

def freq_guarantee_feature(text, freq):
    return float(freq['guarantee'])

def freq_instant_feature(text, freq):
    return float(freq['instant'])

def freq_won_feature(text, freq):
    return float(freq['won'])

def freq_offer_feature(text, freq):
    return float(freq['offer'])

def freq_opportunities_feature(text, freq):
    return float(freq['opportunities'])

def freq_subscription_feature(text, freq): 
    return float(freq['subscription'])

def freq_i_feature(text, freq): 
    return float(freq['i'])

def freq_think_feature(text, freq): 
    return float(freq['think'])

def freq_thanks_feature(text, freq): 
    return float(freq['thanks'])

def freq_http_feature(text, freq):
    return float(freq['http'])

def freq_underline_feature(text, freq):
    return text.count('_')

def freq_at_feature(text, freq):
    return text.count('@')

def freq_dot_feature(text, freq):
    return text.count('.')

def freq_dash_feature(text, freq):
    return text.count('-')

def freq_add_feature(text, freq):
    return text.count('+')

def freq_percent_feature(text, freq):
    return text.count('%')

# Generates a feature vector
def generate_feature_vector(text, freq):
    feature = []
    feature.append(freq_pain_feature(text, freq))
    feature.append(freq_private_feature(text, freq))
    feature.append(freq_bank_feature(text, freq))
    feature.append(freq_money_feature(text, freq))
    feature.append(freq_drug_feature(text, freq))
    feature.append(freq_spam_feature(text, freq))
    feature.append(freq_prescription_feature(text, freq))
    feature.append(freq_subscription_feature(text, freq))
    feature.append(freq_creative_feature(text, freq))
    feature.append(freq_height_feature(text, freq))
    feature.append(freq_featured_feature(text, freq))
    feature.append(freq_differ_feature(text, freq))
    feature.append(freq_width_feature(text, freq))
    feature.append(freq_other_feature(text, freq))
    feature.append(freq_energy_feature(text, freq))
    feature.append(freq_business_feature(text, freq))
    feature.append(freq_message_feature(text, freq))
    feature.append(freq_volumes_feature(text, freq))
    feature.append(freq_revision_feature(text, freq))
    feature.append(freq_path_feature(text, freq))
    feature.append(freq_meter_feature(text, freq))
    feature.append(freq_memo_feature(text, freq)) 
    feature.append(freq_planning_feature(text, freq)) 
    feature.append(freq_pleased_feature(text, freq)) 
    feature.append(freq_record_feature(text, freq)) 
    feature.append(freq_out_feature(text, freq))
    feature.append(freq_semicolon_feature(text, freq))
    feature.append(freq_dollar_feature(text, freq))
    feature.append(freq_sharp_feature(text, freq))
    feature.append(freq_exclamation_feature(text, freq))
    feature.append(freq_para_feature(text, freq))
    feature.append(freq_bracket_feature(text, freq))
    feature.append(freq_and_feature(text, freq))
    feature.append(freq_underline_feature(text, freq))
    feature.append(freq_at_feature(text, freq))

 # added features:

    feature.append(freq_order_feature(text, freq))
    #feature.append(freq_direct_feature(text, freq))
    feature.append(freq_buy_feature(text, freq))
    #feature.append(freq_clearance_feature(text, freq))
    #feature.append(freq_shopper_feature(text, freq))
    feature.append(freq_earn_feature(text, freq))
    feature.append(freq_extra_feature(text, freq))
    feature.append(freq_online_feature(text, freq))
    #feature.append(freq_cash_feature(text, freq))
    #feature.append(freq_bonus_feature(text, freq))
    feature.append(freq_free_feature(text, freq))
    #feature.append(freq_lowest_feature(text, freq))
    #feature.append(freq_refund_feature(text, freq))
    feature.append(freq_click_feature(text, freq))
    #feature.append(freq_member_feature(text, freq))
    feature.append(freq_trial_feature(text, freq))
    #feature.append(freq_satisfied_feature(text, freq))
    feature.append(freq_million_feature(text, freq))
    #feature.append(freq_guarantee_feature(text, freq))
    #feature.append(freq_instant_feature(text, freq))
    feature.append(freq_won_feature(text, freq))
    feature.append(freq_offer_feature(text, freq))
    feature.append(freq_opportunities_feature(text, freq))
    feature.append(freq_dash_feature(text, freq))
    feature.append(freq_dot_feature(text, freq))
    feature.append(freq_add_feature(text, freq))
    feature.append(freq_percent_feature(text, freq))

    feature.append(freq_i_feature(text, freq))
    feature.append(freq_think_feature(text, freq))
    feature.append(freq_thanks_feature(text, freq))

    feature.append(freq_http_feature(text, freq))


    # --------- Add your own features here ---------
    # Make sure type is int or float

    return feature

# This method generates a design matrix with a list of filenames
# Each file is a single training example
def generate_design_matrix(filenames):
    design_matrix = []
    for filename in filenames:
        with open(filename) as f:
            text = f.read() # Read in text from file
            text = text.replace('\r\n', ' ') # Remove newline character
            words = re.findall(r'\w+', text)
            word_freq = defaultdict(int) # Frequency of all words
            for word in words:
                word_freq[word] += 1

            # Create a feature vector
            feature_vector = generate_feature_vector(text, word_freq)
            design_matrix.append(feature_vector)
    return design_matrix

# ************** Script starts here **************
# DO NOT MODIFY ANYTHING BELOW

spam_filenames = glob.glob(BASE_DIR + SPAM_DIR + '*.txt')
spam_design_matrix = generate_design_matrix(spam_filenames)
ham_filenames = glob.glob(BASE_DIR + HAM_DIR + '*.txt')
ham_design_matrix = generate_design_matrix(ham_filenames)
# Important: the test_filenames must be in numerical order as that is the
# order we will be evaluating your classifier
test_filenames = [BASE_DIR + TEST_DIR + str(x) + '.txt' for x in range(NUM_TEST_EXAMPLES)]
test_design_matrix = generate_design_matrix(test_filenames)

X = spam_design_matrix + ham_design_matrix
Y = [1]*len(spam_design_matrix) + [0]*len(ham_design_matrix)

file_dict = {}
file_dict['training_data'] = X
file_dict['training_labels'] = Y
file_dict['test_data'] = test_design_matrix
scipy.io.savemat('spam_data.mat', file_dict)

