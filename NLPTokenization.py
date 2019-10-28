#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 11:39:26 2019

@author: soumyaranjanmohanty
"""
import nltk
nltk.download()

paragraph = "Following the Vivian Bose Commission report indicating serious wrongdoings of the Dalmia–Jain group, on 28 August 1969, the Bombay High Court, under Justice J. L. Nain, passed an interim order to disband the existing board of Bennett Coleman and to constitute a new board under the Government. The bench ruled that Under these circumstances, the best thing would be to pass such orders on the assumption that the allegations made by the petitioners that the affairs of the company were being conducted in a manner prejudicial to public interest and to the interests of the Company are correct.Following that order, Shanti Prasad Jain ceased to be a director and the company ran with new directors on board, appointed by the Government of India, with the exception of a lone stenographer of the Jains. Curiously, the court appointed D K Kunte as Chairman of the Board. Kunte had no prior business experience and was also an opposition member of the Lok Sabha."

sentences = nltk.sent_tokenize(paragraph)
print(sentences)