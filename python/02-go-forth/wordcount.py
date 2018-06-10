#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, re, operator, string

#
# 가장 중요한 데이터 스택
#
stack = []

#
# 힙. 이름을 데이터에 매핑한다(즉, 변수)
#
heap = {}

#
# 프로그램의 새 '단어들'(프로시저)
#
def read_file():
	"""
	Takes a path to a file on the stack and places the entire
	contents of the file back on the stack
	"""
	f = open(stack.pop())
	# 스택에 그 결과를 넣는다
	stack.append([f.read()])
	f.close()

def filter_chars():
	"""
	Takes data on the stack and places back a copy with all
	nonalphasumeric chars replaces by white space.
	"""
	# 이 내용은 형식에 속하진 않는다. 정규 표현식은 너무 고수준이지만 빠르고 짧게
	# 처리하기 위해 사용한다. 해당 패턴을 스택에 넣는다.
	stack.append(re.compile('[\W_+'))
	# 그 결과를 스택에 넣는다.
	stack.append([stack.pop().sub(' ', stack.pop()[0]).lower()])

def scan():
	"""
	Takes a string on the stack and scans for words, placing
	the list of words back on the stack
	"""
	# 다시 이야기하지만 split()은 이 형식에 너무 고수준이지만
	# 빠르고 짧게 처리하기 위해 사용한다. 연습 문제로 남겨둔다.
	stack.extend(stack.pop()[0].split()) # extend: array의 element를 뽑아 append 함. (그냥 append하면 array를 하나의 element로 취급하여 추가함.)

def remove_stop_words():
	"""
	Takes a list of words on the stack and removes stop words.
	"""
	f = open('../../data/stop_words.txt')
	stack.append(f.read().split(','))
	f.close()
	# 한 글자로 된 단어를 추가한다.
	stack[-1].extend(list(string.ascii_lowercase))
	heap['stop_words'] = stack.pop()
	# 다시 이야기하지만 이것은 이 형식에 너무 고수준이지만
	# 빠르고 짧게 처리하기 위해 사용한다. 연습 문제로 남겨둔다.
	heap['words'] = []
	while len(stack) > 0:
		if stack[-1] in heap['stop_words']:
			stack.pop() # 꺼낸 후 버린다.
		else:
			heap['words'].append(stack.pop()) # 꺼낸 후 저장한다.
	stack.extend(heap['words']) # 단어를 스택에 적재한다.
	del heap['stop_words']; del heap['words'] # 불필요하다.